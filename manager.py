#this file use encoding: utf-8

from thislife import app, db
from flask_script import Manager
from thislife.models import User, Image, Comment
from  sqlalchemy import or_, and_
import random

manager = Manager(app)

def get_image_url():
    # 随机生成图片
    return "http://images.nowcoder.com/head/" + str(random.randint) + ".png"


@manager.command
def init_database():
    db.drop_all()
    db.create_all()

    #添加初始的用户
    for i in range(0, 100):
        db.session.add(User('User' + str(i), 'a' + str(i)))
        for j in range(0, 3):
            db.session.add(Image(get_image_url(), i+1))
            for k in range(0, 3):
                db.session.add(Comment('This is a comment' + str(k), 1 + 3*i +j,i+1))
    db.session.commit()


    #把50到100的用户改名
    for i in range(50, 100, 2):
        user = User.query.get(i)
        user.username = '[New]' + user.username


    User.query.filter_by(id=50).update({"username":"[New2]"})



    #查询语句
    print 1, User.query.all()
    print 2, User.query.get(3)
    print 3, User.query.filter_by(id=5).first()
    #desc降序,offset偏移1,limit找两个
    print 4, User.query.order_by(User.id.desc()).offset(1).limit(2).all()
    print 5, User.query.filter(User.username.endwith('0')).limit(3).all()
    #如果去掉all,最后出来的是SQL语句
    print 6, User.query.filter(or_(User.id == 80, User.id == 99)).all()
     #ORM关联
    user = User.query.get(1)
    print 10, user.images
    image = Image.query.get(1)
    print 11, image.user


if __name__ == "__main__":
    manager.run()
