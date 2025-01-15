"""
Análise de dados de vendas
-------------------
Este código tem como objetivo analisar os dados de vendas para descobrir insights sobre o comportamento de gastos dos clientes.
A intenção é buscar ferramentas que possam otimizar a estratégia de marketing da empresa, fidelizar a base de clientes e aumentar as vendas.

Ao longo do projeto, pontuei insights para responder a perguntas como:
- Qual é a distribuição de gênero dos clientes?
- Qual é o gasto total por região?
- Qual é o gasto médio por faixa etária?
- Qual é o gasto total por gênero?
- Qual é a ocupação que mais gasta por gênero?
- Existe diferença significativa entre os gastos dos homens e das mulheres?
- Existe correlação entre as variáveis analisadas?
-------------------
O código inclui as seguintes etapas:
- Limpeza e pré-processamento de dados;
- Análise Exploratória de Dados (EDA) com visualizações;
- Teste Estatístico;
- Matriz de Correlação.
"""

# Importação de bibliotecas

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind
from sklearn.preprocessing import LabelEncoder

# Limpeza e pré-processamento de dados

data = pd.read_csv('sales-data.csv', encoding='latin1')
df = pd.DataFrame(data)

print(df.head(10))
print(df.isnull().sum()) # presença de 12 valores nulos em "Amount"

mean_values = df['Amount'].mean()
df['Amount'] = df['Amount'].fillna(mean_values) # preenchendo valores nulos com a média dos valores da coluna

print(df.head(10))
print(df.isnull().sum()) # valores nulos zerados

# Análise Exploratória de Dados (EDA) com visualizações

## Análise de clientes por gênero

sns.countplot(x='Gender', data=df)
plt.title('Clientes por gênero', fontsize=18)
plt.xlabel('Gênero', fontsize=12)
plt.ylabel('Quantidade', fontsize=12)
plt.show()

### Insight: a quantidade de clientes do sexo feminino é maior do que a quantidade de clientes do sexo masculino.


## Análise de gasto por região

zone_summary = df.groupby('Zone')['Amount'].mean().reset_index()

sns.barplot(x='Zone', y='Amount', data=zone_summary)
plt.title('Média de gasto por região', fontsize=18)
plt.xlabel('Região', fontsize=14)
plt.ylabel('Gasto médio', fontsize=14)
plt.ticklabel_format(style='plain', axis='y')
plt.show()

### Insight 1: a região sul é a que possui a maior média de gasto, seguida pela região central e região oeste.
### Insight 2: não há grande diferença de gasto das regiões, mas sim uma maior quantidade de clientes nas regiões citadas acima.

# Análise de gasto por idade

age_summary = df.groupby('Age Group')['Amount'].mean().reset_index()

sns.barplot(x='Age Group', y='Amount', data=age_summary)
plt.title('Média de gasto por idade', fontsize=18)
plt.xlabel('Idade', fontsize=14)
plt.ylabel('Gasto médio', fontsize=14)
plt.ticklabel_format(style='plain', axis='y')
plt.show()

### Insight: não há diferença considerável entre gastos por faixa etária, mas destacam-se levemente as faixas de 51-55 e 36-45 anos.

## Análise de gasto por gênero

gender_summary = df.groupby('Gender')['Amount'].mean().reset_index()

sns.barplot(x='Gender', y='Amount', data=gender_summary)
plt.title('Média de gasto por gênero', fontsize=18)
plt.xlabel('Gênero', fontsize=14)
plt.ylabel('Gasto médio', fontsize=14)
plt.ticklabel_format(style='plain', axis='y')
plt.show()

### Insight 1: o gasto total das mulheres é maior do que o gasto total dos homens.
### Insight 2: isto ocorre devido à maior quantidade de clientes do sexo feminino.

## Análise de tipo de produto por gênero

sns.countplot(x='Product_Category', hue='Gender', data=df)
plt.xticks(rotation=90)
plt.title('Produtos comprados por categoria (divisão por gênero)', fontsize=18)
plt.xlabel('Categoria', fontsize=12)
plt.ylabel('Quantidade', fontsize=12)
plt.tight_layout()
plt.show()

### Insight 1: os produtos mais consumidos são vestimentas, alimentos e produtos eletrônicos.
### Insight 2: as mulheres consomem mais por serem maioria, porém, homens compram mais ferramentas e livros.

## Análise de gasto por ocupação e gênero

grouped_data = df.groupby(['Gender', 'Occupation'])['Amount'].mean().unstack()

plt.figure(figsize=(10, 6))
sns.heatmap(grouped_data, annot=True, fmt=".2f" ,cmap='coolwarm')
plt.title('Média de gasto por ocupação e gênero', fontsize=18)
plt.xlabel('Ocupação', fontsize=12)
plt.ylabel('Gênero', fontsize=12)
plt.tight_layout()
plt.show()

### Insight 1: no grupo das mulheres, destacam-se as que trabalham com mídias e no governo.
### Insight 2: no grupo dos homens, destacam-se os que trabalham no governo e com processamento de alimentos.

# Teste Estatístico

male_spending = df[df['Gender'] == 'M']['Amount']
female_spending = df[df['Gender'] == 'F']['Amount']
t_stat, p_value = ttest_ind(male_spending, female_spending, equal_var=False)
print(f"\nT-statistic: {t_stat:.2f}")
print(f"P-value: {p_value:.2f}")

if p_value <= 0.05:
    print("\nResultado: diferença significativa entre os gastos dos homens e das mulheres.")
else:
    print("\nResultado: Não há diferença significativa entre os gastos dos homens e das mulheres.\n")

sns.boxplot(x='Gender', y='Amount', data=df)
plt.title('Distribuição de Gasto por Gênero')
plt.show()

### Insight: como citado anteriormente, as mulheres gastam mais do que os homens, mas a diferença não é significativa.

# Matriz de correlação

## Encoding das variáveis categóricas
label_encoder = LabelEncoder() # o encoding é necessário para criar a matriz de correlação com variáveis categórias

df['Gender_Encoded'] = label_encoder.fit_transform(df['Gender'])
df['Occupation_Encoded'] = label_encoder.fit_transform(df['Occupation'])
df['Zone_Encoded'] = label_encoder.fit_transform(df['Zone'])

## Visualização da matriz de correlação

corr_matrix = df[['Age', 'Amount', 'Gender_Encoded', 'Occupation_Encoded', 'Zone_Encoded']].corr()
print(corr_matrix)

# Insight: através da matriz de correlação, podemos perceber que há baixa correlação entre as variáveis analisadas, dificultando a aplicação de modelos preditivos.

"""
Conclusões:
- As mulheres são a maioria dos clientes e contribuem para o maior gasto total.
- A região central possui o maior gasto total, enquanto as diferenças entre as faixas etárias são mínimas.
- Não há correlação forte entre as variáveis analisadas, dificultando modelos preditivos simples.
"""
