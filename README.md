# Mini Painel de Controle de Vendas 📊

Este é um projeto que desenvolvi para explorar a criação de dashboards interativos utilizando Python, pandas, Plotly e Streamlit. O objetivo é fornecer uma ferramenta intuitiva para visualizar e analisar dados de vendas com filtros dinâmicos.

## Sumário

- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Demonstração](#demonstração)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Executar o Projeto](#como-executar-o-projeto)
- [Detalhes Técnicos Importantes](#detalhes-técnicos-importantes)


## Descrição

Este painel permite que os usuários filtrem dados de vendas por ano, mês, país, estado, cidade e produto. Com isso, é possível visualizar:

- **Total de Vendas**: Exibe o total de vendas no período selecionado.
- **Gráfico de Barras**: Mostra as vendas por produto.
- **Gráfico de Linhas**: Apresenta a evolução das vendas ao longo do tempo.

## Funcionalidades

- **Filtros Dinâmicos**: Selecione múltiplos anos, meses, países, estados, cidades e produtos para refinar a análise.
- **Visualizações Interativas**: Gráficos interativos que permitem zoom e detalhes ao passar o mouse.
- **Atualização em Tempo Real**: As visualizações são atualizadas automaticamente conforme os filtros são ajustados.

## Demonstração

Você pode acessar a versão implementada do painel através do link abaixo:

[➡️ Acesse o Mini Painel de Controle de Vendas](https://mini-painel-sales-vrdgeurdhmcvvrczrjus9t.streamlit.app/)

## Tecnologias Utilizadas

- **Python 3.x**
- **Pandas**: Manipulação e análise de dados.
- **Plotly Express**: Criação de gráficos interativos.
- **Streamlit**: Construção da interface web interativa do painel.

## Como Executar o Projeto

### Pré-requisitos

- Python 3.x instalado.
- Instalar as bibliotecas necessárias:
  ```bash
  pip install pandas plotly streamlit
  ```

### Passos para Execução

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. **Navegue até o diretório do projeto**:
   ```bash
   cd seu-repositorio
   ```
3. **Execute o aplicativo Streamlit**:
   ```bash
   streamlit run app.py
   ```
   *Substitua `app.py` pelo nome do arquivo Python contendo o código.*

4. **Acesse o painel**:
   Abra o navegador e vá para `http://localhost:8501` (ou o endereço fornecido pelo Streamlit).

## Detalhes Técnicos Importantes

- **Carregamento dos Dados**:
  - Os dados de vendas são carregados diretamente de um arquivo CSV hospedado no GitHub:
    ```python
    url = "https://raw.githubusercontent.com/jamessalmom/Mini-Painel-Sales/master/vendas.csv"
    df = pd.read_csv(url)
    ```
  - Certifique-se de que o CSV está formatado corretamente e acessível.

- **Processamento dos Dados**:
  - Conversão de strings para datas:
    ```python
    df['Data_Pedido'] = pd.to_datetime(df['Data_Pedido'], format='%d/%m/%Y')
    ```
  - Formatação dos valores monetários para o padrão numérico:
    ```python
    df['ValorVenda'] = df['ValorVenda'].str.replace('.', '').str.replace(',', '.').astype(float)
    ```
  - Criação de colunas adicionais para facilitar os filtros:
    ```python
    df['Ano'] = df['Data_Pedido'].dt.year
    df['Mes'] = df['Data_Pedido'].dt.strftime('%B')
    ```

- **Construção dos Filtros**:
  - Os filtros são implementados usando `st.sidebar.multiselect`, permitindo múltiplas seleções.
  - A atualização dos filtros é encadeada; por exemplo, os estados disponíveis dependem do país selecionado.

- **Visualizações**:
  - **Total de Vendas**: Exibido usando `st.metric` com formatação personalizada para o padrão brasileiro.
  - **Gráfico de Barras (Vendas por Produto)**: Criado com `px.bar` e exibido com `st.plotly_chart`.
  - **Gráfico de Linhas (Vendas ao Longo do Tempo)**: Criado com `px.line` para mostrar a tendência das vendas.
