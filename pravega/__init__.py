from flask import Flask, render_template, send_file, redirect


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True, subdomain_matching=True)

# Change the localhost part to parvega.org
    app.config['SERVER_NAME']='localhost:5000'
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    # Set the captcha height and width
#
#
#   Some thing happens here
#
#
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/aboutus')
    def aboutus():
        return render_template('aboutus.html')

    @app.route('/refund')
    def sendrefund():
        return send_file('files/refund.pdf')
    @app.route('/privacy')
    def sendprivacy():
        return send_file('files/privacy.pdf')
    @app.route('/terms')
    def sendterms():
        return send_file('files/terms of service.pdf')

    @app.route('/tester')
    def test():
        return render_template("registration_message.html");

    @app.route('/validate')
    def validate():
        return render_template("validate.html")

    @app.route('/merch')
    def merchandise():
        return render_template("merch.html")
    
    @app.route('/cong')
    def cong():
        return render_template("cong.html")
    
    @app.route('/rats')
    def rats():
        return render_template("rats.html")

    @app.route('/congrats')
    def congrats():
        return render_template("congrats.html")
 

    from . import admin
    app.register_blueprint(admin.bp, subdomain='admin')
    from . import scitech
    app.register_blueprint(scitech.blueprint)
    from . import culturals
    app.register_blueprint(culturals.blueprint)
    from . import workshops
    app.register_blueprint(workshops.blueprint)
    from . import recreational
    app.register_blueprint(recreational.blueprint)
    from . import speakers
    app.register_blueprint(speakers.blueprint)
    from . import files
    app.register_blueprint(files.blueprint)



    return app
