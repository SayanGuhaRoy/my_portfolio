# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 11:25:23 2020

@author: sayan
"""

from flask import Flask,render_template,send_file

app = Flask(__name__)
#app._static_folder = "D:/Web Design/Avocado/static/styles"

@app.route('/')
def idx():
    return render_template("index.html")

@app.route('/download_cv')
def download_cv():
    p = "Sayan_Guha_Roy_Resume.pdf"
    return send_file(p)

if __name__=='__main__':
    app.run(port=3000)
    
    
