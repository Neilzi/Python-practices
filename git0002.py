#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sqlite3
import git0001
import mysql.connector
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class sqlcoupon(Base):
    #表名
    __tablename__='coupon'
    #表结构
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    sqlcoupon = Column(String(50), nullable=False)


# 初始化数据库连接:
engine = create_engine("mysql+mysqlconnector://root:Tuniu520@localhost:3306/test", echo=True)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

if __name__ == "__main__":
    session = DBSession()
    for x in range(10):
        for y in git0001.generate(20):
            sc = sqlcoupon(user_id=x, sqlcoupon=y)
            session.add(sc)
    session.commit()
    session.close()


