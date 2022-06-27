from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True, subdomain_matching=True)

# Change the localhost part to parvega.org
    app.config['SERVER_NAME']='localhost:5000'
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
#
#
#   Some thing happens here
#
#
    @app.route('/test')
    def testing():
        return "Testing"

    from . import admin, event, scitech, culturals
    app.register_blueprint(admin.bp, subdomain='admin')
    app.register_blueprint(event.blueprint, url_prefix="/events")
    app.register_blueprint(scitech.blueprint, url_prefix="/scitech")
    app.register_blueprint(culturals.blueprint, url_prefix="/culturals")

    return app
