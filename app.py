# _*_ coding: utf-8 _*_
from flask import Flask
from flask import request
from flask import render_template
from flask import json
import settings
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import abort, Api


app = Flask(__name__)

# app.config.from_object(settings)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# api = Api(app)

# class TT(resource):
#     def get(self):
#         return render_template('default.html')

@app.route('/app', methods=['GET','POST'])
def form_request():
    if request.method == 'GET':
        return render_template('default.html')

    if request.method == 'POST':
        values = request.form
        test = values['test']

        response = app.response_class(
            response=json.dumps(test),
            status=200,
            mimetype='application/json'
        )

        return response


if __name__ == '__main__':
    app.debug = True
    app.run(port=8080)


