# Mini Painel de Controle de Vendas 📊

Este projeto foi desenvolvido como parte de um desafio técnico para criar um dashboard interativo de vendas utilizando dados da base **AdventureWorks**. O objetivo é fornecer um painel que permita aos usuários filtrar e visualizar informações detalhadas sobre as vendas.

## Sumário

- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Demonstração](#demonstração)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Executar o Projeto](#como-executar-o-projeto)
- [Query SQL](#query-sql)
- [Detalhes Técnicos Importantes](#detalhes-técnicos-importantes)

## Descrição

Este painel permite que os usuários filtrem dados de vendas por ano, mês, país, estado, cidade e produto. As informações são obtidas a partir de um arquivo **CSV** que contém os dados extraídos da base **AdventureWorks**. A conexão com o banco de dados foi utilizada para realizar a extração dos dados, porém, para este projeto, eles foram salvos no formato **CSV** para facilitar o desenvolvimento e execução sem a necessidade de uma conexão direta com o banco de dados.

Além disso, o painel exibe:

- **Total de Vendas**: KPI, com total de vendas no período selecionado.
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
- **SQL Server**: Utilizado para a extração de dados da base AdventureWorks.

## Como Executar o Projeto

### Pré-requisitos

- Python 3.x instalado.
- Instalar as bibliotecas necessárias:
  ```bash
  pip install pandas plotly streamlit pyodbc
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
3. **Utilização do CSV**:
   - Os dados de vendas foram salvos em um arquivo CSV localizado no repositório, o qual é carregado diretamente para o painel:
   ```python
   url = "https://raw.githubusercontent.com/seu-usuario/seu-repositorio/master/vendas.csv"
   df = pd.read_csv(url)
   ```

4. **Execute o aplicativo Streamlit**:
   ```bash
   streamlit run app.py
   ```

5. **Acesse o painel**:
   Abra o navegador e vá para `http://localhost:8501` (ou o endereço fornecido pelo Streamlit).

## Query SQL

Aqui está a query que criei para coletar os dados do banco **AdventureWorks**, antes de serem salvos no arquivo CSV:

```sql
SELECT
    -- Informações do pedido
    FORMAT(soh.OrderDate, 'dd/MM/yyyy') AS Data_Pedido,     -- Data do pedido formatada (dd/mm/yyyy)
    FORMAT(sod.LineTotal, 'N', 'pt-BR') AS ValorVenda,      -- Valor da venda formatado no padrão brasileiro

    -- Informações de envio
    addr.City AS Cidade,                                    
    sp.Name AS Estado,                                      
    cr.Name AS Pais,                                        

    -- Informações do produto
    prod.Name AS NomeProduto                                

FROM
    Sales.SalesOrderHeader AS soh                           

-- do pedido
INNER JOIN Sales.SalesOrderDetail AS sod 
    ON soh.SalesOrderID = sod.SalesOrderID                  

-- os produtos
INNER JOIN Production.Product AS prod 
    ON sod.ProductID = prod.ProductID                       

-- endereço de envio
INNER JOIN Person.Address AS addr 
    ON soh.ShipToAddressID = addr.AddressID                 

-- estado
INNER JOIN Person.StateProvince AS sp 
    ON addr.StateProvinceID = sp.StateProvinceID            

-- país
INNER JOIN Person.CountryRegion AS cr 
    ON sp.CountryRegionCode = cr.CountryRegionCode;
```

## Fluxograma da Query

Fluxograma lógico da query :

![image](https://github.com/user-attachments/assets/69fba4de-0d18-427e-a4cc-87fe4da4b9cf)


## Detalhes Técnicos Importantes

- **Carregamento dos Dados**:
  - Os dados de vendas foram carregados a partir de um arquivo CSV, que foi extraído anteriormente do banco de dados **AdventureWorks** via uma conexão SQL Server.
  - A query SQL foi otimizada para trazer as informações de data, valor de vendas, região de envio e produto.

- **Processamento dos Dados**:
  - Conversão de strings para datas e formatação dos valores monetários para o padrão decimal do BR.
  - Criação de colunas adicionais no Frame para facilitar os filtros.

- **Construção dos Filtros**:
  - Os filtros são implementados usando `st.sidebar.multiselect`, permitindo múltiplas seleções.
  - A atualização dos filtros é encadeada; por exemplo, os estados disponíveis dependem do país selecionado.

- **Visualizações**:
  - **Total de Vendas**: Exibido usando `st.metric` com formatação personalizada para o padrão brasileiro.
  - **Gráfico de Barras (Vendas por Produto)**: Criado com `px.bar` e exibido com `st.plotly_chart`.
  - **Gráfico de Linhas (Vendas ao Longo do Tempo)**: Criado com `px.line` para mostrar a tendência das vendas.
