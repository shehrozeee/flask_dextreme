import flask
import random
from flask import render_template,request

app = flask.Flask(__name__)

@app.route('/',methods=['GET','POST'])
def grid():
    if request.method == 'GET':
        a = []
        for i in range(1,random.randint(5,50)):
            row = {}
            row['id'] = i
            row['v1'] = random.randint(5,50)
            row['v2'] = random.randint(5,50)
            row['v3'] = random.randint(5,50)
            row['v4'] = random.randint(5,50)
            a.append(row)
        return render_template('ApiTesting.html',data = a)
    #since only get and post are allow and get is handled above, the next line only runs if there is a post request.
    print(request.form['keys'])


app.run(host="127.0.0.1",port=9020)
