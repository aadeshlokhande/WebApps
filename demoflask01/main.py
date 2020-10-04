from flask import Flask,request
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "this is post method"
    else:
        return "this is get method"
app.run(debug=True)