# Santo Digital
### Desafio de Dados

## Linguagem utilizada para realização do desafio 0: 
* Python


## Linguagens e frameworks utilizados para a realização do desafio 1:
* Python;
* MySQL;
* Lucidchart;
* DBeaver.

### Passos realizados:
1. Analise básica dos CSVs disponibilizados;
2. Modelagem do Diagrama de Entidade-Relacionamento(Lucidchart);
3. Modelagem do Banco de Dados(MySQL Workbench);
4. Processos de ETL para modificação de datas para a forma aceita pelo MySQL;
5. Abastecimento do Banco de Dados via Python(Pandas, Numpy, mysql.connector);
6. Visualização dos dados pelo DBeaver(Optei pelo DBeaver por ele ter uma visualização dos dados selecionados mais clara);
7. Querys (DBeaver);
8. Utilização do Python para gerar os CSVs.


### Guia de diretórios:
* Desafio_0 -> Possui os 3 arquivos .py das questões;
* Desafio_1 -> Possui as pastas para cada ação feita (archive, DB, DER, Insert, Query);
* DB -> Possui o .sql com os códigos SQL feitos para a criação do banco e as querys;
* DER -> Possui um PDF do Diagrama;
* Insert -> Possui um código ETL.py utilizado para os processos de ETL e insert.py para o processo de inserção de dados;
* Query -> Possui um código query.py que puxa as querys e baixa os arquivos CSVs.

#### Pasta Archive
Existem alguns CSVs que estão na pasta archive que foram tratados. Logo, considere que todos os arquivos com "_tratado.csv" no nome, estão alterados.


# Dificuldades
### TABLE MISSING
Houve uma confusão quanto a uma das querys solicitadas, já que não existe uma tabela "salesman" ou "vendors" no banco da Adventure Works.
Houve uma outra confusão que foi "Qual seria a média para se tirar de base?".

* Solução tomada
A melhor solução encontrada foi substituir o pensamento de "vendedor" para "região" com mais vendas a cima da "média";
Como a query lista poucas regiões, preferi manter todas as regiões no arquivo para ter uma analise visual caso consiga a informação
da média posteriormente.

# Obrigado!