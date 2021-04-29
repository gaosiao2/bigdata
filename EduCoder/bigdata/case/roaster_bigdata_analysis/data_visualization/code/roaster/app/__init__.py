from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:123456@127.0.0.1:3306/roaster"

# 设置每次请求结束后会自动提交数据库的改动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 打印执行 sql 语句
# app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

def crate_app(config_name):
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .views import index as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
