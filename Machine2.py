import mysql.connector  # Conexão com MySQL
import pandas as pd     # Manipulação de dados
import matplotlib.pyplot as plt  # Gráficos
import numpy as np      # Cálculos numéricos
from sklearn.linear_model import LinearRegression  # Modelo de IA

#Fase1: Extração e Tratamento

db_config = {
'host': 'localhost', # Geralmente 'localhost' se o banco está na sua máquina
'user': 'root', # Seu usuário do MySQL (padrão é 'root')
'password': 'senaisp', # A senha que você definiu para o usuário 'root'
'database': 'logistica_db' # O nome do banco que criamos no Passo 1
}

query="""
SELECT
    ent.nome AS Nome_Entregador, 
    ent.tipo_veiculo AS Veiculo, 
    entre.status_entrega AS Status, 
    entre.valor_frete AS Valor_Frete, 
    entre.data_pedido AS Data,
    ent.zona_atuacao As Zona,
    entre.id_entregador as entregador,
    entre.distancia_km as KM
FROM
    entregadores ent
INNER JOIN
    entregas entre ON ent.id_entregador = entre.id_entregador
"""

try:
# 4.1. Conectar ao banco
# 'mysql.connector.connect()' cria o objeto de conexão.
# O '**db_config' é um atalho do Python para "descompactar"
# nosso dicionário de config, o que é o mesmo que escrever:
# host=db_config['host'], user=db_config['user'], etc.
    conexao = mysql.connector.connect(**db_config)
    print("Conexão bem-sucedida!")
# 4.2. Executar a query e carregar no Pandas
# 'pd.read_sql_query()' é a função do Pandas que faz tudo:
# 1. Envia a 'query' (nossa consulta SQL com JOIN)
# 2. Através da 'conexao' que abrimos
# 3. Pega o resultado
# 4. E o carrega DIRETAMENTE em um DataFrame do Pandas.
# A variável 'df' agora contém nossos dados prontos para análise.
    df = pd.read_sql_query(query, conexao)
    print(f"Passo 2: Dados extraídos com sucesso. {len(df)} linhas recebidas.")
finally:
# 4.3. Fechar a conexão
# Verificamos se a variável 'conexao' existe E se ela está conectada
    if 'conexao' in locals() and conexao.is_connected():
# .close() encerra a conexão com o MySQL.
# É MUITO importante fechar conexões para liberar recursos do servidor.
        conexao.close()
print("Conexão com o MySQL foi fechada.")

#Tratamento dos dados

print("Tratamento dos dados")

#Financeiro: Qual Zona (Norte, Sul, etc.) gerou maior faturamento total?
zona_faturamento = df.groupby('Zona')['Valor_Frete'].sum()
print(zona_faturamento)




#4-Prepaacao para machine learning
x = df['KM'].values.reshape(-1, 1)

y = df['Valor_Frete'].values

#Criação do modelo
modelo = LinearRegression()

#Treinamento
modelo.fit(x,y)

#Predict para o valor de 100km
distancia = [[25]]
previsao = modelo.predict(distancia)
print(f"Se uma entrega for de 25km e de {previsao}")

#DashBoard
# Cria uma figura maior (como um "painel")
fig = plt.figure(figsize=(12, 8))

#KPI
# Cria o primeiro espaço do dashboard (posição 1)
zona_fat = zona_faturamento.idxmax()
total_fat = zona_faturamento.max()


plt.subplot(2, 2, 1)

#Exibe a zona que faturou mais
plt.text(0.1,0.6, f"A zona que faturou mais foi {zona_fat}", fontsize = 14)

#Exibe o total do faturamento
plt.text(0.1, 0.4, f"O total do faturamento foi {total_fat}", fontsize = 14)

# Remove os eixos (fica mais visual, estilo dashboard)
plt.axis('off')

# Título do bloco
plt.title("KPIs Zonas")

#2 Grafico
# Cria o segundo espaço do dashboard
plt.subplot(2, 2, 2)

# Mostra novamente os pontos reais
plt.scatter(x,y)

# Desenha a linha de regressão (linha que o modelo aprendeu)
plt.plot(x, modelo.predict(x))

# Nome dos eixos
plt.xlabel("KM")
plt.ylabel("Valor Frete")

#Titulo
plt.title("Regressao Linear")


# GRÁFICO 2 - Evolução das Vendas

# Cria um gráfico ocupando toda a parte inferior
plt.subplot(2, 1, 2)

# Gráfico de linha (evolução no tempo)
zona_faturamento.plot()

# Título
plt.title("Evolução de venda por Zona")

# Ajusta automaticamente os espaços entre os gráficos
plt.tight_layout()

#Exibe o gráfico
plt.show()