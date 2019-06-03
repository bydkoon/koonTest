# _*_ coding: utf-8 _*_
from flask_restful import abort, Api,Resource
from flask import Flask
from flask import request
from flask import render_template
from flask import json
from app import app

class TestCase(Resource):
    def tag(self):
        if request.method == 'POST':
            values = request.form
            test = values['test']

            response = app.response_class(
                response=json.dumps(test),
                status=200,
                mimetype='application/json'
            )

            return response