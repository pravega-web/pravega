from flask import Flask, render_template, send_file

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True, subdomain_matching=True)

# Change the localhost part to parvega.org
#    app.config['SERVER_NAME']='localhost:5000'
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
#
#
#   Some thing happens here
#
#
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/files/PravegaBrochure.pdf')
    def downloadFile():
        return send_file('files/PravegaBrochure.pdf')


    from . import admin
    app.register_blueprint(admin.bp, subdomain='admin')
    from . import scitech
    app.register_blueprint(scitech.blueprint)
    from . import culturals
    app.register_blueprint(culturals.blueprint)
    from . import workshops
    app.register_blueprint(workshops.blueprint)



    return app
