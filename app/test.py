from flask import Flask,request, render_template

import subprocess
app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('home.html')
    
@app.route('/' , methods=['POST'])
def my_form_post():
#  url= request.form['url']
#  header=request.form['header']
 process = subprocess.Popen(['curl', 'rajesh@gmail.com'], stdout=subprocess.PIPE)
 process = subprocess.Popen(['curl', 'http://169.254.169.254/latest/meta-data/iam/security-credentials/testssrf'], stdout=subprocess.PIPE)
 stdout = process.communicate()[0]    
 return stdout

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 4000, debug = True)