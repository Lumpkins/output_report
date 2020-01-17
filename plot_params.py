# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 20:59:22 2019

@author: jclum
"""

from enum import Enum

class ePlot_type(Enum):
    line = 1
    bar = 2
    scatter = 3
    candlestick=4
    table=5
    text=6
    histogram=7
    span=8


class eLine_style():
    solid=0
    dashed=1
    none=2
    dash_dot=3
    def __init__(self, ype):
        self.value = ype
    def __str__(self):
        if self.value == eLine_style.solid:
            return ''
        if self.value == eLine_style.dashed:
            return '--'
        if self.value == eLine_style.none:
            return ' '
        if self.value == eLine_style.dash_dot:
            return '-.'
    def __eq__(self,y):
       return self.value==y.value


class eColor():
    default=0
    blue=1
    green=2
    red=3
 #   'c','m','y'

    black=4
    white=5
    yellow=6
    def __init__(self, Type):
        self.value = Type
    def __str__(self):
        if self.value == eColor.default:
            return ''
        if self.value == eColor.blue:
            return 'b'
        if self.value == eColor.green:
            return 'g'
        if self.value == eColor.red:
            return 'r'
        if self.value == eColor.black:
            return 'k'
        if self.value == eColor.white:
            return 'w'
        if self.value == eColor.yellow:
            return 'y'




    def __eq__(self,y):
       return self.value==y.value