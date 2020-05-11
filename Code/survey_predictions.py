#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 13:23:02 2020

@author: pranavmanjunath
"""


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelBinarizer


from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score


def build(data):
    data_choice=data
    sc=StandardScaler()
         # Import train_test_split function
#,'Gender','Sem_1','Sem_2','Sem_3','Sem_4','Sem_5','Sem_6','Aggregate'
#'Gender','Sem_1','Sem_2','Sem_3','Sem_4','Sem_5','Sem_6','Aggregate','Branch','10th%','12th%',

#12,sem6,aggregate,10
         
############### GROWTH #########################
    X1=data[['Type ', 'Firm CTC']]  # Features

    y1=data[['Ability to Grow in the industry ']]  # Labels

    X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.20, random_state=66) # 70% training and 30% test
    
    
    
    X1_train=sc.fit_transform(X1_train)
    X1_test=sc.transform(X1_test)

    growth_clf=KNeighborsClassifier(n_neighbors=30,algorithm='auto')
    growth_clf.fit(X1_train,y1_train)




    
################ SATISFACTION ########################
    

    X3=data[['Type ', 'Firm CTC']]  # Features
    y3=data[['Satisfaction in your Company ']]  # Labels

    
    

    X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.20, random_state=66) # 70% training and 30% test
    

    X3_train=sc.fit_transform(X3_train)
    X3_test=sc.transform(X3_test)
    
    satisfaction_clf=KNeighborsClassifier(n_neighbors=30,algorithm='auto')
    satisfaction_clf.fit(X3_train,y3_train)






############### ADVICE #####################

    lb_make1 = LabelEncoder()
    data_choice['Satisfaction in your Company '] = lb_make1.fit_transform(data_choice['Satisfaction in your Company '])
    data_choice['Ability to Grow in the industry '] = lb_make1.fit_transform(data_choice['Ability to Grow in the industry '])



    #12,sem6,aggregate,10
    X2=data_choice[['Satisfaction in your Company ', 'Ability to Grow in the industry ']]  # Features
    y2=data_choice[['Choice']]

    
    
    X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.20, random_state=66) # 70% training and 30% test


    X2_train=sc.fit_transform(X2_train)
    X2_test=sc.transform(X2_test)
    
    
    choice_clf=KNeighborsClassifier(n_neighbors=50,algorithm='auto')
    choice_clf.fit(X2_train,y2_train)
    
    return growth_clf,choice_clf,satisfaction_clf

        
