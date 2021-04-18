# weather
Projeto criado para teste de conhecimento

### Instalação

```
 >   sudo apt-get install python-virtualenv
 >   python3 -m venv venv
```
Para ativar o ambiente
```
 >   . venv/bin/activate 
```

O arquivo requeriments.txt tem algumas bibliotecas para rodar a aplicação, o comando a seguir irá instalar todos.
```
 >   vemv/bin/pip3 install -r requeriments.txt
```
Para entrar no venv (ambiente) roda esse comando
```
>    venv/bin/python3 run.py
```
## Banco de dados
Para criar terá que executar o camponado do docker
```
    docker-composer up -d
``` 
Em segioda execute os comandos que estão no [arquivo](https://github.com/lucasmirandadourado/weather/blob/main/tables.md)

Para ver os Endpoints criados importe para o Postman o arquivo anexado com o nome:
#### Desafio Linx.postman_collection.json

O sistema foi desenvolvida em um micro-framework chamado Flask. Ele é um framework desenvolvido em Python e considerado muito simples e vem com poucos recursos como por exemplo biblioteca para conexão ao Banco de dados.

Por esse motivo que foi usado o psycopg2. 

O projeto foi criado com as seguinte estrutura de pastas: 
 
 - Controllers
 - services (regra de negocio)
 - repositorys (Realiza consultas com o banco de dados)
 - models (Onde estarão as entidades)
 - test 

Veja o diagrama de [pacotes](Weather.png)

