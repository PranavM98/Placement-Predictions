#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 01:05:25 2020

@author: pranavmanjunath
"""
   # Import train_test_split function
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier


def rf(data):
 
    X=data[['Admission_Entrance_Exam','Gender','Sem_1','Sem_2','Sem_3','Sem_4','Sem_5','Sem_6','Aggregate','Branch','10th%','12th%']]  # Features
    y=data[['Tier']]  # Labels
    
    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=126) # 70% training and 30% test
    
    sc=StandardScaler()
    X_train=sc.fit_transform(X_train)
    X_test=sc.transform(X_test)
    
    #Import Random Forest Model

    
    #Create a Gaussian Classifier
    clf_tier=RandomForestClassifier(n_estimators= 600,max_depth= 500,bootstrap=True,random_state=2)
    
    #Train the model using the training sets y_pred=clf.predict(X_test)
    clf_tier.fit(X_train,y_train)

    
    print(clf_tier.predict([[1,1,1,1,1,1,1,1,1,1,1,1]]))
    
    
    Y=data[['Company Type']]
    x=data[['Admission_Entrance_Exam','Gender','Sem_1','Sem_2','Sem_3','Sem_4','Sem_5','Sem_6','Aggregate','Branch','10th%','12th%']]  # Features
    x_train, x_test, Y_train, Y_test = train_test_split(x, Y, test_size=0.20, random_state=126) # 70% training and 30% test
    
    sc=StandardScaler()
    x_train=sc.fit_transform(x_train)
    x_test=sc.transform(x_test)
    
    
    clf_type=RandomForestClassifier(n_estimators= 600, max_depth= 500,bootstrap=True,random_state=2)
    
    #Train the model using the training sets y_pred=clf.predict(X_test)
    clf_type.fit(x_train,Y_train)

    
    

    return clf_tier,clf_type