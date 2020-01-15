# coding:utf-8
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, Text, DateTime,\
    and_, or_, SmallInteger, Float, DECIMAL, desc, asc, Table, join, event
from sqlalchemy.orm import relationship, backref, sessionmaker, scoped_session, aliased, mapper
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from sqlalchemy.orm.collections import attribute_mapped_collection
import datetime

engine_ini = create_engine("mysql://root:123456@127.0.0.1:3306", pool_recycle=7200)
engine_ini.execute("CREATE DATABASE blog01 CHARACTER SET utf8 COLLATE utf8_general_ci") #create db

engine = create_engine("mysql://root:123456@127.0.0.1:3306/blog01?charset=utf8", pool_recycle=7200)

Base = declarative_base()

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base.query = db_session.query_property()


class User(Base):
    __tablename__ = 'user'

    id = Column('id', Integer, primary_key=True)
    phone_number = Column('phone_number', String(11), index=True)
    password = Column('password', String(30))
    nickname = Column('nickname', String(30), index=True, nullable=True)
    register_time = Column('register_time', DateTime, index=True, default=datetime.datetime.now)


if __name__ == '__main__':
    Base.metadata.create_all(engine)



'''
MySQL [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| blog01             |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.00 sec)

MySQL [(none)]> use blog01
Database changed
MySQL [blog01]> show tables;
+------------------+
| Tables_in_blog01 |
+------------------+
| user             |
+------------------+
1 row in set (0.00 sec)

MySQL [blog01]> desc user
    -> ;
+---------------+-------------+------+-----+---------+----------------+
| Field         | Type        | Null | Key | Default | Extra          |
+---------------+-------------+------+-----+---------+----------------+
| id            | int(11)     | NO   | PRI | NULL    | auto_increment |
| phone_number  | varchar(11) | YES  | MUL | NULL    |                |
| password      | varchar(30) | YES  |     | NULL    |                |
| nickname      | varchar(30) | YES  | MUL | NULL    |                |
| register_time | datetime    | YES  | MUL | NULL    |                |
+---------------+-------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)
'''    
