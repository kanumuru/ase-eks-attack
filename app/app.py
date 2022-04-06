

from flask import Flask, render_template, request
import os

import subprocess

app = Flask(__name__)
data =[]

@app.route("/", methods=["GET","POST"])
def get_email():
    temp = ""
    if request.method == "GET":

        return render_template("email.html",data=temp)

    if request.method == "POST":
        if request.form.get("email"):
            emailurl = request.form.get("email")
            print(emailurl)
            email =  request.form.get("email") + " has succesfully subscribed to APPsecengineer"
            process = subprocess.Popen(['curl', str(emailurl)], stdout=subprocess.PIPE)
            temp = process.communicate()[0] 
        else:
            print("Empty string")
            temp =  "please enter valid E-mail Address"
        
        
        return render_template("email.html",data=temp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)