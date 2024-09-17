import pandas as pd

# Carregar o DataFrame (substitua pelo caminho do seu arquivo)
df = pd.read_csv('ecommerce_preparados.csv')  # Substitua pelo caminho do seu arquivo

# Remover espaços extras e padronizar para minúsculas
df['Gênero'] = df['Gênero'].str.strip().str.lower()

# Exibir valores únicos antes da remoção
print("Valores únicos antes da remoção:")
print(df['Gênero'].unique())

# Listar os valores a serem removidos
valores_a_remover = ['mulher', 'short menina verao look mulher', 'roupa para gordinha pluss p ao 52',
                     'unissex', 'menino', 'bermuda feminina brilho blogueira']

# Filtrar o DataFrame para remover as linhas com os valores indesejados
for valor in valores_a_remover:
    df = df[df['Gênero'] != valor]

# Exibir valores únicos após a remoção
print("Valores únicos após a remoção:")
print(df['Gênero'].unique())

# Opcional: Salvar o DataFrame atualizado em um novo arquivo CSV
df.to_csv('meu_arquivo_atualizado.csv', index=False)