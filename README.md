# Análise de Dados de Vendas e Comportamento de Clientes

## Descrição
Este projeto realiza uma análise detalhada de um conjunto de dados de vendas, explorando o comportamento de gastos dos clientes com base em variáveis como gênero, faixa etária, região, ocupação e categorias de produtos. O objetivo é identificar padrões de comportamento que possam auxiliar na criação de estratégias de marketing, fidelização de clientes e aumento de vendas.

## Funcionalidades
- **Limpeza de Dados**: Tratamento de valores ausentes na coluna `Amount`.
- **Análise Exploratória de Dados (EDA)**:
  - Distribuição de clientes por gênero.
  - Análise de gasto médio por faixa etária, região e ocupação.
  - Comparação do comportamento de consumo entre gêneros e categorias de produtos.
- **Teste Estatístico**:
  - Comparação de gastos entre homens e mulheres utilizando o teste t.
- **Visualizações Interativas**:
  - Gráficos de barras, heatmaps e boxplots para explorar os padrões nos dados.
- **Matriz de Correlação**:
  - Avaliação de correlações entre variáveis numéricas e categóricas.

## Requisitos
- Python 3.x
- Bibliotecas Python:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scipy
  - scikit-learn

Você pode instalar os requisitos executando:
```bash
pip install -r requirements.txt
```

## Como usar


1. Clone este repositório em sua máquina local:

```bash
git clone https://github.com/marques-viniciusc/analise-de-vendas
```

2. Instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

3. Certifique-se de que o arquivo sales-data.csv está no mesmo diretório que o script.

4. Execute o script:

```bash
python sales_analysis.py
```

5.Explore os gráficos gerados para obter insights sobre os dados.

## Estrutura do Código

1. Limpeza de Dados:
- Valores ausentes na coluna Amount são preenchidos com a média.

2. Análise Exploratória:
- Visualizações de gasto médio por região, idade e gênero.
- Distribuição de categorias de produtos por gênero.

3. Teste Estatístico:
- Aplicação do teste t para avaliar diferenças significativas entre gêneros.

4. Matriz de Correlação:
- Avaliação da relação entre variáveis como idade, região e ocupação.

## Exemplos de Insights

- **Distribuição de Gênero:** As mulheres são a maioria dos clientes e contribuem para o maior gasto total.

- **Gasto por Região:** A região central possui o maior gasto total, enquanto a região norte apresenta o menor.

- **Categorias de Produtos:** Produtos mais comprados incluem vestimentas, alimentos e eletrônicos.

- **Teste Estatístico:** Não há diferença significativa entre o gasto médio de homens e mulheres.

## Personalização

- **Novas Análises:** O código pode ser adaptado para explorar outras variáveis ou criar modelos preditivos com machine learning.

- **Visualizações:** Estilos de gráficos podem ser alterados para atender diferentes preferências de apresentação.

## Observações

- Certifique-se de que o arquivo sales-data.csv está formatado corretamente, com as colunas esperadas (Gender, Age, Zone, Amount, etc.).

## Licença

Este projeto é de uso livre e pode ser modificado conforme necessário.
