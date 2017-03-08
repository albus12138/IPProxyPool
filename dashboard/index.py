# Dashboard for Proxies
from flask import Flask, request, render_template
from sqlalchemy import Column, String, create_engine, INTEGER
from sqlalchemy.orm import sessionmaker

import config
from db.SqlHelper import Proxy, BaseModel

app = Flask(__name__)


@app.route("/")
def index():
    engine = create_engine(config.DB_CONFIG["DB_CONNECT_STRING"])
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    sess = Session()
    query = sess.query(Proxy)
    num = len(query.all())
    return render_template("index.html", num=num)



@app.route("/list/<num>")
def list_page(num):
    pass


@app.route("/check", methods=["GET", "POST"])
def check():
    pass