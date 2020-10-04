from flask import Flask, render_template
# from flask_sqlalchemy import sqlalchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/techinsecond'
# db = sqlalchemy(app)
#
# class Contact(db.Model):
#     # sno, name, phone_num, mes, date, email
#     sno = db.Column(db.Integer, primery_key = True)
#     name = db.Column(db.String(80), nullable = False)
#     phone_num = db.Column(db.String(12), nullable = False)
#     mes = db.Column(db.String(120), nullable = False)
#     date = db.Column(db.String(12), nullable = False)
#     email = db.Column(db.String(20),  nullable = False)
#


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/post")
def post():
    return render_template('post.html')



app.run(debug= True )