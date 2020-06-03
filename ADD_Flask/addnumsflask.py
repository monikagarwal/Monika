# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 23:00:40 2020

@author: nsriram
"""


from flask import Flask,request

app=Flask(__name__)
@app.route('/add')


   

@app.route('/add', methods=['GET','POST'])
def add():
    
    """
    parameters:
        - name: input1
          in: formData
          type: file
          required: true
        - name: input2
          in: formData
          type: file
          required: true
    """
    if request. method == "GET":
        a=request.args.get("a")
        b=request.args.get("b")
        return str( int(a) + int(b) )
    if request. method == "POST":
        a=request.form["input1"]
        b=request.form["input2"]
        return str( int(a) + int(b) )
if __name__== '__main__':
    app.run()
    