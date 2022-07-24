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
    @app.route('/files/PravegaBrochure.pdf')
    def downloadFile():
        return send_file('files/PravegaBrochure.pdf')

    @app.route('/tester')
    def test():
        return render_template("registration_message.html");

    @app.route('/files/acc.pdf')
    def acc():
        return send_file('files/acc.pdf')

    @app.route('/files/wwdd_brochure.pdf')
    def wwddBrochure():
        return send_file('files/wwdd_brochure.pdf')

    @app.route('/files/exhibitionrules')
    def exhibitions():
        return redirect('https://drive.google.com/file/d/1WnQwrJ5zRxwsIKToOGP10GMpB3vSYESC/view?usp=drivesdk')

    @app.route('/files/QuadsparksSeason3Rules.pdf')
    def quadsparkskimaki():
        return send_file('files/QuadsparksSeason3Rules.pdf')
    @app.route('/files/ALEKHYA-Art.pdf')
    def alekhyaaaaaaa():
        return send_file('files/ALEKHYA-Art.pdf')

    @app.route('/files/Details_Decalcomania.pdf')
    def deeeeeeeeecalllllllcooooooo():
        return send_file('files/Details_Decalcomania.pdf')

    @app.route('/files/chemenigmarules.pdf')
    def chemenigmakimaki():
        return send_file('files/chemenigmarules.pdf')

    @app.route('/files/QuadsparksModelQuestions.pdf')
    def quadsparkssamplepaper():
        return send_file('files/QuadsparksModelQuestions.pdf')

    @app.route('/files/qsacRules.pdf')
    def chesskimaki():
        return send_file('files/qsacRules.pdf')

    @app.route('/files/BAH_Brochure.pdf')
    def bahkimaki():
        return send_file('files/BAH_Brochure.pdf')

    @app.route("/files/Robowars_Rules.pdf")
    def ragnarokkimaki():
        return send_file('files/Robowars_Rules.pdf')
    @app.route('/files/<filename>')
    def snedrandomunsafefile(filename):
        return send_file(f'files/{filename}')

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



    return app
