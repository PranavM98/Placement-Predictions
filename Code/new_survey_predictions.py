#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 13:50:34 2020

@author: pranavmanjunath
"""
#Very Satisfied:2
#Satisfied:1
#Not Satisfied:0

#Huge Growth:0
#Mid Growth:2
#Low Growth:1


def predict(tier,typea,growth_clf,choice_clf,satisfaction_clf):
    
    
    if typea=='MNC':
        ta=0
    else:
        ta=1
        
    gr=growth_clf.predict([[ta,tier]])
       
    sa=satisfaction_clf.predict([[ta,tier]])
    
    g=gr[0]
    s=sa[0]
    
    print(g)
    print(s)
    
    
    
    if g=='High Growth':
        ga=0
        
    elif g=='Mid Growth':
        ga=2
        
    else:
        ga=1
    
    if s=='Very Satisfied':
        sa=2
        
    elif s=='Satisfied':
        sa=1
        
    else:
        sa=0
    
    
    
    ch=choice_clf.predict([[sa,ga]])
    c=ch[0]
     
    
    return g,c,s
    