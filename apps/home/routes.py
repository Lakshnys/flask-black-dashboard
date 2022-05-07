# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
import json

test2 = ' 1237' # Variable trasnsfer to .html and js 
dataTest1 = [60, 70, 80, 90, 100, 100,  100, 100, 110,110, 120, 120]

@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index', test2=test2, dataTest1=json.dumps(dataTest1)) # test2 variable tranfer to index.html

@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            pass

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
