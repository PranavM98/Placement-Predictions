

import pandas as pd
#from tkmacosx import Button
from tkinter import *
import webbrowser
#from winsound import *
from PIL import ImageTk,Image 

import pygame

import time
import logos
import encoding
import predictions
import new_predictions
import survey_predictions
import new_survey_predictions
import gui_1



data=pd.read_csv('final_type.csv')
data=encoding.enc(data)
clf_tier,clf_type=predictions.rf(data)



data1=pd.read_csv('final_survey.csv')
growth_clf,choice_clf,satisfaction_clf=survey_predictions.build(data1)



click=0

root=Tk()

#root.attributes("-fullscreen", True) 
root.geometry("1750x1100")

root.title("Placement Predictions")


bg_color='gray12'
root.configure(background=bg_color)


fg_color='white'

#root.wm_attributes("-transparentcolor", 'grey')



#C = Tkinter.Canvas(top, bg="cyan4", height=900, width=600)




def stats():   
   
    app = Toplevel(root) 
    #newWindow = Tk.Toplevel(app)
    gui_1.newWindow(app)





labelfont0 = ('Helvetica', 19)

title = ('Helvetica', 45,'bold italic')
labelfont = ('times', 20, 'bold')
labelfont1 = ('times', 25, 'bold')



title_label=Label(root,text="PlaceMeUp", font=title, bg=bg_color,fg='SpringGreen4')
title_label.place(x=750,y=10)  










stats_button=Button(root,text="PES Placement Statistics", command=stats)
stats_button.place(x=1500,y=30)


render = ImageTk.PhotoImage(Image.open("PES.png"))
img = Label(image=render)
img.image = render
img.place(x=1000, y=150)

gender_label=Label(root,text="Gender", font=labelfont0, bg=bg_color,fg=fg_color)
gender_label.place(x=150,y=60)  


gender=StringVar(root)
drop=OptionMenu(root,gender,"Male","Female")
drop.place(x=160,y=90)


admission_label=Label(root,text="Admission Entrance Exam",font=labelfont0, bg=bg_color,fg=fg_color)
admission_label.place(x=340,y=60)

admission=StringVar(root)
drop=OptionMenu(root,admission,"CET","COMED-K","Management") 
drop.place(x=410,y=90)


grades=[
        ("FCD",2),
        ("FC",1),
        ("SC",0)
        ]






ten_label=Label(root,text="10th Grade Marks",font=labelfont0, bg=bg_color,fg=fg_color)
ten_label.place(x=150,y=150)

ten=IntVar(root)

Radiobutton(root,text="FCD",variable=ten, value=1,font=labelfont0, bg=bg_color,fg=fg_color).place(x=150,y=190)
Radiobutton(root,text="FC",variable=ten, value=0,font=labelfont0, bg=bg_color,fg=fg_color).place(x=150,y=220)
Radiobutton(root,text="SC",variable=ten, value=2,font=labelfont0, bg=bg_color,fg=fg_color).place(x=150,y=250)



twe_label=Label(root,text="12th Grade Marks",font=labelfont0, bg=bg_color,fg=fg_color)
twe_label.place(x=340,y=150)
twe=IntVar(root)


Radiobutton(root,text="FCD",variable=twe, value=1,font=labelfont0, bg=bg_color,fg=fg_color).place(x=340,y=190)
Radiobutton(root,text="FC",variable=twe, value=0,font=labelfont0, bg=bg_color,fg=fg_color).place(x=340, y=220)
Radiobutton(root,text="SC",variable=twe, value=2,font=labelfont0, bg=bg_color,fg=fg_color).place(x=340,y=250)


branch_label=Label(root,text="Branch",font=labelfont0, bg=bg_color,fg=fg_color)
branch_label.place(x=250,y=270)

branch=StringVar(root)
drop=OptionMenu(root,branch,"CSE","ISE","ECE","MECH")
drop.place(x=260,y=295)


sem1_label=Label(root,text="Semester 1",font=labelfont0, bg=bg_color,fg=fg_color)
sem1_label.place(x=60,y=340)

sem_1=IntVar(root)

Radiobutton(root,text="FCD",variable=sem_1, value=1,font=labelfont0, bg=bg_color,fg=fg_color).place(x=60,y=380)
Radiobutton(root,text="FC",variable=sem_1, value=0,font=labelfont0, bg=bg_color,fg=fg_color).place(x=60,y=410)
Radiobutton(root,text="SC",variable=sem_1, value=2,font=labelfont0, bg=bg_color,fg=fg_color).place(x=60,y=440)



sem2_label=Label(root,text="Semester 2",font=labelfont0, bg=bg_color,fg=fg_color)
sem2_label.place(x=250,y=340)
sem_2=IntVar(root)


Radiobutton(root,text="FCD",variable=sem_2, value=1,font=labelfont0, bg=bg_color,fg=fg_color).place(x=250,y=380)
Radiobutton(root,text="FC",variable=sem_2, value=0,font=labelfont0, bg=bg_color,fg=fg_color).place(x=250, y=410)
Radiobutton(root,text="SC",variable=sem_2, value=2,font=labelfont0, bg=bg_color,fg=fg_color).place(x=250,y=440)


sem3_label=Label(root,text="Semester 3",font=labelfont0, bg=bg_color,fg=fg_color) 
sem3_label.place(x=440,y=340)
sem_3=IntVar(root)


Radiobutton(root,text="FCD",variable=sem_3, value=1,font=labelfont0, bg=bg_color,fg=fg_color).place(x=440,y=380)
Radiobutton(root,text="FC",variable=sem_3, value=0,font=labelfont0, bg=bg_color,fg=fg_color).place(x=440,y=410) 
Radiobutton(root,text="SC",variable=sem_3, value=2,font=labelfont0, bg=bg_color,fg=fg_color).place(x=440,y=440) 





sem4_label=Label(root,text="Semester 4",font=labelfont0, bg=bg_color,fg=fg_color)
sem4_label.place(x=60,y=490)
sem_4=IntVar(root)


Radiobutton(root,text="FCD",variable=sem_4, value=1,font=labelfont0, bg=bg_color,fg=fg_color).place(x=60,y=530) 
Radiobutton(root,text="FC",variable=sem_4, value=0,font=labelfont0, bg=bg_color,fg=fg_color).place(x=60,y=560) 
Radiobutton(root,text="SC",variable=sem_4, value=2,font=labelfont0, bg=bg_color,fg=fg_color).place(x=60,y=590) 


sem5_label=Label(root,text="Semester 5",font=labelfont0, bg=bg_color,fg=fg_color)
sem5_label.place(x=250,y=490)
sem_5=IntVar(root)

Radiobutton(root,text="FCD",variable=sem_5, value=1,font=labelfont0, bg=bg_color,fg=fg_color).place(x=250,y=530)
Radiobutton(root,text="FC",variable=sem_5, value=0,font=labelfont0, bg=bg_color,fg=fg_color).place(x=250,y=560)
Radiobutton(root,text="SC",variable=sem_5, value=2,font=labelfont0, bg=bg_color,fg=fg_color).place(x=250,y=590) 


sem6_label=Label(root,text="Semester 6",font=labelfont0, bg=bg_color,fg=fg_color)
sem6_label.place(x=440,y=490)
sem_6=IntVar(root)

Radiobutton(root,text="FCD",variable=sem_6, value=1,font=labelfont0, bg=bg_color,fg=fg_color).place(x=440,y=530)
Radiobutton(root,text="FC",variable=sem_6, value=0,font=labelfont0, bg=bg_color,fg=fg_color).place(x=440,y=560)
Radiobutton(root,text="SC",variable=sem_6, value=2,font=labelfont0, bg=bg_color,fg=fg_color).place(x=440,y=590)



agg_label=Label(root,text="Aggregate",font=labelfont0, bg=bg_color,fg=fg_color)
agg_label.place(x=250,y=650)
agg=IntVar(root)


Radiobutton(root,text="FCD",variable=agg, value=1,font=labelfont0, bg=bg_color,fg=fg_color).place(x=250,y=690)
Radiobutton(root,text="FC",variable=agg, value=0,font=labelfont0, bg=bg_color,fg=fg_color).place(x=250,y=720)
Radiobutton(root,text="SC",variable=agg, value=2,font=labelfont0, bg=bg_color,fg=fg_color).place(x=250,y=750)




photo123 = ImageTk.PhotoImage(Image.open('/Users/pranavmanjunath/Downloads/Final Year/Application/Marks.png'))   
p123=Label(image = photo123,height=73,width=200)
p123.image=photo123
p123.place(x=400,y=700)


p_label=Label(root,text="YOU WILL BE PLACED IN              ", bg=bg_color, fg='firebrick2')
p_label.config(font=labelfont1)  

c1_label=Label(root,text='COMPANIES THAT COME TO PESIT FOR PLACEMENTS:', bg=bg_color,fg='firebrick2')
c1_label.config(font=labelfont1)  

s1_label=Label(text='ACCORDING TO SENIORS', bg=bg_color,fg='firebrick2')
s1_label.config(font=labelfont1)  




#def url():
#    webbrowser.open("https://www.mcafee.com",new=1)

def display(ti,typea):
    
    comp_list=logos.tt(ti,typea)
    c1_label.place(x=650,y=530)
    s1_label.place(x=1200,y=325)

    
    xp=550
    yp=585
    count=0
    for i in comp_list:
            
            if count%3==0:
                xp=xp+150
                yp=585
                
            path='/Users/pranavmanjunath/Downloads/Final Year/Application/Logos/'+i+'.png'
            photo = ImageTk.PhotoImage(Image.open(path))   
            b11=Label(root, image = photo,height=100,width=100)
            b11.image=photo
            b11.place(x=xp,y=yp)
            
            xp=xp
            yp=yp+150
            count=count+1
            
            
            

     
def tyti(tier,typea):



    p_label.place(x=700,y=150)
    
    p1_label=Label(root,text='COMPANY TIER:', bg=bg_color,fg='gold')
    p1_label.config(font=labelfont)  
    p1_label.place(x=770,y=210)
    
    tier_label=Label(root,text=tier, bg=bg_color,fg='gold')
    tier_label.config(font=labelfont)
    tier_label.place(x=950,y=210)
    
    p2_label=Label(root,text='COMPANY TYPE:', bg=bg_color,fg='gold')
    p2_label.config(font=labelfont)  
    p2_label.place(x=770,y=250)
    
    type_label=Label(text=typea, bg=bg_color,fg='gold') 
    type_label.config(font=labelfont)
    type_label.place(x=950,y=250) 
    



def survey(g,c,s):


    p4_label=Label(root,text='CAREER GROWTH OPPORTUNITIES:', bg=bg_color,fg='gold')
    p4_label.config(font=labelfont)  
    p4_label.place(x=1050,y=375)
    
    growth_label=Label(root,text=g, bg=bg_color,fg='gold')
    growth_label.config(font=labelfont)
    growth_label.place(x=1450,y=375)
    
        
    p5_label=Label(root,text='EMPLOYMENT SATISFACTION:', bg=bg_color,fg='gold')
    p5_label.config(font=labelfont)  
    p5_label.place(x=1050,y=410)
    
    satisfaction_label=Label(text=s, bg=bg_color,fg='gold') 
    satisfaction_label.config(font=labelfont)
    satisfaction_label.place(x=1450,y=410) 
    
    
    p6_label=Label(root,text='PREFERRED CHOICE AFTER B.E:', bg=bg_color,fg='gold')
    p6_label.config(font=labelfont)  
    p6_label.place(x=1050,y=445)
    
    choice_label=Label(text=c, bg=bg_color,fg='gold') 
    choice_label.config(font=labelfont)
    choice_label.place(x=1450,y=445) 
    
''' 
    if g=='Mid Growth':
      
        growth= ImageTk.PhotoImage(Image.open("Normal.png"))
        growth_label = Label(image=growth)
        growth_label.image = growth
        growth_label.place(x=1450, y=375)
      
        growth_label=Label(root,text=g, bg=bg_color,fg='gold')
        growth_label.config(font=labelfont)
        growth_label.place(x=1450,y=375)
        
    elif g=='High Growth':
  
        growth= ImageTk.PhotoImage(Image.open("Great.png"))
        growth_label = Label(image=growth)
        growth_label.image = growth
        growth_label.place(x=1450, y=375)
        
        #growth_label=Label(root,text=g, bg=bg_color,fg='gold')
        #growth_label.config(font=labelfont)
        #growth_label.place(x=1450,y=375)
    
    else:
        
        growth= ImageTk.PhotoImage(Image.open("Poor.png"))
        growth_label = Label(image=growth)
        growth_label.image = growth
        growth_label.place(x=1450, y=375)
        
        #growth_label=Label(root,text=g, bg=bg_color,fg='gold')
        #growth_label.config(font=labelfont)
        #growth_label.place(x=1450,y=375)
           
    
    p5_label=Label(root,text='EMPLOYMENT SATISFACTION:', bg=bg_color,fg='gold')
    p5_label.config(font=labelfont)  
    p5_label.place(x=1050,y=410)
    
    if s=='Satisfied':
    
        sat= ImageTk.PhotoImage(Image.open("Normal.png"))
        sat_label = Label(image=sat)
        sat_label.image = sat
        sat_label.place(x=1450, y=410)
        
        #satisfaction_label=Label(text=s, bg=bg_color,fg='gold') 
        #satisfaction_label.config(font=labelfont)
        #satisfaction_label.place(x=1450,y=410) 
    
    elif s=='Very Satisfied':
        
        sat= ImageTk.PhotoImage(Image.open("Great.png"))
        sat_label = Label(image=sat)
        sat_label.image = sat
        sat_label.place(x=1450, y=410)

        #satisfaction_label=Label(text=s, bg=bg_color,fg='gold') 
        #satisfaction_label.config(font=labelfont)
        #satisfaction_label.place(x=1450,y=410) 
        
    else:
        
        sat= ImageTk.PhotoImage(Image.open("Poor.png"))
        sat_label = Label(image=sat)
        sat_label.image = sat
        sat_label.place(x=1450, y=410)


        #satisfaction_label=Label(text=s, bg=bg_color,fg='gold') 
        #satisfaction_label.config(font=labelfont)
        #satisfaction_label.place(x=1450,y=410) 
        
        
        
        
    p6_label=Label(root,text='PREFERRED CHOICE AFTER B.E:', bg=bg_color,fg='gold')
    p6_label.config(font=labelfont)  
    p6_label.place(x=1050,y=445)
    
    choice_label=Label(text=c, bg=bg_color,fg='gold') 
    choice_label.config(font=labelfont)
    choice_label.place(x=1450,y=445) 
    
'''
        


def onclick():
    
    pygame.init()
    pygame.mixer.music.load('Ta_da.mp3')
    pygame.mixer.music.play(0)
    time.sleep(0.2)
    
    type1_label=Label(text="                 ", bg=bg_color) 
    type1_label.config(font=labelfont)
    type1_label.place(x=950,y=250)
  
    ab=[gender.get(),admission.get(),branch.get(),ten.get(),twe.get(),sem_1.get(),sem_2.get(),sem_3.get(),sem_4.get(),sem_5.get(),sem_6.get(),agg.get()]
    tier,typea=new_predictions.predict(gender.get(),admission.get(),branch.get(),ten.get(),twe.get(),sem_1.get(),sem_2.get(),sem_3.get(),sem_4.get(),sem_5.get(),sem_6.get(),agg.get(),clf_tier,clf_type)
    g,c,s=new_survey_predictions.predict(tier,typea,growth_clf,choice_clf,satisfaction_clf)
    

    
    img.config(image='')
    
    growth1_label=Label(text="                 ", bg=bg_color) 
    growth1_label.config(font=labelfont)
    growth1_label.place(x=1300,y=300) 
  
   # satisfaction_label=Label(text="                 ", bg=bg_color) 
  #  satisfaction_label.config(font=labelfont)
    #satisfaction_label.place(x=1350,y=340) 
    
    choice_label=Label(text="                                                         ", bg=bg_color) 
    choice_label.config(font=labelfont)
    choice_label.place(x=1450,y=445) 

    display(tier,typea)
    tyti(tier,typea)
    survey(g,c,s)
    
    

b=Button(root,text="Click to Discover Your Future", height=8,width=30,command=onclick)
b.place(x=150,y=820)

root.mainloop()