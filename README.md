# VehiclesWebApp

Aplicação web para explorar anúncios de venda de veículos. O projeto foi desenvolvido como parte do MBA em Data Science & Artificial Intelligence da TripleTen.

A interface é feita com Streamlit e os gráficos com Plotly. Os dados vêm do arquivo `vehicles.csv`.

## O que a aplicação mostra

Na página há três botões:

- **Criar histograma** — distribuição de preço, separada pela condição do veículo
- **Criar dispersão** — ano do modelo em relação à quilometragem
- **Criar barras** — quantidade de veículos por tipo e condição

## Como executar localmente

Na pasta do projeto, com as dependências instaladas, execute:

```
streamlit run app.py
```

Abra http://localhost:10000 no navegador.

## Dependências

- pandas
- plotly
- streamlit
