# 5) O arquivo base_vendas.csv contém informações a cerca de vendas de produtos fictícios, as colunas do arquivo são as seguintes:

# **sku**: Identificador único para cada produto.\
# **classe**: Categoria à qual o produto pertence (Móveis, Decoração, Tecnologia, etc...).\
# **qtde_vendida**: Quantidade de vendas do produto no período de análise.\
# **valor_unitario**: Preço unitário de cada produto.

# Carregue a base em um dataframe e responda as seguintes questões:
import pandas as pd

caminho_csv = r'C:\Users\980184\Desktop\QQtech\exercicios6-PythonQQtech\base_vendas.csv'

df = pd.read_csv(caminho_csv, encoding='latin-1', sep=';', decimal=',')

# a) Qual o tipo de cada coluna?

tipos_de_colunas = df.dtypes
print(f"----------------------------------------------------------------------------------------------------------------------------------")
print(tipos_de_colunas)
print(f"----------------------------------------------------------------------------------------------------------------------------------")

# b) Quantas classes de produtos existem na base e quais são elas?

classes_de_produtos = df['classe'].value_counts()

nomes_classes = classes_de_produtos.index.tolist()

print(f"São {len(nomes_classes)}: {', '.join(nomes_classes)}")
print(f"----------------------------------------------------------------------------------------------------------------------------------")

# c) Considerando todos os produtos, qual o total de unidades vendidas?

total_vendido = df['qtde_vendida'].sum()
print(f"Foram vendidos {total_vendido} produtos")
print(f"----------------------------------------------------------------------------------------------------------------------------------")

# d) Qual o total de unidades vendidas por classe?

total_por_classe = df.groupby('classe')['qtde_vendida'].sum()
for classe, total in total_por_classe.items():
    print(f"Classe: {classe}, Total Vendido: {total}")
print(f"----------------------------------------------------------------------------------------------------------------------------------")

# e) Indique os sku's dos 10 produtos mais vendidos e menos vendidos.

produtos_mais_vendidos = df.groupby('sku')['qtde_vendida'].sum().nlargest(10).reset_index()

produtos_menos_vendidos = df.groupby('sku')['qtde_vendida'].sum().nsmallest(10).reset_index()

print("10 produtos mais vendidos:")
print(produtos_mais_vendidos)
print(f"----------------------------------------------------------------------------------------------------------------------------------")

print("\n10 produtos menos vendidos:")
print(produtos_menos_vendidos)
print(f"----------------------------------------------------------------------------------------------------------------------------------")

# f) Qual a média da quantidade de unidades vendidas?

total_vendido = df['qtde_vendida'].sum()
media_vendido= total_vendido/(len(df))
print(f"A média da quantidade vendida é {media_vendido:.0f}")

# g) Qual a média da quantidade de unidades vendidas por classe?

media_por_classe = df.groupby('classe')['qtde_vendida'].mean()

print("Média da quantidade de unidades vendidas por classe:")
print(media_por_classe)

print(f"----------------------------------------------------------------------------------------------------------------------------------")

# h) Crie uma coluna indicando a receita total de cada produto.

df['receita_total'] = df['qtde_vendida'] * df['valor_unitario']

print(df)
print(f"----------------------------------------------------------------------------------------------------------------------------------")

# i) Qual a receita total no período analisado?

receita_total_soma = df['receita_total'].sum()
print(f"A receita total no período analisado é: R$ {receita_total_soma:.2f}")
print(f"----------------------------------------------------------------------------------------------------------------------------------")

# j) Considerando os 10 produtos mais rentáveis, quantos por cento da receita total eles representam?

receita_total = df.sort_values(by='receita_total', ascending=False)
dez_produtos = receita_total.head(10)
receita_total_dez_produtos = dez_produtos['receita_total'].sum()
porcentagem = (receita_total_dez_produtos / receita_total['receita_total'].sum()) * 100
print(f"Os 10 produtos mais rentáveis representam {porcentagem:.1f}% da receita total.")
print(f"----------------------------------------------------------------------------------------------------------------------------------")


# k) Quantos dos produtos mais rentáveis somam 50% da receita total?

df_sorted = df.sort_values(by='receita_total', ascending=False)

metade_receita_total = 0.5 * df_sorted['receita_total'].sum()

soma_receita = 0
num_produtos = 0

for index, row in df_sorted.iterrows():
    soma_receita += row['receita_total']
    num_produtos += 1
    if soma_receita >= metade_receita_total:
        break

print(f"Foram necessários {num_produtos} dos produtos mais rentáveis para somar 50% da receita total.")
print(f"----------------------------------------------------------------------------------------------------------------------------------")
