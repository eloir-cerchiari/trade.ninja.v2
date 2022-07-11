# trade.ninja

_Atualmente está __Em Desenvolvimento__, não use para investir o seu dinheiro_

Projeto com o intuito de Aprendizagem da Linguagem Python, juntamento com o framework flask.

A proposta do software é indicar a compra ou venda de papéis(symbols) ou ativos listados em bolsas ou exchanges, de acordo com indicadores técnicos.

## Estou usando os seguintes links como base para a aprendizagem:
* Eduardo Mendes
  * <https://github.com/dunossauro/crudzin/> 
  * <https://www.youtube.com/watch?v=WzaKIRJBGXo>

* Hedgar Bezerra
  * <https://medium.com/@hedgarbezerra35/api-rest-com-flask-autenticacao-25d99b8679b6>
  * <https://github.com/hedgarbezerra/Another-FlaskAPI>

## Passos para usar o software

* Instalar as dependencias do projeto 
    ~~~
    $ pip install flask-sqlalchemy marhmallow-sqlalchemy flask_marshmallow flask-migrate
    ~~~
* Cria o banco de dados, versiona e atualiza a versão
    ~~~
    $ flask db init
    $ flask db migrate
    $ flask db upgrade
    ~~~
* Rodar a aplicação
    ~~~
    ./trade_env/bin/python ./run.py 
    ~~~
