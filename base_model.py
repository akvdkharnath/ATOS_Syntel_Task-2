#!/usr/bin/env python
# --coding:utf-8 --
'''
@File    :   run.py
@Time    :   2022/02/04 08:41:19
@Author  :   Harnath 
@Version :   1.0
@Contact :   akvdkharnath@gmail.com
@License :   © Copyright 2021 Harnath Atmakuri. All rights reserved
@Desc    :   base model for all table where will have common columns of all tables
'''

from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta, timezone
from database import engine

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class BaseTime(object):
    @classmethod
    def get_time(cls):
        """ returns current Indian datetime """
        utc_dt = datetime.now(timezone.utc) # UTC time
        hours_added = timedelta(hours = 5, minutes= 30)
        current_date_and_time = utc_dt + hours_added # IST time
        return current_date_and_time

class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    @declared_attr
    def created_datetime(cls):
        return Column(DateTime, default=BaseTime.get_time)

    @declared_attr
    def updated_datetime(cls):
        return Column(DateTime, default=BaseTime.get_time, onupdate=BaseTime.get_time)

    def __repr__(self):
        name = self.id
        return "{}('{}')".format(self.__class__.__name__, name)