from flask import Flask,render_template,request,redirect,url_for
from app import app
from os import path
import os
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import math 
from mpmath import *
from scipy import interpolate
from scipy.interpolate import interp1d
import scipy.io
import csv 
import xlsxwriter
@app.route('/',methods =['GET','POST'])
def upload():
    return render_template('index.html')

@app.route('/step2',methods =['GET','POST'])
def step2():
    if request.method=='POST':
        f = request.files['file']
        name = f.filename
        type_file = name.split(".")[-1]
        if type_file == "csv" or type_file == "txt":
            type_file = "n"
        else:
            type_file = "y" 
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath,'static/Database',f.filename)
        upload_path = os.path.abspath(upload_path)
        f.save(upload_path)
        global period,x,y,lowercutoff,uppercutoff
        period = request.form.get("designperiod")
        x = request.form.get("unitx")
        y = request.form.get("unity")
        lowercutoff = request.form.get("lowercutoff")
        uppercutoff = request.form.get("uppercutoff")
        return redirect(url_for("step3"))
    return render_template('step2.html')

@app.route('/step3',methods =['GET','POST'])
def step3():
    if request.method == "POST":
        global technology,doi,orientationsize,modemotion,method,characteristic,submerged,depth
        technology = request.form.get("technology")
        doi = request.form.get("doi")
        orientationsize = request.form.get("orientationsize")
        modemotion = request.form.get("modemotion")
        method = request.form.get("method")
        characteristic = request.form.get("characteristic")
        submerged = request.form.get("submerged")
        depth = request.form.get("submerged")
        return redirect(url_for("step4"))
    return render_template('step3.html')

@app.route('/step4')
def step4():
    
    return render_template('step4.html')

@app.route('/step5')
def step5():
    return render_template('step5.html')

@app.route('/step6')
def step6():
    return render_template('step6.html')



