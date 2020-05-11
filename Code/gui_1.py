#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:52:44 2020

@author: pranavmanjunath
"""
from tkinter import *
#from tkinter import Label
#import tkinter as tk
from PIL import ImageTk,Image 


import webbrowser


#https://pesitsouth.pes.edu/department/computer-science/



def opencse():
    new = 1
    url = "https://pesitsouth.pes.edu/department/computer-science/"
    webbrowser.open(url,new=new)


def openise():
    new = 1
    url = "https://pesitsouth.pes.edu/department/information-science/"
    webbrowser.open(url,new=new)



def openmech():
    new = 1
    url = "https://pesitsouth.pes.edu/department/mechanical/"
    webbrowser.open(url,new=new)



def openece():
    new = 1
    url = "https://pesitsouth.pes.edu/department/electronics/"
    webbrowser.open(url,new=new)







def newWindow(app):
    #app.title("PES Placement Statistics")
    title1 = ('Helvetica', 45,'bold italic')
    bg1_color='MistyRose2'
    app.configure(background=bg1_color)
    
    #root.attributes("-fullscreen", True) 
    app.geometry("1802x1100")
    
    
    
    title_label=Label(app,text="Placement Statistics",fg='black',bg=bg1_color, font=title1)
    title_label.place(x=675,y=10)  
    
    
    cse_button=Button(app,text='Computer Science & Engineering', height=5,width=32,command=opencse)
    cse_button.place(x=150,y=20)
     
    ise_button=Button(app,text='Information Science & Engineering', height=5,width=32, command=openise)
    ise_button.place(x=150,y=170)
    
    mech_button=Button(app,text='Mechanical Engineering', height=5,width=32,command=openmech)
    mech_button.place(x=150,y=320)
    
    ece_button=Button(app,text='Electronics & Communication Engineering', height=5,width=32,command=openece)
    ece_button.place(x=150,y=470)
    
    
    
    
    g1 = ImageTk.PhotoImage(Image.open("/Users/pranavmanjunath/Downloads/Final Year/Application/PES1.png"))
    g11 = Label(app,image=g1,width=450,height=292)
    g11.image = g1
    g11.place(x=1260, y=140)

    
    
    g1 = ImageTk.PhotoImage(Image.open("/Users/pranavmanjunath/Downloads/Final Year/Application/Overall_Placement.png"))
    g11 = Label(app,image=g1,width=600,height=360)
    g11.image = g1
    g11.place(x=600, y=100)


    g1 = ImageTk.PhotoImage(Image.open("/Users/pranavmanjunath/Downloads/Final Year/Application/CSE.png"))
    g11 = Label(app,image=g1,width=584,height=350)
    g11.image = g1
    g11.place(x=0, y=570)


    g1 = ImageTk.PhotoImage(Image.open("/Users/pranavmanjunath/Downloads/Final Year/Application/ISE.png"))
    g11 = Label(app,image=g1,width=584,height=350)
    g11.image = g1
    g11.place(x=609, y=570)


    g1 = ImageTk.PhotoImage(Image.open("/Users/pranavmanjunath/Downloads/Final Year/Application/ECE.png"))
    g11 = Label(app,image=g1,width=575,height=350)
    g11.image = g1
    g11.place(x=1218, y=570)
