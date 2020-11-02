# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 11:25:23 2020

@author: sayan
"""

from flask import Flask,render_template

app = Flask(__name__)
#app._static_folder = "D:/Web Design/Avocado/static/styles"

@app.route('/')
def idx():
    return render_template("index.html")


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
    
    
