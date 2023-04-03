# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 11:19:43 2023

@author: Akshara Sagar Dhoble
"""

from tkinter import*
from tkinter import messagebox 

root = Tk()
root.title("Conditions")

root.geometry("400x400")


question1_radiobtn = StringVar(value="0")
question1_lbl = Label(root , text= "Do you experience shortness of breath during routine activities ? " )
question1_lbl.pack()
question1_r1 = Radiobutton(root , text="yes" , variable=question1_radiobtn , value="yes")
question1_r1.pack()
question1_r2 = Radiobutton(root , text="no" , variable=question1_radiobtn , value="no")
question1_r2.pack()

question2_radiobtn = StringVar(value="0")
question2_lbl = Label(root , text= "Do you have swelling in the feet / ankles / legs ( shouse feel tighter ) or abdome ? ")
question2_lbl.pack()
question2_r1 = Radiobutton(root , text="yes" , variable=question1_radiobtn , value="yes")
question2_r1.pack()
question2_r2 = Radiobutton(root , text="no" , variable=question1_radiobtn , value="no")
question2_r2.pack()

question3_radiobtn = StringVar(value="0")
question3_lbl = Label(root , text= "Do you feel any of these symptoms - confusion , disorientation or loss of memory ? ")
question3_lbl.pack()
question3_r1 = Radiobutton(root , text="yes" , variable=question1_radiobtn , value="yes")
question3_r1.pack()
question3_r2 = Radiobutton(root , text="no" , variable=question1_radiobtn , value="no")
question3_r2.pack()

question4_radiobtn = StringVar(value="0")
question4_lbl = Label(root , text= "Do you experience shortness of breath while at rest / lying down ? ")
question4_lbl.pack()
question4_r1 = Radiobutton(root , text="yes" , variable=question1_radiobtn , value="yes")
question4_r1.pack()
question4_r2 = Radiobutton(root , text="no" , variable=question1_radiobtn , value="no")
question4_r2.pack()

question5_radiobtn = StringVar(value="0")
question5_lbl = Label(root , text= "Do you experience persistent wheezing / coughing that produces white or pink blood tinged mucus ? ")
question5_lbl.pack()
question5_r1 = Radiobutton(root , text="yes" , variable=question1_radiobtn , value="yes")
question5_r1.pack()
question5_r2 = Radiobutton(root , text="no" , variable=question1_radiobtn , value="no")
question5_r2.pack()

def clickme() :
    score = 0
    if question1_radiobtn.get()=="yes" :
        score = score+10
        print(score)
    if question2_radiobtn.get()=="yes" :
        score = score+10
        print(score)
    if question3_radiobtn.get()=="yes" :
        score = score+10
        print(score)
    if question4_radiobtn.get() == "yes" :
        score = score+10
        print(score)
    if question5_radiobtn.get() == "yes" :
        score = score+10
        print(score)
    if score <=10 :
        messagebox.showinfo("Report" , "You don't need to visit to doctor")
    elif score >=10 and score <= 30:
        messagebox.showinfo("Report" , "You might prehaps to visit a doctor")
    else  :
        messagebox.showinfo("Report" , "I strongly advise you to visit a doctor")
      
      
  

btn_1 = Button(root , text="click me" , command=clickme )
btn_1.pack()
root.mainloop()
