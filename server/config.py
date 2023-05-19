# from flask_restful import Api
# from flask_migrate import Migrate
# from flask import Flask, abort
# from flask_sqlalchemy import SQLAlchemy
# import os



# app = Flask(
#     __name__,
#     static_url_path='',
#     static_folder='../client/build',
#     template_folder='../client/build'
# )


# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False


# # db = SQLAlchemy()
# migrate = Migrate(app, db)
# # db.init_app(app)
# # api = Api(app)