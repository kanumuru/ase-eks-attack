from flask import Flask, render_template, request
import os

import subprocess

app = Flask(__name__)
data =[]

@app.route("/", methods=["GET","POST"])
def get_email():
    if request.method == "GET":

        return render_template("email.html")

    if request.method == "POST":
        if request.form.get("email"):
            email = request.form.get("email")
            print(email)
            temp =  request.form.get("email") + " has succesfully subscribed to APPsecengineer"
        else:
            print("Empty string")
            temp =  "please enter valid E-mail Address"
        subprocess.run(["python3", "-c",email])

        
        return render_template("email.html",data=temp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
