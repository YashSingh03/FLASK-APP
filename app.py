from flask import Flask, jsonify, request, render_template

app = Flask(__name__, template_folder='template')
tasks = [
    {
        'Contact': 1234567890,
        'Name': u'Abc',
        'Done': u'False',
        'ID': 1
    },
    {
        'Contact': 0987654321,
        'Name': u'Def',
        'Done': u'False',
        'ID': 2
    }
]


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data!"
        }, 400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status": "success",
        "message": "Task added successfully!"
    })


@app.route('/get-data')
def get_data():
    return jsonify({
        "data": tasks
    })


if __name__ == "__main__":
    app.run(debug=True)