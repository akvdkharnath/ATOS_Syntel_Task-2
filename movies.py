#!/usr/bin/env python
# --coding:utf-8 --
'''
@File    :   run.py
@Time    :   2022/02/04 08:41:19
@Author  :   Harnath 
@Version :   1.0
@Contact :   akvdkharnath@gmail.com
@License :   © Copyright 2021 Harnath Atmakuri. All rights reserved
@Desc    :   movies table
'''
from base_model import BaseModel

from sqlalchemy import Column, String

class Movie(BaseModel):
    """ master table for asn Movies"""
    __tablename__ = 'movie'
    Title = Column(String(255), nullable=False)
    Year = Column(String(255))
    imdbID = Column(String(255))
    Type = Column(String(255))
    Poster  = Column(String(255))

