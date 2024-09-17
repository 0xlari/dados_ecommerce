# Projeto de Visualização e Análise de Dados de E-commerce

## Descrição do Projeto

Este projeto foca na análise de dados de um dataset de e-commerce. Utilizando gráficos de dispersão, mapa de calor, gráficos de barras, gráfico de pizza e gráfico de densidade, conseguimos obter insights sobre as relações entre variáveis importantes, como **preço**, **quantidade vendida**, **descontos**, **nota** e **gênero** dos produtos. Além disso, o projeto inclui uma etapa de limpeza de dados da coluna "Gênero", essencial para análises precisas.

## Objetivo

O objetivo é explorar os dados de e-commerce para identificar correlações e padrões importantes que possam fornecer insights sobre vendas, avaliação de produtos e comportamento do consumidor.

## Etapas Realizadas

### 1. **Limpeza de Dados**
Antes de realizar as análises, foi necessário limpar a coluna "Gênero" para remover valores inconsistentes e padronizar os dados. O procedimento de limpeza envolveu:
- Remover valores indesejados e padronizar o texto da coluna "Gênero" para minúsculas.
  
### 2. **Gráfico de Dispersão (Preço vs. Quantidade Vendida por Marca)**

Para visualizar a relação entre o **preço** dos produtos e a **quantidade vendida**, foi gerado um gráfico de dispersão. Neste gráfico, os pontos foram coloridos de acordo com o código da marca (`Marca_Cod`), permitindo uma visualização mais detalhada das variações entre as diferentes marcas.

- **Eixo X**: Preço do produto
- **Eixo Y**: Quantidade vendida
- **Cor**: Código da marca (Marca_Cod)

```python
plt.scatter(df['Preço'], df['Qtd_Vendidos'], c=df['Marca_Cod'], cmap='viridis')
plt.colorbar(label='Marca_Cod')
```

### 3. **Mapa de Calor (Correlação entre Variáveis)**

Foi gerado um mapa de calor para visualizar a correlação entre variáveis como **Nota**, **Número de Avaliações**, **Desconto**, **Quantidade Vendida** e **Preço**. A correlação entre essas variáveis permite entender melhor como elas se relacionam, identificando tendências.

- Foi necessário tratar a coluna "Qtd_Vendidos" para remover texto não numérico (ex: '+', 'mil') e convertê-la para um formato numérico.

```python
corr = df[['Nota', 'N_Avaliações', 'Desconto', 'Qtd_Vendidos', 'Preço']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
```

### 4. **Gráfico de Barras (Número de Avaliações por Nota)**

Para entender a distribuição de avaliações com base nas notas dos produtos, foi gerado um gráfico de barras. O gráfico mostra a soma das avaliações para cada **nota** disponível no dataset.

- **Eixo X**: Nota do produto
- **Eixo Y**: Número de avaliações somadas

```python
df_grouped = df.groupby('Nota')['N_Avaliações'].sum().reset_index()
plt.bar(df_grouped['Nota'], df_grouped['N_Avaliações'], color='#90ee70')
```

### 5. **Gráfico de Pizza (Distribuição de Vendas por Gênero)**

Um gráfico de pizza foi criado para visualizar a distribuição de vendas por **gênero** dos produtos. Isso nos dá uma visão clara de qual gênero de produto tem maior participação nas vendas.

- **Setores**: Gêneros dos produtos (ex: feminino, masculino)
- **Proporção**: Soma dos preços por gênero

```python
vendas_por_genero = df.groupby('Gênero')['Preço'].sum()
plt.pie(vendas_por_genero, labels=vendas_por_genero.index, autopct='%.1f%%')
```

### 6. **Gráfico de Densidade (Preço)**

Para visualizar a distribuição dos **preços** dos produtos, foi gerado um gráfico de densidade. Este gráfico ajuda a entender como os preços estão distribuídos, destacando áreas de maior concentração.

```python
sns.kdeplot(df['Preço'], fill=True, color='#863e9c')
```

## Conclusão

Este projeto apresenta uma análise detalhada dos dados de e-commerce através de visualizações. Cada gráfico gerado oferece uma perspectiva valiosa sobre o comportamento dos produtos, suas avaliações, vendas e preços. A limpeza inicial dos dados, especialmente a coluna "Gênero", foi essencial para garantir a precisão dos insights. Com esses gráficos, podemos observar correlações e tendências, facilitando tomadas de decisão estratégicas em e-commerce.

## Próximos Passos

1. Expandir a análise para outras variáveis do dataset.
2. Aplicar técnicas de modelagem preditiva para prever a quantidade vendida com base em preço e desconto.
3. Realizar segmentação de clientes com base em padrões de compra e avaliação.
