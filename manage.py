from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config():
    # 项目的配置
    DEBUG = True

    # 数据库的配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information14"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app.config.from_object(Config)

db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'hello 3333'


if __name__ == '__main__':
    print(app.url_map)
    app.run()
