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
            email = request.form.get("email")
            print(email)
            temp =  request.form.get("email") + " has succesfully subscribed to APPsecengineer"
            process = subprocess.Popen(['curl', email,'-H',header], stdout=subprocess.PIPE)
            print(process)
        else:
            print("Empty string")
            temp =  "please enter valid E-mail Address"
        # subprocess.run(["python3", "-c",email])
        
        
        return render_template("email.html",data=process)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)
