import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('meu_arquivo_atualizado.csv')

pd.set_option('display.width', None)
print(df.head())


# Gráfico de Dispersão
plt.scatter(df['Preço'], df['Qtd_Vendidos'], c=df['Marca_Cod'], cmap='viridis')
plt.title('Dispersão - Preço e Vendidos')
plt.xlabel('Preço')
plt.ylabel('Vendidos')
# Adiciona barra de cores para visualizar os códigos das marcas
plt.colorbar(label='Marca_Cod')
plt.show()

# Mapa de Calor / Nota, N_Avaliações, Desconto, Qtd_Vendidos, Preço
# Remover texto não numérico (ex: '+', 'mil') e converter para numérico
df['Qtd_Vendidos'] = df['Qtd_Vendidos'].replace({'\+': '', 'mil': '000'}, regex=True)
df['Qtd_Vendidos'] = pd.to_numeric(df['Qtd_Vendidos'], errors='coerce')  # Converte strings para números, NaN se não for possível

# Agora calculando a correlação
corr = df[['Nota', 'N_Avaliações', 'Desconto', 'Qtd_Vendidos', 'Preço']].corr()

# Criando o mapa de calor
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação entre Nota, Avaliações, Desconto, Vendidos e Preço')
plt.show()


#Gráfico de Barras
print(df[['Nota', 'N_Avaliações']].head())

# Agrupar os dados pela coluna 'Nota' e somar as avaliações associadas a cada nota
df_grouped = df.groupby('Nota')['N_Avaliações'].sum().reset_index()

# Criar o gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(df_grouped['Nota'], df_grouped['N_Avaliações'], color='#90ee70')
plt.title('Número de Avaliações por Nota')
plt.xlabel('Nota')
plt.ylabel('Número de Avaliações')
plt.show()


# Agrupar as vendas por gênero e somar
vendas_por_genero = df.groupby('Gênero')['Preço'].sum()

# Verificar os valores únicos na coluna 'Gênero'
valores_genero = df['Gênero'].unique()

# Exibir os valores únicos
print(valores_genero)

# Verificar a contagem de cada valor na coluna 'Gênero'
contagem_genero = df['Gênero'].value_counts()

# Exibir a contagem de cada valor
print(contagem_genero)

# Criar o gráfico de pizza
plt.figure(figsize=(10, 6))
plt.pie(vendas_por_genero, labels=vendas_por_genero.index, autopct='%.1f%%', startangle=90, colors=plt.get_cmap('Pastel1').colors)
plt.title('Distribuição de Vendas por Gênero')
plt.show()

#Gráfico de Densidade
plt.figure(figsize=(18,6))
sns.kdeplot(df['Preço'], fill=True, color='#863e9c')
plt.title('Densidade de Preço')
plt.xlabel('Preço')
plt.show()