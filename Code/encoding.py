#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 00:50:14 2020

@author: pranavmanjunath
"""

import pandas as pd
import numpy as np



from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelBinarizer


def enc(data):
    #BRANCH
    
    lb_make = LabelEncoder()
    data["Branch"] = lb_make.fit_transform(data["Branch"])
    #Mechanical:3
    #ISE:2
    #CSE:0
    #ECE:1
    
    
    data["Admission_Entrance_Exam"]=lb_make.fit_transform(data["Admission_Entrance_Exam"])
    #print(data[['Admission_Entrance_Exam1','Admission_Entrance_Exam']].head(11))
    #CET:0
    #COMEDK:1
    #MANAGEMENT:2
    
    data["Sem_1"]=lb_make.fit_transform(data["Sem_1"])
    data["Sem_2"]=lb_make.fit_transform(data["Sem_2"])
    data["Sem_3"]=lb_make.fit_transform(data["Sem_3"])
    data["Sem_4"]=lb_make.fit_transform(data["Sem_4"])
    data["Sem_5"]=lb_make.fit_transform(data["Sem_5"])
    data["Sem_6"]=lb_make.fit_transform(data["Sem_6"])
    data["Aggregate"]=lb_make.fit_transform(data["Aggregate"])
    data["10th%"]=lb_make.fit_transform(data["10th%"])
    data["12th%"]=lb_make.fit_transform(data["12th%"])
    
    
    #FC:0
    #FCD:1
    #SC:2
    
    #data["Sem_1"]=lb_make.fit_transform(data["Sem_1"])
    #print(data[['Sem_11','Sem_1']].head(11))
    
    
    
    lb_style = LabelBinarizer()
    data["Gender"] = lb_style.fit_transform(data["Gender"])
    
    #male:1
    #female:0
    
    return data
    
