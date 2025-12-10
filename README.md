# Projeto IMDb Top 250 – Scraping, Banco de Dados e Análise com Python

Este projeto realiza scraping dos 250 filmes mais bem avaliados do IMDb, armazena os dados em um banco SQLite e realiza análises utilizando Pandas.  
Foi desenvolvido seguindo uma série de exercícios estruturados que incluem scraping, programação orientada a objetos, banco de dados e análise de dados.


## 📌 Funcionalidades Implementadas

### **1. Scraping do IMDb Top 250**
- Baixa o HTML da página do IMDb.
- Extrai título, ano e nota dos filmes.
- Converte os dados em objetos da classe `Movie`.

### **2. Hierarquia de Classes**
- `TV` (classe base)
- `Movie(TV)` com `rating`
- `Series(TV)` com `seasons` e `episodes`
- `__str__` implementado em todas as classes

### **3. Banco de Dados (`imdb.db`)**
Usando SQLAlchemy:
- Tabela `movies(id, title, year, rating)`
- Tabela `series(id, title, year, seasons, episodes)`
- Inserção com tratamento de duplicidade

### **4. Análise de Dados**
Com Pandas:
- Leitura das tabelas do banco
- Ordenação por nota
- Filtro de filmes com rating > 9.0
- Exportação para CSV e JSON
- Classificação das notas em categorias:
  - Obra-prima  
  - Excelente  
  - Bom  
  - Mediano  

### **5. Resumo por Categoria e Ano**
- Geração de tabela agrupada por categoria x ano.


