#!/usr/bin/env python
# --coding:utf-8 --
'''
@File    :   run.py
@Time    :   2022/02/04 08:41:19
@Author  :   Harnath 
@Version :   1.0
@Contact :   akvdkharnath@gmail.com
@License :   © Copyright 2021 Harnath Atmakuri. All rights reserved
@Desc    :   database connections
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = 'sqlite:///movie.db'

engine = create_engine(DATABASE_URL, echo = True)
