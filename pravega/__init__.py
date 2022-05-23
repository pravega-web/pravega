from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True, subdomain_matching=True)

# Change the localhost part to parvega.org
    app.config['SERVER_NAME']='localhost:5000'
#
#
#   Some thing happens here
#
#
    @app.route('/test')
    def testing():
        return "Testing"

    from . import admin
    app.register_blueprint(admin.bp, subdomain='admin')

    return app
