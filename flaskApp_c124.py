from flask import Flask, jsonify, request
app = Flask(__name__)

#@app.route("/")

#def hello_world():
#    return "hello world"

#if(__name__ == "__main__"):
#    app.run(debug = True)

#creating an array of tasks with each task as a different object in it
tasks = [
    {
        'id':1,
        'name': u'jay', 
        'contact': u'1231231234',
        'contacted': False
    }, 
    {
        'id':2,
        'name': u'joe',
        'contact': u'4321321321',
        'contacted': False
    }
]

@app.route("/")

def hello_world():
    return "this is contact flask app"

@app.route("/add-data", methods = ["POST"])

def add_task():
    if(not request.json):
        return jsonify({
            'status':"error",
            'message':'please provide the contact info'
        },
        400)

    task = {
        'id':tasks[-1]['id']+1,
        'name':request.json['name'],
        'contact':request.json.get('contact',""),
        'contacted':False
    }

    tasks.append(task)
    return jsonify({
        'status':"success",
        'message':"contact added successfully"
    })

@app.route("/get-data")

def get_task():
    return jsonify({
        'data':tasks
    })

if(__name__ == "__main__"):
    app.run(debug = True)