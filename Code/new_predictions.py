#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 01:19:23 2020

@author: pranavmanjunath
"""


#gender.get(),admission.get(),branch.get(),ten.get(),twe.get(),sem_1.get(),sem_2.get(),sem_3.get(),sem_4.get(),sem_5.get(),sem_6.get(),agg.get()]

#X=data[['Admission_Entrance_Exam','Gender','Sem_1','Sem_2','Sem_3','Sem_4','Sem_5','Sem_6','Aggregate','Branch','10th%','12th%']]  # Features

def predict(gender,admission,branch,ten,twe,sem1,sem2,sem3,sem4,sem5,sem6,agg,clf_tier,clf_type):

    
    if gender=='Female':
        g=0
    else:
        g=1
    
    
    #print("gender:"+g)
    
    if admission=='CET':
        ad=0
    elif admission=='COMED-K':
        ad=1
    else:
        ad=2
        
    if branch=='CSE':
        b=0
    elif branch=='ISE':
        b=2
    elif branch=='ECE':
        b=1
    else:
        b=3
    
    tier=clf_tier.predict([[ad,g,sem1,sem2,sem3,sem4,sem5,sem6,agg,b,ten,twe]])
    typea=clf_type.predict([[ad,g,sem1,sem2,sem3,sem4,sem5,sem6,agg,b,ten,twe]])
    
    ti=tier[0]
    ty=typea[0]
    
    print("PRINT: "+ty)
    
    return ti,ty