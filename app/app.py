from flask import Flask, render_template, request
import os
import redis
import subprocess

app = Flask(__name__)
data =[]


# redisClient = redis.StrictRedis(host=os.getenv('redisip'),port=6379,db=0,decode_responses=True)
redisClient = redis.StrictRedis(host='localhost',port=6379,db=0,decode_responses=True)

@app.route("/", methods=["GET","POST"])
def get_email():
    if request.method == "GET":

        return render_template("email.html")

    if request.method == "POST":
        if request.form.get("email"):
            query = "email*"
            keys = redisClient.keys(query)
            for j in keys:
                if redisClient.get(j) == request.form.get("email"):
                    temp =  request.form.get("email") + " has already part of  APPsecengineer subscription"
                    return render_template("email.html",data=temp)
            
            if len(keys)<=0:
                keyid=1
            else:
                keyid=len(keys)+1
            count="email"+str(keyid)
            redisClient.set(count, request.form.get("email"))
        email = request.form.get("email")
        print(email)
        temp =  request.form.get("email") + " has succesfully subscribed to APPsecengineer"

        subprocess.run(["python3", "-c",email])

        
        return render_template("email.html",data=temp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
