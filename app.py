import pandas as pd
import plotly.express as px
import streamlit as st

# Configurar a página ----- Primeira Chamada------
st.set_page_config(
    page_title="Painel de Vendas",
    page_icon="📊",
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Input do CSV
#file_path = "E:/Projeto_new/vendas.csv"
#df = pd.read_csv(file_path)

# Carregar o CSV diretamente da URL do GitHub
url = "https://raw.githubusercontent.com/jamessalmom/Mini-Painel-Sales/master/vendas.csv"
df = pd.read_csv(url)

# Ajusta formato da data e do valor das vendas
df['Data_Pedido'] = pd.to_datetime(df['Data_Pedido'], format='%d/%m/%Y')
df['ValorVenda'] = df['ValorVenda'].str.replace('.', '').str.replace(',', '.').astype(float)

# Adicionar colunas de Ano e Mês ao frame
df['Ano'] = df['Data_Pedido'].dt.year
df['Mes'] = df['Data_Pedido'].dt.strftime('%B')  # Nome do mês

# Função para gerar o painel com filtros Dinâmico
def gerar_painel(df):
    st.markdown("<h3 style='text-align: center; color: #2C3E50;'> 📊 Mini Painel de Controle de Vendas</h3>", unsafe_allow_html=True)
    
    # Filtro Ano
    anos_disponiveis = df['Ano'].unique()
    filtro_anos = st.sidebar.multiselect("Ano", options=anos_disponiveis, default=[])

    # Filtrar o frame baseado nos anos
    df_filtrado = df.copy()
    if filtro_anos:
        df_filtrado = df_filtrado[df_filtrado['Ano'].isin(filtro_anos)]
    
    # Filtro Mês
    meses_disponiveis = df_filtrado['Mes'].unique()
    filtro_meses = st.sidebar.multiselect("Mês", options=meses_disponiveis, default=[])

    # Filtrar o frame baseado nos meses
    if filtro_meses:
        df_filtrado = df_filtrado[df_filtrado['Mes'].isin(filtro_meses)]
    
    # Filtro País
    paises_disponiveis = df_filtrado['Pais'].unique()
    filtro_pais = st.sidebar.multiselect("País", options=paises_disponiveis, default=[])
    
    if filtro_pais:
        df_filtrado = df_filtrado[df_filtrado['Pais'].isin(filtro_pais)]
    
    # Atualizar o filtro dinâmico de estado (com base no país selecionado)
    estados_disponiveis = df_filtrado['Estado'].unique()
    filtro_estado = st.sidebar.multiselect("Estado", options=estados_disponiveis, default=[])
    
    if filtro_estado:
        df_filtrado = df_filtrado[df_filtrado['Estado'].isin(filtro_estado)]
    
    # Atualizar o filtro de cidade (com base no estado selecionado)
    cidades_disponiveis = df_filtrado['Cidade'].unique()
    filtro_cidade = st.sidebar.multiselect("Cidade", options=cidades_disponiveis, default=[])
    
    if filtro_cidade:
        df_filtrado = df_filtrado[df_filtrado['Cidade'].isin(filtro_cidade)]
    
    # Filtros Produto
    produtos_disponiveis = df_filtrado['NomeProduto'].unique()
    
    filtro_produto = st.sidebar.multiselect("Produto", options=produtos_disponiveis, default=[])
    
    if filtro_produto:
        df_filtrado = df_filtrado[df_filtrado['NomeProduto'].isin(filtro_produto)]

################################################## Exibir no painel #############################################################   

    # Seção 1: KPI - Total de Vendas (casas decimais padrão brasil)
    total_vendas = df_filtrado['ValorVenda'].sum() if not df_filtrado.empty else 0
    total_vendas_formatado = f"$ {total_vendas:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    st.metric(label="Total de Vendas", value=total_vendas_formatado)

    #################################### Gráficos ##########################################

    # Seção 2: barras - Vendas por Produto
    if not df_filtrado.empty:
        vendas_por_produto = df_filtrado.groupby('NomeProduto')['ValorVenda'].sum().reset_index()
        fig_produto = px.bar(vendas_por_produto, x='NomeProduto', y='ValorVenda', 
                             title="Vendas por Produto", labels={'ValorVenda': 'Vendas ($)'})
        st.plotly_chart(fig_produto)
    
    # Seção 3: Linhas - Vendas ao Longo do Tempo
    if not df_filtrado.empty:
        vendas_por_data = df_filtrado.groupby('Data_Pedido')['ValorVenda'].sum().reset_index()
        fig_data = px.line(vendas_por_data, x='Data_Pedido', y='ValorVenda', 
                           title="Vendas ao Longo do Tempo", labels={'ValorVenda': 'Vendas ($)', 'Data_Pedido': 'Data'})
        st.plotly_chart(fig_data)

# Gerar painel
if __name__ == '__main__':
    gerar_painel(df)
