# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 12:56:21 2019

@author: lenovo
"""

from socket import socket, AF_INET, SOCK_STREAM
from _thread import *
from threading import *

#from tkinter import *
#from tkinter import Tk
from tkinter import messagebox , Button , Label 
#Object of TK fun
window = Tk()
window.title(" Tic Tac Toe ")#title of window
window.geometry("400x300")#dimentions
label2 = Label(window,text = "player2 : O  ",font = ('Helvetica','15'))
label2.grid(row =0 ,column =0)
#flag to no. of 10 action to terminated
player = 2
flag =1

def check ():
    global flag
    flag +=1
    
    b1 =button1["text"]
    b2 =button2["text"]
    b3 =button3["text"]
    b4 =button4["text"]
    b5 =button5["text"]
    b6 =button6["text"]
    b7 =button7["text"]
    b8 =button8["text"]
    b9 =button9["text"]
    
    if (b1==b2 and b2==b3 and b1=='O')or(b1==b2 and b2==b3 and b1=='X'):
        win(b1)
    if (b4==b5 and b5==b6 and b4=='O')or(b4==b5 and b5==b6 and b4=='X'):
        win(b4)
    if (b7==b8 and b8==b9 and b7=='O')or(b7==b8 and b8==b9 and b7=='X'):
        win(b7)
    if (b1==b4 and b4==b7 and b1=='O')or(b1==b4 and b4==b7 and b1=='X'):
        win(b1)
    if (b2==b5 and b8==b3 and b2=='O')or(b2==b5 and b8==b3 and b2=='X'):
        win(b2)
    if (b3==b6 and b9==b3 and b3=='O')or(b3==b6 and b9==b3 and b3=='X'):
        win(b3)
    if (b1==b5 and b9==b3 and b1=='O')or(b1==b5 and b9==b3 and b1=='X'):
        win(b1)
    if (b3==b5 and b7==b3 and b3=='O')or(b3==b5 and b7==b3 and b3=='X'):
        win(b3)
    if flag ==10:
        messagebox.showinfo("Game Draw")
        window.destroy()
#fun of messaging congrats
def win(player):
    messagebox.showinfo("Congratulation",player)
    window.destroy()        
#flag to chose player
turn =1
#fun of button command 1
def clicked1():
    global turn 
    if button1["text"]==" ":
        if turn ==1:
            turn =2
            button1["text"] ='O'
            send(1)
        check() 
#fun of button command 2      
def clicked2():
    global turn 
    if button2["text"]==" ":
        if turn ==1:
            turn =2
            button2["text"] ='O'
            send(2)
        check() 
#fun of button command 3
def clicked3():
    global turn 
    if button3["text"]==" ":
        if turn ==1:
            turn =2
            button3["text"] ='O'
            send(3)
        check() 
#fun of button command 4
def clicked4():
    global turn 
    if button4["text"]==" ":
        if turn ==1:
            turn =2
            button4["text"] ='O'
            send(4)
        check() 
#fun of button command 5
def clicked5():
    global turn 
    if button5["text"]==" ":
        if turn ==1:
            turn =2
            button5["text"] ='O'
            send(5)
        check() 
#fun of button command 6
def clicked6():
    global turn 
    if button6["text"]==" ":
        if turn ==1:
            turn =2
            button6["text"] ='O'
            send(6)
        check() 
#fun of button command 7
def clicked7():
    global turn 
    if button7["text"]==" ":
        if turn ==1:
            turn =2
            button7["text"] ='O'
            send(7)
        check() 
#fun of button command 8
def clicked8():
    global turn 
    if button8["text"]==" ":
        if turn ==1:
            turn =2
            button8["text"] ='O'
            send(8)  
        check() 
#fun of button command 9
def clicked9():
    global turn 
    if button9["text"]==" ":
        if turn ==1:
            turn =2
            button9["text"] ='O'
            send(9)
        check()         
#list of the buttons pressed     
butList = list()
#button 1
button1 = Button(window ,text =" ",bg ="yellow",fg ="black",width =3,height =1,font =('Helvetica','15'),command =clicked1)
button1.grid(row =0 ,column =1)
#button 2
button2 = Button(window ,text =" ",bg ="yellow",fg ="black",width =3,height =1,font =('Helvetica','15'),command =clicked2)
button2.grid(row =0 ,column =2)
#button 3
button3 = Button(window ,text =" ",bg ="yellow",fg ="black",width =3,height =1,font =('Helvetica','15'),command =clicked3)
button3.grid(row =0 ,column =3)
#button 4
button4 = Button(window ,text =" ",bg ="yellow",fg ="black",width =3,height =1,font =('Helvetica','15'),command =clicked4)
button4.grid(row =1 ,column =1)
#button 5
button5 = Button(window ,text =" ",bg ="yellow",fg ="black",width =3,height =1,font =('Helvetica','15'),command =clicked5)
button5.grid(row =1 ,column =2)
#button 6
button6 = Button(window ,text =" ",bg ="yellow",fg ="black",width =3,height =1,font =('Helvetica','15'),command =clicked6)
button6.grid(row =1 ,column =3)
#button 7
button7 = Button(window ,text =" ",bg ="yellow",fg ="black",width =3,height =1,font =('Helvetica','15'),command =clicked7)
button7.grid(row =2 ,column =1)
#button 8
button8 = Button(window ,text =" ",bg ="yellow",fg ="black",width =3,height =1,font =('Helvetica','15'),command =clicked8)
button8.grid(row =2 ,column =2)
#button 9
button9 = Button(window ,text =" ",bg ="yellow",fg ="black",width =3,height =1,font =('Helvetica','15'),command =clicked9)
button9.grid(row =2 ,column =3)
#Appending buttons to a List
butList.append(button1)
butList.append(button2)
butList.append(button3)
butList.append(button4)
butList.append(button5)
butList.append(button6)
butList.append(button7)
butList.append(button8)
butList.append(button9)
#fun for sending actions
def send(x):
    x = str(x)
    x = x.encode()
    c.send(x)
#fun to receive actions
def ClientReceive(c): 
    global turn
    turn = 1
    while True:
        x = c.recv(50)
        x = int(x.decode())
        x = x-1
        butList[x]["text"]= "X"
        turn = 1
    
soc=socket(AF_INET, SOCK_STREAM)
host = '127.0.0.1'
port = 7000
soc.bind((host, port))
soc.listen(5)
print ("== ::SERVER Established")
c , add = soc.accept()
print("connection from", add[0])
#create thread for serving that session.
start_new_thread(ClientReceive,(c,))
window.mainloop()