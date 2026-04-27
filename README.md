# An-lise-e-Previs-o-de-Frete-com-Machine-Learning
Este projeto tem como objetivo realizar a análise de dados logísticos e a previsão de valores de frete utilizando técnicas de Machine Learning.

Os dados são extraídos diretamente de um banco de dados MySQL, tratados com Python e analisados para gerar insights de negócio.
Além disso, foi desenvolvido um modelo de Regressão Linear capaz de prever o valor do frete com base na distância percorrida.

Tecnologias Utilizadas:
-Python
-MySQL
-Pandas
-NumPy
-Matplotlib
-Scikit-learn

🧠 Etapas do Projeto
🔹 1. Extração de Dados
Conexão com banco MySQL
Execução de query com JOIN entre tabelas
Importação direta para DataFrame (Pandas)
🔹 2. Tratamento de Dados
Organização dos dados
Agrupamento por zona de atuação
Cálculo de faturamento total por região
🔹 3. Análise Exploratória
Identificação da zona com maior faturamento
Visualização de padrões de receita
🔹 4. Machine Learning
Modelo utilizado: Regressão Linear
Variáveis:
Entrada (X): Distância (KM)
Saída (Y): Valor do Frete
Treinamento do modelo com dados reais
🔹 5. Visualização (Dashboard)
Indicadores principais (KPIs)
Gráfico de regressão
Evolução do faturamento por zona
