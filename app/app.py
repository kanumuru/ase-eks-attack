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
            command = ["python", "-c", str(emailurl)]
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            temp = "Successfully subscribed to the AppSecEngineer newsletter"
        else:
            print("Empty string")
            temp =  "please enter valid E-mail Address"

        return render_template("email.html",data=temp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
