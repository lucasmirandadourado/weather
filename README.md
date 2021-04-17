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
Em segioda execute os comandos que estão no [arquivo]](tables.md)