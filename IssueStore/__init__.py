# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template, jsonify

from IssueStore.blueprints.api_v1.api import api_v1

def create_app():

    app = Flask('IssueStore')
    register_blueprints(app)
    return app



def register_blueprints(app):
    app.register_blueprint(api_v1, url_prefix='/api/v1')


def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({
            "result": "Not Found This Page.",
            "code": "404"
        })
    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({
            "result": "Not Found This Page.",
            "code": "404"
        })
    
    @app.errorhandler(500)
    def service_error(e):
        return jsonify({
            "result": "Server Error.",
            "code": "500"
        })

if __name__ == '__main__':
    app = create_app()
    app.run()