# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import csv
from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
import json
# Reading data from .csv file and stroting in the variable ##
import os
import glob
import pandas as pd
import numpy as np

df = pd.read_csv(r"D:\GIT_Hub_Lakshnys\Flask_Black_Dashboard\flask_black_dashboard_work\test.csv")

dataLable1 = df['Month'].tolist() # Y-axis values from .csv file
dataTest1 = df["Energy_Generation"].tolist() # X-Axis values from .csv file
dataTest2 = df["Energy_Exported"].tolist() # X-Axis values from .csv file
dataTest3 = df["Energy_Consumed"].tolist() # X-Axis values from .csv file

### dataLable1 & dataTest1 hold the values from .csv file

test2 = ' 1237' # Variable trasnsfer to .html and js 
# dataTest1 = [60, 70, 80, 90, 100, 100,  100, 100, 110,110, 120, 120]

@blueprint.route('/index')
@login_required
def index(): 
    return render_template('home/index.html', segment='index', test2=test2, 
                                              dataLable1=json.dumps(dataLable1),
                                              dataTest1=json.dumps(dataTest1),
                                              dataTest2=json.dumps(dataTest2),
                                              dataTest3=json.dumps(dataTest3))# test2 variable tranfer to index.html

                                              

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
