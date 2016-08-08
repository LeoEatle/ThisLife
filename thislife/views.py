#this file use encoding: utf-8


from thislife import app
from flask import render_template
#这里是要准备render的东西
from models import Image, User


@app.route("/")
def index():
    image = Image.query.order_by('id_dsec').limit(10).all()#把最新的图片选出来
    return render_template('index.html', image=image)