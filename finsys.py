
from calendar import c
from cgitb import enable, reset, text
from distutils import command
from itertools import count
from pydoc import describe
from secrets import choice
from sqlite3 import enable_callback_tracebacks
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from textwrap import wrap
from tkinter import font
from tkinter.font import BOLD
from urllib.parse import parse_qs
from PIL import ImageTk, Image, ImageFile
from matplotlib.font_manager import json_dump
from numpy import choose, empty, place
import pandas as pd
from tkinter.messagebox import showinfo
import tkinter.scrolledtext as scrolledtext
from tkinter.filedialog import askopenfilename
import os
import webbrowser
from pip import main
from tkcalendar import Calendar
from tkcalendar import DateEntry
from datetime import date
from tkinter import filedialog
import subprocess
import mysql.connector
import io
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import shutil
import csv
import json
from tkPDFViewer import tkPDFViewer as pdf
from tkinter import Tk, Canvas
from tkinter.messagebox import showinfo
from turtle import bgcolor, color

import customtkinter
import PIL.Image
from PIL import ImageGrab
from PIL import ImageTk, Image, ImageFile
import PIL.Image



# fbilldb = mysql.connector.connect(
#     host="localhost", user="root", password="", database="fbilling", port="3306"
# )
# fbcursor = fbilldb.cursor()

root=Tk()
root.geometry("1366x768")

root.title("Fin sYs")

p1 = PhotoImage(file = 'images/favicon.png')
root.iconphoto(False, p1)

#--------------------------------------------------------------------------------------------Images

imgr1 =PIL.Image.open("images\logs.png")
exprefreshIcon=ImageTk.PhotoImage(imgr1)

mnu =PIL.Image.open("images\menu bar.PNG")
mnus=ImageTk.PhotoImage(mnu)


srh =PIL.Image.open("images\search.PNG")
srh_img=ImageTk.PhotoImage(srh)

logo =PIL.Image.open("images\logo-icon.png")
resized_image= logo.resize((50,50))
mai_logo= ImageTk.PhotoImage(resized_image)

lowstock = PhotoImage(file="images/lowstock.png")
outofstock = PhotoImage(file="images/outofstock.png")

#--------------------------------------------------------------------------------------------Create Sign In customer

def main_sign_in():
    try:
        main_frame_signup.destroy()
    except:
        pass
    try:
        main_frame_signin.destroy()
    except:
        pass
    Sys_top_frame=Frame(root, height=70,bg="#213b52")
    Sys_top_frame.pack(fill=X,)

    #---------------------------------------------------------------------------------------Top Menu
    tp_lb_nm=LabelFrame(Sys_top_frame,height=70,bg="#213b52",width=400)#-----------------------------Logo Name Frame
    tp_lb_nm.grid(row=1,column=1)

    label = Label(tp_lb_nm, image = mai_logo,height=70,bg="#213b52",border=0)
    label.grid(row=2,column=1)
    label = Label(tp_lb_nm, text="Fin sYs",bg="#213b52", fg="white",font=('Calibri 30 bold'),border=0)
    label.grid(row=2,column=2)
  
    mnu_btn = Button(tp_lb_nm, image=mnus, bg="white", fg="black",border=0)
    mnu_btn.grid(row=2,column=4,padx=50)

    tp_lb_srh=LabelFrame(Sys_top_frame,height=70,bg="#213b52",width=700)#-------------------------Serch area Frame
    tp_lb_srh.grid(row=1,column=2)
    def srh_fn(event):
        if srh_top.get()=="Search":
            srh_top.delete(0,END)
        else:
            pass

    srh_top = Entry(tp_lb_srh, width=50, font=('Calibri 16'))
    srh_top.insert(0,"Search")
    srh_top.bind("<Button-1>",srh_fn)
    srh_top.grid(row=2,column=1,padx=(70,0), pady=20)

    srh_btn = Button(tp_lb_srh, image=srh_img, bg="white", fg="black",border=0)
    srh_btn.grid(row=2,column=4,padx=(0,70))

    tp_lb_nm=LabelFrame(Sys_top_frame,height=70,bg="#213b52",width=100)#----------------Notification
    tp_lb_nm.grid(row=1,column=3)
    tp_lb_nm=LabelFrame(Sys_top_frame,height=70,bg="#213b52",width=200)#----------------profile area name
    tp_lb_nm.grid(row=1,column=4)

    Sys_top_frame2=Frame(root, height=10,bg="#213b52")
    Sys_top_frame2.pack(fill=X,)
    
    
  
    s = ttk.Style()
    s.theme_use('default')
    s.configure('TNotebook.Tab', background="#213b52",foreground="white", width=150,anchor="center", padding=5)
    s.map('TNotebook.Tab',background=[("selected","#2f516f")])
    def right_nav():
        
        tabControl.pack_forget()
        btn_nav.place_forget()
        tabControl2.pack(expand = 1, fill ="both")
        btn_nav2.place(x=0,y=0)
        try:
            btn_nav3.place_forget()
        except:
            pass
    def left_nav():
        
        tabControl2.pack_forget()
        btn_nav2.place_forget()
        tabControl.pack(expand = 1, fill ="both")
        global btn_nav3
        btn_nav3=Button(Sys_top_frame2,text=">>", command=right_nav, width=3, bg="#213b52",fg="white")
        btn_nav3.place(x=1325,y=0)

    tabControl = ttk.Notebook(Sys_top_frame2)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3=  ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)
    tab6=  ttk.Frame(tabControl)
    tab7 = ttk.Frame(tabControl)
    tab8 = ttk.Frame(tabControl)
    
    
    btn_nav=Button(Sys_top_frame2,text=">>", command=right_nav, width=3, bg="#213b52",fg="white")
    btn_nav.place(x=1325,y=0)
    tabControl.add(tab1,compound = LEFT, text ='Dashboard',)
    tabControl.add(tab2,compound = LEFT, text ='Bancking')
    tabControl.add(tab3,compound = LEFT, text ='Sales')
    tabControl.add(tab4,compound = LEFT, text ='Expenses')
    tabControl.add(tab5,compound = LEFT, text ='Payroll') 
    tabControl.add(tab6,compound = LEFT, text ='Report')
    tabControl.add(tab7,compound = LEFT, text ='Taxes')
    tabControl.add(tab8,compound = LEFT, text ='Accounting')
    
    tabControl.pack(expand = 1, fill ="both")


    
    tabControl2 = ttk.Notebook(Sys_top_frame2)
    tab9 =  ttk.Frame(tabControl2)
    tab10=  ttk.Frame(tabControl2)
    tab11 = ttk.Frame(tabControl2)
    tab12=  ttk.Frame(tabControl2)
    tab13 = ttk.Frame(tabControl2)
    tab14 = ttk.Frame(tabControl2)
    tab15 =  ttk.Frame(tabControl2)

    btn_nav2=Button(Sys_top_frame2,text="<<", command=left_nav, width=3, bg="#213b52",fg="white")
    
        
    tabControl2.add(tab9,compound = LEFT, text ='My Account')
    tabControl2.add(tab10,compound = LEFT, text ='Cash Management')
    tabControl2.add(tab11,compound = LEFT, text ='Production')
    tabControl2.add(tab12,compound = LEFT, text ='Quality Management')
    tabControl2.add(tab13,compound = LEFT, text ='Project Management')
    tabControl2.add(tab14,compound = LEFT, text ='Usage Decisions')
    tabControl2.add(tab15,compound = LEFT, text ='Account & Payable')

   

    Sys_mains_frame=Frame(tab1, height=750,bg="#213b52")
    Sys_mains_frame.pack(fill=X)

    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333Banking Section(Tab2)

    tab_bank = ttk.Notebook(tab2)
    tab2_1 =  ttk.Frame(tab_bank)
    tab2_2=  ttk.Frame(tab_bank)
    tab2_3 = ttk.Frame(tab_bank)

    tab_bank.add(tab2_1,compound = LEFT, text ='Online Banking')
    tab_bank.add(tab2_2,compound = LEFT, text ='Offline banking')
    tab_bank.add(tab2_3,compound = LEFT, text ='Bank Reconvilation')

 
    tab_bank.pack(expand = 1, fill ="both")

    #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Sales Tab}
    tab_sales = ttk.Notebook(tab3)
    tab3_1 =  ttk.Frame(tab_sales)
    tab3_2=  ttk.Frame(tab_sales)
    tab3_3 = ttk.Frame(tab_sales)
    tab3_4=  ttk.Frame(tab_sales)

    
        
    tab_sales.add(tab3_1,compound = LEFT, text ='Sales Records')
    tab_sales.add(tab3_2,compound = LEFT, text ='Invoices')
    tab_sales.add(tab3_3,compound = LEFT, text ='Customers')
    tab_sales.add(tab3_4,compound = LEFT, text ='Product & Services')
 
    tab_sales.pack(expand = 1, fill ="both")
    #--------------------------------Invoices-----------------------------#
    inv_frame = Frame(tab3_2)
    inv_frame.grid(row=0,column=0,sticky='nsew')
    canvas=Canvas(inv_frame, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,1000))

    vertibar=Scrollbar(inv_frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1325,height=559)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)

    def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
            
        points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]
    
        return canvas.create_polygon(points, **kwargs, smooth=True)
    
    my_rectangle = round_rectangle(20, 50, 1300, 200, radius=20, fill="#1b3857")
    label_1 = Label(canvas,width=10,height=1,text="INVOICES", font=('arial 25'),background="#1b3857",fg="white") 
    window_label_1 = canvas.create_window(550, 85, anchor="nw", window=label_1)
    canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

    my_rectangle_1 = round_rectangle(20, 250, 1300, 600, radius=20, fill="#1b3857")


    # s = ttk.Style()
    # s.configure('mystyle_2.Treeview.Heading', background='lime', State='DISABLE')
    # tree=ttk.Treeview(canvas, column=("c1", "c2","c3", "c4", "c5", "c6", "c7", "c8"), show='headings',height= 0, style='mystyle_2.Treeview')   
    # tree.column("# 1", anchor=E, stretch=NO, width=150)
    # tree.heading("# 1", text="INVOICE NO")
    # tree.column("# 2", anchor=E, stretch=NO, width=150)
    # tree.heading("# 2", text="INVOICE DATE")
    # tree.column("# 3", anchor=E, stretch=NO, width=150)
    # tree.heading("# 3", text="CUSTOMER")
    # tree.column("# 4", anchor=E, stretch=NO, width=150)
    # tree.heading("# 4", text="EMAIL ID")
    # tree.column("# 5", anchor=E, stretch=NO, width=150)
    # tree.heading("# 5", text="DUE DATE")    
    # tree.column("# 6", anchor=E, stretch=NO, width=150)
    # tree.heading("# 6", text="GRAND TOTAL")    
    # tree.column("# 7", anchor=E, stretch=NO, width=150)
    # tree.heading("# 7", text="BALANCE DUE")    
    # tree.column("# 8", anchor=E, stretch=NO, width=150)
    # tree.heading("# 8", text="ACTION")    
    # window = canvas.create_window(60, 350, anchor="nw", window=tree)
    canvas.create_line(60, 350, 1260, 350, fill='gray',width=1)
    canvas.create_line(60, 350, 60, 400, fill='gray',width=1)
    canvas.create_line(210, 350, 210, 400, fill='gray',width=1)
    canvas.create_line(360, 350, 360, 400, fill='gray',width=1)
    canvas.create_line(510, 350, 510, 400, fill='gray',width=1)
    canvas.create_line(660, 350, 660, 400, fill='gray',width=1)
    canvas.create_line(810, 350, 810, 400, fill='gray',width=1)
    canvas.create_line(960, 350, 960, 400, fill='gray',width=1)
    canvas.create_line(1110, 350, 1110, 400, fill='gray',width=1)
    canvas.create_line(1260, 350, 1260, 400, fill='gray',width=1)

    label_2 = Label(canvas,width=10,height=1,text="INVOICE NO", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(90, 365, anchor="nw", window=label_2)
    label_3 = Label(canvas,width=11,height=1,text="INVOICE DATE", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_3 = canvas.create_window(240, 365, anchor="nw", window=label_3)
    label_4 = Label(canvas,width=11,height=1,text="CUSTOMER", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = canvas.create_window(390, 365, anchor="nw", window=label_4)
    label_4 = Label(canvas,width=11,height=1,text="EMAIL ID", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = canvas.create_window(540, 365, anchor="nw", window=label_4)
    label_4 = Label(canvas,width=11,height=1,text="DUE DATE", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = canvas.create_window(690, 365, anchor="nw", window=label_4)
    label_4 = Label(canvas,width=11,height=1,text="GRAND TOTAL", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = canvas.create_window(840, 365, anchor="nw", window=label_4)
    label_4 = Label(canvas,width=11,height=1,text="BALANCE DUE", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = canvas.create_window(990, 365, anchor="nw", window=label_4)
    label_4 = Label(canvas,width=11,height=1,text="ACTION", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = canvas.create_window(1140, 365, anchor="nw", window=label_4)


    canvas.create_line(60, 400, 1260, 400, fill='gray',width=1)
    canvas.create_line(60, 400, 60, 450, fill='gray',width=1)
    canvas.create_line(210, 400, 210, 450, fill='gray',width=1)
    canvas.create_line(360, 400, 360, 450, fill='gray',width=1)
    canvas.create_line(510, 400, 510, 450, fill='gray',width=1)
    canvas.create_line(660, 400, 660, 450, fill='gray',width=1)
    canvas.create_line(810, 400, 810, 450, fill='gray',width=1)
    canvas.create_line(960, 400, 960, 450, fill='gray',width=1)
    canvas.create_line(1110, 400, 1110, 450, fill='gray',width=1)
    canvas.create_line(1260, 400, 1260, 450, fill='gray',width=1)


    # Define the style for combobox widget
    # styl= ttk.Style()
    # styl.theme_use('clam')
    # styl.configure("TCombobox", fieldbackground= "#2f516f", background= "#2f516f")

    inv_comb_1 = ttk.Combobox(canvas,font=('arial 10'),foreground="white")
    inv_comb_1['values'] = ("Actions","Edit","Delete")
    inv_comb_1.current(0)
    window_inv_comb_1 = canvas.create_window(1135, 410, anchor="nw", width=110,height=30,window=inv_comb_1)


    canvas.create_line(60, 450, 1260, 450, fill='gray',width=1)



    def add_invoice():
        inv_frame.grid_forget()
        inv_frame_1 = Frame(tab3_2)
        inv_frame_1.grid(row=0,column=0,sticky='nsew')
        canvas=Canvas(inv_frame_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1800))
        
        vertibar=Scrollbar(inv_frame_1, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)

        canvas.config(width=1325,height=559)
        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
            
            points = [x1+radius, y1,
                    x1+radius, y1,
                    x2-radius, y1,
                    x2-radius, y1,
                    x2, y1,
                    x2, y1+radius,
                    x2, y1+radius,
                    x2, y2-radius,
                    x2, y2-radius,
                    x2, y2,
                    x2-radius, y2,
                    x2-radius, y2,
                    x1+radius, y2,
                    x1+radius, y2,
                    x1, y2,
                    x1, y2-radius,
                    x1, y2-radius,
                    x1, y1+radius,
                    x1, y1+radius,
                    x1, y1]
        
            return canvas.create_polygon(points, **kwargs, smooth=True)
    
        my_rectangle = round_rectangle(20, 50, 1300, 200, radius=20, fill="#1b3857")
        label_1 = Label(canvas,width=10,height=1,text="INVOICE", font=('arial 20'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(550, 85, anchor="nw", window=label_1)
        canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

        my_rectangle = round_rectangle(20, 250, 1300, 1735, radius=20, fill="#1b3857")
        label_1 = Label(canvas,width=10,height=1,text="Fin sYs", font=('arial 20'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(550, 275, anchor="nw", window=label_1)

        inv_back_btn=Button(canvas,text='Back', width=10,height=1,foreground="white",background="#1b3857",font='arial 12')
        window_inv_back_btn = canvas.create_window(1050, 275, anchor="nw", window=inv_back_btn)

        label_2 = Label(canvas,width=15,height=1,text="Company name", font=('arial 16'),background="#1b3857",fg="skyblue") 
        window_label_2 = canvas.create_window(60, 330, anchor="nw", window=label_2)
        label_2 = Label(canvas,width=15,height=1,text="Company email-id", font=('arial 16'),background="#1b3857",fg="skyblue") 
        window_label_2 = canvas.create_window(68, 375, anchor="nw", window=label_2)

        label_2 = Label(canvas,width=15,height=1,text="Select Customer", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(66, 450, anchor="nw", window=label_2)

        comb_1 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_1['values'] = ("Select Customer",)
        comb_1.current(0)
        window_comb_1 = canvas.create_window(78, 475, anchor="nw", width=200, height=30,window=comb_1)

        def add_inv_customer():
            #inv_frame.grid_forget()
            inv_frame_1.grid_forget()
            inv_frame_2 = Frame(tab3_2)
            inv_frame_2.grid(row=0,column=0,sticky='nsew')
            canvas=Canvas(inv_frame_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1600))
            
            vertibar=Scrollbar(inv_frame_2, orient=VERTICAL)
            vertibar.pack(side=RIGHT,fill=Y)
            vertibar.config(command=canvas.yview)

            canvas.config(width=1325,height=559)
            canvas.config(yscrollcommand=vertibar.set)
            canvas.pack(expand=True,side=LEFT,fill=BOTH)
            def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
                
                points = [x1+radius, y1,
                        x1+radius, y1,
                        x2-radius, y1,
                        x2-radius, y1,
                        x2, y1,
                        x2, y1+radius,
                        x2, y1+radius,
                        x2, y2-radius,
                        x2, y2-radius,
                        x2, y2,
                        x2-radius, y2,
                        x2-radius, y2,
                        x1+radius, y2,
                        x1+radius, y2,
                        x1, y2,
                        x1, y2-radius,
                        x1, y2-radius,
                        x1, y1+radius,
                        x1, y1+radius,
                        x1, y1]
            
                return canvas.create_polygon(points, **kwargs, smooth=True)
    
            my_rectangle = round_rectangle(20, 50, 1300, 200, radius=20, fill="#1b3857")
            label_1 = Label(canvas,width=15,height=1,text="ADD CUSTOMER", font=('arial 20'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(550, 85, anchor="nw", window=label_1)
            canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

            my_rectangle = round_rectangle(20, 250, 1300, 1535, radius=20, fill="#1b3857")
            label_1 = Label(canvas,width=20,height=1,text="Customer Information", font=('arial 20'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(60, 275, anchor="nw", window=label_1)
            canvas.create_line(60, 330, 1260, 330, fill='gray',width=1)

            label_2 = Label(canvas,width=5,height=1,text="Title", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = canvas.create_window(62, 365, anchor="nw", window=label_2)

            comb_cus_1 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            comb_cus_1['values'] = ("Mr","Mrs","Miss","Ms",)
            comb_cus_1.current(0)
            window_comb_cus_1 = canvas.create_window(75, 395, anchor="nw", width=245, height=30,window=comb_cus_1)

            label_2 = Label(canvas,width=10,height=1,text="First name", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = canvas.create_window(400, 365, anchor="nw", window=label_2)

            entry_cus_1=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_cus_1 = canvas.create_window(410, 395, anchor="nw", height=30,window=entry_cus_1)

            label_2 = Label(canvas,width=10,height=1,text="Last name", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = canvas.create_window(745, 365, anchor="nw", window=label_2)

            entry_cus_2=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_cus_2 = canvas.create_window(755, 395, anchor="nw", height=30,window=entry_cus_2)

            label_2 = Label(canvas,width=10,height=1,text="Company", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = canvas.create_window(62, 465, anchor="nw", window=label_2)

            entry_cus_3=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_cus_3 = canvas.create_window(75, 495, anchor="nw", height=30,window=entry_cus_3)

            label_2 = Label(canvas,width=10,height=1,text="Location", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = canvas.create_window(395, 465, anchor="nw", window=label_2)

            cus_4=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_cus_4 = canvas.create_window(410, 495, anchor="nw", height=30,window=cus_4)

            label_2 = Label(canvas,width=10,height=1,text="GST type", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = canvas.create_window(62, 565, anchor="nw", window=label_2)

            comb_cus_2 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            comb_cus_2['values'] = ("Choose...","GST registered Regular","GST registered-Composition","GST unregistered","Consumer","Overseas","SEZ","Deemed exports-EOU's STP's EHTP's etc",)
            comb_cus_2.current(0)
            window_comb_cus_2 = canvas.create_window(75, 595, anchor="nw", width=245, height=30,window=comb_cus_2)

            label_2 = Label(canvas,width=10,height=1,text="GSTIN", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = canvas.create_window(385, 565, anchor="nw", window=label_2)

            cus_entry_str_1 = StringVar()
            entry_cus_5=Entry(canvas,width=34,justify=LEFT,background='#2f516f',foreground="white",font=('arial 10'),textvariable=cus_entry_str_1)
            cus_entry_str_1.set(' 29APPCK7465F1Z1')
            window_entry_cus_5 = canvas.create_window(410, 595, anchor="nw", height=30,window=entry_cus_5)

            label_2 = Label(canvas,width=10,height=1,text="PAN NO", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = canvas.create_window(740, 565, anchor="nw", window=label_2)

            cus_entry_str_2 = StringVar()
            entry_cus_6=Entry(canvas,width=34,justify=LEFT,background='#2f516f',foreground="white",font=('arial 10'),textvariable=cus_entry_str_2)
            cus_entry_str_2.set(' APPCK7465F')
            window_entry_cus_6 = canvas.create_window(755, 595, anchor="nw", height=30,window=entry_cus_6)

            label_2 = Label(canvas,width=5,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = canvas.create_window(71, 665, anchor="nw", window=label_2)

            entry_cus_7=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_cus_7 = canvas.create_window(75, 695, anchor="nw", height=30,window=entry_cus_7)

            label_2 = Label(canvas,width=10,height=1,text="Website", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = canvas.create_window(395, 665, anchor="nw", window=label_2)

            entry_cus_8=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_cus_8 = canvas.create_window(410, 695, anchor="nw", height=30,window=entry_cus_8)

            label_2 = Label(canvas,width=10,height=1,text="Mobile", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = canvas.create_window(736, 665, anchor="nw", window=label_2)

            entry_cus_9=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_cus_9 = canvas.create_window(752, 695, anchor="nw", height=30,window=entry_cus_9)

            label_1 = Label(canvas,width=20,height=1,text="Billing Address", font=('arial 16'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(23, 775, anchor="nw", window=label_1)

            label_2 = Label(canvas,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = canvas.create_window(71, 825, anchor="nw", window=label_2)

            entry_cus_10=Entry(canvas,width=95,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_cus_10 = canvas.create_window(75, 855, anchor="nw", height=60,window=entry_cus_10)

            label_1 = Label(canvas,width=20,height=1,text="Shipping Address", font=('arial 16'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(645, 775, anchor="nw", window=label_1)

            chk_str = StringVar()
            chkbtn1 = Checkbutton(canvas, text = "Same As Billing Address", variable = chk_str, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white")
            chkbtn1.select()
            window_chkbtn_1 = canvas.create_window(865, 775, anchor="nw", window=chkbtn1)

            label_2 = Label(canvas,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = canvas.create_window(681, 825, anchor="nw", window=label_2)

            entry_cus_11=Entry(canvas,width=95,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_cus_11 = canvas.create_window(685, 855, anchor="nw", height=60,window=entry_cus_11)

            label_2 = Label(canvas,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = canvas.create_window(65, 950, anchor="nw", window=label_2)

            entry_cus_12=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_cus_12 = canvas.create_window(75, 985, anchor="nw", height=30,window=entry_cus_12)
            
            label_2 = Label(canvas,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = canvas.create_window(395, 950, anchor="nw", window=label_2)

            entry_cus_13=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_cus_13 = canvas.create_window(400, 985, anchor="nw", height=30,window=entry_cus_13)

            label_2 = Label(canvas,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = canvas.create_window(675, 950, anchor="nw", window=label_2)

            entry_cus_14=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_cus_14 = canvas.create_window(685, 985, anchor="nw", height=30,window=entry_cus_14)

            label_2 = Label(canvas,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = canvas.create_window(1001, 950, anchor="nw", window=label_2)

            entry_cus_15=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_cus_15 = canvas.create_window(1010, 985, anchor="nw", height=30,window=entry_cus_15)

            label_2 = Label(canvas,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = canvas.create_window(65, 1050, anchor="nw", window=label_2)

            entry_cus_12=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_cus_12 = canvas.create_window(75, 1085, anchor="nw", height=30,window=entry_cus_12)
            
            label_2 = Label(canvas,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = canvas.create_window(394, 1050, anchor="nw", window=label_2)

            entry_cus_13=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_cus_13 = canvas.create_window(400, 1085, anchor="nw", height=30,window=entry_cus_13)

            label_2 = Label(canvas,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = canvas.create_window(675, 1050, anchor="nw", window=label_2)

            entry_cus_14=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_cus_14 = canvas.create_window(685, 1085, anchor="nw", height=30,window=entry_cus_14)

            label_2 = Label(canvas,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = canvas.create_window(1001, 1050, anchor="nw", window=label_2)

            entry_cus_15=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_cus_15 = canvas.create_window(1010, 1085, anchor="nw", height=30,window=entry_cus_15)

            chk_str_1 = StringVar()
            chkbtn2 = Checkbutton(canvas, text = "Agree to terms and conditions", variable = chk_str_1, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white")
            chkbtn2.select()
            window_chkbtn_2 = canvas.create_window(69, 1150, anchor="nw", window=chkbtn2)

            cus_btn2=Button(canvas,text='Submit Form', width=25,height=2,foreground="white",background="#1b3857",font='arial 12')
            window_cus_btn2 = canvas.create_window(550, 1200, anchor="nw", window=cus_btn2)



        btn2=Button(canvas,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=add_inv_customer)
        window_btn2 = canvas.create_window(285, 475, anchor="nw", window=btn2)

        label_2 = Label(canvas,width=15,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(400, 450, anchor="nw", window=label_2)

        entry_1=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_1 = canvas.create_window(450, 475, anchor="nw", height=30,window=entry_1)

        label_2 = Label(canvas,width=15,height=1,text="Invoice Date:", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(57, 550, anchor="nw", window=label_2)

        entry_1=DateEntry(canvas,width=40,justify=LEFT,foreground='white')
        window_entry_1 = canvas.create_window(80, 575, anchor="nw", height=30, window=entry_1)

        label_2 = Label(canvas,width=15,height=1,text="Terms", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(402, 550, anchor="nw", window=label_2)

        entry_1=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_1 = canvas.create_window(450, 575, anchor="nw", height=30, window=entry_1)

        label_2 = Label(canvas,width=15,height=1,text="Due Date:", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(770, 550, anchor="nw", window=label_2)

        entry_1=DateEntry(canvas,width=40,justify=LEFT,foreground='white')
        window_entry_1 = canvas.create_window(805, 575, anchor="nw", height=30, window=entry_1)

        label_2 = Label(canvas,width=15,height=1,text="Bill To:", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(35, 650, anchor="nw", window=label_2)

        # text_1=Text(canvas,width=31)
        # window_text_1 = canvas.create_window(81, 675, anchor="nw", height=150, window=text_1)
        entry_1=Entry(canvas,width=42,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_1 = canvas.create_window(81, 675, anchor="nw", height=150, window=entry_1)

        label_2 = Label(canvas,width=15,height=1,text="Place of supply", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(64, 860, anchor="nw", window=label_2)

        comb_2 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_2['values'] = ("Kerala","Andaman and Nicobar Islands","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Daman and Diu","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Ladakh","Lakshadweep","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Other Territory",)
        comb_2.current(0)
        window_comb_2 = canvas.create_window(82, 885, anchor="nw", width=251, height=30,window=comb_2)

        canvas.create_line(80, 950, 1240, 950, fill='gray',width=1)
        canvas.create_line(80, 1000, 1240, 1000, fill='gray',width=1)
        canvas.create_line(80, 1075, 1240, 1075, fill='gray',width=1)
        canvas.create_line(80, 950, 80, 1075, fill='gray',width=1)
        canvas.create_line(125, 950, 125, 1075, fill='gray',width=1)
        canvas.create_line(325, 950, 325, 1075, fill='gray',width=1)
        canvas.create_line(525, 950, 525, 1075, fill='gray',width=1)
        canvas.create_line(735, 950, 735, 1075, fill='gray',width=1)
        canvas.create_line(850, 950, 850, 1075, fill='gray',width=1)
        canvas.create_line(980, 950, 980, 1075, fill='gray',width=1)
        canvas.create_line(1100, 950, 1100, 1075, fill='gray',width=1)
        canvas.create_line(1240, 950, 1240, 1075, fill='gray',width=1)

        label_2 = Label(canvas,width=2,height=1,text="#", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(90, 970, anchor="nw", window=label_2)
        label_3 = Label(canvas,width=15,height=1,text="PRODUCT/SERVICE", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_3 = canvas.create_window(155, 970, anchor="nw", window=label_3)
        label_4 = Label(canvas,width=10,height=1,text="HSN", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_4 = canvas.create_window(380, 970, anchor="nw", window=label_4)
        label_4 = Label(canvas,width=11,height=1,text="DESCRIPTION", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_4 = canvas.create_window(580, 970, anchor="nw", window=label_4)
        label_4 = Label(canvas,width=5,height=1,text="QTY", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_4 = canvas.create_window(770, 970, anchor="nw", window=label_4)
        label_4 = Label(canvas,width=8,height=1,text="PRICE", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_4 = canvas.create_window(880, 970, anchor="nw", window=label_4)
        label_4 = Label(canvas,width=8,height=1,text="TOTAL", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_4 = canvas.create_window(1005, 970, anchor="nw", window=label_4)
        label_4 = Label(canvas,width=8,height=1,text="TAX (%)", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_4 = canvas.create_window(1130, 970, anchor="nw", window=label_4)

        label_2 = Label(canvas,width=2,height=1,text="1", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(90, 1020, anchor="nw", window=label_2)

        comb_3 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_3['values'] = ("Select Product",)
        comb_3.current(0)
        window_comb_3 = canvas.create_window(135, 1015, anchor="nw", width=180, height=30,window=comb_3)

        entry_1=Entry(canvas,width=30,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_1 = canvas.create_window(335, 1015, anchor="nw", height=30, window=entry_1)

        entry_1=Entry(canvas,width=31,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_1 = canvas.create_window(535, 1015, anchor="nw", height=30, window=entry_1)

        entry_1=Entry(canvas,width=15,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_1 = canvas.create_window(745, 1015, anchor="nw", height=30, window=entry_1)

        entry_1=Entry(canvas,width=18,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_1 = canvas.create_window(860, 1015, anchor="nw", height=30, window=entry_1)

        entry_1=Entry(canvas,width=16,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_1 = canvas.create_window(990, 1015, anchor="nw", height=30, window=entry_1)

        comb_4 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_4['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
        comb_4.current(0)
        window_comb_4 = canvas.create_window(1110, 1015, anchor="nw", width=120, height=30,window=comb_4)

        canvas.create_line(80, 1150, 1240, 1150, fill='gray',width=1)
        canvas.create_line(80, 1225, 1240, 1225, fill='gray',width=1)
        canvas.create_line(80, 1300, 1240, 1300, fill='gray',width=1)
        canvas.create_line(80, 1075, 80, 1300, fill='gray',width=1)
        canvas.create_line(1240, 1075, 1240, 1300, fill='gray',width=1)
        canvas.create_line(125, 1075, 125, 1300, fill='gray',width=1)
        canvas.create_line(325, 1075, 325, 1300, fill='gray',width=1)
        canvas.create_line(525, 1075, 525, 1300, fill='gray',width=1)
        canvas.create_line(735, 1075, 735, 1300, fill='gray',width=1)
        canvas.create_line(850, 1075, 850, 1300, fill='gray',width=1)
        canvas.create_line(980, 1075, 980, 1300, fill='gray',width=1)
        canvas.create_line(1100, 1075, 1100, 1300, fill='gray',width=1)

        label_2 = Label(canvas,width=2,height=1,text="2", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(90, 1100, anchor="nw", window=label_2)

        comb_4 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_4['values'] = ("Select Product",)
        comb_4.current(0)
        window_comb_4 = canvas.create_window(135, 1095, anchor="nw", width=180, height=30,window=comb_4)

        entry_2=Entry(canvas,width=30,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_2 = canvas.create_window(335, 1095, anchor="nw", height=30, window=entry_2)

        entry_2_1=Entry(canvas,width=31,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_2_1 = canvas.create_window(535, 1095, anchor="nw", height=30, window=entry_2_1)

        entry_2_2=Entry(canvas,width=15,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_2_2 = canvas.create_window(745, 1095, anchor="nw", height=30, window=entry_2_2)

        entry_2_3=Entry(canvas,width=18,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_2_3 = canvas.create_window(860, 1095, anchor="nw", height=30, window=entry_2_3)

        entry_2_4=Entry(canvas,width=16,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_2_4 = canvas.create_window(990, 1095, anchor="nw", height=30, window=entry_2_4)

        comb_2_5 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_2_5['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
        comb_2_5.current(0)
        window_comb_2_5 = canvas.create_window(1110, 1095, anchor="nw", width=120, height=30,window=comb_2_5)


        label_2 = Label(canvas,width=2,height=1,text="3", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(90, 1170, anchor="nw", window=label_2)

        comb_5 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_5['values'] = ("Select Product",)
        comb_5.current(0)
        window_comb_5 = canvas.create_window(135, 1165, anchor="nw", width=180, height=30,window=comb_5)

        entry_3=Entry(canvas,width=30,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_3 = canvas.create_window(335, 1165, anchor="nw", height=30, window=entry_3)

        entry_3_1=Entry(canvas,width=31,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_3_1 = canvas.create_window(535, 1165, anchor="nw", height=30, window=entry_3_1)

        entry_3_2=Entry(canvas,width=15,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_3_2 = canvas.create_window(745, 1165, anchor="nw", height=30, window=entry_3_2)

        entry_3_3=Entry(canvas,width=18,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_3_3 = canvas.create_window(860, 1165, anchor="nw", height=30, window=entry_3_3)

        entry_3_4=Entry(canvas,width=16,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_3_4 = canvas.create_window(990, 1165, anchor="nw", height=30, window=entry_3_4)

        comb_3_5 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_3_5['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
        comb_3_5.current(0)
        window_comb_3_5 = canvas.create_window(1110, 1165, anchor="nw", width=120, height=30,window=comb_3_5)

        label_2 = Label(canvas,width=2,height=1,text="4", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(90, 1245, anchor="nw", window=label_2)

        comb_6 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_6['values'] = ("Select Product",)
        comb_6.current(0)
        window_comb_6 = canvas.create_window(135, 1240, anchor="nw", width=180, height=30,window=comb_6)

        entry_4=Entry(canvas,width=30,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_4 = canvas.create_window(335, 1240, anchor="nw", height=30, window=entry_4)

        entry_4_1=Entry(canvas,width=31,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_4_1 = canvas.create_window(535, 1240, anchor="nw", height=30, window=entry_4_1)

        entry_4_2=Entry(canvas,width=15,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_4_2 = canvas.create_window(745, 1240, anchor="nw", height=30, window=entry_4_2)

        entry_4_3=Entry(canvas,width=18,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_4_3 = canvas.create_window(860, 1240, anchor="nw", height=30, window=entry_4_3)

        entry_4_4=Entry(canvas,width=16,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_4_4 = canvas.create_window(990, 1240, anchor="nw", height=30, window=entry_4_4)

        comb_4_5 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_4_5['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
        comb_4_5.current(0)
        window_comb_4_5 = canvas.create_window(1110, 1240, anchor="nw", width=120, height=30,window=comb_4_5)

        canvas.create_line(850, 1350, 1240, 1350, fill='gray',width=1)
        canvas.create_line(850, 1400, 1240, 1400, fill='gray',width=1)
        canvas.create_line(850, 1450, 1240, 1450, fill='gray',width=1)
        canvas.create_line(850, 1500, 1240, 1500, fill='gray',width=1)
        canvas.create_line(850, 1550, 1240, 1550, fill='gray',width=1)
        canvas.create_line(850, 1600, 1240, 1600, fill='gray',width=1)
        canvas.create_line(850, 1350, 850, 1600, fill='gray',width=1)
        canvas.create_line(1000, 1350, 1000, 1600, fill='gray',width=1)
        canvas.create_line(1240, 1350, 1240, 1600, fill='gray',width=1)

        label_5 = Label(canvas,width=12,height=1,text="Sub Total", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_5 = canvas.create_window(870, 1365, anchor="nw", window=label_5)
        label_5 = Label(canvas,width=12,height=1,text="Tax Amount", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_5 = canvas.create_window(870, 1415, anchor="nw", window=label_5)
        label_5 = Label(canvas,width=12,height=1,text="Grand Total", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_5 = canvas.create_window(870, 1465, anchor="nw", window=label_5)
        label_5 = Label(canvas,width=12,height=1,text="Amount Received", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_5 = canvas.create_window(870, 1515, anchor="nw", window=label_5)
        label_5 = Label(canvas,width=12,height=1,text="Balance Due", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_5 = canvas.create_window(870, 1565, anchor="nw", window=label_5)

        sub_entry_1=Entry(canvas,width=36,justify=LEFT,background='#2f516f',foreground="white")
        window_sub_entry_1 = canvas.create_window(1010, 1360, anchor="nw", height=30, window=sub_entry_1)

        tax_entry_1=Entry(canvas,width=36,justify=LEFT,background='#2f516f',foreground="white")
        window_tax_entry_1 = canvas.create_window(1010, 1410, anchor="nw", height=30, window=tax_entry_1)

        grand_entry_1=Entry(canvas,width=36,justify=LEFT,background='#2f516f',foreground="white")
        window_grand_entry_1 = canvas.create_window(1010, 1460, anchor="nw", height=30, window=grand_entry_1)

        amount_entry_1=Entry(canvas,width=36,justify=LEFT,background='#2f516f',foreground="white")
        window_amount_entry_1 = canvas.create_window(1010, 1510, anchor="nw", height=30, window=amount_entry_1)

        bal_entry_1=Entry(canvas,width=36,justify=LEFT,background='#2f516f',foreground="white")
        window_bal_entry_1 = canvas.create_window(1010, 1560, anchor="nw", height=30, window=bal_entry_1)


        btn1=Button(canvas,text='Save', width=15,height=2,foreground="white",background="#1b3857",font='arial 12')
        window_btn1 = canvas.create_window(1050, 1625, anchor="nw", window=btn1)
        

    btn1=Button(canvas,text='Add Invoices', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_invoice)
    window_btn1 = canvas.create_window(1050, 275, anchor="nw", window=btn1)

    #-------------------------------Customers-----------------------------#
    cus_frame = Frame(tab3_3)
    cus_frame.grid(row=0,column=0,sticky='nsew')
    canvas=Canvas(cus_frame, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,1000))

    vertibar=Scrollbar(cus_frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1325,height=559)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)

    def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
            
        points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]
    
        return canvas.create_polygon(points, **kwargs, smooth=True)
    
    my_rectangle = round_rectangle(20, 50, 1300, 200, radius=20, fill="#1b3857")
    label_1 = Label(canvas,width=12,height=1,text="CUSTOMERS", font=('arial 25'),background="#1b3857",fg="white") 
    window_label_1 = canvas.create_window(550, 85, anchor="nw", window=label_1)
    canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

    my_rectangle_1 = round_rectangle(20, 250, 1300, 700, radius=20, fill="#1b3857")


    canvas.create_line(60, 350, 1260, 350, fill='gray',width=1)
    canvas.create_line(60, 350, 60, 400, fill='gray',width=1)
    canvas.create_line(210, 350, 210, 400, fill='gray',width=1)
    canvas.create_line(490, 350, 490, 400, fill='gray',width=1)
    canvas.create_line(640, 350, 640, 400, fill='gray',width=1)
    canvas.create_line(800, 350, 800, 400, fill='gray',width=1)
    canvas.create_line(970, 350, 970, 400, fill='gray',width=1)
    canvas.create_line(1120, 350, 1120, 400, fill='gray',width=1)
    canvas.create_line(1260, 350, 1260, 400, fill='gray',width=1)

    label_2 = Label(canvas,width=10,height=1,text="CUSTOMER", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(90, 365, anchor="nw", window=label_2)
    label_3 = Label(canvas,width=11,height=1,text="GST TYPE", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_3 = canvas.create_window(300, 365, anchor="nw", window=label_3)
    label_4 = Label(canvas,width=11,height=1,text="GSTIN", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = canvas.create_window(520, 365, anchor="nw", window=label_4)
    label_4 = Label(canvas,width=8,height=1,text="PAN NO", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = canvas.create_window(680, 365, anchor="nw", window=label_4)
    label_4 = Label(canvas,width=8,height=1,text="EMAIL ID", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = canvas.create_window(850, 365, anchor="nw", window=label_4)
    label_4 = Label(canvas,width=11,height=1,text="MOBILE NO", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = canvas.create_window(1000, 365, anchor="nw", window=label_4)
    label_4 = Label(canvas,width=11,height=1,text="ACTION", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = canvas.create_window(1140, 365, anchor="nw", window=label_4)

    canvas.create_line(60, 400, 1260, 400, fill='gray',width=1)
    canvas.create_line(60, 400, 60, 450, fill='gray',width=1)
    canvas.create_line(210, 400, 210, 450, fill='gray',width=1)
    canvas.create_line(490, 400, 490, 450, fill='gray',width=1)
    canvas.create_line(640, 400, 640, 450, fill='gray',width=1)
    canvas.create_line(800, 400, 800, 450, fill='gray',width=1)
    canvas.create_line(970, 400, 970, 450, fill='gray',width=1)
    canvas.create_line(1120, 400, 1120, 450, fill='gray',width=1)
    canvas.create_line(1260, 400, 1260, 450, fill='gray',width=1)

    # Define the style for combobox widget
    # style= ttk.Style()
    # style.theme_use('clam')
    # style.configure("TCombobox", fieldbackground= "#2f516f", background= "#2f516f")

    cus_comb_1 = ttk.Combobox(canvas,font=('arial 10'),foreground="white")
    cus_comb_1['values'] = ("Actions","Edit","Delete")
    cus_comb_1.current(0)
    window_cus_comb_1 = canvas.create_window(1135, 410, anchor="nw", width=110,height=30,window=cus_comb_1)


    canvas.create_line(60, 450, 1260, 450, fill='gray',width=1)

    def add_customer():
        cus_frame.grid_forget()
        cus_frame_1 = Frame(tab3_3)
        cus_frame_1.grid(row=0,column=0,sticky='nsew')
        canvas=Canvas(cus_frame_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1600))
        
        vertibar=Scrollbar(cus_frame_1, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)

        canvas.config(width=1325,height=559)
        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
            
            points = [x1+radius, y1,
                    x1+radius, y1,
                    x2-radius, y1,
                    x2-radius, y1,
                    x2, y1,
                    x2, y1+radius,
                    x2, y1+radius,
                    x2, y2-radius,
                    x2, y2-radius,
                    x2, y2,
                    x2-radius, y2,
                    x2-radius, y2,
                    x1+radius, y2,
                    x1+radius, y2,
                    x1, y2,
                    x1, y2-radius,
                    x1, y2-radius,
                    x1, y1+radius,
                    x1, y1+radius,
                    x1, y1]
        
            return canvas.create_polygon(points, **kwargs, smooth=True)

        my_rectangle = round_rectangle(20, 50, 1300, 200, radius=20, fill="#1b3857")
        label_1 = Label(canvas,width=15,height=1,text="ADD CUSTOMER", font=('arial 20'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(550, 85, anchor="nw", window=label_1)
        canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

        my_rectangle = round_rectangle(20, 250, 1300, 1535, radius=20, fill="#1b3857")
        label_1 = Label(canvas,width=20,height=1,text="Customer Information", font=('arial 20'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(60, 275, anchor="nw", window=label_1)
        canvas.create_line(60, 330, 1260, 330, fill='gray',width=1)

        label_2 = Label(canvas,width=5,height=1,text="Title", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(62, 365, anchor="nw", window=label_2)

        comb_cus_1 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_cus_1['values'] = ("Mr","Mrs","Miss","Ms",)
        comb_cus_1.current(0)
        window_comb_cus_1 = canvas.create_window(75, 395, anchor="nw", width=245, height=30,window=comb_cus_1)

        label_2 = Label(canvas,width=10,height=1,text="First name", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(400, 365, anchor="nw", window=label_2)

        entry_cus_1=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_1 = canvas.create_window(410, 395, anchor="nw", height=30,window=entry_cus_1)

        label_2 = Label(canvas,width=10,height=1,text="Last name", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(745, 365, anchor="nw", window=label_2)

        entry_cus_2=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_2 = canvas.create_window(755, 395, anchor="nw", height=30,window=entry_cus_2)

        label_2 = Label(canvas,width=10,height=1,text="Company", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(62, 465, anchor="nw", window=label_2)

        entry_cus_3=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_3 = canvas.create_window(75, 495, anchor="nw", height=30,window=entry_cus_3)

        label_2 = Label(canvas,width=10,height=1,text="Location", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(395, 465, anchor="nw", window=label_2)

        cus_4=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_cus_4 = canvas.create_window(410, 495, anchor="nw", height=30,window=cus_4)

        label_2 = Label(canvas,width=10,height=1,text="GST type", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(62, 565, anchor="nw", window=label_2)

        comb_cus_2 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
        comb_cus_2['values'] = ("Choose...","GST registered Regular","GST registered-Composition","GST unregistered","Consumer","Overseas","SEZ","Deemed exports-EOU's STP's EHTP's etc",)
        comb_cus_2.current(0)
        window_comb_cus_2 = canvas.create_window(75, 595, anchor="nw", width=245, height=30,window=comb_cus_2)

        label_2 = Label(canvas,width=10,height=1,text="GSTIN", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(385, 565, anchor="nw", window=label_2)

        cus_entry_str_1 = StringVar()
        entry_cus_5=Entry(canvas,width=34,justify=LEFT,background='#2f516f',foreground="white",font=('arial 10'),textvariable=cus_entry_str_1)
        cus_entry_str_1.set(' 29APPCK7465F1Z1')
        window_entry_cus_5 = canvas.create_window(410, 595, anchor="nw", height=30,window=entry_cus_5)

        label_2 = Label(canvas,width=10,height=1,text="PAN NO", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(740, 565, anchor="nw", window=label_2)

        cus_entry_str_2 = StringVar()
        entry_cus_6=Entry(canvas,width=34,justify=LEFT,background='#2f516f',foreground="white",font=('arial 10'),textvariable=cus_entry_str_2)
        cus_entry_str_2.set(' APPCK7465F')
        window_entry_cus_6 = canvas.create_window(755, 595, anchor="nw", height=30,window=entry_cus_6)

        label_2 = Label(canvas,width=5,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(71, 665, anchor="nw", window=label_2)

        entry_cus_7=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_7 = canvas.create_window(75, 695, anchor="nw", height=30,window=entry_cus_7)

        label_2 = Label(canvas,width=10,height=1,text="Website", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(395, 665, anchor="nw", window=label_2)

        entry_cus_8=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_8 = canvas.create_window(410, 695, anchor="nw", height=30,window=entry_cus_8)

        label_2 = Label(canvas,width=10,height=1,text="Mobile", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(736, 665, anchor="nw", window=label_2)

        entry_cus_9=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_9 = canvas.create_window(752, 695, anchor="nw", height=30,window=entry_cus_9)

        label_1 = Label(canvas,width=20,height=1,text="Billing Address", font=('arial 16'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(23, 775, anchor="nw", window=label_1)

        label_2 = Label(canvas,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(71, 825, anchor="nw", window=label_2)

        entry_cus_10=Entry(canvas,width=95,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_10 = canvas.create_window(75, 855, anchor="nw", height=60,window=entry_cus_10)

        label_1 = Label(canvas,width=20,height=1,text="Shipping Address", font=('arial 16'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(645, 775, anchor="nw", window=label_1)

        chk_str = StringVar()
        chkbtn1 = Checkbutton(canvas, text = "Same As Billing Address", variable = chk_str, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f")
        chkbtn1.select()
        window_chkbtn_1 = canvas.create_window(865, 775, anchor="nw", window=chkbtn1)

        label_2 = Label(canvas,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(681, 825, anchor="nw", window=label_2)

        entry_cus_11=Entry(canvas,width=95,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_11 = canvas.create_window(685, 855, anchor="nw", height=60,window=entry_cus_11)

        label_2 = Label(canvas,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(65, 950, anchor="nw", window=label_2)

        entry_cus_12=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_12 = canvas.create_window(75, 985, anchor="nw", height=30,window=entry_cus_12)
        
        label_2 = Label(canvas,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(395, 950, anchor="nw", window=label_2)

        entry_cus_13=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_13 = canvas.create_window(400, 985, anchor="nw", height=30,window=entry_cus_13)

        label_2 = Label(canvas,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(675, 950, anchor="nw", window=label_2)

        entry_cus_14=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_14 = canvas.create_window(685, 985, anchor="nw", height=30,window=entry_cus_14)

        label_2 = Label(canvas,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(1001, 950, anchor="nw", window=label_2)

        entry_cus_15=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_15 = canvas.create_window(1010, 985, anchor="nw", height=30,window=entry_cus_15)

        label_2 = Label(canvas,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(65, 1050, anchor="nw", window=label_2)

        entry_cus_12=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_12 = canvas.create_window(75, 1085, anchor="nw", height=30,window=entry_cus_12)
        
        label_2 = Label(canvas,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(394, 1050, anchor="nw", window=label_2)

        entry_cus_13=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_13 = canvas.create_window(400, 1085, anchor="nw", height=30,window=entry_cus_13)

        label_2 = Label(canvas,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(675, 1050, anchor="nw", window=label_2)

        entry_cus_14=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_14 = canvas.create_window(685, 1085, anchor="nw", height=30,window=entry_cus_14)

        label_2 = Label(canvas,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = canvas.create_window(1001, 1050, anchor="nw", window=label_2)

        entry_cus_15=Entry(canvas,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_15 = canvas.create_window(1010, 1085, anchor="nw", height=30,window=entry_cus_15)

        chk_str_1 = StringVar()
        chkbtn2 = Checkbutton(canvas, text = "Agree to terms and conditions", variable = chk_str_1, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white")
        chkbtn2.select()
        window_chkbtn_2 = canvas.create_window(69, 1150, anchor="nw", window=chkbtn2)

        cus_btn2=Button(canvas,text='Submit Form', width=25,height=2,foreground="white",background="#1b3857",font='arial 12')
        window_cus_btn2 = canvas.create_window(550, 1200, anchor="nw", window=cus_btn2)

    btn1=Button(canvas,text='Add Customer', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_customer)
    window_btn1 = canvas.create_window(1050, 275, anchor="nw", window=btn1)

    #---------------------------Product & Services------------------------#
    pro_frame = Frame(tab3_4)
    pro_frame.grid(row=0,column=0,sticky='nsew')
    canvas=Canvas(pro_frame, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,1000))

    vertibar=Scrollbar(pro_frame, orient=VERTICAL)
    vertibar.pack(side=RIGHT,fill=Y)
    vertibar.config(command=canvas.yview)
    canvas.config(width=1325,height=559)

    canvas.config(yscrollcommand=vertibar.set)
    canvas.pack(expand=True,side=LEFT,fill=BOTH)

    def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
            
        points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]
    
        return canvas.create_polygon(points, **kwargs, smooth=True)
    
    my_rectangle = round_rectangle(20, 50, 1300, 200, radius=20, fill="#1b3857")
    label_1 = Label(canvas,width=23,height=1,text="PRODUCT AND SERVICES", font=('arial 25'),background="#1b3857",fg="white") 
    window_label_1 = canvas.create_window(480, 85, anchor="nw", window=label_1)
    canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

    my_rectangle_1 = round_rectangle(20, 250, 1300, 800, radius=20, fill="#1b3857")

    image_1 = Image.open("images/lowstock.png")
    resize_image = image_1.resize((90,90))
    image_1 = ImageTk.PhotoImage(resize_image)
    btlogo = Label(canvas, width=90, height=90, background="#1b3857", image = image_1) 
    window_image = canvas.create_window(250, 280, anchor="nw", window=btlogo)
    btlogo.photo = image_1

    label_2 = Label(canvas,width=15,height=1,text="LOW STOCK : ", font=('arial 18'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(230, 380, anchor="nw", window=label_2)

    image_2 = Image.open("images/outofstock.png")
    resize_image_1 = image_2.resize((90,90))
    image_2 = ImageTk.PhotoImage(resize_image_1)
    btlogo_1 = Label(canvas, width=90, height=90, background="#1b3857", image = image_2) 
    window_image_1 = canvas.create_window(650, 280, anchor="nw", window=btlogo_1)
    btlogo_1.photo = image_2

    label_2 = Label(canvas,width=15,height=1,text="OUT OF STOCK : ", font=('arial 18'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(640, 380, anchor="nw", window=label_2)


    canvas.create_line(60, 500, 1260, 500, fill='gray',width=1)
    canvas.create_line(60, 500, 60, 550, fill='gray',width=1)
    canvas.create_line(280, 500, 280, 550, fill='gray',width=1)
    canvas.create_line(640, 500, 640, 550, fill='gray',width=1)
    canvas.create_line(800, 500, 800, 550, fill='gray',width=1)
    canvas.create_line(970, 500, 970, 550, fill='gray',width=1)
    canvas.create_line(1120, 500, 1120, 550, fill='gray',width=1)
    canvas.create_line(1260, 500, 1260, 550, fill='gray',width=1)

    label_2 = Label(canvas,width=10,height=1,text="TYPE", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_2 = canvas.create_window(125, 515, anchor="nw", window=label_2)
    label_3 = Label(canvas,width=11,height=1,text="NAME", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_3 = canvas.create_window(410, 515, anchor="nw", window=label_3)
    label_4 = Label(canvas,width=11,height=1,text="SKU", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = canvas.create_window(680, 515, anchor="nw", window=label_4)
    label_4 = Label(canvas,width=8,height=1,text="HSN/SAC", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = canvas.create_window(850, 515, anchor="nw", window=label_4)
    label_4 = Label(canvas,width=11,height=1,text="QUANTITY", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = canvas.create_window(1000, 515, anchor="nw", window=label_4)
    label_4 = Label(canvas,width=11,height=1,text="ACTION", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = canvas.create_window(1140, 515, anchor="nw", window=label_4)

    canvas.create_line(60, 550, 1260, 550, fill='gray',width=1)
    canvas.create_line(60, 550, 60, 600, fill='gray',width=1)
    canvas.create_line(280, 550, 280, 600, fill='gray',width=1)
    canvas.create_line(640, 550, 640, 600, fill='gray',width=1)
    canvas.create_line(800, 550, 800, 600, fill='gray',width=1)
    canvas.create_line(970, 550, 970, 600, fill='gray',width=1)
    canvas.create_line(1120, 550, 1120, 600, fill='gray',width=1)
    canvas.create_line(1260, 500, 1260, 600, fill='gray',width=1)

    # Define the style for combobox widget
    # style= ttk.Style(canvas)
    # style.theme_use('clam')
    # style.configure("TCombobox", fieldbackground= "#2f516f", background= "#2f516f")

    cus_comb_1 = ttk.Combobox(canvas,font=('arial 10'),foreground="white")
    cus_comb_1['values'] = ("Actions","Edit","Delete")
    cus_comb_1.current(0)
    window_cus_comb_1 = canvas.create_window(1135, 560, anchor="nw", width=110,height=30,window=cus_comb_1)


    canvas.create_line(60, 600, 1260, 600, fill='gray',width=1)

    def add_product():
        pro_frame.grid_forget()
        pro_frame_1 = Frame(tab3_4)
        pro_frame_1.grid(row=0,column=0,sticky='nsew')
        canvas=Canvas(pro_frame_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1000))
        
        vertibar=Scrollbar(pro_frame_1, orient=VERTICAL)
        vertibar.pack(side=RIGHT,fill=Y)
        vertibar.config(command=canvas.yview)

        canvas.config(width=1325,height=559)
        canvas.config(yscrollcommand=vertibar.set)
        canvas.pack(expand=True,side=LEFT,fill=BOTH)
        def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
            
            points = [x1+radius, y1,
                    x1+radius, y1,
                    x2-radius, y1,
                    x2-radius, y1,
                    x2, y1,
                    x2, y1+radius,
                    x2, y1+radius,
                    x2, y2-radius,
                    x2, y2-radius,
                    x2, y2,
                    x2-radius, y2,
                    x2-radius, y2,
                    x1+radius, y2,
                    x1+radius, y2,
                    x1, y2,
                    x1, y2-radius,
                    x1, y2-radius,
                    x1, y1+radius,
                    x1, y1+radius,
                    x1, y1]
        
            return canvas.create_polygon(points, **kwargs, smooth=True)

        my_rectangle = round_rectangle(20, 50, 1300, 200, radius=20, fill="#1b3857")
        label_1 = Label(canvas,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
        window_label_1 = canvas.create_window(480, 85, anchor="nw", window=label_1)
        canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

        my_rectangle = round_rectangle(20, 250, 1300, 900, radius=20, fill="#1b3857")

        my_rectangle = round_rectangle(200, 300, 650, 550, radius=20, fill="#2f516f")

        label_1 = Label(canvas,width=10,height=1,text="Inventory", font=('arial 20'),background="#2f516f",fg="white") 
        window_label_1 = canvas.create_window(340, 350, anchor="nw", window=label_1)

        label_1 = Label(canvas,width=45,height=2,text="Inventory is the goods available for sale and raw materials \nused to produce goods available for sale.", font=('arial 12'),background="#2f516f",fg="white") 
        window_label_1 = canvas.create_window(220, 400, anchor="nw", window=label_1)

        def inv_add_item():
            pro_frame_1.grid_forget()
            pro_frame_2 = Frame(tab3_4)
            pro_frame_2.grid(row=0,column=0,sticky='nsew')
            canvas=Canvas(pro_frame_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))
            
            vertibar=Scrollbar(pro_frame_2, orient=VERTICAL)
            vertibar.pack(side=RIGHT,fill=Y)
            vertibar.config(command=canvas.yview)

            canvas.config(width=1325,height=559)
            canvas.config(yscrollcommand=vertibar.set)
            canvas.pack(expand=True,side=LEFT,fill=BOTH)
            def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
                
                points = [x1+radius, y1,
                        x1+radius, y1,
                        x2-radius, y1,
                        x2-radius, y1,
                        x2, y1,
                        x2, y1+radius,
                        x2, y1+radius,
                        x2, y2-radius,
                        x2, y2-radius,
                        x2, y2,
                        x2-radius, y2,
                        x2-radius, y2,
                        x1+radius, y2,
                        x1+radius, y2,
                        x1, y2,
                        x1, y2-radius,
                        x1, y2-radius,
                        x1, y1+radius,
                        x1, y1+radius,
                        x1, y1]
            
                return canvas.create_polygon(points, **kwargs, smooth=True)

            my_rectangle = round_rectangle(20, 50, 1300, 200, radius=20, fill="#1b3857")
            label_1 = Label(canvas,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(470, 85, anchor="nw", window=label_1)
            canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

            my_rectangle = round_rectangle(20, 250, 1300, 2000, radius=20, fill="#1b3857")

            my_rectangle = round_rectangle(50, 300, 1270, 450, radius=20, fill="#2f516f")
            label_1 = Label(canvas,width=10,height=2,text="INVENTORY", font=('arial 20'),background="#2f516f",fg="white") 
            window_label_1 = canvas.create_window(475, 350, anchor="nw", window=label_1)
            btn_item_1=Button(canvas,text='Choose Type', width=15,height=1,foreground="white",background="#2f516f",font='arial 20',  command=add_product)
            window_btn_item_1 = canvas.create_window(750, 350, anchor="nw", window=btn_item_1)

            label_1 = Label(canvas,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(51, 500, anchor="nw", window=label_1)

            entry_inv_item_1=Entry(canvas,width=200,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_1 = canvas.create_window(55, 530, anchor="nw", height=30,window=entry_inv_item_1)

            label_1 = Label(canvas,width=5,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(51, 600, anchor="nw", window=label_1)

            str_inv_item_1 = StringVar()
            entry_inv_item_2=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_inv_item_1)
            str_inv_item_1.set('  Eg: N41554')
            window_entry_entry_inv_item_2 = canvas.create_window(55, 630, anchor="nw", height=30,window=entry_inv_item_2)

            label_1 = Label(canvas,width=9,height=1,text="HSN Code", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(710, 600, anchor="nw", window=label_1)

            entry_inv_item_2=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_2 = canvas.create_window(710, 630, anchor="nw", height=30,window=entry_inv_item_2)

            label_1 = Label(canvas,width=30,height=1,text="Not sure about HSN Code..? Click here", font=('arial 12'),background="#1b3857",fg="skyblue") 
            window_label_1 = canvas.create_window(710, 660, anchor="nw", window=label_1)

            label_1 = Label(canvas,width=5,height=1,text="Unit", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(48, 710, anchor="nw", window=label_1)

            comb_inv_item_1 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            comb_inv_item_1['values'] = ("Choose...","BAG Bags","BAL Bale BOU","BDL Bundles","BKL Buckles","BOX Box","BTL Bottles","CAN Cans","CTN Cartons","CCM Cubic centimeters","CBM Cubic meters","CMS Centimeters","DRM Drums","DOZ Dozens","GGK Great gross GYD","GRS GrossGMS","KME Kilometre","KGS Kilograms","KLR Kilo litre","MTS Metric ton","MLT Mili litre","MTR Meters","NOS Numbers","PAC Packs","PCS Pieces","PRS Pairs","QTL Quintal","ROL Rolls","SQY Square Yards","SET Sets","SQF Square feet","SQM Square meters","TBS Tablets","TUB Tubes","TGM Ten Gross","THD Thousands","TON Tonnes","UNT Units","UGS US Gallons","YDS Yards",)
            comb_inv_item_1.current(0)
            window_comb_inv_item_1 = canvas.create_window(55, 740, anchor="nw", width=540, height=30,window=comb_inv_item_1)

            label_1 = Label(canvas,width=9,height=1,text="Category", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(705, 710, anchor="nw", window=label_1)

            entry_inv_item_3=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_3 = canvas.create_window(710, 740, anchor="nw", height=30,window=entry_inv_item_3)

            label_1 = Label(canvas,width=22,height=1,text="Initial quantity on hand", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(30, 810, anchor="nw", window=label_1)

            entry_inv_item_4=Entry(canvas,width=60,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_4 = canvas.create_window(55, 840, anchor="nw", height=30,window=entry_inv_item_4)

            label_1 = Label(canvas,width=10,height=1,text="As of date", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(450, 810, anchor="nw", window=label_1)

            entry_inv_item_5=DateEntry(canvas,width=60,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_5 = canvas.create_window(460, 840, anchor="nw", height=30,window=entry_inv_item_5)

            label_1 = Label(canvas,width=14,height=1,text="Low stock alert", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(875, 810, anchor="nw", window=label_1)

            entry_inv_item_6=Entry(canvas,width=60,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_6 = canvas.create_window(885, 840, anchor="nw", height=30,window=entry_inv_item_6)

            label_1 = Label(canvas,width=22,height=1,text="Inventory asset account", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(35, 910, anchor="nw", window=label_1)

            comb_inv_item_2 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            comb_inv_item_2['values'] = ("Inventory Asset",)
            comb_inv_item_2.current(0)
            window_comb_inv_item_2 = canvas.create_window(55, 940, anchor="nw", width=480, height=30,window=comb_inv_item_2)

            def inv_acc_create_1():
                pro_frame_2.grid_forget()
                pro_frame_2_1 = Frame(tab3_4)
                pro_frame_2_1.grid(row=0,column=0,sticky='nsew')
                canvas=Canvas(pro_frame_2_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))
                
                vertibar=Scrollbar(pro_frame_2_1, orient=VERTICAL)
                vertibar.pack(side=RIGHT,fill=Y)
                vertibar.config(command=canvas.yview)

                canvas.config(width=1325,height=559)
                canvas.config(yscrollcommand=vertibar.set)
                canvas.pack(expand=True,side=LEFT,fill=BOTH)
                def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
                    
                    points = [x1+radius, y1,
                            x1+radius, y1,
                            x2-radius, y1,
                            x2-radius, y1,
                            x2, y1,
                            x2, y1+radius,
                            x2, y1+radius,
                            x2, y2-radius,
                            x2, y2-radius,
                            x2, y2,
                            x2-radius, y2,
                            x2-radius, y2,
                            x1+radius, y2,
                            x1+radius, y2,
                            x1, y2,
                            x1, y2-radius,
                            x1, y2-radius,
                            x1, y1+radius,
                            x1, y1+radius,
                            x1, y1]
                
                    return canvas.create_polygon(points, **kwargs, smooth=True)

                my_rectangle = round_rectangle(20, 50, 1300, 200, radius=20, fill="#1b3857")
                label_1 = Label(canvas,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(465, 85, anchor="nw", window=label_1)
                canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

                my_rectangle = round_rectangle(20, 250, 1300, 950, radius=20, fill="#1b3857")

                label_1 = Label(canvas,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(56, 300, anchor="nw", window=label_1)

                comb_inv_1_1 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_inv_1_1['values'] = ("Current Assets",)
                comb_inv_1_1.current(0)
                window_comb_inv_1_1 = canvas.create_window(55, 330, anchor="nw", width=540, height=30,window=comb_inv_1_1)

                label_1 = Label(canvas,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(710, 300, anchor="nw", window=label_1)

                entry_inv_1_2=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_inv_1_2 = canvas.create_window(710, 330, anchor="nw", height=30,window=entry_inv_1_2)

                label_1 = Label(canvas,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(54, 400, anchor="nw", window=label_1)

                comb_inv_1_2 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_inv_1_2['values'] = ("Inventory",)
                comb_inv_1_2.current(0)
                window_comb_inv_1_2 = canvas.create_window(55, 430, anchor="nw", width=540, height=30,window=comb_inv_1_2)

                label_1 = Label(canvas,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(705, 400, anchor="nw", window=label_1)

                entry_inv_1_4=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_inv_1_4 = canvas.create_window(710, 430, anchor="nw", height=30,window=entry_inv_1_4)

                inv_text_1 = Text(canvas,width=67, height=14, background='black',foreground='white')
                inv_text_1.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                window_inv_text_1 = canvas.create_window(55, 500, anchor="nw",window=inv_text_1)

                chk_str_inv_1_1 = StringVar()
                chkbtn_inv_1_1 = Checkbutton(canvas, text = "Is sub-account", variable = chk_str_inv_1_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white")
                chkbtn_inv_1_1.select()
                window_chkbtn_inv_1_1 = canvas.create_window(709, 500, anchor="nw", window=chkbtn_inv_1_1)

                comb_inv_1_3 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_inv_1_3['values'] = ("Choose...",)
                comb_inv_1_3.current(0)
                window_comb_inv_1_3 = canvas.create_window(710, 530, anchor="nw", width=540, height=30,window=comb_inv_1_3)

                label_1 = Label(canvas,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(705, 600, anchor="nw", window=label_1)

                comb_inv_1_4 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_inv_1_4['values'] = ("Choose...",)
                comb_inv_1_4.current(0)
                window_comb_inv_1_4 = canvas.create_window(710, 630, anchor="nw", width=540, height=30,window=comb_inv_1_4)

                inv_bac_btn_1_1=Button(canvas,text='Back', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=inv_add_item)
                window_inv_bac_btn_1_1 = canvas.create_window(450, 800, anchor="nw", window=inv_bac_btn_1_1)

                inv_sub_btn_1_1=Button(canvas,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                window_inv_sub_btn_1_1 = canvas.create_window(685, 800, anchor="nw", window=inv_sub_btn_1_1)

                

            asset_btn=Button(canvas,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=inv_acc_create_1)
            window_asset_btn = canvas.create_window(545, 940, anchor="nw", window=asset_btn)

            label_1 = Label(canvas,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(51, 1010, anchor="nw", window=label_1)

            entry_inv_item_7=Entry(canvas,width=200,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_7 = canvas.create_window(55, 1040, anchor="nw", height=60,window=entry_inv_item_7)

            label_1 = Label(canvas,width=15,height=1,text="Sales price/rate", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(45, 1140, anchor="nw", window=label_1)
            
            entry_inv_item_8=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_8 = canvas.create_window(55, 1170, anchor="nw", height=30,window=entry_inv_item_8)

            chk_str_inv_item = StringVar()
            chkbtn_inv_item_1 = Checkbutton(canvas, text = "Inclusive of tax", variable = chk_str_inv_item, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white")
            chkbtn_inv_item_1.select()
            window_chkbtn_inv_item_1 = canvas.create_window(55, 1205, anchor="nw", window=chkbtn_inv_item_1)

            label_1 = Label(canvas,width=4,height=1,text="Tax", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(703, 1140, anchor="nw", window=label_1)

            comb_inv_item_3 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            comb_inv_item_3['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
            comb_inv_item_3.current(0)
            window_comb_inv_item_3 = canvas.create_window(710, 1170, anchor="nw", width=540, height=30,window=comb_inv_item_3)

            label_1 = Label(canvas,width=15,height=1,text="Income account", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(41, 1270, anchor="nw", window=label_1)

            comb_inv_item_4 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            comb_inv_item_4['values'] = ("Choose...","Billable Expense Income","Product Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintanance","Sales of Product Income","Uncategorised Income",)
            comb_inv_item_4.current(0)
            window_comb_inv_item_4 = canvas.create_window(55, 1300, anchor="nw", width=480, height=30,window=comb_inv_item_4)

            def inv_inc_acc_1():
                pro_frame_2.grid_forget()
                pro_frame_2_2 = Frame(tab3_4)
                pro_frame_2_2.grid(row=0,column=0,sticky='nsew')
                canvas=Canvas(pro_frame_2_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))
                
                vertibar=Scrollbar(pro_frame_2_2, orient=VERTICAL)
                vertibar.pack(side=RIGHT,fill=Y)
                vertibar.config(command=canvas.yview)

                canvas.config(width=1325,height=559)
                canvas.config(yscrollcommand=vertibar.set)
                canvas.pack(expand=True,side=LEFT,fill=BOTH)
                def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
                    
                    points = [x1+radius, y1,
                            x1+radius, y1,
                            x2-radius, y1,
                            x2-radius, y1,
                            x2, y1,
                            x2, y1+radius,
                            x2, y1+radius,
                            x2, y2-radius,
                            x2, y2-radius,
                            x2, y2,
                            x2-radius, y2,
                            x2-radius, y2,
                            x1+radius, y2,
                            x1+radius, y2,
                            x1, y2,
                            x1, y2-radius,
                            x1, y2-radius,
                            x1, y1+radius,
                            x1, y1+radius,
                            x1, y1]
                
                    return canvas.create_polygon(points, **kwargs, smooth=True)

                my_rectangle = round_rectangle(20, 50, 1300, 200, radius=20, fill="#1b3857")
                label_1 = Label(canvas,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(465, 85, anchor="nw", window=label_1)
                canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

                my_rectangle = round_rectangle(20, 250, 1300, 950, radius=20, fill="#1b3857")

                label_1 = Label(canvas,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(56, 300, anchor="nw", window=label_1)

                comb_inv_2_1 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_inv_2_1['values'] = ("Income",)
                comb_inv_2_1.current(0)
                window_comb_inv_2_1 = canvas.create_window(55, 330, anchor="nw", width=540, height=30,window=comb_inv_2_1)

                label_1 = Label(canvas,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(710, 300, anchor="nw", window=label_1)

                entry_inv_2_2=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_inv_2_2 = canvas.create_window(710, 330, anchor="nw", height=30,window=entry_inv_2_2)

                label_1 = Label(canvas,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(54, 400, anchor="nw", window=label_1)

                comb_inv_2_2 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_inv_2_2['values'] = ("Sales of Product Income",)
                comb_inv_2_2.current(0)
                window_comb_inv_2_2 = canvas.create_window(55, 430, anchor="nw", width=540, height=30,window=comb_inv_2_2)

                label_1 = Label(canvas,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(705, 400, anchor="nw", window=label_1)

                entry_inv_2_4=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_inv_2_4 = canvas.create_window(710, 430, anchor="nw", height=30,window=entry_inv_2_4)

                inv_text_2 = Text(canvas,width=67, height=14, background='black',foreground='white')
                inv_text_2.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                window_inv_text_2 = canvas.create_window(55, 500, anchor="nw",window=inv_text_2)

                chk_str_inv_2_1 = StringVar()
                chkbtn_inv_2_1 = Checkbutton(canvas, text = "Is sub-account", variable = chk_str_inv_2_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white")
                chkbtn_inv_2_1.select()
                window_chkbtn_inv_2_1 = canvas.create_window(709, 500, anchor="nw", window=chkbtn_inv_2_1)

                comb_inv_2_3 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_inv_2_3['values'] = ("Choose...",)
                comb_inv_2_3.current(0)
                window_comb_inv_2_3 = canvas.create_window(710, 530, anchor="nw", width=540, height=30,window=comb_inv_2_3)

                label_1 = Label(canvas,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(705, 600, anchor="nw", window=label_1)

                comb_inv_2_4 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_inv_2_4['values'] = ("Choose...",)
                comb_inv_2_4.current(0)
                window_comb_inv_2_4 = canvas.create_window(710, 630, anchor="nw", width=540, height=30,window=comb_inv_2_4)

                inv_bac_btn_2_1=Button(canvas,text='Back', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=inv_add_item)
                window_inv_bac_btn_2_1 = canvas.create_window(450, 800, anchor="nw", window=inv_bac_btn_2_1)

                inv_sub_btn_2_1=Button(canvas,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                window_inv_sub_btn_2_1 = canvas.create_window(685, 800, anchor="nw", window=inv_sub_btn_2_1)


            account_btn=Button(canvas,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=inv_inc_acc_1)
            window_account_btn = canvas.create_window(545, 1300, anchor="nw", window=account_btn)

            canvas.create_line(55, 1375, 1260, 1375, fill='gray',width=1)

            label_1 = Label(canvas,width=25,height=1,text="Purchasing information", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(26, 1400, anchor="nw", window=label_1)

            entry_inv_item_9=Entry(canvas,width=200,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_9 = canvas.create_window(55, 1430, anchor="nw", height=60,window=entry_inv_item_9)

            label_1 = Label(canvas,width=5,height=1,text="Cost", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(50, 1530, anchor="nw", window=label_1)
            
            entry_inv_item_10=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_10 = canvas.create_window(55, 1560, anchor="nw", height=30,window=entry_inv_item_10)

            chk_str_inv_item_1 = StringVar()
            chkbtn_inv_item_2 = Checkbutton(canvas, text = "Inclusive of purchase tax", variable = chk_str_inv_item_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white")
            chkbtn_inv_item_2.select()
            window_chkbtn_inv_item_2 = canvas.create_window(55, 1600, anchor="nw", window=chkbtn_inv_item_2)

            label_1 = Label(canvas,width=12,height=1,text="Purchase tax", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(700, 1530, anchor="nw", window=label_1)

            comb_inv_item_5 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            comb_inv_item_5['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
            comb_inv_item_5.current(0)
            window_comb_inv_item_5 = canvas.create_window(710, 1560, anchor="nw", width=540, height=30,window=comb_inv_item_5)

            label_1 = Label(canvas,width=15,height=1,text="Expense account", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(47, 1660, anchor="nw", window=label_1)

            comb_inv_item_6 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            comb_inv_item_6['values'] = ("Cost of sales",)
            comb_inv_item_6.current(0)
            window_comb_inv_item_6 = canvas.create_window(55, 1690, anchor="nw", width=480, height=30,window=comb_inv_item_6)

            def inv_exp_acc_1():
                pro_frame_2.grid_forget()
                pro_frame_2_3 = Frame(tab3_4)
                pro_frame_2_3.grid(row=0,column=0,sticky='nsew')
                canvas=Canvas(pro_frame_2_3, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))
                
                vertibar=Scrollbar(pro_frame_2_3, orient=VERTICAL)
                vertibar.pack(side=RIGHT,fill=Y)
                vertibar.config(command=canvas.yview)

                canvas.config(width=1325,height=559)
                canvas.config(yscrollcommand=vertibar.set)
                canvas.pack(expand=True,side=LEFT,fill=BOTH)
                def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
                    
                    points = [x1+radius, y1,
                            x1+radius, y1,
                            x2-radius, y1,
                            x2-radius, y1,
                            x2, y1,
                            x2, y1+radius,
                            x2, y1+radius,
                            x2, y2-radius,
                            x2, y2-radius,
                            x2, y2,
                            x2-radius, y2,
                            x2-radius, y2,
                            x1+radius, y2,
                            x1+radius, y2,
                            x1, y2,
                            x1, y2-radius,
                            x1, y2-radius,
                            x1, y1+radius,
                            x1, y1+radius,
                            x1, y1]
                
                    return canvas.create_polygon(points, **kwargs, smooth=True)

                my_rectangle = round_rectangle(20, 50, 1300, 200, radius=20, fill="#1b3857")
                label_1 = Label(canvas,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(465, 85, anchor="nw", window=label_1)
                canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

                my_rectangle = round_rectangle(20, 250, 1300, 950, radius=20, fill="#1b3857")

                label_1 = Label(canvas,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(56, 300, anchor="nw", window=label_1)

                comb_inv_3_1 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_inv_3_1['values'] = ("Cost of Goods Sold",)
                comb_inv_3_1.current(0)
                window_comb_inv_3_1 = canvas.create_window(55, 330, anchor="nw", width=540, height=30,window=comb_inv_3_1)

                label_1 = Label(canvas,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(710, 300, anchor="nw", window=label_1)

                entry_inv_3_2=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_inv_3_2 = canvas.create_window(710, 330, anchor="nw", height=30,window=entry_inv_3_2)

                label_1 = Label(canvas,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(54, 400, anchor="nw", window=label_1)

                comb_inv_3_2 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_inv_3_2['values'] = ("Suppliers and Materials-COS",)
                comb_inv_3_2.current(0)
                window_comb_inv_3_2 = canvas.create_window(55, 430, anchor="nw", width=540, height=30,window=comb_inv_3_2)

                label_1 = Label(canvas,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(705, 400, anchor="nw", window=label_1)

                entry_inv_3_4=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_inv_3_4 = canvas.create_window(710, 430, anchor="nw", height=30,window=entry_inv_3_4)

                inv_text_3 = Text(canvas,width=67, height=14, background='black',foreground='white')
                inv_text_3.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                window_inv_text_3 = canvas.create_window(55, 500, anchor="nw",window=inv_text_3)

                chk_str_inv_3_1 = StringVar()
                chkbtn_inv_3_1 = Checkbutton(canvas, text = "Is sub-account", variable = chk_str_inv_3_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white")
                chkbtn_inv_3_1.select()
                window_chkbtn_inv_3_1 = canvas.create_window(709, 500, anchor="nw", window=chkbtn_inv_3_1)

                comb_inv_3_3 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_inv_3_3['values'] = ("Choose...",)
                comb_inv_3_3.current(0)
                window_comb_inv_3_3 = canvas.create_window(710, 530, anchor="nw", width=540, height=30,window=comb_inv_3_3)

                label_1 = Label(canvas,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(705, 600, anchor="nw", window=label_1)

                comb_inv_3_4 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_inv_3_4['values'] = ("Choose...",)
                comb_inv_3_4.current(0)
                window_comb_inv_3_4 = canvas.create_window(710, 630, anchor="nw", width=540, height=30,window=comb_inv_3_4)

                inv_bac_btn_3_1=Button(canvas,text='Back', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=inv_add_item)
                window_inv_bac_btn_3_1 = canvas.create_window(450, 800, anchor="nw", window=inv_bac_btn_3_1)

                inv_sub_btn_3_1=Button(canvas,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                window_inv_sub_btn_3_1 = canvas.create_window(685, 800, anchor="nw", window=inv_sub_btn_3_1)


            expense_btn=Button(canvas,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=inv_exp_acc_1)
            window_expense_btn = canvas.create_window(545, 1690, anchor="nw", window=expense_btn)

            label_1 = Label(canvas,width=15,height=1,text="Reverse Charge %", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(52, 1760, anchor="nw", window=label_1)

            str_inv_item_2 = StringVar()
            entry_inv_item_11=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_inv_item_2)
            str_inv_item_2.set(' 0')
            window_entry_entry_inv_item_11 = canvas.create_window(55, 1790, anchor="nw", height=30,window=entry_inv_item_11)

            label_1 = Label(canvas,width=15,height=1,text="Preferred Supplier", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(707, 1760, anchor="nw", window=label_1)

            comb_inv_item_7 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            comb_inv_item_7['values'] = ("Select Supplier",)
            comb_inv_item_7.current(0)
            window_comb_inv_item_7 = canvas.create_window(710, 1790, anchor="nw", width=540, height=30,window=comb_inv_item_7)

            inv_sub_btn1=Button(canvas,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
            window_inv_sub_btn1 = canvas.create_window(575, 1900, anchor="nw", window=inv_sub_btn1)



        btn_1=Button(canvas,text='Add Item', width=20,height=1,foreground="white",background="blue",font='arial 12',command=inv_add_item)
        window_btn_1 = canvas.create_window(330, 470, anchor="nw", window=btn_1)

        my_rectangle = round_rectangle(700, 300, 1150, 550, radius=20, fill="#2f516f")

        label_1 = Label(canvas,width=11,height=1,text="Non-Inventory", font=('arial 20'),background="#2f516f",fg="white") 
        window_label_1 = canvas.create_window(835, 350, anchor="nw", window=label_1)

        label_1 = Label(canvas,width=46,height=2,text="A non-inventory is a type of product that is procured, sold, \nconsumed in production but we do not keep inventories for it.", font=('arial 12'),background="#2f516f",fg="white") 
        window_label_1 = canvas.create_window(720, 400, anchor="nw", window=label_1)

        def non_add_item():
            pro_frame_1.grid_forget()
            pro_frame_3 = Frame(tab3_4)
            pro_frame_3.grid(row=0,column=0,sticky='nsew')
            canvas=Canvas(pro_frame_3, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))
            
            vertibar=Scrollbar(pro_frame_3, orient=VERTICAL)
            vertibar.pack(side=RIGHT,fill=Y)
            vertibar.config(command=canvas.yview)

            canvas.config(width=1325,height=559)
            canvas.config(yscrollcommand=vertibar.set)
            canvas.pack(expand=True,side=LEFT,fill=BOTH)
            def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
                
                points = [x1+radius, y1,
                        x1+radius, y1,
                        x2-radius, y1,
                        x2-radius, y1,
                        x2, y1,
                        x2, y1+radius,
                        x2, y1+radius,
                        x2, y2-radius,
                        x2, y2-radius,
                        x2, y2,
                        x2-radius, y2,
                        x2-radius, y2,
                        x1+radius, y2,
                        x1+radius, y2,
                        x1, y2,
                        x1, y2-radius,
                        x1, y2-radius,
                        x1, y1+radius,
                        x1, y1+radius,
                        x1, y1]
            
                return canvas.create_polygon(points, **kwargs, smooth=True)

            my_rectangle = round_rectangle(20, 50, 1300, 200, radius=20, fill="#1b3857")
            label_1 = Label(canvas,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(470, 85, anchor="nw", window=label_1)
            canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

            my_rectangle = round_rectangle(20, 250, 1300, 2000, radius=20, fill="#1b3857")

            my_rectangle = round_rectangle(50, 300, 1270, 450, radius=20, fill="#2f516f")
            label_1 = Label(canvas,width=15,height=2,text="NON-INVENTORY", font=('arial 20'),background="#2f516f",fg="white") 
            window_label_1 = canvas.create_window(490, 350, anchor="nw", window=label_1)
            btn_non_item_2=Button(canvas,text='Choose Type', width=15,height=1,foreground="white",background="#2f516f",font='arial 20',  command=add_product)
            window_btn_non_item_2 = canvas.create_window(750, 350, anchor="nw", window=btn_non_item_2)

            label_1 = Label(canvas,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(51, 500, anchor="nw", window=label_1)

            entry_non_item_1=Entry(canvas,width=200,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_1 = canvas.create_window(55, 530, anchor="nw", height=30,window=entry_non_item_1)

            label_1 = Label(canvas,width=5,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(51, 600, anchor="nw", window=label_1)

            str_non_item_1 = StringVar()
            entry_non_iitem_2=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_non_item_1)
            str_non_item_1.set('  Eg: N41554')
            window_entry_non_iitem_2 = canvas.create_window(55, 630, anchor="nw", height=30,window=entry_non_iitem_2)

            label_1 = Label(canvas,width=9,height=1,text="HSN Code", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(710, 600, anchor="nw", window=label_1)

            entry_non_item_2=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_non_item_2 = canvas.create_window(710, 630, anchor="nw", height=30,window=entry_non_item_2)

            label_non_1 = Label(canvas,width=30,height=1,text="Not sure about HSN Code..? Click here", font=('arial 12'),background="#1b3857",fg="skyblue") 
            window_label_non_1 = canvas.create_window(710, 660, anchor="nw", window=label_non_1)

            label_1 = Label(canvas,width=5,height=1,text="Unit", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(48, 710, anchor="nw", window=label_1)

            comb_inv_item_1 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            comb_inv_item_1['values'] = ("Choose Unit Quantity Code(UQC)...","BAG Bags","BAL Bale BOU","BDL Bundles","BKL Buckles","BOX Box","BTL Bottles","CAN Cans","CTN Cartons","CCM Cubic centimeters","CBM Cubic meters","CMS Centimeters","DRM Drums","DOZ Dozens","GGK Great gross GYD","GRS GrossGMS","KME Kilometre","KGS Kilograms","KLR Kilo litre","MTS Metric ton","MLT Mili litre","MTR Meters","NOS Numbers","PAC Packs","PCS Pieces","PRS Pairs","QTL Quintal","ROL Rolls","SQY Square Yards","SET Sets","SQF Square feet","SQM Square meters","TBS Tablets","TUB Tubes","TGM Ten Gross","THD Thousands","TON Tonnes","UNT Units","UGS US Gallons","YDS Yards","OTH Others",)
            comb_inv_item_1.current(0)
            window_comb_inv_item_1 = canvas.create_window(55, 740, anchor="nw", width=540, height=30,window=comb_inv_item_1)

            label_1 = Label(canvas,width=9,height=1,text="Category", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(705, 710, anchor="nw", window=label_1)

            entry_non_item_3=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_inv_item_3 = canvas.create_window(710, 740, anchor="nw", height=30,window=entry_non_item_3)

            canvas.create_line(55, 815, 1260, 815, fill='gray',width=1)


            label_1 = Label(canvas,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(51, 840, anchor="nw", window=label_1)

            chk_str_non_item = StringVar()
            chkbtn_non_item = Checkbutton(canvas, text = "I sell this product/service to my customers.", variable = chk_str_non_item, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white")
            window_chkbtn_non_item = canvas.create_window(55, 870, anchor="nw", window=chkbtn_non_item)

            label_1 = Label(canvas,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(51, 940, anchor="nw", window=label_1)

            entry_non_item_7=Entry(canvas,width=200,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_non_item_7 = canvas.create_window(55, 970, anchor="nw", height=60,window=entry_non_item_7)

            label_1 = Label(canvas,width=15,height=1,text="Sales price/rate", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(45, 1070, anchor="nw", window=label_1)
            
            entry_non_item_8=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_non_item_8 = canvas.create_window(55, 1100, anchor="nw", height=30,window=entry_non_item_8)

            chk_str_non_item_1 = StringVar()
            chkbtn_non_item_1 = Checkbutton(canvas, text = "Inclusive of tax", variable = chk_str_non_item_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white")
            chkbtn_non_item_1.select()
            window_chkbtn_non_item_1 = canvas.create_window(55, 1135, anchor="nw", window=chkbtn_non_item_1)

            label_1 = Label(canvas,width=4,height=1,text="Tax", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(703, 1070, anchor="nw", window=label_1)

            comb_non_item_3 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            comb_non_item_3['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
            comb_non_item_3.current(0)
            window_comb_non_item_3 = canvas.create_window(710, 1100, anchor="nw", width=540, height=30,window=comb_non_item_3)

            label_1 = Label(canvas,width=15,height=1,text="Income account", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(41, 1180, anchor="nw", window=label_1)

            comb_non_item_4 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            comb_non_item_4['values'] = ("Billable Expense Income","Consulting Income","Product Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintanance","Sales Discount","Sales of Product Income","Services","Unapplied Cash Payment Income","Uncategorised Income",)
            comb_non_item_4.current(0)
            window_comb_non_item_4 = canvas.create_window(55, 1210, anchor="nw", width=480, height=30,window=comb_non_item_4)

            def non_inc_acc_1():
                pro_frame_3.grid_forget()
                pro_frame_3_1 = Frame(tab3_4)
                pro_frame_3_1.grid(row=0,column=0,sticky='nsew')
                canvas=Canvas(pro_frame_3_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))
                
                vertibar=Scrollbar(pro_frame_3_1, orient=VERTICAL)
                vertibar.pack(side=RIGHT,fill=Y)
                vertibar.config(command=canvas.yview)

                canvas.config(width=1325,height=559)
                canvas.config(yscrollcommand=vertibar.set)
                canvas.pack(expand=True,side=LEFT,fill=BOTH)
                def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
                    
                    points = [x1+radius, y1,
                            x1+radius, y1,
                            x2-radius, y1,
                            x2-radius, y1,
                            x2, y1,
                            x2, y1+radius,
                            x2, y1+radius,
                            x2, y2-radius,
                            x2, y2-radius,
                            x2, y2,
                            x2-radius, y2,
                            x2-radius, y2,
                            x1+radius, y2,
                            x1+radius, y2,
                            x1, y2,
                            x1, y2-radius,
                            x1, y2-radius,
                            x1, y1+radius,
                            x1, y1+radius,
                            x1, y1]
                
                    return canvas.create_polygon(points, **kwargs, smooth=True)

                my_rectangle = round_rectangle(20, 50, 1300, 200, radius=20, fill="#1b3857")
                label_1 = Label(canvas,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(465, 85, anchor="nw", window=label_1)
                canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

                my_rectangle = round_rectangle(20, 250, 1300, 950, radius=20, fill="#1b3857")

                label_1 = Label(canvas,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(56, 300, anchor="nw", window=label_1)

                comb_non_2_1 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_non_2_1['values'] = ("Income",)
                comb_non_2_1.current(0)
                window_comb_non_2_1 = canvas.create_window(55, 330, anchor="nw", width=540, height=30,window=comb_non_2_1)

                label_1 = Label(canvas,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(710, 300, anchor="nw", window=label_1)

                entry_non_2_2=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_non_2_2 = canvas.create_window(710, 330, anchor="nw", height=30,window=entry_non_2_2)

                label_1 = Label(canvas,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(54, 400, anchor="nw", window=label_1)

                comb_non_2_2 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_non_2_2['values'] = ("Discounts/Refunds Given",)
                comb_non_2_2.current(0)
                window_comb_non_2_2 = canvas.create_window(55, 430, anchor="nw", width=540, height=30,window=comb_non_2_2)

                label_1 = Label(canvas,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(705, 400, anchor="nw", window=label_1)

                entry_non_2_4=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_non_2_4 = canvas.create_window(710, 430, anchor="nw", height=30,window=entry_non_2_4)

                non_text_2 = Text(canvas,width=67, height=14, background='black',foreground='white')
                non_text_2.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                window_non_text_2 = canvas.create_window(55, 500, anchor="nw",window=non_text_2)

                chk_str_non_2_1 = StringVar()
                chkbtn_non_2_1 = Checkbutton(canvas, text = "Is sub-account", variable = chk_str_non_2_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white")
                chkbtn_non_2_1.select()
                window_chkbtn_non_2_1 = canvas.create_window(709, 500, anchor="nw", window=chkbtn_non_2_1)

                comb_non_2_3 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_non_2_3['values'] = ("Choose...",)
                comb_non_2_3.current(0)
                window_comb_non_2_3 = canvas.create_window(710, 530, anchor="nw", width=540, height=30,window=comb_non_2_3)

                label_1 = Label(canvas,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(705, 600, anchor="nw", window=label_1)

                comb_non_2_4 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_non_2_4['values'] = ("Choose...",)
                comb_non_2_4.current(0)
                window_comb_non_2_4 = canvas.create_window(710, 630, anchor="nw", width=540, height=30,window=comb_non_2_4)

                non_bac_btn_2_1=Button(canvas,text='Back', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=non_add_item)
                window_non_bac_btn_2_1 = canvas.create_window(450, 800, anchor="nw", window=non_bac_btn_2_1)

                non_sub_btn_2_1=Button(canvas,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                window_non_sub_btn_2_1 = canvas.create_window(685, 800, anchor="nw", window=non_sub_btn_2_1)

            account_non_btn=Button(canvas,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=non_inc_acc_1)
            window_account_non_btn = canvas.create_window(545, 1210, anchor="nw", window=account_non_btn)

            canvas.create_line(55, 1275, 1260, 1275, fill='gray',width=1)

            label_1 = Label(canvas,width=25,height=1,text="Purchasing information", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(26, 1300, anchor="nw", window=label_1)

            chk_str_non_pitem = StringVar()
            chkbtn_non_pitem = Checkbutton(canvas, text = "I Purchase this product/service from Supplier.", variable = chk_str_non_pitem, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white")
            window_chkbtn_non_pitem = canvas.create_window(55, 1330, anchor="nw", window=chkbtn_non_pitem)


            label_1 = Label(canvas,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(51, 1400, anchor="nw", window=label_1)

            entry_non_item_9=Entry(canvas,width=200,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_non_item_9 = canvas.create_window(55, 1430, anchor="nw", height=60,window=entry_non_item_9)

            label_1 = Label(canvas,width=5,height=1,text="Cost", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(50, 1530, anchor="nw", window=label_1)
            
            entry_non_item_10=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_non_item_10 = canvas.create_window(55, 1560, anchor="nw", height=30,window=entry_non_item_10)

            chk_str_non_item_2 = StringVar()
            chkbtn_non_item_2 = Checkbutton(canvas, text = "Inclusive of purchase tax", variable = chk_str_non_item_2, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white")
            chkbtn_non_item_2.select()
            window_chkbtn_non_item_2 = canvas.create_window(55, 1600, anchor="nw", window=chkbtn_non_item_2)

            label_1 = Label(canvas,width=12,height=1,text="Purchase tax", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(700, 1530, anchor="nw", window=label_1)

            comb_non_item_5 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            comb_non_item_5['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
            comb_non_item_5.current(0)
            window_comb_non_item_5 = canvas.create_window(710, 1560, anchor="nw", width=540, height=30,window=comb_non_item_5)

            label_1 = Label(canvas,width=15,height=1,text="Expense account", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(47, 1660, anchor="nw", window=label_1)

            comb_non_item_6 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            comb_non_item_6['values'] = ("Choose","Advertising/Promotional","Bank Charges","Business Licenses and Permitts","Charitable Contributions","Computer and Internet Expense","Continuing Education","Depreciation Expense","Dues and Subscriptions","House Keeping Charges","Insurance Expenses","Insurance Expenses-General Liability Insurance","Insurance Expenses-Health Insurance","Insurance Expenses-Life and Disability Insurance","Insurance Expenses-Professional Liability","Interest Expenses","Meals and Entertainment","Office Supplies","Postage and Delivery","Printing and Reproduction","Professional Fees","Purchases","Rent Expense","Repair and Maintanance","Small Tools and Equipments","Swachh Barath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities",)
            comb_non_item_6.current(0)
            window_comb_non_item_6 = canvas.create_window(55, 1690, anchor="nw", width=330, height=30,window=comb_non_item_6)

            def non_exp_acc_1():
                pro_frame_3.grid_forget()
                pro_frame_3_2 = Frame(tab3_4)
                pro_frame_3_2.grid(row=0,column=0,sticky='nsew')
                canvas=Canvas(pro_frame_3_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))
                
                vertibar=Scrollbar(pro_frame_3_2, orient=VERTICAL)
                vertibar.pack(side=RIGHT,fill=Y)
                vertibar.config(command=canvas.yview)

                canvas.config(width=1325,height=559)
                canvas.config(yscrollcommand=vertibar.set)
                canvas.pack(expand=True,side=LEFT,fill=BOTH)
                def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
                    
                    points = [x1+radius, y1,
                            x1+radius, y1,
                            x2-radius, y1,
                            x2-radius, y1,
                            x2, y1,
                            x2, y1+radius,
                            x2, y1+radius,
                            x2, y2-radius,
                            x2, y2-radius,
                            x2, y2,
                            x2-radius, y2,
                            x2-radius, y2,
                            x1+radius, y2,
                            x1+radius, y2,
                            x1, y2,
                            x1, y2-radius,
                            x1, y2-radius,
                            x1, y1+radius,
                            x1, y1+radius,
                            x1, y1]
                
                    return canvas.create_polygon(points, **kwargs, smooth=True)

                my_rectangle = round_rectangle(20, 50, 1300, 200, radius=20, fill="#1b3857")
                label_1 = Label(canvas,width=30,height=1,text="ACCOUNT CREATE", font=('arial 20'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(465, 85, anchor="nw", window=label_1)
                canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

                my_rectangle = round_rectangle(20, 250, 1300, 950, radius=20, fill="#1b3857")

                label_1 = Label(canvas,width=10,height=1,text="Account Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(56, 300, anchor="nw", window=label_1)

                comb_non_3_1 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_non_3_1['values'] = ("Expense",)
                comb_non_3_1.current(0)
                window_comb_non_3_1 = canvas.create_window(55, 330, anchor="nw", width=540, height=30,window=comb_non_3_1)

                label_1 = Label(canvas,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(710, 300, anchor="nw", window=label_1)

                entry_non_3_2=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_non_3_2 = canvas.create_window(710, 330, anchor="nw", height=30,window=entry_non_3_2)

                label_1 = Label(canvas,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(54, 400, anchor="nw", window=label_1)

                comb_non_3_2 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_non_3_2['values'] = ("Advertising/Promotional",)
                comb_non_3_2.current(0)
                window_comb_non_3_2 = canvas.create_window(55, 430, anchor="nw", width=540, height=30,window=comb_non_3_2)

                label_1 = Label(canvas,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(705, 400, anchor="nw", window=label_1)

                entry_non_3_4=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_non_3_4 = canvas.create_window(710, 430, anchor="nw", height=30,window=entry_non_3_4)

                non_text_3 = Text(canvas,width=67, height=14, background='black',foreground='white')
                non_text_3.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                window_non_text_3 = canvas.create_window(55, 500, anchor="nw",window=non_text_3)

                chk_str_non_3_1 = StringVar()
                chkbtn_non_3_1 = Checkbutton(canvas, text = "Is sub-account", variable = chk_str_non_3_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white")
                chkbtn_non_3_1.select()
                window_chkbtn_non_3_1 = canvas.create_window(709, 500, anchor="nw", window=chkbtn_non_3_1)

                comb_non_3_3 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_non_3_3['values'] = ("Choose...",)
                comb_non_3_3.current(0)
                window_comb_non_3_3 = canvas.create_window(710, 530, anchor="nw", width=540, height=30,window=comb_non_3_3)

                label_1 = Label(canvas,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(705, 600, anchor="nw", window=label_1)

                comb_non_3_4 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_non_3_4['values'] = ("Choose...",)
                comb_non_3_4.current(0)
                window_comb_non_3_4 = canvas.create_window(710, 630, anchor="nw", width=540, height=30,window=comb_non_3_4)

                non_bac_btn_3_1=Button(canvas,text='Back', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=non_add_item)
                window_non_bac_btn_3_1 = canvas.create_window(450, 800, anchor="nw", window=non_bac_btn_3_1)

                non_sub_btn_3_1=Button(canvas,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                window_non_sub_btn_3_1 = canvas.create_window(685, 800, anchor="nw", window=non_sub_btn_3_1)

            expense_non_btn=Button(canvas,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=non_exp_acc_1)
            window_expense_non_btn = canvas.create_window(395, 1690, anchor="nw", window=expense_non_btn)

            label_1 = Label(canvas,width=15,height=1,text="Reverse Charge %", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(520, 1660, anchor="nw", window=label_1)

            str_non_item_2 = StringVar()
            entry_non_item_11=Entry(canvas,width=50,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_non_item_2)
            str_non_item_2.set(' 0')
            window_entry_non_item_11 = canvas.create_window(520, 1690, anchor="nw", height=30,window=entry_non_item_11)

            label_1 = Label(canvas,width=15,height=1,text="Preferred Supplier", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(897, 1660, anchor="nw", window=label_1)

            comb_non_item_7 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            comb_non_item_7['values'] = ("Select Supplier",)
            comb_non_item_7.current(0)
            window_comb_non_item_7 = canvas.create_window(900, 1690, anchor="nw", width=345, height=30,window=comb_non_item_7)

            non_sub_btn1=Button(canvas,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
            window_non_sub_btn1 = canvas.create_window(575, 1800, anchor="nw", window=non_sub_btn1)

        btn_2=Button(canvas,text='Add Item', width=20,height=1,foreground="white",background="blue",font='arial 12',command=non_add_item)
        window_btn_2 = canvas.create_window(830, 470, anchor="nw", window=btn_2)

        my_rectangle = round_rectangle(200, 600, 650, 850, radius=20, fill="#2f516f")

        label_1 = Label(canvas,width=10,height=1,text="Services", font=('arial 20'),background="#2f516f",fg="white") 
        window_label_1 = canvas.create_window(340, 650, anchor="nw", window=label_1)

        label_1 = Label(canvas,width=45,height=2,text="A service is a transaction in which no physical goods are \ntransferred from the seller to the buyer.", font=('arial 12'),background="#2f516f",fg="white") 
        window_label_1 = canvas.create_window(220, 700, anchor="nw", window=label_1)

        def ser_add_item():
            pro_frame_1.grid_forget()
            pro_frame_4 = Frame(tab3_4)
            pro_frame_4.grid(row=0,column=0,sticky='nsew')
            canvas=Canvas(pro_frame_4, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))
            
            vertibar=Scrollbar(pro_frame_4, orient=VERTICAL)
            vertibar.pack(side=RIGHT,fill=Y)
            vertibar.config(command=canvas.yview)

            canvas.config(width=1325,height=559)
            canvas.config(yscrollcommand=vertibar.set)
            canvas.pack(expand=True,side=LEFT,fill=BOTH)
            def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
                
                points = [x1+radius, y1,
                        x1+radius, y1,
                        x2-radius, y1,
                        x2-radius, y1,
                        x2, y1,
                        x2, y1+radius,
                        x2, y1+radius,
                        x2, y2-radius,
                        x2, y2-radius,
                        x2, y2,
                        x2-radius, y2,
                        x2-radius, y2,
                        x1+radius, y2,
                        x1+radius, y2,
                        x1, y2,
                        x1, y2-radius,
                        x1, y2-radius,
                        x1, y1+radius,
                        x1, y1+radius,
                        x1, y1]
            
                return canvas.create_polygon(points, **kwargs, smooth=True)

            my_rectangle = round_rectangle(20, 50, 1300, 200, radius=20, fill="#1b3857")
            label_1 = Label(canvas,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(470, 85, anchor="nw", window=label_1)
            canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

            my_rectangle = round_rectangle(20, 250, 1300, 2000, radius=20, fill="#1b3857")

            my_rectangle = round_rectangle(50, 300, 1270, 450, radius=20, fill="#2f516f")
            label_1 = Label(canvas,width=15,height=2,text="SERVICES", font=('arial 20'),background="#2f516f",fg="white") 
            window_label_1 = canvas.create_window(500, 350, anchor="nw", window=label_1)
            btn_ser_item_2=Button(canvas,text='Choose Type', width=15,height=1,foreground="white",background="#2f516f",font='arial 20',  command=add_product)
            window_btn_ser_item_2 = canvas.create_window(750, 350, anchor="nw", window=btn_ser_item_2)

            label_1 = Label(canvas,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(51, 500, anchor="nw", window=label_1)

            entry_ser_item_1=Entry(canvas,width=200,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ser_item_1 = canvas.create_window(55, 530, anchor="nw", height=30,window=entry_ser_item_1)

            label_1 = Label(canvas,width=5,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(51, 600, anchor="nw", window=label_1)

            str_ser_item_1 = StringVar()
            entry_ser_iitem_2=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_ser_item_1)
            str_ser_item_1.set('  Eg: N41554')
            window_entry_ser_iitem_2 = canvas.create_window(55, 630, anchor="nw", height=30,window=entry_ser_iitem_2)

            label_1 = Label(canvas,width=9,height=1,text="SAC Code", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(710, 600, anchor="nw", window=label_1)

            str_ser_iitem_1 = StringVar()
            entry_ser_item_2=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_ser_iitem_1)
            str_ser_iitem_1.set(' Eg: 998841-Coke and refined petroleum product manufacturing services')
            window_entry_ser_item_2 = canvas.create_window(710, 630, anchor="nw", height=30,window=entry_ser_item_2)


            label_1 = Label(canvas,width=5,height=1,text="Unit", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(48, 710, anchor="nw", window=label_1)

            comb_ser_item_1 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            comb_ser_item_1['values'] = ("Choose Unit Quantity Code(UQC)...","BAG-BAGS","BAL-BALE","BDL-BUNDLES","BKL-BUCKLES","BOX-BOX","BOU-BILLIONS OF UNITS","BTL-BOTTLES","BUN-BUNCHES","CAN-CANS","CBM-CUBIC METER","CMS-CENTIMETER","CCM-CUBIC CENTIMETER","CTN-CARTONS","DOZ-DOZEN","DRM-DRUM","GGR-GREAT GROSS","GMS-GRAMS","GRS-GROSS","GYD-GRODD YARDS","KGS-KILOGRAMS","KLR-KILOLITER","KME-KILOMETRE","MTS-METRIC TON","MLT-MILLILITRE","MTR-METERS","NOS-NUMBER","PAC-PACKS","PCS-PIECES","PRS-PAIRS","QTL-QUINTAL","ROL-ROLLS","SQF-SQUARE FEET","SET-SETS","SQM-SQUARE METERS","SQY-SQUARE YARDS","TBS-TABLETS","TGM-TEN GROSS","THD-THOUSAND","TON-TONNES","TUB-TUBES","UGS-US GALLONS","UNT-UNITS","YDS-YARDS","OTH-OTHERS",)
            comb_ser_item_1.current(0)
            window_comb_ser_item_1 = canvas.create_window(55, 740, anchor="nw", width=540, height=30,window=comb_ser_item_1)

            label_1 = Label(canvas,width=9,height=1,text="Category", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(705, 710, anchor="nw", window=label_1)

            entry_ser_item_3=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ser_item_3 = canvas.create_window(710, 740, anchor="nw", height=30,window=entry_ser_item_3)

            canvas.create_line(55, 815, 1260, 815, fill='gray',width=1)


            label_1 = Label(canvas,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(51, 840, anchor="nw", window=label_1)

            chk_str_ser_item = StringVar()
            chkbtn_ser_item = Checkbutton(canvas, text = "I sell this product/service to my customers.", variable = chk_str_ser_item, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white")
            window_chkbtn_ser_item = canvas.create_window(55, 870, anchor="nw", window=chkbtn_ser_item)

            label_1 = Label(canvas,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(51, 940, anchor="nw", window=label_1)

            entry_ser_item_7=Entry(canvas,width=200,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ser_item_7 = canvas.create_window(55, 970, anchor="nw", height=60,window=entry_ser_item_7)

            label_1 = Label(canvas,width=15,height=1,text="Sales price/rate", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(45, 1070, anchor="nw", window=label_1)
            
            entry_non_item_8=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_non_item_8 = canvas.create_window(55, 1100, anchor="nw", height=30,window=entry_non_item_8)

            chk_str_ser_item_1 = StringVar()
            chkbtn_ser_item_1 = Checkbutton(canvas, text = "Inclusive of tax", variable = chk_str_ser_item_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white")
            chkbtn_ser_item_1.select()
            window_chkbtn_ser_item_1 = canvas.create_window(55, 1135, anchor="nw", window=chkbtn_ser_item_1)

            label_1 = Label(canvas,width=4,height=1,text="Tax", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(703, 1070, anchor="nw", window=label_1)

            comb_ser_item_3 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            comb_ser_item_3['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
            comb_ser_item_3.current(0)
            window_comb_ser_item_3 = canvas.create_window(710, 1100, anchor="nw", width=540, height=30,window=comb_ser_item_3)

            label_1 = Label(canvas,width=15,height=1,text="Income account", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(41, 1180, anchor="nw", window=label_1)

            
            comb_ser_item_6 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            comb_ser_item_6['values'] = ("Choose...","Billable Expense income","Product Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintanance","Sales Discounts","Sales of Product Income","Cost of sales","Equipment Rental for Jobs","Uncategorised Income","Advertising/Promotional","Bank Charges","Business Licenses and Permitts","Charitable Contributions","Computer and Internet Expense","Depreciation Expense","Dues and Subscriptions","Housekeeping Charges","Insurance Expenses","Insurance Expenses-General Liability Insurance","Insurance Expenses-Health Insurance","Insurance Expenses-Life and Disability Insurance","Insurance Expenses-Professional Liability","Internet Expenses","Meals and Enetrtainments","Office Suppliers","Postage and Delivery","Printing and Reprooduction","Professional Fees","Purchases","Rent Expense","Repair and Maintananace","Small Tools and Equipments","Swachh Barath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities","Finance charge Income","Insurance Proceeds Received","Interest Income","Proceeds From Sale os Assets","Shipping and delivery Income","Ask My Accountant","CGST Write-off","GST Write-off","IGST Write-off","Miscellaneous Expense","Political Contributions","Reconcilation Discrepancies","SGST Write-off","Vehicles","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi kalyan Cess","Input Krishi kalyan Cess RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Krishi Kalyan Cess Payable","Input VAT 5%","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output SGST Tax RCM","Output Service Tax","Output Service Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","SGST Payable","Service Tax Payable","Srvice Tax Suspense","Swachh Barath Cess Payable","TDS Payable","VAT Payable","VAT Suspense","Deferred CGST","Deferred GST Input credit","Deferred IGST","Deferred SGST","Deferred Service Tax Input Credit","Deferred VAT Input Credit","GST Refund","Inventory Asset","Krishi Kalyan Cess Refund","Prepaid Insurance","Sevice Tax Refund","TDS Receivable","Uncategorised Asset","Undeposited Fund","Billable Expense Income","Consulting Income","Product Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and maintanance","Sales Discount","Sales of Product Income","Uncategorised Income","accumulated Depreciation","Building and Improvements","Furniture and Equipments","Land","Leasehold Improvements","Vehicles","Retained Earnings","Cost of Sales","Equipment Rental for Jobs","Freight and Shipping Costs","Merchant Account Fees","Purchases-Hardware for Resales","Purchases-Software for Resales","Subcontracted Services","Tools and Craft Suppliers",)
            comb_ser_item_6.current(0)
            window_comb_ser_item_6 = canvas.create_window(55, 1210, anchor="nw", width=330, height=30,window=comb_ser_item_6)

            income_ser_btn=Button(canvas,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12')
            window_income_ser_btn = canvas.create_window(395, 1210, anchor="nw", window=income_ser_btn)

            label_1 = Label(canvas,width=10,height=1,text="Abatement %", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(522 , 1180, anchor="nw", window=label_1)

            str_ser_iitem_2 = StringVar()
            entry_ser_iitem_11=Entry(canvas,width=50,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_ser_iitem_2)
            str_ser_iitem_2.set(' 0')
            window_entry_ser_iitem_11 = canvas.create_window(520, 1210, anchor="nw", height=30,window=entry_ser_iitem_11)

            label_1 = Label(canvas,width=15,height=1,text="Service Type", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(877, 1180, anchor="nw", window=label_1)

            comb_ser_iitem_7 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            comb_ser_iitem_7['values'] = ("Choose...","Stock Broking","Genral Insurance","Courier","Advertsing Agency","Consulting Engineer","Custom House Agent","Steamer Agent","Clearing and Forwarding","Man power Recruiting","Air Travel Agent","Tour operator","Rent a Cab","Architect","Interior Director","Management Consultment","Chartered Accountant","Cost Accountant","Company Scretary","Real Estate Agent","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",)
            comb_ser_iitem_7.current(0)
            window_comb_ser_iitem_7 = canvas.create_window(900, 1210, anchor="nw", width=345, height=30,window=comb_ser_iitem_7)

            canvas.create_line(55, 1275, 1260, 1275, fill='gray',width=1)

            label_1 = Label(canvas,width=25,height=1,text="Purchasing information", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(26, 1300, anchor="nw", window=label_1)

            chk_str_ser_pitem = StringVar()
            chkbtn_ser_pitem = Checkbutton(canvas, text = "I Purchase this product/service from Supplier.", variable = chk_str_ser_pitem, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white")
            window_chkbtn_ser_pitem = canvas.create_window(55, 1330, anchor="nw", window=chkbtn_ser_pitem)


            label_1 = Label(canvas,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(51, 1400, anchor="nw", window=label_1)

            entry_ser_item_9=Entry(canvas,width=200,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ser_item_9 = canvas.create_window(55, 1430, anchor="nw", height=60,window=entry_ser_item_9)

            label_1 = Label(canvas,width=5,height=1,text="Cost", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(50, 1530, anchor="nw", window=label_1)
            
            entry_ser_item_10=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ser_item_10 = canvas.create_window(55, 1560, anchor="nw", height=30,window=entry_ser_item_10)

            chk_str_sser_item_2 = StringVar()
            chkbtn_sser_item_2 = Checkbutton(canvas, text = "Inclusive of Tax", variable = chk_str_sser_item_2, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white")
            chkbtn_sser_item_2.select()
            window_chkbtn_sser_item_2 = canvas.create_window(55, 1600, anchor="nw", window=chkbtn_sser_item_2)

            label_1 = Label(canvas,width=12,height=1,text="Purchase tax", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(700, 1530, anchor="nw", window=label_1)

            comb_ser_item_5 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            comb_ser_item_5['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
            comb_ser_item_5.current(0)
            window_comb_ser_item_5 = canvas.create_window(710, 1560, anchor="nw", width=540, height=30,window=comb_ser_item_5)

            label_1 = Label(canvas,width=15,height=1,text="Expense account", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(47, 1660, anchor="nw", window=label_1)

            comb_ser_item_6 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            comb_ser_item_6['values'] = ("Choose","Advertising/Promotional","Bank Charges","Business Licenses and Permitts","Charitable Contributions","Computer and Internet Expense","Continuing Education","Depreciation Expense","Dues and Subscriptions","House Keeping Charges","Insurance Expenses","Insurance Expenses-General Liability Insurance","Insurance Expenses-Health Insurance","Insurance Expenses-Life and Disability Insurance","Insurance Expenses-Professional Liability","Interest Expenses","Meals and Entertainment","Office Supplies","Postage and Delivery","Printing and Reproduction","Professional Fees","Purchases","Rent Expense","Repair and Maintanance","Small Tools and Equipments","Swachh Barath Cess Expense","Taxes-Property","Telephone Expense","Travel Expense","Uncategorised Expense","Utilities",)
            comb_ser_item_6.current(0)
            window_comb_ser_item_6 = canvas.create_window(55, 1690, anchor="nw", width=330, height=30,window=comb_ser_item_6)

            expense_ser_btn=Button(canvas,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12')
            window_expense_ser_btn = canvas.create_window(395, 1690, anchor="nw", window=expense_ser_btn)

            label_1 = Label(canvas,width=15,height=1,text="Reverse Charge %", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(520, 1660, anchor="nw", window=label_1)

            str_sser_iitem_2 = StringVar()
            entry_sser_item_11=Entry(canvas,width=50,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_sser_iitem_2)
            str_sser_iitem_2.set(' 0')
            window_entry_sser_item_11 = canvas.create_window(520, 1690, anchor="nw", height=30,window=entry_sser_item_11)

            label_1 = Label(canvas,width=15,height=1,text="Preferred Supplier", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(897, 1660, anchor="nw", window=label_1)

            comb_ser_item_7 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            comb_ser_item_7['values'] = ("Select Supplier",)
            comb_ser_item_7.current(0)
            window_comb_ser_item_7 = canvas.create_window(900, 1690, anchor="nw", width=345, height=30,window=comb_ser_item_7)

            ser_sub_btn1=Button(canvas,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
            window_ser_sub_btn1 = canvas.create_window(575, 1800, anchor="nw", window=ser_sub_btn1)

        btn_3=Button(canvas,text='Add Item', width=20,height=1,foreground="white",background="blue",font='arial 12',command=ser_add_item)
        window_btn_3 = canvas.create_window(330, 770, anchor="nw", window=btn_3)

        my_rectangle = round_rectangle(700, 600, 1150, 850, radius=20, fill="#2f516f")

        label_1 = Label(canvas,width=10,height=1,text="Bundle", font=('arial 20'),background="#2f516f",fg="white") 
        window_label_1 = canvas.create_window(845, 650, anchor="nw", window=label_1)

        label_1 = Label(canvas,width=46,height=2,text="A bundle is a group of software programs or hardware \ndevices that are grouped together and sold as one.", font=('arial 12'),background="#2f516f",fg="white") 
        window_label_1 = canvas.create_window(720, 700, anchor="nw", window=label_1)

        def bun_add_item():
            pro_frame_1.grid_forget()
            pro_frame_5 = Frame(tab3_4)
            pro_frame_5.grid(row=0,column=0,sticky='nsew')
            canvas=Canvas(pro_frame_5, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))
            
            vertibar=Scrollbar(pro_frame_5, orient=VERTICAL)
            vertibar.pack(side=RIGHT,fill=Y)
            vertibar.config(command=canvas.yview)

            canvas.config(width=1325,height=559)
            canvas.config(yscrollcommand=vertibar.set)
            canvas.pack(expand=True,side=LEFT,fill=BOTH)
            def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
                
                points = [x1+radius, y1,
                        x1+radius, y1,
                        x2-radius, y1,
                        x2-radius, y1,
                        x2, y1,
                        x2, y1+radius,
                        x2, y1+radius,
                        x2, y2-radius,
                        x2, y2-radius,
                        x2, y2,
                        x2-radius, y2,
                        x2-radius, y2,
                        x1+radius, y2,
                        x1+radius, y2,
                        x1, y2,
                        x1, y2-radius,
                        x1, y2-radius,
                        x1, y1+radius,
                        x1, y1+radius,
                        x1, y1]
            
                return canvas.create_polygon(points, **kwargs, smooth=True)

            my_rectangle = round_rectangle(20, 50, 1300, 200, radius=20, fill="#1b3857")
            label_1 = Label(canvas,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(470, 85, anchor="nw", window=label_1)
            canvas.create_line(60, 150, 1260, 150, fill='gray',width=1)

            my_rectangle = round_rectangle(20, 250, 1300, 1400, radius=20, fill="#1b3857")

            my_rectangle = round_rectangle(50, 300, 1270, 450, radius=20, fill="#2f516f")
            label_1 = Label(canvas,width=15,height=2,text="BUNDLE", font=('arial 20'),background="#2f516f",fg="white") 
            window_label_1 = canvas.create_window(500, 350, anchor="nw", window=label_1)
            btn_bun_item_2=Button(canvas,text='Choose Type', width=15,height=1,foreground="white",background="#2f516f",font='arial 20',  command=add_product)
            window_btn_bun_item_2 = canvas.create_window(750, 350, anchor="nw", window=btn_bun_item_2)

            label_1 = Label(canvas,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(51, 500, anchor="nw", window=label_1)

            entry_bun_item_1=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_bun_item_1 = canvas.create_window(55, 530, anchor="nw", height=30,window=entry_bun_item_1)

            label_1 = Label(canvas,width=5,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(704, 500, anchor="nw", window=label_1)

            str_bun_item_1 = StringVar()
            entry_bun_iitem_2=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_item_1)
            str_bun_item_1.set('  Eg: N41554')
            window_entry_bun_iitem_2 = canvas.create_window(712, 530, anchor="nw", height=30,window=entry_bun_iitem_2)

            label_1 = Label(canvas,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(51, 600, anchor="nw", window=label_1)

            entry_bun_item_7=Entry(canvas,width=200,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_bun_item_7 = canvas.create_window(55, 630, anchor="nw", height=60,window=entry_bun_item_7)

            label_1 = Label(canvas,width=30,height=1,text="Products/services included in the bundle", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(60, 760, anchor="nw", window=label_1)

            canvas.create_line(60, 800, 1250, 800, fill='gray',width=1)
            canvas.create_line(60, 850, 1250, 850, fill='gray',width=1)
            canvas.create_line(60, 925, 1250, 925, fill='gray',width=1)
            canvas.create_line(60, 800, 60, 925, fill='gray',width=1)
            canvas.create_line(275, 800, 275, 925, fill='gray',width=1)
            canvas.create_line(500, 800, 500, 925, fill='gray',width=1)
            canvas.create_line(735, 800, 735, 925, fill='gray',width=1)
            canvas.create_line(850, 800, 850, 925, fill='gray',width=1)
            canvas.create_line(980, 800, 980, 925, fill='gray',width=1)
            canvas.create_line(1110, 800, 1110, 925, fill='gray',width=1)
            canvas.create_line(1250, 800, 1250, 925, fill='gray',width=1)
            canvas.create_line(60, 1000, 1250, 1000, fill='gray',width=1)
            canvas.create_line(60, 1075, 1250, 1075, fill='gray',width=1)
            canvas.create_line(60, 1150, 1250, 1150, fill='gray',width=1)
            canvas.create_line(60, 925, 60, 1150, fill='gray',width=1)
            canvas.create_line(275, 925, 275, 1150, fill='gray',width=1)
            canvas.create_line(500, 925, 500, 1150, fill='gray',width=1)
            canvas.create_line(735, 925, 735, 1150, fill='gray',width=1)
            canvas.create_line(850, 925, 850, 1150, fill='gray',width=1)
            canvas.create_line(980, 925, 980, 1150, fill='gray',width=1)
            canvas.create_line(1110, 925, 1110, 1150, fill='gray',width=1)
            canvas.create_line(1250, 925, 1250, 1150, fill='gray',width=1)

            label_3 = Label(canvas,width=15,height=1,text="PRODUCT/SERVICE", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_3 = canvas.create_window(105, 815, anchor="nw", window=label_3)

            label_4 = Label(canvas,width=10,height=1,text="HSN", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_4 = canvas.create_window(340, 815, anchor="nw", window=label_4)

            label_4 = Label(canvas,width=11,height=1,text="DESCRIPTION", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_4 = canvas.create_window(570, 815, anchor="nw", window=label_4)

            label_4 = Label(canvas,width=5,height=1,text="QTY", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_4 = canvas.create_window(770, 815, anchor="nw", window=label_4)

            label_4 = Label(canvas,width=8,height=1,text="PRICE", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_4 = canvas.create_window(880, 815, anchor="nw", window=label_4)

            label_4 = Label(canvas,width=8,height=1,text="TOTAL", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_4 = canvas.create_window(1005, 815, anchor="nw", window=label_4)

            label_4 = Label(canvas,width=8,height=1,text="TAX", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_4 = canvas.create_window(1150, 815, anchor="nw", window=label_4)

            bun_comb_1 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            bun_comb_1['values'] = ("Choose",)
            bun_comb_1.current(0)
            window_bun_comb_1 = canvas.create_window(80, 870, anchor="nw", width=180, height=30,window=bun_comb_1)

            bun_comb_2 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            bun_comb_2['values'] = ("Choose",)
            bun_comb_2.current(0)
            window_bun_comb_2 = canvas.create_window(80, 945, anchor="nw", width=180, height=30,window=bun_comb_2)

            bun_comb_3 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            bun_comb_3['values'] = ("Choose",)
            bun_comb_3.current(0)
            window_bun_comb_3 = canvas.create_window(80, 1020, anchor="nw", width=180, height=30,window=bun_comb_3)

            bun_comb_4 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
            bun_comb_4['values'] = ("Choose",)
            bun_comb_4.current(0)
            window_bun_comb_4 = canvas.create_window(80, 1095, anchor="nw", width=180, height=30,window=bun_comb_4)

            bun_entry_1=Entry(canvas,width=30,justify=LEFT,background='#2f516f',foreground="white")
            window_bun_entry_1 = canvas.create_window(295, 870, anchor="nw", height=30, window=bun_entry_1)

            bun_entry_2=Entry(canvas,width=30,justify=LEFT,background='#2f516f',foreground="white")
            window_bun_entry_2 = canvas.create_window(295, 945, anchor="nw", height=30, window=bun_entry_2)

            bun_entry_3=Entry(canvas,width=30,justify=LEFT,background='#2f516f',foreground="white")
            window_bun_entry_3 = canvas.create_window(295, 1020, anchor="nw", height=30, window=bun_entry_3)

            bun_entry_4=Entry(canvas,width=30,justify=LEFT,background='#2f516f',foreground="white")
            window_bun_entry_4 = canvas.create_window(295, 1095, anchor="nw", height=30, window=bun_entry_4)

            bun_entry_5=Entry(canvas,width=32,justify=LEFT,background='#2f516f',foreground="white")
            window_bun_entry_5 = canvas.create_window(520, 870, anchor="nw", height=30, window=bun_entry_5)

            bun_entry_6=Entry(canvas,width=32,justify=LEFT,background='#2f516f',foreground="white")
            window_bun_entry_6 = canvas.create_window(520, 945, anchor="nw", height=30, window=bun_entry_6)

            bun_entry_7=Entry(canvas,width=32,justify=LEFT,background='#2f516f',foreground="white")
            window_bun_entry_7 = canvas.create_window(520, 1020, anchor="nw", height=30, window=bun_entry_7)

            bun_entry_8=Entry(canvas,width=32,justify=LEFT,background='#2f516f',foreground="white")
            window_bun_entry_8 = canvas.create_window(520, 1095, anchor="nw", height=30, window=bun_entry_8)

            str_bun_entry_9 = StringVar()
            bun_entry_9=Entry(canvas,width=15,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_9)
            str_bun_entry_9.set(' 0')
            window_bun_entry_9 = canvas.create_window(745, 870, anchor="nw", height=30, window=bun_entry_9)

            str_bun_entry_10 = StringVar()
            bun_entry_10=Entry(canvas,width=15,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_10)
            str_bun_entry_10.set(' 0')
            window_bun_entry_10 = canvas.create_window(745, 945, anchor="nw", height=30, window=bun_entry_10)

            str_bun_entry_11 = StringVar()
            bun_entry_11=Entry(canvas,width=15,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_11)
            str_bun_entry_11.set(' 0')
            window_bun_entry_11 = canvas.create_window(745, 1020, anchor="nw", height=30, window=bun_entry_11)

            str_bun_entry_12 = StringVar()
            bun_entry_12=Entry(canvas,width=15,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_12)
            str_bun_entry_12.set(' 0')
            window_bun_entry_12 = canvas.create_window(745, 1095, anchor="nw", height=30, window=bun_entry_12)

            str_bun_entry_13 = StringVar()
            bun_entry_13=Entry(canvas,width=18,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_13)
            str_bun_entry_13.set(' 0.0')
            window_bun_entry_13 = canvas.create_window(860, 870, anchor="nw", height=30, window=bun_entry_13)

            str_bun_entry_14 = StringVar()
            bun_entry_14=Entry(canvas,width=18,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_14)
            str_bun_entry_14.set(' 0.0')
            window_bun_entry_14 = canvas.create_window(860, 945, anchor="nw", height=30, window=bun_entry_14)

            str_bun_entry_15 = StringVar()
            bun_entry_15=Entry(canvas,width=18,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_15)
            str_bun_entry_15.set(' 0.0')
            window_bun_entry_15 = canvas.create_window(860, 1020, anchor="nw", height=30, window=bun_entry_15)

            str_bun_entry_16 = StringVar()
            bun_entry_16=Entry(canvas,width=18,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_16)
            str_bun_entry_16.set(' 0.0')
            window_bun_entry_16 = canvas.create_window(860, 1095, anchor="nw", height=30, window=bun_entry_16)

            str_bun_entry_17 = StringVar()
            bun_entry_17=Entry(canvas,width=18,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_17)
            str_bun_entry_17.set(' 0.0')
            window_bun_entry_17 = canvas.create_window(990, 870, anchor="nw", height=30, window=bun_entry_17)

            str_bun_entry_18 = StringVar()
            bun_entry_18=Entry(canvas,width=18,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_18)
            str_bun_entry_18.set(' 0.0')
            window_bun_entry_18 = canvas.create_window(990, 945, anchor="nw", height=30, window=bun_entry_18)

            str_bun_entry_19 = StringVar()
            bun_entry_19=Entry(canvas,width=18,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_19)
            str_bun_entry_19.set(' 0.0')
            window_bun_entry_19 = canvas.create_window(990, 1020, anchor="nw", height=30, window=bun_entry_19)

            str_bun_entry_20 = StringVar()
            bun_entry_20=Entry(canvas,width=18,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_20)
            str_bun_entry_20.set(' 0.0')
            window_bun_entry_20 = canvas.create_window(990, 1095, anchor="nw", height=30, window=bun_entry_20)

            str_bun_entry_21 = StringVar()
            bun_entry_21=Entry(canvas,width=19,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_21)
            str_bun_entry_21.set(' 0.0')
            window_bun_entry_21 = canvas.create_window(1120, 870, anchor="nw", height=30, window=bun_entry_21)

            str_bun_entry_22 = StringVar()
            bun_entry_22=Entry(canvas,width=19,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_22)
            str_bun_entry_22.set(' 0.0')
            window_bun_entry_22 = canvas.create_window(1120, 945, anchor="nw", height=30, window=bun_entry_22)

            str_bun_entry_23 = StringVar()
            bun_entry_23=Entry(canvas,width=19,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_23)
            str_bun_entry_23.set(' 0.0')
            window_bun_entry_23 = canvas.create_window(1120, 1020, anchor="nw", height=30, window=bun_entry_23)

            str_bun_entry_24 = StringVar()
            bun_entry_24=Entry(canvas,width=19,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_bun_entry_24)
            str_bun_entry_24.set(' 0.0')
            window_bun_entry_24 = canvas.create_window(1120, 1095, anchor="nw", height=30, window=bun_entry_24)


            bun_sub_btn1=Button(canvas,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
            window_bun_sub_btn1 = canvas.create_window(575, 1200, anchor="nw", window=bun_sub_btn1)


        btn_4=Button(canvas,text='Add Item', width=20,height=1,foreground="white",background="blue",font='arial 12',command=bun_add_item)
        window_btn_4 = canvas.create_window(830, 770, anchor="nw", window=btn_4)


    btn1=Button(canvas,text='Add Products', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_product)
    window_btn1 = canvas.create_window(1050, 430, anchor="nw", window=btn1)

    

    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Expenses Tab}
    tab_exp = ttk.Notebook(tab4)
    tab4_1 =  ttk.Frame(tab_exp)
    tab4_2=  ttk.Frame(tab_exp)
    tab_exp.add(tab4_1,compound = LEFT, text ='Expenses')
    tab_exp.add(tab4_2,compound = LEFT, text ='Supliers')
    tab_exp.pack(expand = 1, fill ="both")
    #33333333333333333333333333333333333333333333333333333333333333333333333333333333333{Pay Roll Tab}
    tab_payroll = ttk.Notebook(tab5)
    tab5_1 =  ttk.Frame(tab_payroll)
    tab5_2=  ttk.Frame(tab_payroll)
     
    tab_payroll.add(tab5_1,compound = LEFT, text ='Employee')
    tab_payroll.add(tab5_2,compound = LEFT, text ='Payslip')

    tab_payroll.pack(expand = 1, fill ="both")

    #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Report Tab}

    tab_report = ttk.Notebook(tab6)
    tab6_1 =  ttk.Frame(tab_report)
    tab6_2=  ttk.Frame(tab_report)
    tab6_3 = ttk.Frame(tab_report)
    tab6_4=  ttk.Frame(tab_report)

    
        
    tab_report.add(tab6_1,compound = LEFT, text ='Profit & Loss')
    tab_report.add(tab6_2,compound = LEFT, text ='Balance Sheet')
    tab_report.add(tab6_3,compound = LEFT, text ='Accounts Receivables')
    tab_report.add(tab6_4,compound = LEFT, text ='Accounts Payables')
 
    tab_report.pack(expand = 1, fill ="both")

    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Taxes}

    tab_tax = ttk.Notebook(tab7)
    tab7_1 =  ttk.Frame(tab_tax)
    tab7_2=  ttk.Frame(tab_tax)

    tab_tax.add(tab7_1,compound = LEFT, text ='GST')
    tab_tax.add(tab7_2,compound = LEFT, text ='New')

    tab_tax.pack(expand = 1, fill ="both")

    #333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Accounting}
    tab_account = ttk.Notebook(tab8)
    tab8_1 =  ttk.Frame(tab_account)
    tab8_2=  ttk.Frame(tab_account)

    tab_account.add(tab8_1,compound = LEFT, text ='Chart Of Accounts')
    tab_account.add(tab8_2,compound = LEFT, text ='Reconcile')
   
 
    tab_account.pack(expand = 1, fill ="both")
    #33333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{Cash Management}
    tab_cash = ttk.Notebook(tab10)
    
    tab10_1 =  ttk.Frame(tab_cash)
    tab10_2=  ttk.Frame(tab_cash)
    tab10_3 = ttk.Frame(tab_cash)

    tab_cash.add(tab10_1,compound = LEFT, text ='Cash Position')
    tab_cash.add(tab10_2,compound = LEFT, text ='Cash Flow Analyzer')
    tab_cash.add(tab10_3,compound = LEFT, text ='Check Cash Flow')

    tab_cash.pack(expand = 1, fill ="both")
    #3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333{My Account}
    Sys_mains_frame=Frame(tab9, height=750,bg="#2f516f")
    Sys_mains_frame.pack(fill=X)
#----------------------------------------------------------------------------------Sign in frame in signup section
def fun_sign_in():
    
    main_frame_signup.destroy()
    global main_frame_signin
    main_frame_signin=Frame(root, height=750)
    main_frame_signin.pack(fill=X,)

    sign_in=Label(main_frame_signin, text="Sign In",font=('Calibri 30 bold'), fg="black")
    sign_in.place(x=900, y=220)


    def sig_nm(event):
        if nm_ent.get()=="Username":
            nm_ent.delete(0,END)
        else:
            pass

    def sig_pass(event):
            if pass_ent.get()=="Password":
                pass_ent.delete(0,END)
            else:
                pass
    nm_ent = Entry(main_frame_signin, width=25, font=('Calibri 16'))
    nm_ent.insert(0,"Username")
    nm_ent.bind("<Button-1>",sig_nm)
    nm_ent.place(x=820,y=300)

    pass_ent = Entry(main_frame_signin, width=25, font=('Calibri 16'))
    pass_ent.insert(0,"Password")
    pass_ent.bind("<Button-1>",sig_pass)
    pass_ent.place(x=820,y=350)

    but_sign2 = customtkinter.CTkButton(master=main_frame_signin,command=lambda:main_sign_in(),text="Log In",bg="#213b52")
    but_sign2.place(relx=0.69, rely=0.58)

    #----------------------------------------------------------------------------------------left canvas
    lf_signup= Canvas(main_frame_signin,width=1500, height=1500)
    lf_signup.place(x=-700,y=0)

    lf_signup.create_oval(1400,1400,-800,-1700,fill="#213b52")

    label = Label(main_frame_signin, image = exprefreshIcon,bg="#213b52", width=500, justify=RIGHT)
    label.place(x=0,y=150)

    lft_lab=Label(main_frame_signin, text="New here ?",font=('Calibri 20 bold'), fg="white", bg="#213b52")
    lft_lab.place(x=250, y=40)
    lft_lab=Label(main_frame_signin, text="Join here to start a business with FinsYs!",font=('Calibri 16 bold'), fg="white", bg="#213b52")
    lft_lab.place(x=150, y=80)

    btn2 = Button(main_frame_signin, text = 'Sign Up', command=lambda:func_sign_up(), bg="white", fg="black",borderwidth = 3,height=1,width=10)
    btn2.place(x=275,y=130)


#-----------------------------------------------------------------------------------Sign Up Section
def func_sign_up():
    global main_frame_signup
    main_frame_signin.destroy()

    main_frame_signup=Frame(root, height=750)
    main_frame_signup.pack(fill=X,)

    lf_signup= Canvas(main_frame_signup,width=1500, height=1500)
    lf_signup.place(x=500,y=0)

    lf_signup.create_oval(1400,1400,150,-1700,fill="#213b52")

    #--------------------------------------------------------------------------------sign up section
    sign_in=Label(main_frame_signup, text="Sign Up",font=('Calibri 30 bold'), fg="black")
    sign_in.place(x=260, y=100)

    def nme(event):
        if fst_nm.get()=="Firstname":
            fst_nm.delete(0,END)
        else:
            pass

    def nme1(event):
        if lst_nm.get()=="Lastname":
            lst_nm.delete(0,END)
        else:
            pass
        
    def nme2(event):
        if sys_em.get()=="Email":
            sys_em.delete(0,END)
        else:
            pass
        
        
    def nme3(event):
        if sys_usr.get()=="Username":
            sys_usr.delete(0,END)
        else:
            pass
        
    def nme4(event):
        if sys_pass.get()=="Password":
            sys_pass.delete(0,END)
        else:
            pass
    
    def nme5(event):
        if sys_cf.get()=="Confirm Password":
            sys_cf.delete(0,END)
        else:
            pass
    
    

    fst_nm = Entry(main_frame_signup, width=25,text="Firstname", font=('Calibri 16'))
    fst_nm.insert(0,"Firstname")
    fst_nm.bind("<Button-1>",nme)
    fst_nm.place(x=200,y=200)

    lst_nm = Entry(main_frame_signup,  width=25, font=('Calibri 16'))
    lst_nm.insert(0,"Lastname")
    lst_nm.bind("<Button-1>",nme1)
    lst_nm.place(x=200,y=250)

    sys_em = Entry(main_frame_signup, width=25, font=('Calibri 16'))
    sys_em.insert(0,"Email")
    sys_em.bind("<Button-1>",nme2)
    sys_em.place(x=200,y=300)

    sys_usr = Entry(main_frame_signup, width=25, font=('Calibri 16'))
    sys_usr.insert(0,"Username")
    sys_usr.bind("<Button-1>",nme3)
    sys_usr.place(x=200,y=350)

    sys_pass = Entry(main_frame_signup, width=25, font=('Calibri 16'))
    sys_pass.insert(0,"Password")
    sys_pass.bind("<Button-1>",nme4)
    sys_pass.place(x=200,y=400)

    sys_cf = Entry(main_frame_signup, width=25, font=('Calibri 16'))
    sys_cf.insert(0,"Confirm Password")
    sys_cf.bind("<Button-1>",nme5)
    sys_cf.place(x=200,y=450)

    # sig_up =PIL.Image.open("images/register.png")
    # sign_up=ImageTk.PhotoImage(sig_up)

    # label = Label(main_frame_signup, image = sign_up,bg="#213b52", width=500, justify=RIGHT)
    # label.place(x=200,y=150)
    
    button_sign = customtkinter.CTkButton(master=main_frame_signup,text="Sign Up",bg="#213b52")
    button_sign.place(relx=0.2, rely=0.7) 

    lft_lab=Label(main_frame_signup, text="One of us ?",font=('Calibri 20 bold'), fg="white", bg="#213b52")
    lft_lab.place(x=900, y=40)
    lft_lab=Label(main_frame_signup, text="click here for work with FinsYs.",font=('Calibri 16 bold'), fg="white", bg="#213b52")
    lft_lab.place(x=820, y=80)

    btn_signup = Button(main_frame_signup, text='Sign In', command=fun_sign_in, bg="white", fg="black",borderwidth = 3,height=1,width=10)
    btn_signup.place(x=920,y=130)


main_frame_signin=Frame(root, height=750)
main_frame_signin.pack(fill=X,)

sign_in=Label(main_frame_signin, text="Sign In",font=('Calibri 30 bold'), fg="black")
sign_in.place(x=900, y=220)

def sig_nm(event):
        if nm_ent.get()=="Username":
            nm_ent.delete(0,END)
        else:
            pass

def sig_pass(event):
        if pass_ent.get()=="Password":
            pass_ent.delete(0,END)
        else:
            pass
nm_ent = Entry(main_frame_signin, width=25, font=('Calibri 16'))
nm_ent.insert(0,"Username")
nm_ent.bind("<Button-1>",sig_nm)
nm_ent.place(x=820,y=300)

pass_ent = Entry(main_frame_signin, width=25, font=('Calibri 16'))
pass_ent.insert(0,"Password")
pass_ent.bind("<Button-1>",sig_pass)
pass_ent.place(x=820,y=350)

button = customtkinter.CTkButton(master=main_frame_signin,command=main_sign_in,text="Log In",bg="#213b52")
button.place(relx=0.69, rely=0.58)

#----------------------------------------------------------------------------------------left canvas
lf_signup= Canvas(main_frame_signin,width=1500, height=1500)
lf_signup.place(x=-700,y=0)

lf_signup.create_oval(1400,1400,-800,-1700,fill="#213b52")

label = Label(main_frame_signin, image = exprefreshIcon,bg="#213b52", width=500, justify=RIGHT)
label.place(x=0,y=150)

lft_lab=Label(main_frame_signin, text="New here ?",font=('Calibri 20 bold'), fg="white", bg="#213b52")
lft_lab.place(x=250, y=40)
lft_lab=Label(main_frame_signin, text="Join here to start a business with FinsYs!",font=('Calibri 16 bold'), fg="white", bg="#213b52")
lft_lab.place(x=150, y=80)

btn2 = Button(main_frame_signin, text = 'Sign Up', command = func_sign_up, bg="white", fg="black",borderwidth = 3,height=1,width=10)
btn2.place(x=275,y=130)

root.mainloop()