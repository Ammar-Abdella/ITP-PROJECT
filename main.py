from flask import Flask,render_template,request,send_from_directory
from datetime import datetime as dt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy.orm import Mapped, mapped_column,DeclarativeBase


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///itp-project.db"
db.init_app(app)


class Data(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    body:Mapped[str]
    img:Mapped[str]


# with app.app_context():
#     book_to_update = Data.query.filter_by(id=2).first()
#     book_to_update.img = "./../static/images/pic012.jpg"
#     db.session.commit()  

# with app.app_context():
#     book_to_update = Data.query.filter_by(id=3).first()
#     book_to_update.img = "./../static/images/pic013.jpg"
#     db.session.commit()  

# with app.app_context():
#     book_to_update = Data.query.filter_by(id=4).first()
#     book_to_update.img = "./../static/images/pic014.jpg"
#     db.session.commit()  


# with app.app_context():
#     book_to_update = Data.query.filter_by(id=5).first()
#     book_to_update.img = "./../static/images/pic015.jpg"
#     db.session.commit()  


date=dt.now().date()


@app.route("/")
def home_page():

    return render_template('index.html',date=date)

@app.route("/show case/<id>")
def projects(id):
    data = Data.query.filter_by(id =id).first()
    return render_template("showcase.html",data=data )


@app.route("/Download")
def PDF():
    return send_from_directory(directory='static',path='files/ITP_PDF.pdf')



if __name__=="__main__":
    app.run(debug=True)