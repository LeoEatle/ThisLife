#this file use encoding: utf-8

from thislife import db
from  datetime import datetime
import random

#用户
class User(db.Model):
    #创建数据库辣
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(32))
    head_url = db.Column(db.String(256))
    #与图片产生关联
    #backref反向关联
    images = db.relationship("Image", backref="user", lazy="dynamic")


    def __init__(self, username, password):
        self.username = username
        self.password = password
        #随机生成图片
        self.head_url = "http://images.nowcoder.com/head/" + str(random.randint) + ".png"

    def __repr__(self):
        return '<User %d %s>' % (self.id, self.username)

#图片
class Image(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    url = db.Column(db.String(512))
    userid = db.Column(db.Integar, db.ForeignKey('user.id'))
    create_date = db.Column(db.DateTime)

    def __init__(self, url, userid):
        self.url = url
        self.userid = userid
        self.create_date = datetime.now()

    def __repr__(self):
        return '<Image %d %s>' % (self.id, self.url)

#评论
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    content = db.Column(db.String(1024))
    image_id = db.Column(db.ForeignKey("image.id"))
    user_id = db.Column(db.ForeignKey("user.id"))
    status = db.Column(db.Integar, default = 0) #正常 0 #删除 1
    user = db.relationship('User')

    def __init__(self, content, imageid, userid):
        self.content = content
        self.image_id = imageid
        self.userid = userid

    def __repr__(self):
        return '<Comment %d %s>' % (self.id, self.content)






