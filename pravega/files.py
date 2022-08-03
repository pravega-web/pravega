from flask import Blueprint, flash, g, redirect, render_template, request, send_file

blueprint = Blueprint('files', __name__, url_prefix='/files')

@blueprint.route('/astrowiz/<filename>')
def sendastrowizfile(filename):
    return send_file(f'files/astrowiz/{filename}')

@blueprint.route('/enumeration/<filename>')
def sendenumeratuinwizfile(filename):
    return send_file(f'files/enumeration/{filename}')

@blueprint.route('/workshops/<filename>')
def sendeworkshopfile(filename):
    return send_file(f'files/workshops/{filename}')

@blueprint.route('/lasya/<filename>')
def sendlasyafile(filename):
    return send_file(f'files/lasya/{filename}')

@blueprint.route('/exhibitionrules')
def exhibitions():
    return redirect('https://drive.google.com/file/d/1WnQwrJ5zRxwsIKToOGP10GMpB3vSYESC/view?usp=drivesdk')

@blueprint.route('/<filename>')
def snedrandomunsafefile(filename):
    return send_file(f'files/{filename}')

@blueprint.route('/PravegaBrochure.pdf')
def downloadFile():
    return send_file('files/PravegaBrochure.pdf')
