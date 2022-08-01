
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
    tab3_2.grid_columnconfigure(0,weight=1)
    tab3_2.grid_rowconfigure(0,weight=1)

    inv_frame = Frame(tab3_2)
    inv_frame.grid(row=0,column=0,sticky='nsew')

    def inv_responsive_widgets(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget

        r1 = 25
        x1 = dwidth/63
        x2 = dwidth/1.021
        y1 = dheight/14 
        y2 = dheight/3.505

        dcanvas.coords("ipoly1",x1 + r1,y1,
        x1 + r1,y1,
        x2 - r1,y1,
        x2 - r1,y1,     
        x2,y1,     
        #--------------------
        x2,y1 + r1,     
        x2,y1 + r1,     
        x2,y2 - r1,     
        x2,y2 - r1,     
        x2,y2,
        #--------------------
        x2 - r1,y2,     
        x2 - r1,y2,     
        x1 + r1,y2,
        x1 + r1,y2,
        x1,y2,
        #--------------------
        x1,y2 - r1,
        x1,y2 - r1,
        x1,y1 + r1,
        x1,y1 + r1,
        x1,y1,
        )

        dcanvas.coords("ihline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
        dcanvas.coords("ilabel1",dwidth/2.5,dheight/8.00)

        r2 = 25
        x11 = dwidth/63
        x21 = dwidth/1.021
        y11 = dheight/2.8
        y21 = dheight/1.168


        dcanvas.coords("ipoly2",x11 + r2,y11,
        x11 + r2,y11,
        x21 - r2,y11,
        x21 - r2,y11,     
        x21,y11,     
        #--------------------
        x21,y11 + r2,     
        x21,y11 + r2,     
        x21,y21 - r2,     
        x21,y21 - r2,     
        x21,y21,
        #--------------------
        x21 - r2,y21,     
        x21 - r2,y21,     
        x11 + r2,y21,
        x11 + r2,y21,
        x11,y21,
        #--------------------
        x11,y21 - r2,
        x11,y21 - r2,
        x11,y11 + r2,
        x11,y11 + r2,
        x11,y11,
        )

        dcanvas.coords("iline1", dwidth/22.00, dheight/1.8, dwidth/1.060, dheight/1.8)
        dcanvas.coords("iline2", dwidth/22.00, dheight/1.8, dwidth/22.00, dheight/1.35)
        dcanvas.coords("iline3", dwidth/22.00, dheight/1.35, dwidth/1.060, dheight/1.35)
        dcanvas.coords("iline4", dwidth/1.060, dheight/1.8, dwidth/1.060, dheight/1.35)
        dcanvas.coords("iline5", dwidth/22.00, dheight/1.575, dwidth/1.060, dheight/1.575)
        dcanvas.coords("iline6", dwidth/6.20, dheight/1.8, dwidth/6.20, dheight/1.35)
        dcanvas.coords("iline7", dwidth/4.00, dheight/1.8, dwidth/4.00, dheight/1.35)
        dcanvas.coords("iline8", dwidth/2.7, dheight/1.8, dwidth/2.7, dheight/1.35)
        dcanvas.coords("iline9", dwidth/1.95, dheight/1.8, dwidth/1.95, dheight/1.35)
        dcanvas.coords("iline10", dwidth/1.65, dheight/1.8, dwidth/1.65, dheight/1.35)
        dcanvas.coords("iline11", dwidth/1.38, dheight/1.8, dwidth/1.38, dheight/1.35)
        dcanvas.coords("iline12", dwidth/1.20, dheight/1.8, dwidth/1.20, dheight/1.35)


        dcanvas.coords("ilabel2",dwidth/13.5,dheight/1.74)
        dcanvas.coords("ilabel3",dwidth/5.78,dheight/1.74)
        dcanvas.coords("ilabel4",dwidth/3.6,dheight/1.74)
        dcanvas.coords("ilabel5",dwidth/2.45,dheight/1.74)
        dcanvas.coords("ilabel6",dwidth/1.9,dheight/1.74)
        dcanvas.coords("ilabel7",dwidth/1.59,dheight/1.74)
        dcanvas.coords("ilabel8",dwidth/1.345,dheight/1.74)
        dcanvas.coords("ilabel9",dwidth/1.17,dheight/1.74)

        dcanvas.coords("ibutton1",dwidth/1.28,dheight/2.4)
        dcanvas.coords("icombo1",dwidth/1.179,dheight/1.52)



    inv_canvas=Canvas(inv_frame, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,1000))

    inv_frame.grid_rowconfigure(0,weight=1)
    inv_frame.grid_columnconfigure(0,weight=1)

    vertibar=Scrollbar(inv_frame, orient=VERTICAL)
    vertibar.grid(row=0,column=1,sticky='ns')
    vertibar.config(command=inv_canvas.yview)
    
    inv_canvas.bind("<Configure>", inv_responsive_widgets)
    inv_canvas.config(yscrollcommand=vertibar.set)
    inv_canvas.grid(row=0,column=0,sticky='nsew')

    
    inv_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("ipoly1"))

    label_1 = Label(inv_canvas,width=10,height=1,text="INVOICES", font=('arial 25'),background="#1b3857",fg="white") 
    window_label_1 = inv_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("ilabel1"))

    inv_canvas.create_line(0,0,0,0,fill='gray',width=1,tags=("ihline"))

    inv_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("ipoly2"))


    inv_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("iline1"))
    inv_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("iline2"))
    inv_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("iline3"))
    inv_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("iline4"))
    inv_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("iline5"))
    inv_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("iline6"))
    inv_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("iline7"))
    inv_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("iline8"))
    inv_canvas.create_line(0, 0, 0, 0, 
    fill='gray',width=1,tags=("iline9"))
    inv_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("iline10"))
    inv_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("iline11"))
    inv_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("iline12"))
    
    

    label_2 = Label(inv_canvas,width=10,height=1,text="INVOICE NO", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_2 = inv_canvas.create_window(0, 0, anchor="nw", window=label_2,tags=('ilabel2'))

    label_3 = Label(inv_canvas,width=11,height=1,text="INVOICE DATE", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_3 = inv_canvas.create_window(0, 0, anchor="nw", window=label_3,tags=('ilabel3'))

    label_4 = Label(inv_canvas,width=11,height=1,text="CUSTOMER", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = inv_canvas.create_window(0, 0, anchor="nw", window=label_4,tags=('ilabel4'))

    label_4 = Label(inv_canvas,width=11,height=1,text="EMAIL ID", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = inv_canvas.create_window(0, 0, anchor="nw", window=label_4,tags=('ilabel5'))

    label_4 = Label(inv_canvas,width=11,height=1,text="DUE DATE", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = inv_canvas.create_window(0, 0, anchor="nw", window=label_4,tags=('ilabel6'))

    label_4 = Label(inv_canvas,width=11,height=1,text="GRAND TOTAL", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = inv_canvas.create_window(0, 0, anchor="nw", window=label_4,tags=('ilabel7'))

    label_4 = Label(inv_canvas,width=11,height=1,text="BALANCE DUE", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = inv_canvas.create_window(0, 0, anchor="nw", window=label_4,tags=('ilabel8'))

    label_4 = Label(inv_canvas,width=11,height=1,text="ACTION", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = inv_canvas.create_window(0, 0, anchor="nw", window=label_4,tags=('ilabel9'))




    def add_invoice():
        inv_frame.grid_forget()
        inv_frame_1 = Frame(tab3_2)
        inv_frame_1.grid(row=0,column=0,sticky='nsew')

        def inv_responsive_widgets2(event):
            try:
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget
                
                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/14 
                y2 = dheight/3.505

                dcanvas.coords("aipoly1",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )

                dcanvas.coords("ailabel1",dwidth/2.45,dheight/8.24)
                dcanvas.coords("aihline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                r2 = 25
                x11 = dwidth/63
                x21 = dwidth/1.021
                y11 = dheight/2.8
                y21 = dheight/0.36


                dcanvas.coords("aipoly2",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                dcanvas.coords("ailabel2",dwidth/2.45,dheight/2.34)
                dcanvas.coords("ailabel3",dwidth/22.80,dheight/1.90)
                dcanvas.coords("ailabel4",dwidth/20.00,dheight/1.65)
                dcanvas.coords("ailabel5",dwidth/20.00,dheight/1.37)
                dcanvas.coords("ailabel6",dwidth/3.34,dheight/1.37)
                dcanvas.coords("ailabel7",dwidth/21.66 ,dheight/1.12)
                dcanvas.coords("ailabel8",dwidth/3.34,dheight/1.12)
                dcanvas.coords("ailabel9",dwidth/19.10,dheight/0.947)
                dcanvas.coords("ailabel10",dwidth/19.40,dheight/0.717)
                dcanvas.coords("ailabel11",dwidth/16.50,dheight/0.638)
                dcanvas.coords("ailabel12",dwidth/8.40,dheight/0.638)
                dcanvas.coords("ailabel13",dwidth/3.34,dheight/0.638)
                dcanvas.coords("ailabel14",dwidth/2.28,dheight/0.638)
                dcanvas.coords("ailabel15",dwidth/1.73,dheight/0.638)
                dcanvas.coords("ailabel16",dwidth/1.52,dheight/0.638)
                dcanvas.coords("ailabel17",dwidth/1.325,dheight/0.638)
                dcanvas.coords("ailabel18",dwidth/1.165,dheight/0.638)
                dcanvas.coords("ailabel19",dwidth/16.50,dheight/0.604)
                dcanvas.coords("ailabel20",dwidth/16.50,dheight/0.562)
                dcanvas.coords("ailabel21",dwidth/16.50,dheight/0.526)
                dcanvas.coords("ailabel22",dwidth/16.50,dheight/0.496)
                dcanvas.coords("ailabel23",dwidth/1.53,dheight/0.45)
                dcanvas.coords("ailabel24",dwidth/1.54,dheight/0.435)
                dcanvas.coords("ailabel25",dwidth/1.54,dheight/0.42)
                dcanvas.coords("ailabel26",dwidth/1.54,dheight/0.406)
                dcanvas.coords("ailabel27",dwidth/1.54,dheight/0.392)
                dcanvas.coords("ailabel28",dwidth/1.72,dheight/1.12)

                dcanvas.coords("aientry1",dwidth/3.0,dheight/1.295)
                dcanvas.coords("aientry2",dwidth/18.00,dheight/0.91)
                dcanvas.coords("aientry3",dwidth/4.00,dheight/0.604)
                dcanvas.coords("aientry4",dwidth/2.51,dheight/0.604)
                dcanvas.coords("aientry5",dwidth/1.8,dheight/0.604)
                dcanvas.coords("aientry6",dwidth/1.565,dheight/0.604)
                dcanvas.coords("aientry7",dwidth/1.357,dheight/0.604)
                dcanvas.coords("aientry8",dwidth/4.00,dheight/0.562)
                dcanvas.coords("aientry9",dwidth/4.00,dheight/0.526)
                dcanvas.coords("aientry10",dwidth/4.00,dheight/0.496)
                dcanvas.coords("aientry11",dwidth/2.51,dheight/0.562)
                dcanvas.coords("aientry12",dwidth/2.51,dheight/0.526)
                dcanvas.coords("aientry13",dwidth/2.51,dheight/0.496)
                dcanvas.coords("aientry14",dwidth/1.8,dheight/0.562)
                dcanvas.coords("aientry15",dwidth/1.8,dheight/0.526)
                dcanvas.coords("aientry16",dwidth/1.8,dheight/0.496)
                dcanvas.coords("aientry17",dwidth/1.565,dheight/0.562)
                dcanvas.coords("aientry18",dwidth/1.565,dheight/0.526)
                dcanvas.coords("aientry19",dwidth/1.565,dheight/0.496)
                dcanvas.coords("aientry20",dwidth/1.357,dheight/0.562)
                dcanvas.coords("aientry21",dwidth/1.357,dheight/0.526)
                dcanvas.coords("aientry22",dwidth/1.357,dheight/0.496)
                dcanvas.coords("aientry23",dwidth/1.33,dheight/0.452)
                dcanvas.coords("aientry24",dwidth/1.33,dheight/0.4365)
                dcanvas.coords("aientry25",dwidth/1.33,dheight/0.4215)
                dcanvas.coords("aientry26",dwidth/1.33,dheight/0.407)
                dcanvas.coords("aientry27",dwidth/1.33,dheight/0.393)

                dcanvas.coords("aicombo1",dwidth/18.00,dheight/1.295)
                dcanvas.coords("aicombo2",dwidth/3.00,dheight/1.074)
                dcanvas.coords("aicombo3",dwidth/18.00,dheight/0.695)
                dcanvas.coords("aicombo4",dwidth/10.10,dheight/0.604)
                dcanvas.coords("aicombo5",dwidth/1.21,dheight/0.604)
                dcanvas.coords("aicombo6",dwidth/10.10,dheight/0.562)
                dcanvas.coords("aicombo7",dwidth/10.10,dheight/0.526)
                dcanvas.coords("aicombo8",dwidth/10.10,dheight/0.496)
                dcanvas.coords("aicombo9",dwidth/1.21,dheight/0.562)
                dcanvas.coords("aicombo10",dwidth/1.21,dheight/0.526)
                dcanvas.coords("aicombo11",dwidth/1.21,dheight/0.496)

                dcanvas.coords("aibutton1",dwidth/4.74,dheight/1.295)
                dcanvas.coords("aibutton2",dwidth/1.28,dheight/0.377)
                dcanvas.coords("aibutton3",dwidth/23,dheight/3.415)

                #-------------------------------H Lines-----------------------------------#
                dcanvas.coords("ailine1",dwidth/21,dheight/0.645,dwidth/1.055,dheight/0.645)
                dcanvas.coords("ailine2",dwidth/21,dheight/0.617,dwidth/1.055,dheight/0.617)
                dcanvas.coords("ailine3",dwidth/21,dheight/0.576,dwidth/1.055,dheight/0.576)
                dcanvas.coords("ailine4",dwidth/21,dheight/0.536,dwidth/1.055,dheight/0.536)
                dcanvas.coords("ailine5",dwidth/21,dheight/0.506,dwidth/1.055,dheight/0.506)
                dcanvas.coords("ailine6",dwidth/21,dheight/0.476,dwidth/1.055,dheight/0.476)
                #-------------------------------V Lines-----------------------------------#
                dcanvas.coords("ailine7",dwidth/21,dheight/0.645,dwidth/21,dheight/0.476)
                dcanvas.coords("ailine8",dwidth/1.055,dheight/0.645,dwidth/1.055,dheight/0.476)
                dcanvas.coords("ailine9",dwidth/11,dheight/0.645,dwidth/11,dheight/0.476)
                dcanvas.coords("ailine10",dwidth/4.15,dheight/0.645,dwidth/4.15,dheight/0.476)
                dcanvas.coords("ailine11",dwidth/2.55,dheight/0.645,dwidth/2.55,dheight/0.476)
                dcanvas.coords("ailine12",dwidth/1.83,dheight/0.645,dwidth/1.83,dheight/0.476)
                dcanvas.coords("ailine13",dwidth/1.58,dheight/0.645,dwidth/1.58,dheight/0.476)
                dcanvas.coords("ailine14",dwidth/1.37,dheight/0.645,dwidth/1.37,dheight/0.476)
                dcanvas.coords("ailine15",dwidth/1.22,dheight/0.645,dwidth/1.22,dheight/0.476)

                #-------------------------------V Lines-----------------------------------#
                dcanvas.coords("ailine16",dwidth/1.58,dheight/0.455,dwidth/1.58,dheight/0.383)
                dcanvas.coords("ailine17",dwidth/1.348,dheight/0.455,dwidth/1.348,dheight/0.383)
                dcanvas.coords("ailine18",dwidth/1.084,dheight/0.455,dwidth/1.084,dheight/0.383)
                #-------------------------------H Lines-----------------------------------#
                dcanvas.coords("ailine19",dwidth/1.58,dheight/0.455,dwidth/1.084,dheight/0.455)
                dcanvas.coords("ailine20",dwidth/1.58,dheight/0.383,dwidth/1.084,dheight/0.383)
                dcanvas.coords("ailine21",dwidth/1.58,dheight/0.439,dwidth/1.084,dheight/0.439)
                dcanvas.coords("ailine22",dwidth/1.58,dheight/0.424,dwidth/1.084,dheight/0.424)
                dcanvas.coords("ailine23",dwidth/1.58,dheight/0.41,dwidth/1.084,dheight/0.41)
                dcanvas.coords("ailine24",dwidth/1.58,dheight/0.396,dwidth/1.084,dheight/0.396)
            except:
                pass

            try:
                dcanvas.coords("aidate1",dwidth/17.8,dheight/1.074)
                dcanvas.coords("aidate2",dwidth/1.65,dheight/1.074)
            except:
                pass



        inv_canvas_1=Canvas(inv_frame_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1800))

        inv_frame_1.grid_columnconfigure(0,weight=1)
        inv_frame_1.grid_rowconfigure(0,weight=1)
        
        vertibar=Scrollbar(inv_frame_1, orient=VERTICAL)
        vertibar.grid(row=0,column=1,sticky='ns')
        vertibar.config(command=inv_canvas_1.yview)

        inv_canvas_1.bind("<Configure>", inv_responsive_widgets2)
        inv_canvas_1.config(yscrollcommand=vertibar.set)
        inv_canvas_1.grid(row=0,column=0,sticky='nsew')

        inv_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("aipoly1"))

        
        label_1 = Label(inv_canvas_1,width=10,height=1,text="INVOICE", font=('arial 20'),background="#1b3857",fg="white") 
        window_label_1 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("ailabel1"))

        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("aihline"))

        inv_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("aipoly2"))

        label_1 = Label(inv_canvas_1,width=10,height=1,text="Fin sYs", font=('arial 20'),background="#1b3857",fg="white") 
        window_label_1 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("ailabel2"))

        label_2 = Label(inv_canvas_1,width=15,height=1,text="Company name", font=('arial 16'),background="#1b3857",fg="skyblue") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ailabel3"))

        label_2 = Label(inv_canvas_1,width=15,height=1,text="Company email-id", font=('arial 16'),background="#1b3857",fg="skyblue") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ailabel4"))

        label_2 = Label(inv_canvas_1,width=15,height=1,text="Select Customer", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ailabel5"))

        aicomb_1 = ttk.Combobox(inv_canvas_1, font=('arial 10'),foreground="white")
        aicomb_1['values'] = ("Select Customer",)
        aicomb_1.current(0)
        window_aicomb_1 = inv_canvas_1.create_window(0, 0, anchor="nw", width=200, height=30,window=aicomb_1, tags=("aicombo1"))

        def add_inv_customer():
            #inv_frame.grid_forget()
            inv_frame_1.grid_forget()
            inv_frame_2 = Frame(tab3_2)
            inv_frame_2.grid(row=0,column=0,sticky='nsew')

            def inc_responsive_widgets2(event):
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget
            
                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/14 
                y2 = dheight/3.505

                dcanvas.coords("acpoly1",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )

                dcanvas.coords("aclabel1",dwidth/2.5,dheight/8.24)
                dcanvas.coords("achline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                r2 = 25
                x11 = dwidth/63
                x21 = dwidth/1.021
                y11 = dheight/2.8
                y21 = dheight/0.45


                dcanvas.coords("acpoly2",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                dcanvas.coords("aclabel2",dwidth/17.0,dheight/2.35)
                dcanvas.coords("achline1",dwidth/21,dheight/1.95,dwidth/1.055,dheight/1.95)
                dcanvas.coords("aclabel3",dwidth/20.2,dheight/1.69)
                dcanvas.coords("aclabel4",dwidth/3.35,dheight/1.69)
                dcanvas.coords("aclabel5",dwidth/1.8,dheight/1.69)
                dcanvas.coords("aclabel6",dwidth/20.2,dheight/1.32)
                dcanvas.coords("aclabel7",dwidth/3.375,dheight/1.32)
                dcanvas.coords("aclabel8",dwidth/20.2,dheight/1.088)
                dcanvas.coords("aclabel9",dwidth/3.48,dheight/1.088)
                dcanvas.coords("aclabel10",dwidth/1.82,dheight/1.088)
                dcanvas.coords("aclabel11",dwidth/18.7,dheight/0.92)
                dcanvas.coords("aclabel12",dwidth/3.40,dheight/0.92)
                dcanvas.coords("aclabel13",dwidth/1.83,dheight/0.92)
                dcanvas.coords("aclabel14",dwidth/55.5,dheight/0.79)
                dcanvas.coords("aclabel15",dwidth/2.09,dheight/0.79)
                dcanvas.coords("aclabel16",dwidth/19.5,dheight/0.74)
                dcanvas.coords("aclabel17",dwidth/1.97,dheight/0.74)
                dcanvas.coords("aclabel18",dwidth/19.49,dheight/0.645)
                dcanvas.coords("aclabel19",dwidth/3.40,dheight/0.645)
                dcanvas.coords("aclabel20",dwidth/2.0,dheight/0.645)
                dcanvas.coords("aclabel21",dwidth/1.33,dheight/0.645)
                dcanvas.coords("aclabel22",dwidth/21.0,dheight/0.58)
                dcanvas.coords("aclabel23",dwidth/3.42,dheight/0.58)
                dcanvas.coords("aclabel24",dwidth/2.0,dheight/0.58)
                dcanvas.coords("aclabel25",dwidth/1.34,dheight/0.58)

                dcanvas.coords("accombo1",dwidth/18.5,dheight/1.55)
                dcanvas.coords("accombo2",dwidth/18.5,dheight/1.027)

                dcanvas.coords("acentry1",dwidth/3.30,dheight/1.55)
                dcanvas.coords("acentry2",dwidth/1.785,dheight/1.55)
                dcanvas.coords("acentry3",dwidth/18.5,dheight/1.24)
                dcanvas.coords("acentry4",dwidth/3.30,dheight/1.24)
                dcanvas.coords("acentry5",dwidth/3.30,dheight/1.027)
                dcanvas.coords("acentry6",dwidth/1.785,dheight/1.027)
                dcanvas.coords("acentry7",dwidth/18.5,dheight/0.88)
                dcanvas.coords("acentry8",dwidth/3.30,dheight/0.88)
                dcanvas.coords("acentry9",dwidth/1.785,dheight/0.88)
                dcanvas.coords("acentry10",dwidth/18.5,dheight/0.715)
                dcanvas.coords("acentry11",dwidth/1.97,dheight/0.715)
                dcanvas.coords("acentry12",dwidth/18.5,dheight/0.625)
                dcanvas.coords("acentry13",dwidth/3.40,dheight/0.625)
                dcanvas.coords("acentry14",dwidth/1.98,dheight/0.625)
                dcanvas.coords("acentry15",dwidth/1.33,dheight/0.625)
                dcanvas.coords("acentry16",dwidth/19.51,dheight/0.565)
                dcanvas.coords("acentry17",dwidth/3.40,dheight/0.565)
                dcanvas.coords("acentry18",dwidth/1.98,dheight/0.565)
                dcanvas.coords("acentry19",dwidth/1.33,dheight/0.565)

                dcanvas.coords("accheck1",dwidth/1.55,dheight/0.79)
                dcanvas.coords("accheck2",dwidth/19.0,dheight/0.546)

                dcanvas.coords("acbutton1",dwidth/2.5,dheight/0.5)
                dcanvas.coords("acbutton2",dwidth/23,dheight/3.415)


            inv_canvas_2=Canvas(inv_frame_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1600))

            inv_frame_2.grid_columnconfigure(0,weight=1)
            inv_frame_2.grid_rowconfigure(0,weight=1)

            
            vertibar=Scrollbar(inv_frame_2, orient=VERTICAL)
            vertibar.grid(row=0,column=1,sticky='ns')
            vertibar.config(command=inv_canvas_2.yview)

            inv_canvas_2.bind("<Configure>", inc_responsive_widgets2)
            inv_canvas_2.config(yscrollcommand=vertibar.set)
            inv_canvas_2.grid(row=0,column=0,sticky='nsew')
            

            inv_canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly1"))

            label_1 = Label(inv_canvas_2,width=15,height=1,text="ADD CUSTOMER", font=('arial 20'),background="#1b3857",fg="white") 
            window_label_1 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel1"))

            inv_canvas_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline"))

            inv_canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly2"))

            label_1 = Label(inv_canvas_2,width=20,height=1,text="Customer Information", font=('arial 20'),background="#1b3857",fg="white") 
            window_label_1 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel2"))

            inv_canvas_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline1"))

            label_2 = Label(inv_canvas_2,width=5,height=1,text="Title", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel3"))

            ic_comb_cus_1 = ttk.Combobox(inv_canvas_2, font=('arial 10'),foreground="white")
            ic_comb_cus_1['values'] = ("Mr","Mrs","Miss","Ms",)
            ic_comb_cus_1.current(0)
            window_ic_comb_cus_1 = inv_canvas_2.create_window(0, 0, anchor="nw", width=245, height=30,window=ic_comb_cus_1, tags=("accombo1"))

            label_2 = Label(inv_canvas_2,width=10,height=1,text="First name", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel4"))

            ic_entry_cus_1=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_1 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_1, tags=("acentry1"))

            label_2 = Label(inv_canvas_2,width=10,height=1,text="Last name", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel5"))

            ic_entry_cus_2=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_2 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_2, tags=("acentry2"))

            label_2 = Label(inv_canvas_2,width=10,height=1,text="Company", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel6"))

            ic_entry_cus_3=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_3 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_3, tags=("acentry3"))

            label_2 = Label(inv_canvas_2,width=10,height=1,text="Location", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel7"))

            ic_cus_4=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_cus_4 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_cus_4, tags=("acentry4"))

            label_2 = Label(inv_canvas_2,width=10,height=1,text="GST type", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel8"))

            ic_comb_cus_2 = ttk.Combobox(inv_canvas_2, font=('arial 10'),foreground="white")
            ic_comb_cus_2['values'] = ("Choose...","GST registered Regular","GST registered-Composition","GST unregistered","Consumer","Overseas","SEZ","Deemed exports-EOU's STP's EHTP's etc",)
            ic_comb_cus_2.current(0)
            window_ic_comb_cus_2 = inv_canvas_2.create_window(0, 0, anchor="nw", width=245, height=30,window=ic_comb_cus_2, tags=("accombo2"))

            label_2 = Label(inv_canvas_2,width=10,height=1,text="GSTIN", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel9"))

            ic_cus_entry_str_1 = StringVar()
            ic_entry_cus_5=Entry(inv_canvas_2,width=34,justify=LEFT,background='#2f516f',foreground="white",font=('arial 10'),textvariable=ic_cus_entry_str_1)
            ic_cus_entry_str_1.set(' 29APPCK7465F1Z1')
            window_ic_entry_cus_5 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_5, tags=("acentry5"))

            label_2 = Label(inv_canvas_2,width=10,height=1,text="PAN NO", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel10"))

            ic_cus_entry_str_2 = StringVar()
            ic_entry_cus_6=Entry(inv_canvas_2,width=34,justify=LEFT,background='#2f516f',foreground="white",font=('arial 10'),textvariable=ic_cus_entry_str_2)
            ic_cus_entry_str_2.set(' APPCK7465F')
            window_ic_entry_cus_6 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_6, tags=("acentry6"))

            label_2 = Label(inv_canvas_2,width=5,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel11"))

            ic_entry_cus_7=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_7 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_7, tags=("acentry7"))

            label_2 = Label(inv_canvas_2,width=10,height=1,text="Website", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel12"))

            ic_entry_cus_8=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_8 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_8, tags=("acentry8"))

            label_2 = Label(inv_canvas_2,width=10,height=1,text="Mobile", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel13"))

            ic_entry_cus_9=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_9 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_9, tags=("acentry9"))

            label_1 = Label(inv_canvas_2,width=20,height=1,text="Billing Address", font=('arial 16'),background="#1b3857",fg="white") 
            window_label_1 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel14"))

            label_2 = Label(inv_canvas_2,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel16"))

            ic_entry_cus_10=Entry(inv_canvas_2,width=95,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_10 = inv_canvas_2.create_window(0, 0, anchor="nw", height=60,window=ic_entry_cus_10, tags=("acentry10"))

            label_1 = Label(inv_canvas_2,width=20,height=1,text="Shipping Address", font=('arial 16'),background="#1b3857",fg="white") 
            window_label_1 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel15"))

            ic_chk_str = StringVar()
            ic_chkbtn1 = Checkbutton(inv_canvas_2, text = "Same As Billing Address", variable = ic_chk_str, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f")
            ic_chkbtn1.select()
            window_ic_chkbtn_1 = inv_canvas_2.create_window(0, 0, anchor="nw", window=ic_chkbtn1, tags=("accheck1"))

            label_2 = Label(inv_canvas_2,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel17"))

            ic_entry_cus_11=Entry(inv_canvas_2,width=95,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_11 = inv_canvas_2.create_window(0, 0, anchor="nw", height=60,window=ic_entry_cus_11, tags=("acentry11"))

            label_2 = Label(inv_canvas_2,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel18"))

            ic_entry_cus_12=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_12 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_12, tags=("acentry12"))
            
            label_2 = Label(inv_canvas_2,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel19"))

            ic_entry_cus_13=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_13 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_13, tags=("acentry13"))

            label_2 = Label(inv_canvas_2,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel20"))

            ic_entry_cus_14=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_14 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_14, tags=("acentry14"))

            label_2 = Label(inv_canvas_2,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel21"))

            ic_entry_cus_15=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_15 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_15, tags=("acentry15"))

            label_2 = Label(inv_canvas_2,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel22"))

            ic_entry_cus_12=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_12 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_12, tags=("acentry16"))
            
            label_2 = Label(inv_canvas_2,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel23"))

            ic_entry_cus_13=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_13 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_13, tags=("acentry17"))

            label_2 = Label(inv_canvas_2,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel24"))

            ic_entry_cus_14=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_14 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_14, tags=("acentry18"))

            label_2 = Label(inv_canvas_2,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel25"))

            ic_entry_cus_15=Entry(inv_canvas_2,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ic_entry_cus_15 = inv_canvas_2.create_window(0, 0, anchor="nw", height=30,window=ic_entry_cus_15, tags=("acentry19"))

            ic_chk_str_1 = StringVar()
            ic_chkbtn2 = Checkbutton(inv_canvas_2, text = "Agree to terms and conditions", variable = ic_chk_str_1, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f")
            ic_chkbtn2.select()
            window_ic_chkbtn_2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=ic_chkbtn2,tags=("accheck2"))

            ic_cus_btn2=Button(inv_canvas_2,text='Submit Form', width=25,height=2,foreground="white",background="#1b3857",font='arial 12')
            window_ic_cus_btn2 = inv_canvas_2.create_window(0, 0, anchor="nw", window=ic_cus_btn2,tags=("acbutton1"))

            def inv_back_1_():
                inv_frame_2.grid_forget()
                inv_frame_1.grid(row=0,column=0,sticky='nsew')

            bck_btn1=Button(inv_canvas_2,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=inv_back_1_)
            window_bck_btn1 = inv_canvas_2.create_window(0, 0, anchor="nw", window=bck_btn1,tags=('acbutton2'))
            


        aibtn2=Button(inv_canvas_1,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=add_inv_customer)
        window_aibtn2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=aibtn2, tags=('aibutton1'))

        label_2 = Label(inv_canvas_1,width=15,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel6'))

        aientry_1=Entry(inv_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_aientry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30,window=aientry_1,tags=('aientry1'))


        label_2 = Label(inv_canvas_1,width=15,height=1,text="Terms", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel8'))

        comb_t_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'),foreground="white")
        comb_t_2['values'] = ("Due on Receipt","NET 15","NET 30","NET 60","Add New Term",)
        comb_t_2.current(0)
        window_comb_t_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=251, height=30,window=comb_t_2,tags=('aicombo2'))


        label_2 = Label(inv_canvas_1,width=6,height=1,text="Bill To:", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel9'))

        # text_1=Text(inv_canvas_1,width=31)
        # window_text_1 = inv_canvas_1.create_window(81, 675, anchor="nw", height=150, window=text_1)
        ai_b_entry_1=Entry(inv_canvas_1,width=42,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_b_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=150, window=ai_b_entry_1,tags=('aientry2'))

        label_2 = Label(inv_canvas_1,width=12,height=1,text="Place of supply", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel10'))

        ai_p_comb_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'),foreground="white")
        ai_p_comb_2['values'] = ("Kerala","Andaman and Nicobar Islands","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Daman and Diu","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Ladakh","Lakshadweep","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Other Territory",)
        ai_p_comb_2.current(0)
        window_ai_p_comb_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=251, height=30,window=ai_p_comb_2,tags=('aicombo3'))


        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine1'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine2'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine3'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine4'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine5'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine6'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine7'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine8'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine9'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine10'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine11'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine12'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine13'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine14'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine15'))


        label_2 = Label(inv_canvas_1,width=2,height=1,text="#", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel11'))

        label_3 = Label(inv_canvas_1,width=15,height=1,text="PRODUCT/SERVICE", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_3 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_3,tags=('ailabel12'))

        label_4 = Label(inv_canvas_1,width=4,height=1,text="HSN", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_4 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel13'))

        label_4 = Label(inv_canvas_1,width=11,height=1,text="DESCRIPTION", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_4 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel14'))

        label_4 = Label(inv_canvas_1,width=4,height=1,text="QTY", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_4 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel15'))

        label_4 = Label(inv_canvas_1,width=8,height=1,text="PRICE", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_4 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel16'))

        label_4 = Label(inv_canvas_1,width=6,height=1,text="TOTAL", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_4 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel17'))

        label_4 = Label(inv_canvas_1,width=7,height=1,text="TAX (%)", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_4 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel18'))

        label_2 = Label(inv_canvas_1,width=2,height=1,text="1", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_2 = inv_canvas_1.create_window(90, 1020, anchor="nw", window=label_2,tags=('ailabel19'))

        ai_comb_p_1 = ttk.Combobox(inv_canvas_1, font=('arial 10'),foreground="white")
        ai_comb_p_1['values'] = ("Select Product",)
        ai_comb_p_1.current(0)
        window_ai_comb_p_1 = inv_canvas_1.create_window(0, 0, anchor="nw", width=180, height=30,window=ai_comb_p_1,tags=('aicombo4'))

        ai_entry_p_1=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_p_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_1,tags=('aientry3'))

        ai_entry_p_1_2=Entry(inv_canvas_1,width=31,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_p_1_2 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_1_2,tags=('aientry4'))

        ai_entry_p_1_3=Entry(inv_canvas_1,width=15,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_p_1_3 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_1_3,tags=('aientry5'))

        ai_entry_p_1_4=Entry(inv_canvas_1,width=18,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_p_1_4 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_1_4,tags=('aientry6'))

        ai_entry_p_1_5=Entry(inv_canvas_1,width=16,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_p_1_5 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_1_5,tags=('aientry7'))

        ai_comb_p_1_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'),foreground="white")
        ai_comb_p_1_2['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
        ai_comb_p_1_2.current(0)
        window_ai_comb_p_1_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=150, height=30,window=ai_comb_p_1_2,tags=('aicombo5'))


        label_2 = Label(inv_canvas_1,width=2,height=1,text="2", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel20'))

        ai_comb_P_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'),foreground="white")
        ai_comb_P_2['values'] = ("Select Product",)
        ai_comb_P_2.current(0)
        window_ai_comb_P_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=180, height=30,window=ai_comb_P_2,tags=('aicombo6'))

        ai_entry_p_2=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_p_2 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_2,tags=('aientry8'))

        ai_entry_p_2_1=Entry(inv_canvas_1,width=31,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_p_2_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_p_2_1,tags=('aientry11'))

        ai_entry_2_2=Entry(inv_canvas_1,width=15,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_2_2 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_2_2,tags=('aientry14'))

        ai_entry_2_3=Entry(inv_canvas_1,width=18,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_2_3 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_2_3,tags=('aientry17'))

        ai_entry_2_4=Entry(inv_canvas_1,width=16,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_2_4 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_2_4,tags=('aientry20'))

        ai_comb_P_2_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'),foreground="white")
        ai_comb_P_2_2['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
        ai_comb_P_2_2.current(0)
        window_ai_comb_P_2_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=150, height=30,window=ai_comb_P_2_2,tags=('aicombo9'))


        label_2 = Label(inv_canvas_1,width=2,height=1,text="3", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel21'))

        ai_comb_p_3 = ttk.Combobox(inv_canvas_1, font=('arial 10'),foreground="white")
        ai_comb_p_3['values'] = ("Select Product",)
        ai_comb_p_3.current(0)
        window_ai_comb_p_3 = inv_canvas_1.create_window(0, 0, anchor="nw", width=180, height=30,window=ai_comb_p_3,tags=('aicombo7'))

        ai_entry_3=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_3 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_3,tags=('aientry9'))

        ai_entry_3_1=Entry(inv_canvas_1,width=31,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_3_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_3_1,tags=('aientry12'))

        ai_entry_3_2=Entry(inv_canvas_1,width=15,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_3_2 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_3_2,tags=('aientry15'))

        ai_entry_3_3=Entry(inv_canvas_1,width=18,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_3_3 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_3_3,tags=('aientry18'))

        ai_entry_3_4=Entry(inv_canvas_1,width=16,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_3_4 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_3_4,tags=('aientry21'))

        ai_comb_P_3_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'),foreground="white")
        ai_comb_P_3_2['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
        ai_comb_P_3_2.current(0)
        window_ai_comb_P_3_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=150, height=30,window=ai_comb_P_3_2,tags=('aicombo10'))

        label_2 = Label(inv_canvas_1,width=2,height=1,text="4", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel22'))

        ai_comb_p_4 = ttk.Combobox(inv_canvas_1, font=('arial 10'),foreground="white")
        ai_comb_p_4['values'] = ("Select Product",)
        ai_comb_p_4.current(0)
        window_ai_comb_p_4 = inv_canvas_1.create_window(0, 0, anchor="nw", width=180, height=30,window=ai_comb_p_4,tags=('aicombo8'))

        ai_entry_4=Entry(inv_canvas_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_4 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_4,tags=('aientry10'))

        ai_entry_4_1=Entry(inv_canvas_1,width=31,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_4_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_4_1,tags=('aientry13'))

        ai_entry_4_2=Entry(inv_canvas_1,width=15,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_4_2 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_4_2,tags=('aientry16'))

        ai_entry_4_3=Entry(inv_canvas_1,width=18,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_4_3 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_4_3,tags=('aientry19'))

        ai_entry_4_4=Entry(inv_canvas_1,width=16,justify=LEFT,background='#2f516f',foreground="white")
        window_ai_entry_4_4 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=ai_entry_4_4,tags=('aientry22'))

        ai_comb_P_4_2 = ttk.Combobox(inv_canvas_1, font=('arial 10'),foreground="white")
        ai_comb_P_4_2['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
        ai_comb_P_4_2.current(0)
        window_ai_comb_P_4_2 = inv_canvas_1.create_window(0, 0, anchor="nw", width=150, height=30,window=ai_comb_P_4_2,tags=('aicombo11'))

        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine16'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine17'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine18'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine19'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine20'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine21'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine22'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine23'))
        inv_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine24'))
        

        label_5 = Label(inv_canvas_1,width=10,height=1,text="Sub Total", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel23'))

        label_5 = Label(inv_canvas_1,width=12,height=1,text="Tax Amount", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel24'))

        label_5 = Label(inv_canvas_1,width=12,height=1,text="Grand Total", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel25'))

        label_5 = Label(inv_canvas_1,width=12,height=1,text="Amount Received", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel26'))

        label_5 = Label(inv_canvas_1,width=12,height=1,text="Balance Due", font=('arial 10'),background="#1b3857",fg="white") 
        window_label_5 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel27'))

        sub_entry_1=Entry(inv_canvas_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
        window_sub_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=sub_entry_1,tags=('aientry23'))

        tax_entry_1=Entry(inv_canvas_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
        window_tax_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=tax_entry_1,tags=('aientry24'))

        grand_entry_1=Entry(inv_canvas_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
        window_grand_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=grand_entry_1,tags=('aientry25'))

        amount_entry_1=Entry(inv_canvas_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
        window_amount_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=amount_entry_1,tags=('aientry26'))

        bal_entry_1=Entry(inv_canvas_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
        window_bal_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=bal_entry_1,tags=('aientry27'))
        

        ai_save_btn1=Button(inv_canvas_1,text='Save', width=15,height=2,foreground="white",background="#1b3857",font='arial 12')
        window_ai_save_btn1 = inv_canvas_1.create_window(0, 0, anchor="nw", window=ai_save_btn1,tags=('aibutton2'))

        def inv_back_1_():
            inv_frame_1.grid_forget()
            inv_frame.grid(row=0,column=0,sticky='nsew')

        bck_btn1=Button(inv_canvas_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=inv_back_1_)
        window_bck_btn1 = inv_canvas_1.create_window(0, 0, anchor="nw", window=bck_btn1,tags=('aibutton3'))

        label_2 = Label(inv_canvas_1,width=14,height=1,text="Invoice Date:", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel7'))

        label_2 = Label(inv_canvas_1,width=15,height=1,text="Due Date:", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = inv_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel28'))

        aid_entry_1=DateEntry(inv_canvas_1,width=40,justify=LEFT,foreground='white')
        window_aid_entry_1 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=aid_entry_1,tags=('aidate1'))

        aid_entry_2=DateEntry(inv_canvas_1,width=40,justify=LEFT,foreground='white')
        window_aid_entry_2 = inv_canvas_1.create_window(0, 0, anchor="nw", height=30, window=aid_entry_2,tags=('aidate2'))


    def edit_invoice(event):
        inv_frame.grid_forget()
        inv_frame_edit_1 = Frame(tab3_2)
        inv_frame_edit_1.grid(row=0,column=0,sticky='nsew')

        def inv_eresponsive_widgets2(event):
            try:
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget
                
                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/14 
                y2 = dheight/3.505

                dcanvas.coords("aipoly1",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )

                dcanvas.coords("ailabel1",dwidth/2.45,dheight/8.24)
                dcanvas.coords("aihline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                r2 = 25
                x11 = dwidth/63
                x21 = dwidth/1.021
                y11 = dheight/2.8
                y21 = dheight/0.36


                dcanvas.coords("aipoly2",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                dcanvas.coords("ailabel2",dwidth/2.45,dheight/2.34)
                dcanvas.coords("ailabel3",dwidth/22.80,dheight/1.90)
                dcanvas.coords("ailabel4",dwidth/20.00,dheight/1.65)
                dcanvas.coords("ailabel5",dwidth/20.00,dheight/1.37)
                dcanvas.coords("ailabel6",dwidth/3.34,dheight/1.37)
                dcanvas.coords("ailabel7",dwidth/21.66 ,dheight/1.12)
                dcanvas.coords("ailabel8",dwidth/3.34,dheight/1.12)
                dcanvas.coords("ailabel9",dwidth/19.10,dheight/0.947)
                dcanvas.coords("ailabel10",dwidth/19.40,dheight/0.717)
                dcanvas.coords("ailabel11",dwidth/16.50,dheight/0.638)
                dcanvas.coords("ailabel12",dwidth/8.40,dheight/0.638)
                dcanvas.coords("ailabel13",dwidth/3.34,dheight/0.638)
                dcanvas.coords("ailabel14",dwidth/2.28,dheight/0.638)
                dcanvas.coords("ailabel15",dwidth/1.73,dheight/0.638)
                dcanvas.coords("ailabel16",dwidth/1.52,dheight/0.638)
                dcanvas.coords("ailabel17",dwidth/1.325,dheight/0.638)
                dcanvas.coords("ailabel18",dwidth/1.165,dheight/0.638)
                dcanvas.coords("ailabel19",dwidth/16.50,dheight/0.604)
                dcanvas.coords("ailabel20",dwidth/16.50,dheight/0.562)
                dcanvas.coords("ailabel21",dwidth/16.50,dheight/0.526)
                dcanvas.coords("ailabel22",dwidth/16.50,dheight/0.496)
                dcanvas.coords("ailabel23",dwidth/1.53,dheight/0.45)
                dcanvas.coords("ailabel24",dwidth/1.54,dheight/0.435)
                dcanvas.coords("ailabel25",dwidth/1.54,dheight/0.42)
                dcanvas.coords("ailabel26",dwidth/1.54,dheight/0.406)
                dcanvas.coords("ailabel27",dwidth/1.54,dheight/0.392)
                dcanvas.coords("ailabel28",dwidth/1.72,dheight/1.12)

                dcanvas.coords("aientry1",dwidth/3.0,dheight/1.295)
                dcanvas.coords("aientry2",dwidth/18.00,dheight/0.91)
                dcanvas.coords("aientry3",dwidth/4.00,dheight/0.604)
                dcanvas.coords("aientry4",dwidth/2.51,dheight/0.604)
                dcanvas.coords("aientry5",dwidth/1.8,dheight/0.604)
                dcanvas.coords("aientry6",dwidth/1.565,dheight/0.604)
                dcanvas.coords("aientry7",dwidth/1.357,dheight/0.604)
                dcanvas.coords("aientry8",dwidth/4.00,dheight/0.562)
                dcanvas.coords("aientry9",dwidth/4.00,dheight/0.526)
                dcanvas.coords("aientry10",dwidth/4.00,dheight/0.496)
                dcanvas.coords("aientry11",dwidth/2.51,dheight/0.562)
                dcanvas.coords("aientry12",dwidth/2.51,dheight/0.526)
                dcanvas.coords("aientry13",dwidth/2.51,dheight/0.496)
                dcanvas.coords("aientry14",dwidth/1.8,dheight/0.562)
                dcanvas.coords("aientry15",dwidth/1.8,dheight/0.526)
                dcanvas.coords("aientry16",dwidth/1.8,dheight/0.496)
                dcanvas.coords("aientry17",dwidth/1.565,dheight/0.562)
                dcanvas.coords("aientry18",dwidth/1.565,dheight/0.526)
                dcanvas.coords("aientry19",dwidth/1.565,dheight/0.496)
                dcanvas.coords("aientry20",dwidth/1.357,dheight/0.562)
                dcanvas.coords("aientry21",dwidth/1.357,dheight/0.526)
                dcanvas.coords("aientry22",dwidth/1.357,dheight/0.496)
                dcanvas.coords("aientry23",dwidth/1.33,dheight/0.452)
                dcanvas.coords("aientry24",dwidth/1.33,dheight/0.4365)
                dcanvas.coords("aientry25",dwidth/1.33,dheight/0.4215)
                dcanvas.coords("aientry26",dwidth/1.33,dheight/0.407)
                dcanvas.coords("aientry27",dwidth/1.33,dheight/0.393)
                dcanvas.coords("aientry28",dwidth/18.00,dheight/1.295)

                dcanvas.coords("aicombo2",dwidth/3.00,dheight/1.074)
                dcanvas.coords("aicombo3",dwidth/18.00,dheight/0.695)
                dcanvas.coords("aicombo4",dwidth/10.10,dheight/0.604)
                dcanvas.coords("aicombo5",dwidth/1.21,dheight/0.604)
                dcanvas.coords("aicombo6",dwidth/10.10,dheight/0.562)
                dcanvas.coords("aicombo7",dwidth/10.10,dheight/0.526)
                dcanvas.coords("aicombo8",dwidth/10.10,dheight/0.496)
                dcanvas.coords("aicombo9",dwidth/1.21,dheight/0.562)
                dcanvas.coords("aicombo10",dwidth/1.21,dheight/0.526)
                dcanvas.coords("aicombo11",dwidth/1.21,dheight/0.496)

                dcanvas.coords("aibutton1",dwidth/4.74,dheight/1.295)
                dcanvas.coords("aibutton2",dwidth/1.28,dheight/0.377)
                dcanvas.coords("aibutton3",dwidth/23,dheight/3.415)

                #-------------------------------H Lines-----------------------------------#
                dcanvas.coords("ailine1",dwidth/21,dheight/0.645,dwidth/1.055,dheight/0.645)
                dcanvas.coords("ailine2",dwidth/21,dheight/0.617,dwidth/1.055,dheight/0.617)
                dcanvas.coords("ailine3",dwidth/21,dheight/0.576,dwidth/1.055,dheight/0.576)
                dcanvas.coords("ailine4",dwidth/21,dheight/0.536,dwidth/1.055,dheight/0.536)
                dcanvas.coords("ailine5",dwidth/21,dheight/0.506,dwidth/1.055,dheight/0.506)
                dcanvas.coords("ailine6",dwidth/21,dheight/0.476,dwidth/1.055,dheight/0.476)
                #-------------------------------V Lines-----------------------------------#
                dcanvas.coords("ailine7",dwidth/21,dheight/0.645,dwidth/21,dheight/0.476)
                dcanvas.coords("ailine8",dwidth/1.055,dheight/0.645,dwidth/1.055,dheight/0.476)
                dcanvas.coords("ailine9",dwidth/11,dheight/0.645,dwidth/11,dheight/0.476)
                dcanvas.coords("ailine10",dwidth/4.15,dheight/0.645,dwidth/4.15,dheight/0.476)
                dcanvas.coords("ailine11",dwidth/2.55,dheight/0.645,dwidth/2.55,dheight/0.476)
                dcanvas.coords("ailine12",dwidth/1.83,dheight/0.645,dwidth/1.83,dheight/0.476)
                dcanvas.coords("ailine13",dwidth/1.58,dheight/0.645,dwidth/1.58,dheight/0.476)
                dcanvas.coords("ailine14",dwidth/1.37,dheight/0.645,dwidth/1.37,dheight/0.476)
                dcanvas.coords("ailine15",dwidth/1.22,dheight/0.645,dwidth/1.22,dheight/0.476)

                #-------------------------------V Lines-----------------------------------#
                dcanvas.coords("ailine16",dwidth/1.58,dheight/0.455,dwidth/1.58,dheight/0.383)
                dcanvas.coords("ailine17",dwidth/1.348,dheight/0.455,dwidth/1.348,dheight/0.383)
                dcanvas.coords("ailine18",dwidth/1.084,dheight/0.455,dwidth/1.084,dheight/0.383)
                #-------------------------------H Lines-----------------------------------#
                dcanvas.coords("ailine19",dwidth/1.58,dheight/0.455,dwidth/1.084,dheight/0.455)
                dcanvas.coords("ailine20",dwidth/1.58,dheight/0.383,dwidth/1.084,dheight/0.383)
                dcanvas.coords("ailine21",dwidth/1.58,dheight/0.439,dwidth/1.084,dheight/0.439)
                dcanvas.coords("ailine22",dwidth/1.58,dheight/0.424,dwidth/1.084,dheight/0.424)
                dcanvas.coords("ailine23",dwidth/1.58,dheight/0.41,dwidth/1.084,dheight/0.41)
                dcanvas.coords("ailine24",dwidth/1.58,dheight/0.396,dwidth/1.084,dheight/0.396)
            except:
                pass

            try:
                dcanvas.coords("aidate1",dwidth/17.8,dheight/1.074)
                dcanvas.coords("aidate2",dwidth/1.65,dheight/1.074)
            except:
                pass


        inv_canvas_edit_1=Canvas(inv_frame_edit_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1800))

        inv_frame_edit_1.grid_columnconfigure(0,weight=1)
        inv_frame_edit_1.grid_rowconfigure(0,weight=1)
        
        vertibar=Scrollbar(inv_frame_edit_1, orient=VERTICAL)
        vertibar.grid(row=0,column=1,sticky='ns')
        vertibar.config(command=inv_canvas_edit_1.yview)

        inv_canvas_edit_1.bind("<Configure>", inv_eresponsive_widgets2)
        inv_canvas_edit_1.config(yscrollcommand=vertibar.set)
        inv_canvas_edit_1.grid(row=0,column=0,sticky='nsew')

        if inv_comb_1.get() == 'Edit':

            inv_canvas_edit_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("aipoly1"))

            
            label_1 = Label(inv_canvas_edit_1,width=10,height=1,text="INVOICE", font=('arial 20'),background="#1b3857",fg="white") 
            window_label_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=("ailabel1"))

            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("aihline"))

            inv_canvas_edit_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("aipoly2"))

            label_1 = Label(inv_canvas_edit_1,width=10,height=1,text="Fin sYs", font=('arial 20'),background="#1b3857",fg="white") 
            window_label_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_1, tags=("ailabel2"))

            label_2 = Label(inv_canvas_edit_1,width=15,height=1,text="Company name", font=('arial 16'),background="#1b3857",fg="skyblue") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ailabel3"))

            label_2 = Label(inv_canvas_edit_1,width=15,height=1,text="Company email-id", font=('arial 16'),background="#1b3857",fg="skyblue") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ailabel4"))

            label_2 = Label(inv_canvas_edit_1,width=15,height=1,text="Select Customer", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2, tags=("ailabel5"))


            eientry_1=Entry(inv_canvas_edit_1,width=42,justify=LEFT,background='#2f516f',foreground="white")
            window_eientry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=eientry_1,tags=('aientry28'))


            label_2 = Label(inv_canvas_edit_1,width=15,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel6'))

            eaientry_1=Entry(inv_canvas_edit_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_eaientry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30,window=eaientry_1,tags=('aientry1'))


            label_2 = Label(inv_canvas_edit_1,width=15,height=1,text="Terms", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel8'))

            ecomb_t_2 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
            ecomb_t_2['values'] = ("Due on Receipt","NET 15","NET 30","NET 60","Add New Term",)
            ecomb_t_2.current(0)
            window_ecomb_t_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=251, height=30,window=ecomb_t_2,tags=('aicombo2'))


            label_2 = Label(inv_canvas_edit_1,width=6,height=1,text="Bill To:", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel9'))

            
            eai_b_entry_1=Entry(inv_canvas_edit_1,width=42,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_b_entry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=150, window=eai_b_entry_1,tags=('aientry2'))

            label_2 = Label(inv_canvas_edit_1,width=12,height=1,text="Place of supply", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel10'))

            eai_p_comb_2 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
            eai_p_comb_2['values'] = ("Kerala","Andaman and Nicobar Islands","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra and Nagar Haveli","Daman and Diu","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Ladakh","Lakshadweep","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Other Territory",)
            eai_p_comb_2.current(0)
            window_eai_p_comb_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=251, height=30,window=eai_p_comb_2,tags=('aicombo3'))


            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine1'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine2'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine3'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine4'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine5'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine6'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine7'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine8'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine9'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine10'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine11'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine12'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine13'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine14'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine15'))


            label_2 = Label(inv_canvas_edit_1,width=2,height=1,text="#", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel11'))

            label_3 = Label(inv_canvas_edit_1,width=15,height=1,text="PRODUCT/SERVICE", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_3 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_3,tags=('ailabel12'))

            label_4 = Label(inv_canvas_edit_1,width=4,height=1,text="HSN", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel13'))

            label_4 = Label(inv_canvas_edit_1,width=11,height=1,text="DESCRIPTION", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel14'))

            label_4 = Label(inv_canvas_edit_1,width=4,height=1,text="QTY", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel15'))

            label_4 = Label(inv_canvas_edit_1,width=8,height=1,text="PRICE", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel16'))

            label_4 = Label(inv_canvas_edit_1,width=6,height=1,text="TOTAL", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel17'))

            label_4 = Label(inv_canvas_edit_1,width=7,height=1,text="TAX (%)", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_4,tags=('ailabel18'))

            label_2 = Label(inv_canvas_edit_1,width=2,height=1,text="1", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_edit_1.create_window(90, 1020, anchor="nw", window=label_2,tags=('ailabel19'))

            eai_comb_p_1 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
            eai_comb_p_1['values'] = ("Select Product",)
            eai_comb_p_1.current(0)
            window_eai_comb_p_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=180, height=30,window=eai_comb_p_1,tags=('aicombo4'))

            eai_entry_p_1=Entry(inv_canvas_edit_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_p_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_p_1,tags=('aientry3'))

            eai_entry_p_1_2=Entry(inv_canvas_edit_1,width=31,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_p_1_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_p_1_2,tags=('aientry4'))

            eai_entry_p_1_3=Entry(inv_canvas_edit_1,width=15,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_p_1_3 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_p_1_3,tags=('aientry5'))

            eai_entry_p_1_4=Entry(inv_canvas_edit_1,width=18,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_p_1_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_p_1_4,tags=('aientry6'))

            eai_entry_p_1_5=Entry(inv_canvas_edit_1,width=16,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_p_1_5 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_p_1_5,tags=('aientry7'))

            eai_comb_p_1_2 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
            eai_comb_p_1_2['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
            eai_comb_p_1_2.current(0)
            window_eai_comb_p_1_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=150, height=30,window=eai_comb_p_1_2,tags=('aicombo5'))


            label_2 = Label(inv_canvas_edit_1,width=2,height=1,text="2", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel20'))

            eai_comb_P_2 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
            eai_comb_P_2['values'] = ("Select Product",)
            eai_comb_P_2.current(0)
            window_eai_comb_P_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=180, height=30,window=eai_comb_P_2,tags=('aicombo6'))

            eai_entry_p_2=Entry(inv_canvas_edit_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_p_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_p_2,tags=('aientry8'))

            eai_entry_p_2_1=Entry(inv_canvas_edit_1,width=31,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_p_2_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_p_2_1,tags=('aientry11'))

            eai_entry_2_2=Entry(inv_canvas_edit_1,width=15,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_2_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_2_2,tags=('aientry14'))

            eai_entry_2_3=Entry(inv_canvas_edit_1,width=18,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_2_3 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_2_3,tags=('aientry17'))

            eai_entry_2_4=Entry(inv_canvas_edit_1,width=16,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_2_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_2_4,tags=('aientry20'))

            eai_comb_P_2_2 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
            eai_comb_P_2_2['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
            eai_comb_P_2_2.current(0)
            window_eai_comb_P_2_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=150, height=30,window=eai_comb_P_2_2,tags=('aicombo9'))


            label_2 = Label(inv_canvas_edit_1,width=2,height=1,text="3", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel21'))

            eai_comb_p_3 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
            eai_comb_p_3['values'] = ("Select Product",)
            eai_comb_p_3.current(0)
            window_eai_comb_p_3 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=180, height=30,window=eai_comb_p_3,tags=('aicombo7'))

            eai_entry_3=Entry(inv_canvas_edit_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_3 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_3,tags=('aientry9'))

            eai_entry_3_1=Entry(inv_canvas_edit_1,width=31,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_3_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_3_1,tags=('aientry12'))

            eai_entry_3_2=Entry(inv_canvas_edit_1,width=15,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_3_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_3_2,tags=('aientry15'))

            eai_entry_3_3=Entry(inv_canvas_edit_1,width=18,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_3_3 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_3_3,tags=('aientry18'))

            eai_entry_3_4=Entry(inv_canvas_edit_1,width=16,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_3_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_3_4,tags=('aientry21'))

            eai_comb_P_3_2 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
            eai_comb_P_3_2['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
            eai_comb_P_3_2.current(0)
            window_eai_comb_P_3_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=150, height=30,window=eai_comb_P_3_2,tags=('aicombo10'))

            label_2 = Label(inv_canvas_edit_1,width=2,height=1,text="4", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel22'))

            eai_comb_p_4 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
            eai_comb_p_4['values'] = ("Select Product",)
            eai_comb_p_4.current(0)
            window_eai_comb_p_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=180, height=30,window=eai_comb_p_4,tags=('aicombo8'))

            eai_entry_4=Entry(inv_canvas_edit_1,width=30,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_4,tags=('aientry10'))

            eai_entry_4_1=Entry(inv_canvas_edit_1,width=31,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_4_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_4_1,tags=('aientry13'))

            eai_entry_4_2=Entry(inv_canvas_edit_1,width=15,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_4_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_4_2,tags=('aientry16'))

            eai_entry_4_3=Entry(inv_canvas_edit_1,width=18,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_4_3 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_4_3,tags=('aientry19'))

            eai_entry_4_4=Entry(inv_canvas_edit_1,width=16,justify=LEFT,background='#2f516f',foreground="white")
            window_eai_entry_4_4 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eai_entry_4_4,tags=('aientry22'))

            eai_comb_P_4_2 = ttk.Combobox(inv_canvas_edit_1, font=('arial 10'),foreground="white")
            eai_comb_P_4_2['values'] = ("Choose","28.0%\n GST(28%)","18.0%\n GST(18%)","12.0%\n GST(12%)","06.0%\n GST(06%)","05.0%\n GST(05%)","03.0%\n GST(03%)","0.25%\n GST(0.25%)","0.0%\n GST(0%)","Exempt GST(0%)","Out of Scope(0%)",)
            eai_comb_P_4_2.current(0)
            window_eai_comb_P_4_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", width=150, height=30,window=eai_comb_P_4_2,tags=('aicombo11'))

            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine16'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine17'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine18'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine19'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine20'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine21'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine22'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine23'))
            inv_canvas_edit_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('ailine24'))
            

            label_5 = Label(inv_canvas_edit_1,width=10,height=1,text="Sub Total", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_5 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel23'))

            label_5 = Label(inv_canvas_edit_1,width=12,height=1,text="Tax Amount", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_5 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel24'))

            label_5 = Label(inv_canvas_edit_1,width=12,height=1,text="Grand Total", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_5 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel25'))

            label_5 = Label(inv_canvas_edit_1,width=12,height=1,text="Amount Received", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_5 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel26'))

            label_5 = Label(inv_canvas_edit_1,width=12,height=1,text="Balance Due", font=('arial 10'),background="#1b3857",fg="white") 
            window_label_5 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_5,tags=('ailabel27'))

            esub_entry_1=Entry(inv_canvas_edit_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
            window_esub_entry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=esub_entry_1,tags=('aientry23'))

            etax_entry_1=Entry(inv_canvas_edit_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
            window_etax_entry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=etax_entry_1,tags=('aientry24'))

            egrand_entry_1=Entry(inv_canvas_edit_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
            window_egrand_entry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=egrand_entry_1,tags=('aientry25'))

            eamount_entry_1=Entry(inv_canvas_edit_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
            window_eamount_entry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eamount_entry_1,tags=('aientry26'))

            ebal_entry_1=Entry(inv_canvas_edit_1,width=36,justify=LEFT,background='#2f516f',foreground="white")
            window_ebal_entry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=ebal_entry_1,tags=('aientry27'))
            

            eai_save_btn1=Button(inv_canvas_edit_1,text='Save', width=15,height=2,foreground="white",background="#1b3857",font='arial 12')
            window_eai_save_btn1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=eai_save_btn1,tags=('aibutton2'))

            def einv_back_1_():
                inv_frame_edit_1.grid_forget()
                inv_frame.grid(row=0,column=0,sticky='nsew')

            eibck_btn1=Button(inv_canvas_edit_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=einv_back_1_)
            window_eibck_btn1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=eibck_btn1,tags=('aibutton3'))

            label_2 = Label(inv_canvas_edit_1,width=14,height=1,text="Invoice Date:", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel7'))

            label_2 = Label(inv_canvas_edit_1,width=15,height=1,text="Due Date:", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", window=label_2,tags=('ailabel28'))

            eaid_entry_1=DateEntry(inv_canvas_edit_1,width=40,justify=LEFT,foreground='white')
            window_eaid_entry_1 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eaid_entry_1,tags=('aidate1'))

            eaid_entry_2=DateEntry(inv_canvas_edit_1,width=40,justify=LEFT,foreground='white')
            window_eaid_entry_2 = inv_canvas_edit_1.create_window(0, 0, anchor="nw", height=30, window=eaid_entry_2,tags=('aidate2'))
        else:
            pass
            
        
    # Define the style for combobox widget
    # styl= ttk.Style()
    # styl.theme_use('clam')
    # styl.configure("TCombobox", fieldbackground= "#2f516f", background= "#2f516f")

    inv_comb_1 = ttk.Combobox(inv_canvas,)
    inv_comb_1['values'] = ("Actions","Edit","Delete")
    #inv_comb_1.current(0)
    inv_comb_1.bind('<<ComboboxSelected>>',edit_invoice)
    window_inv_comb_1 = inv_canvas.create_window(0, 0, anchor="nw", width=110,height=30,window=inv_comb_1,tags=('icombo1'))
        

    btn1=Button(inv_canvas,text='Add Invoices', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_invoice)
    window_btn1 = inv_canvas.create_window(0, 0, anchor="nw", window=btn1,tags=('ibutton1'))

    #-------------------------------Customers-----------------------------#
    tab3_3.grid_columnconfigure(0,weight=1)
    tab3_3.grid_rowconfigure(0,weight=1)

    cus_frame = Frame(tab3_3)
    cus_frame.grid(row=0,column=0,sticky='nsew')

    def cus_responsive_widgets(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget
        dcanvas.coords("cline1", dwidth/22.00, dheight/1.8, dwidth/1.060, dheight/1.8)
        dcanvas.coords("cline2", dwidth/22.00, dheight/1.8, dwidth/22.00, dheight/1.35)
        dcanvas.coords("cline3", dwidth/22.00, dheight/1.35, dwidth/1.060, dheight/1.35)
        dcanvas.coords("cline4", dwidth/1.060, dheight/1.8, dwidth/1.060, dheight/1.35)
        dcanvas.coords("cline5", dwidth/22.00, dheight/1.575, dwidth/1.060, dheight/1.575)
        dcanvas.coords("cline6", dwidth/5.00, dheight/1.8, dwidth/5.00, dheight/1.35)
        dcanvas.coords("cline7", dwidth/2.9, dheight/1.8, dwidth/2.9, dheight/1.35)
        dcanvas.coords("cline8", dwidth/2.2, dheight/1.8, dwidth/2.2, dheight/1.35)
        dcanvas.coords("cline9", dwidth/1.75, dheight/1.8, dwidth/1.75, dheight/1.35)
        dcanvas.coords("cline10", dwidth/1.37, dheight/1.8, dwidth/1.37, dheight/1.35)
        dcanvas.coords("cline11", dwidth/1.20, dheight/1.8, dwidth/1.20, dheight/1.35)
        

        r1 = 25
        x1 = dwidth/63
        x2 = dwidth/1.021
        y1 = dheight/14 
        y2 = dheight/3.505

        dcanvas.coords("cpoly1",x1 + r1,y1,
        x1 + r1,y1,
        x2 - r1,y1,
        x2 - r1,y1,     
        x2,y1,     
        #--------------------
        x2,y1 + r1,     
        x2,y1 + r1,     
        x2,y2 - r1,     
        x2,y2 - r1,     
        x2,y2,
        #--------------------
        x2 - r1,y2,     
        x2 - r1,y2,     
        x1 + r1,y2,
        x1 + r1,y2,
        x1,y2,
        #--------------------
        x1,y2 - r1,
        x1,y2 - r1,
        x1,y1 + r1,
        x1,y1 + r1,
        x1,y1,
        )

        dcanvas.coords("chline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
        dcanvas.coords("clabel1",dwidth/2.5,dheight/8.00)

        r2 = 25
        x11 = dwidth/63
        x21 = dwidth/1.021
        y11 = dheight/2.8
        y21 = dheight/1.168


        dcanvas.coords("cpoly2",x11 + r2,y11,
        x11 + r2,y11,
        x21 - r2,y11,
        x21 - r2,y11,     
        x21,y11,     
        #--------------------
        x21,y11 + r2,     
        x21,y11 + r2,     
        x21,y21 - r2,     
        x21,y21 - r2,     
        x21,y21,
        #--------------------
        x21 - r2,y21,     
        x21 - r2,y21,     
        x11 + r2,y21,
        x11 + r2,y21,
        x11,y21,
        #--------------------
        x11,y21 - r2,
        x11,y21 - r2,
        x11,y11 + r2,
        x11,y11 + r2,
        x11,y11,
        )

        dcanvas.coords("clabel2",dwidth/11.5,dheight/1.74)
        dcanvas.coords("clabel3",dwidth/4.2,dheight/1.74)
        dcanvas.coords("clabel4",dwidth/2.75,dheight/1.74)
        dcanvas.coords("clabel5",dwidth/2.05,dheight/1.74)
        dcanvas.coords("clabel6",dwidth/1.60,dheight/1.74)
        dcanvas.coords("clabel7",dwidth/1.34,dheight/1.74)
        dcanvas.coords("clabel8",dwidth/1.17,dheight/1.74)
        dcanvas.coords("cbutton1",dwidth/1.28,dheight/2.4)
        dcanvas.coords("ccombo1",dwidth/1.179,dheight/1.52)

    cus_canvas=Canvas(cus_frame, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,1000))

    cus_frame.grid_rowconfigure(0,weight=1)
    cus_frame.grid_columnconfigure(0,weight=1)

    vertibar=Scrollbar(cus_frame, orient=VERTICAL)
    vertibar.grid(row=0,column=1,sticky='ns')
    vertibar.config(command=cus_canvas.yview)
    cus_canvas.bind("<Configure>", cus_responsive_widgets)
    cus_canvas.config(yscrollcommand=vertibar.set)
    cus_canvas.grid(row=0,column=0,sticky='nsew')

    cus_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("cpoly1"))

    label_1 = Label(cus_canvas,width=12,height=1,text="CUSTOMERS", font=('arial 25'),background="#1b3857",fg="white") 
    window_label_1 = cus_canvas.create_window(0, 0, anchor="nw", window=label_1, tags=("clabel1"))

    cus_canvas.create_line(0,0,0,0,fill='gray',width=1,tags=("chline"))

    
    cus_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("cpoly2"))


    cus_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("cline1"))
    cus_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("cline2"))
    cus_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("cline3"))
    cus_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("cline4"))
    cus_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("cline5"))
    cus_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("cline6"))
    cus_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("cline7"))
    cus_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("cline8"))
    cus_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("cline9"))
    cus_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("cline10"))
    cus_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=("cline11"))
    
    

    label_2 = Label(cus_canvas,width=10,height=1,text="CUSTOMER", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_2 = cus_canvas.create_window(0, 0, anchor="nw", window=label_2, tags=("clabel2"))

    label_3 = Label(cus_canvas,width=11,height=1,text="GST TYPE", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_3 = cus_canvas.create_window(0, 0, anchor="nw", window=label_3, tags=("clabel3"))

    label_4 = Label(cus_canvas,width=11,height=1,text="GSTIN", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = cus_canvas.create_window(0, 0, anchor="nw", window=label_4, tags=("clabel4"))

    label_4 = Label(cus_canvas,width=8,height=1,text="PAN NO", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = cus_canvas.create_window(0, 0, anchor="nw", window=label_4, tags=("clabel5"))

    label_4 = Label(cus_canvas,width=8,height=1,text="EMAIL ID", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = cus_canvas.create_window(0, 0, anchor="nw", window=label_4, tags=("clabel6"))

    label_4 = Label(cus_canvas,width=11,height=1,text="MOBILE NO", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = cus_canvas.create_window(0, 0, anchor="nw", window=label_4, tags=("clabel7"))

    label_4 = Label(cus_canvas,width=11,height=1,text="ACTION", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = cus_canvas.create_window(0, 0, anchor="nw", window=label_4, tags=("clabel8"))


    def add_customer():
        cus_frame.grid_forget()
        cus_frame_1 = Frame(tab3_3)
        cus_frame_1.grid(row=0,column=0,sticky='nsew')

        def cus_responsive_widgets2(event):
            dwidth = event.width
            dheight = event.height
            dcanvas = event.widget
            
            r1 = 25
            x1 = dwidth/63
            x2 = dwidth/1.021
            y1 = dheight/14 
            y2 = dheight/3.505

            dcanvas.coords("acpoly1",x1 + r1,y1,
            x1 + r1,y1,
            x2 - r1,y1,
            x2 - r1,y1,     
            x2,y1,     
            #--------------------
            x2,y1 + r1,     
            x2,y1 + r1,     
            x2,y2 - r1,     
            x2,y2 - r1,     
            x2,y2,
            #--------------------
            x2 - r1,y2,     
            x2 - r1,y2,     
            x1 + r1,y2,
            x1 + r1,y2,
            x1,y2,
            #--------------------
            x1,y2 - r1,
            x1,y2 - r1,
            x1,y1 + r1,
            x1,y1 + r1,
            x1,y1,
            )

            dcanvas.coords("aclabel1",dwidth/2.5,dheight/8.24)
            dcanvas.coords("achline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

            r2 = 25
            x11 = dwidth/63
            x21 = dwidth/1.021
            y11 = dheight/2.8
            y21 = dheight/0.45


            dcanvas.coords("acpoly2",x11 + r2,y11,
            x11 + r2,y11,
            x21 - r2,y11,
            x21 - r2,y11,     
            x21,y11,     
            #--------------------
            x21,y11 + r2,     
            x21,y11 + r2,     
            x21,y21 - r2,     
            x21,y21 - r2,     
            x21,y21,
            #--------------------
            x21 - r2,y21,     
            x21 - r2,y21,     
            x11 + r2,y21,
            x11 + r2,y21,
            x11,y21,
            #--------------------
            x11,y21 - r2,
            x11,y21 - r2,
            x11,y11 + r2,
            x11,y11 + r2,
            x11,y11,
            )

            dcanvas.coords("aclabel2",dwidth/17.0,dheight/2.35)
            dcanvas.coords("achline1",dwidth/21,dheight/1.95,dwidth/1.055,dheight/1.95)
            dcanvas.coords("aclabel3",dwidth/20.2,dheight/1.69)
            dcanvas.coords("aclabel4",dwidth/3.35,dheight/1.69)
            dcanvas.coords("aclabel5",dwidth/1.8,dheight/1.69)
            dcanvas.coords("aclabel6",dwidth/20.2,dheight/1.32)
            dcanvas.coords("aclabel7",dwidth/3.375,dheight/1.32)
            dcanvas.coords("aclabel8",dwidth/20.2,dheight/1.088)
            dcanvas.coords("aclabel9",dwidth/3.48,dheight/1.088)
            dcanvas.coords("aclabel10",dwidth/1.82,dheight/1.088)
            dcanvas.coords("aclabel11",dwidth/18.7,dheight/0.92)
            dcanvas.coords("aclabel12",dwidth/3.40,dheight/0.92)
            dcanvas.coords("aclabel13",dwidth/1.83,dheight/0.92)
            dcanvas.coords("aclabel14",dwidth/55.5,dheight/0.79)
            dcanvas.coords("aclabel15",dwidth/2.09,dheight/0.79)
            dcanvas.coords("aclabel16",dwidth/19.5,dheight/0.74)
            dcanvas.coords("aclabel17",dwidth/1.97,dheight/0.74)
            dcanvas.coords("aclabel18",dwidth/19.49,dheight/0.645)
            dcanvas.coords("aclabel19",dwidth/3.40,dheight/0.645)
            dcanvas.coords("aclabel20",dwidth/2.0,dheight/0.645)
            dcanvas.coords("aclabel21",dwidth/1.33,dheight/0.645)
            dcanvas.coords("aclabel22",dwidth/21.0,dheight/0.58)
            dcanvas.coords("aclabel23",dwidth/3.42,dheight/0.58)
            dcanvas.coords("aclabel24",dwidth/2.0,dheight/0.58)
            dcanvas.coords("aclabel25",dwidth/1.34,dheight/0.58)

            dcanvas.coords("accombo1",dwidth/18.5,dheight/1.55)
            dcanvas.coords("accombo2",dwidth/18.5,dheight/1.027)

            dcanvas.coords("acentry1",dwidth/3.30,dheight/1.55)
            dcanvas.coords("acentry2",dwidth/1.785,dheight/1.55)
            dcanvas.coords("acentry3",dwidth/18.5,dheight/1.24)
            dcanvas.coords("acentry4",dwidth/3.30,dheight/1.24)
            dcanvas.coords("acentry5",dwidth/3.30,dheight/1.027)
            dcanvas.coords("acentry6",dwidth/1.785,dheight/1.027)
            dcanvas.coords("acentry7",dwidth/18.5,dheight/0.88)
            dcanvas.coords("acentry8",dwidth/3.30,dheight/0.88)
            dcanvas.coords("acentry9",dwidth/1.785,dheight/0.88)
            dcanvas.coords("acentry10",dwidth/18.5,dheight/0.715)
            dcanvas.coords("acentry11",dwidth/1.97,dheight/0.715)
            dcanvas.coords("acentry12",dwidth/18.5,dheight/0.625)
            dcanvas.coords("acentry13",dwidth/3.40,dheight/0.625)
            dcanvas.coords("acentry14",dwidth/1.98,dheight/0.625)
            dcanvas.coords("acentry15",dwidth/1.33,dheight/0.625)
            dcanvas.coords("acentry16",dwidth/19.51,dheight/0.565)
            dcanvas.coords("acentry17",dwidth/3.40,dheight/0.565)
            dcanvas.coords("acentry18",dwidth/1.98,dheight/0.565)
            dcanvas.coords("acentry19",dwidth/1.33,dheight/0.565)

            dcanvas.coords("accheck1",dwidth/1.55,dheight/0.79)
            dcanvas.coords("accheck2",dwidth/19.0,dheight/0.546)

            dcanvas.coords("acbutton1",dwidth/2.5,dheight/0.5)
            dcanvas.coords("acbutton3",dwidth/23,dheight/3.415)


        cus_canvas_1=Canvas(cus_frame_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1600))

        cus_frame_1.grid_columnconfigure(0,weight=1)
        cus_frame_1.grid_rowconfigure(0,weight=1)

        
        vertibar=Scrollbar(cus_frame_1, orient=VERTICAL)
        vertibar.grid(row=0,column=1,sticky='ns')
        vertibar.config(command=cus_canvas_1.yview)

        cus_canvas_1.bind("<Configure>", cus_responsive_widgets2)
        cus_canvas_1.config(yscrollcommand=vertibar.set)
        cus_canvas_1.grid(row=0,column=0,sticky='nsew')
        

        cus_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly1"))

        label_1 = Label(cus_canvas_1,width=15,height=1,text="ADD CUSTOMER", font=('arial 20'),background="#1b3857",fg="white") 
        window_label_1 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel1"))

        cus_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline"))

        cus_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly2"))

        label_1 = Label(cus_canvas_1,width=20,height=1,text="Customer Information", font=('arial 20'),background="#1b3857",fg="white") 
        window_label_1 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel2"))

        cus_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline1"))

        label_2 = Label(cus_canvas_1,width=5,height=1,text="Title", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel3"))

        comb_cus_1 = ttk.Combobox(cus_canvas_1, font=('arial 10'),foreground="white")
        comb_cus_1['values'] = ("Mr","Mrs","Miss","Ms",)
        comb_cus_1.current(0)
        window_comb_cus_1 = cus_canvas_1.create_window(0, 0, anchor="nw", width=245, height=30,window=comb_cus_1, tags=("accombo1"))

        label_2 = Label(cus_canvas_1,width=10,height=1,text="First name", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel4"))

        entry_cus_1=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_1 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_1, tags=("acentry1"))

        label_2 = Label(cus_canvas_1,width=10,height=1,text="Last name", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel5"))

        entry_cus_2=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_2 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_2, tags=("acentry2"))

        label_2 = Label(cus_canvas_1,width=10,height=1,text="Company", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel6"))

        entry_cus_3=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_3 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_3, tags=("acentry3"))

        label_2 = Label(cus_canvas_1,width=10,height=1,text="Location", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel7"))

        cus_4=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_cus_4 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=cus_4, tags=("acentry4"))

        label_2 = Label(cus_canvas_1,width=10,height=1,text="GST type", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel8"))

        comb_cus_2 = ttk.Combobox(cus_canvas_1, font=('arial 10'),foreground="white")
        comb_cus_2['values'] = ("Choose...","GST registered Regular","GST registered-Composition","GST unregistered","Consumer","Overseas","SEZ","Deemed exports-EOU's STP's EHTP's etc",)
        comb_cus_2.current(0)
        window_comb_cus_2 = cus_canvas_1.create_window(0, 0, anchor="nw", width=245, height=30,window=comb_cus_2, tags=("accombo2"))

        label_2 = Label(cus_canvas_1,width=10,height=1,text="GSTIN", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel9"))

        cus_entry_str_1 = StringVar()
        entry_cus_5=Entry(cus_canvas_1,width=34,justify=LEFT,background='#2f516f',foreground="white",font=('arial 10'),textvariable=cus_entry_str_1)
        cus_entry_str_1.set(' 29APPCK7465F1Z1')
        window_entry_cus_5 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_5, tags=("acentry5"))

        label_2 = Label(cus_canvas_1,width=10,height=1,text="PAN NO", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel10"))

        cus_entry_str_2 = StringVar()
        entry_cus_6=Entry(cus_canvas_1,width=34,justify=LEFT,background='#2f516f',foreground="white",font=('arial 10'),textvariable=cus_entry_str_2)
        cus_entry_str_2.set(' APPCK7465F')
        window_entry_cus_6 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_6, tags=("acentry6"))

        label_2 = Label(cus_canvas_1,width=5,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel11"))

        entry_cus_7=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_7 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_7, tags=("acentry7"))

        label_2 = Label(cus_canvas_1,width=10,height=1,text="Website", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel12"))

        entry_cus_8=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_8 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_8, tags=("acentry8"))

        label_2 = Label(cus_canvas_1,width=10,height=1,text="Mobile", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel13"))

        entry_cus_9=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_9 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_9, tags=("acentry9"))

        label_1 = Label(cus_canvas_1,width=20,height=1,text="Billing Address", font=('arial 16'),background="#1b3857",fg="white") 
        window_label_1 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel14"))

        label_2 = Label(cus_canvas_1,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel16"))

        entry_cus_10=Entry(cus_canvas_1,width=95,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_10 = cus_canvas_1.create_window(0, 0, anchor="nw", height=60,window=entry_cus_10, tags=("acentry10"))

        label_1 = Label(cus_canvas_1,width=20,height=1,text="Shipping Address", font=('arial 16'),background="#1b3857",fg="white") 
        window_label_1 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel15"))

        chk_str = StringVar()
        chkbtn1 = Checkbutton(cus_canvas_1, text = "Same As Billing Address", variable = chk_str, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f")
        chkbtn1.select()
        window_chkbtn_1 = cus_canvas_1.create_window(0, 0, anchor="nw", window=chkbtn1, tags=("accheck1"))

        label_2 = Label(cus_canvas_1,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel17"))

        entry_cus_11=Entry(cus_canvas_1,width=95,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_11 = cus_canvas_1.create_window(0, 0, anchor="nw", height=60,window=entry_cus_11, tags=("acentry11"))

        label_2 = Label(cus_canvas_1,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel18"))

        entry_cus_12=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_12 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_12, tags=("acentry12"))
        
        label_2 = Label(cus_canvas_1,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel19"))

        entry_cus_13=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_13 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_13, tags=("acentry13"))

        label_2 = Label(cus_canvas_1,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel20"))

        entry_cus_14=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_14 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_14, tags=("acentry14"))

        label_2 = Label(cus_canvas_1,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel21"))

        entry_cus_15=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_15 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_15, tags=("acentry15"))

        label_2 = Label(cus_canvas_1,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel22"))

        entry_cus_12=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_12 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_12, tags=("acentry16"))
        
        label_2 = Label(cus_canvas_1,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel23"))

        entry_cus_13=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_13 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_13, tags=("acentry17"))

        label_2 = Label(cus_canvas_1,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel24"))

        entry_cus_14=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_14 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_14, tags=("acentry18"))

        label_2 = Label(cus_canvas_1,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
        window_label_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel25"))

        entry_cus_15=Entry(cus_canvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
        window_entry_cus_15 = cus_canvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_cus_15, tags=("acentry19"))

        chk_str_1 = StringVar()
        chkbtn2 = Checkbutton(cus_canvas_1, text = "Agree to terms and conditions", variable = chk_str_1, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f")
        chkbtn2.select()
        window_chkbtn_2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=chkbtn2,tags=("accheck2"))

        def ac_back_1_():
            cus_frame_1.grid_forget()
            cus_frame.grid(row=0,column=0,sticky='nsew')

        ac_bck_btn1=Button(cus_canvas_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=ac_back_1_)
        window_ac_bck_btn1 = cus_canvas_1.create_window(0, 0, anchor="nw", window=ac_bck_btn1,tags=('acbutton3'))

        cus_btn2=Button(cus_canvas_1,text='Submit Form', width=25,height=2,foreground="white",background="#1b3857",font='arial 12')
        window_cus_btn2 = cus_canvas_1.create_window(0, 0, anchor="nw", window=cus_btn2,tags=("acbutton1"))

    btn1=Button(cus_canvas,text='Add Customer', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_customer)
    window_btn1 = cus_canvas.create_window(0, 0, anchor="nw", window=btn1, tags=("cbutton1"))

    def edit_customer(event):
        cus_frame.grid_forget()
        cus_eframe_1 = Frame(tab3_3)
        cus_eframe_1.grid(row=0,column=0,sticky='nsew')

        def ecus_responsive_widgets2(event):
            dwidth = event.width
            dheight = event.height
            dcanvas = event.widget
            
            r1 = 25
            x1 = dwidth/63
            x2 = dwidth/1.021
            y1 = dheight/14 
            y2 = dheight/3.505

            dcanvas.coords("acpoly1",x1 + r1,y1,
            x1 + r1,y1,
            x2 - r1,y1,
            x2 - r1,y1,     
            x2,y1,     
            #--------------------
            x2,y1 + r1,     
            x2,y1 + r1,     
            x2,y2 - r1,     
            x2,y2 - r1,     
            x2,y2,
            #--------------------
            x2 - r1,y2,     
            x2 - r1,y2,     
            x1 + r1,y2,
            x1 + r1,y2,
            x1,y2,
            #--------------------
            x1,y2 - r1,
            x1,y2 - r1,
            x1,y1 + r1,
            x1,y1 + r1,
            x1,y1,
            )

            dcanvas.coords("aclabel1",dwidth/2.5,dheight/8.24)
            dcanvas.coords("achline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

            r2 = 25
            x11 = dwidth/63
            x21 = dwidth/1.021
            y11 = dheight/2.8
            y21 = dheight/0.45


            dcanvas.coords("acpoly2",x11 + r2,y11,
            x11 + r2,y11,
            x21 - r2,y11,
            x21 - r2,y11,     
            x21,y11,     
            #--------------------
            x21,y11 + r2,     
            x21,y11 + r2,     
            x21,y21 - r2,     
            x21,y21 - r2,     
            x21,y21,
            #--------------------
            x21 - r2,y21,     
            x21 - r2,y21,     
            x11 + r2,y21,
            x11 + r2,y21,
            x11,y21,
            #--------------------
            x11,y21 - r2,
            x11,y21 - r2,
            x11,y11 + r2,
            x11,y11 + r2,
            x11,y11,
            )

            dcanvas.coords("aclabel2",dwidth/17.0,dheight/2.35)
            dcanvas.coords("achline1",dwidth/21,dheight/1.95,dwidth/1.055,dheight/1.95)
            dcanvas.coords("aclabel3",dwidth/20.2,dheight/1.69)
            dcanvas.coords("aclabel4",dwidth/3.35,dheight/1.69)
            dcanvas.coords("aclabel5",dwidth/1.8,dheight/1.69)
            dcanvas.coords("aclabel6",dwidth/20.2,dheight/1.32)
            dcanvas.coords("aclabel7",dwidth/3.375,dheight/1.32)
            dcanvas.coords("aclabel8",dwidth/20.2,dheight/1.088)
            dcanvas.coords("aclabel9",dwidth/3.48,dheight/1.088)
            dcanvas.coords("aclabel10",dwidth/1.82,dheight/1.088)
            dcanvas.coords("aclabel11",dwidth/18.7,dheight/0.92)
            dcanvas.coords("aclabel12",dwidth/3.40,dheight/0.92)
            dcanvas.coords("aclabel13",dwidth/1.83,dheight/0.92)
            dcanvas.coords("aclabel14",dwidth/55.5,dheight/0.79)
            dcanvas.coords("aclabel15",dwidth/2.09,dheight/0.79)
            dcanvas.coords("aclabel16",dwidth/19.5,dheight/0.74)
            dcanvas.coords("aclabel17",dwidth/1.97,dheight/0.74)
            dcanvas.coords("aclabel18",dwidth/19.49,dheight/0.645)
            dcanvas.coords("aclabel19",dwidth/3.40,dheight/0.645)
            dcanvas.coords("aclabel20",dwidth/2.0,dheight/0.645)
            dcanvas.coords("aclabel21",dwidth/1.33,dheight/0.645)
            dcanvas.coords("aclabel22",dwidth/21.0,dheight/0.58)
            dcanvas.coords("aclabel23",dwidth/3.42,dheight/0.58)
            dcanvas.coords("aclabel24",dwidth/2.0,dheight/0.58)
            dcanvas.coords("aclabel25",dwidth/1.34,dheight/0.58)

            dcanvas.coords("accombo1",dwidth/18.5,dheight/1.55)
            dcanvas.coords("accombo2",dwidth/18.5,dheight/1.027)

            dcanvas.coords("acentry1",dwidth/3.30,dheight/1.55)
            dcanvas.coords("acentry2",dwidth/1.785,dheight/1.55)
            dcanvas.coords("acentry3",dwidth/18.5,dheight/1.24)
            dcanvas.coords("acentry4",dwidth/3.30,dheight/1.24)
            dcanvas.coords("acentry5",dwidth/3.30,dheight/1.027)
            dcanvas.coords("acentry6",dwidth/1.785,dheight/1.027)
            dcanvas.coords("acentry7",dwidth/18.5,dheight/0.88)
            dcanvas.coords("acentry8",dwidth/3.30,dheight/0.88)
            dcanvas.coords("acentry9",dwidth/1.785,dheight/0.88)
            dcanvas.coords("acentry10",dwidth/18.5,dheight/0.715)
            dcanvas.coords("acentry11",dwidth/1.97,dheight/0.715)
            dcanvas.coords("acentry12",dwidth/18.5,dheight/0.625)
            dcanvas.coords("acentry13",dwidth/3.40,dheight/0.625)
            dcanvas.coords("acentry14",dwidth/1.98,dheight/0.625)
            dcanvas.coords("acentry15",dwidth/1.33,dheight/0.625)
            dcanvas.coords("acentry16",dwidth/19.51,dheight/0.565)
            dcanvas.coords("acentry17",dwidth/3.40,dheight/0.565)
            dcanvas.coords("acentry18",dwidth/1.98,dheight/0.565)
            dcanvas.coords("acentry19",dwidth/1.33,dheight/0.565)

            dcanvas.coords("accheck1",dwidth/1.55,dheight/0.79)
            dcanvas.coords("accheck2",dwidth/19.0,dheight/0.546)

            dcanvas.coords("acbutton1",dwidth/2.5,dheight/0.5)
            dcanvas.coords("acbutton3",dwidth/23,dheight/3.415)


        cus_ecanvas_1=Canvas(cus_eframe_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1600))

        cus_eframe_1.grid_columnconfigure(0,weight=1)
        cus_eframe_1.grid_rowconfigure(0,weight=1)

        
        vertibar=Scrollbar(cus_eframe_1, orient=VERTICAL)
        vertibar.grid(row=0,column=1,sticky='ns')
        vertibar.config(command=cus_ecanvas_1.yview)

        cus_ecanvas_1.bind("<Configure>", ecus_responsive_widgets2)
        cus_ecanvas_1.config(yscrollcommand=vertibar.set)
        cus_ecanvas_1.grid(row=0,column=0,sticky='nsew')

        
        if ecus_comb_1.get() == 'Edit':
            print('hai')

            cus_ecanvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly1"))

            label_1 = Label(cus_ecanvas_1,width=15,height=1,text="ADD CUSTOMER", font=('arial 20'),background="#1b3857",fg="white") 
            window_label_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel1"))

            cus_ecanvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline"))

            cus_ecanvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("acpoly2"))

            label_1 = Label(cus_ecanvas_1,width=20,height=1,text="Customer Information", font=('arial 20'),background="#1b3857",fg="white") 
            window_label_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel2"))

            cus_ecanvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("achline1"))

            label_2 = Label(cus_ecanvas_1,width=5,height=1,text="Title", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel3"))

            comb_ecus_1 = ttk.Combobox(cus_ecanvas_1, font=('arial 10'),foreground="white")
            comb_ecus_1['values'] = ("Mr","Mrs","Miss","Ms",)
            comb_ecus_1.current(0)
            window_comb_ecus_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", width=245, height=30,window=comb_ecus_1, tags=("accombo1"))

            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="First name", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel4"))

            entry_ecus_1=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_1, tags=("acentry1"))

            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Last name", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel5"))

            entry_ecus_2=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_2, tags=("acentry2"))

            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Company", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel6"))

            entry_ecus_3=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_3 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_3, tags=("acentry3"))

            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Location", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel7"))

            ecus_4=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_ecus_4 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=ecus_4, tags=("acentry4"))

            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="GST type", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel8"))

            comb_ecus_2 = ttk.Combobox(cus_ecanvas_1, font=('arial 10'),foreground="white")
            comb_ecus_2['values'] = ("Choose...","GST registered Regular","GST registered-Composition","GST unregistered","Consumer","Overseas","SEZ","Deemed exports-EOU's STP's EHTP's etc",)
            comb_ecus_2.current(0)
            window_comb_ecus_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", width=245, height=30,window=comb_ecus_2, tags=("accombo2"))

            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="GSTIN", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel9"))

            ecus_entry_str_1 = StringVar()
            entry_ecus_5=Entry(cus_ecanvas_1,width=34,justify=LEFT,background='#2f516f',foreground="white",font=('arial 10'),textvariable=ecus_entry_str_1)
            ecus_entry_str_1.set(' 29APPCK7465F1Z1')
            window_entry_ecus_5 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_5, tags=("acentry5"))

            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="PAN NO", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel10"))

            ecus_entry_str_2 = StringVar()
            entry_ecus_6=Entry(cus_ecanvas_1,width=34,justify=LEFT,background='#2f516f',foreground="white",font=('arial 10'),textvariable=ecus_entry_str_2)
            ecus_entry_str_2.set(' APPCK7465F')
            window_entry_ecus_6 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_6, tags=("acentry6"))

            label_2 = Label(cus_ecanvas_1,width=5,height=1,text="Email", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel11"))

            entry_ecus_7=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_7 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_7, tags=("acentry7"))

            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Website", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel12"))

            entry_ecus_8=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_8 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_8, tags=("acentry8"))

            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Mobile", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel13"))

            entry_ecus_9=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_9 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_9, tags=("acentry9"))

            label_1 = Label(cus_ecanvas_1,width=20,height=1,text="Billing Address", font=('arial 16'),background="#1b3857",fg="white") 
            window_label_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel14"))

            label_2 = Label(cus_ecanvas_1,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel16"))

            entry_ecus_10=Entry(cus_ecanvas_1,width=95,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_10 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=60,window=entry_ecus_10, tags=("acentry10"))

            label_1 = Label(cus_ecanvas_1,width=20,height=1,text="Shipping Address", font=('arial 16'),background="#1b3857",fg="white") 
            window_label_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aclabel15"))

            echk_str = StringVar()
            echkbtn1 = Checkbutton(cus_ecanvas_1, text = "Same As Billing Address", variable = echk_str, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f")
            echkbtn1.select()
            window_echkbtn_1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=echkbtn1, tags=("accheck1"))

            label_2 = Label(cus_ecanvas_1,width=5,height=1,text="Street", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel17"))

            entry_ecus_11=Entry(cus_ecanvas_1,width=95,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_11 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=60,window=entry_ecus_11, tags=("acentry11"))

            label_2 = Label(cus_ecanvas_1,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel18"))

            entry_ecus_12=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_12 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_12, tags=("acentry12"))
            
            label_2 = Label(cus_ecanvas_1,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel19"))

            entry_ecus_13=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_13 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_13, tags=("acentry13"))

            label_2 = Label(cus_ecanvas_1,width=5,height=1,text="City", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel20"))

            entry_ecus_14=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_14 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_14, tags=("acentry14"))

            label_2 = Label(cus_ecanvas_1,width=5,height=1,text="State", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2,tags=("aclabel21"))

            entry_ecus_15=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_15 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_15, tags=("acentry15"))

            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel22"))

            entry_ecus_12=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_12 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_12, tags=("acentry16"))
            
            label_2 = Label(cus_ecanvas_1,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel23"))

            entry_ecus_13=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_13 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_13, tags=("acentry17"))

            label_2 = Label(cus_ecanvas_1,width=10,height=1,text="Pin Code", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel24"))

            entry_ecus_14=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_14 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_14, tags=("acentry18"))

            label_2 = Label(cus_ecanvas_1,width=8,height=1,text="Country", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=label_2, tags=("aclabel25"))

            entry_ecus_15=Entry(cus_ecanvas_1,width=40,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_ecus_15 = cus_ecanvas_1.create_window(0, 0, anchor="nw", height=30,window=entry_ecus_15, tags=("acentry19"))

            echk_str_1 = StringVar()
            echkbtn2 = Checkbutton(cus_ecanvas_1, text = "Agree to terms and conditions", variable = echk_str_1, onvalue = 1, offvalue = 0, font=("arial", 10),background="#1b3857",foreground="white",selectcolor="#2f516f")
            echkbtn2.select()
            window_echkbtn_2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=echkbtn2,tags=("accheck2"))

            def ec_back_1_():
                cus_eframe_1.grid_forget()
                cus_frame.grid(row=0,column=0,sticky='nsew')

            ec_bck_btn1=Button(cus_ecanvas_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=ec_back_1_)
            window_ec_bck_btn1 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=ec_bck_btn1,tags=('acbutton3'))

            ecus_btn2=Button(cus_ecanvas_1,text='Submit Form', width=25,height=2,foreground="white",background="#1b3857",font='arial 12')
            window_ecus_btn2 = cus_ecanvas_1.create_window(0, 0, anchor="nw", window=ecus_btn2,tags=("acbutton1"))
        else:
            pass

    # Define the style for combobox widget
    # style= ttk.Style()
    # style.theme_use('clam')
    # style.configure("TCombobox", fieldbackground= "#2f516f", background= "#2f516f")

    ecus_comb_1 = ttk.Combobox(cus_canvas,)
    ecus_comb_1['values'] = ['Actions','Edit','Delete']
    #cus_comb_1.current(0)
    ecus_comb_1.bind('<<ComboboxSelected>>',edit_customer)
    window_ecus_comb_1 = cus_canvas.create_window(0, 0, anchor="nw", width=110,height=30,window=ecus_comb_1, tags=("ccombo1"))

    # btn1=Button(cus_canvas,text='Add Customer', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_customer)
    # window_btn1 = cus_canvas.create_window(0, 0, anchor="nw", window=btn1, tags=("cbutton1"))

    #---------------------------Product & Services------------------------#
    tab3_4.grid_columnconfigure(0,weight=1)
    tab3_4.grid_rowconfigure(0,weight=1)

    pro_frame = Frame(tab3_4)
    pro_frame.grid(row=0,column=0,sticky='nsew')

    def pro_responsive_widgets(event):
        dwidth = event.width
        dheight = event.height
        dcanvas = event.widget

        r1 = 25
        x1 = dwidth/63
        x2 = dwidth/1.021
        y1 = dheight/14 
        y2 = dheight/3.505

        dcanvas.coords("ppoly1",x1 + r1,y1,
        x1 + r1,y1,
        x2 - r1,y1,
        x2 - r1,y1,     
        x2,y1,     
        #--------------------
        x2,y1 + r1,     
        x2,y1 + r1,     
        x2,y2 - r1,     
        x2,y2 - r1,     
        x2,y2,
        #--------------------
        x2 - r1,y2,     
        x2 - r1,y2,     
        x1 + r1,y2,
        x1 + r1,y2,
        x1,y2,
        #--------------------
        x1,y2 - r1,
        x1,y2 - r1,
        x1,y1 + r1,
        x1,y1 + r1,
        x1,y1,
        )

        dcanvas.coords("phline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)
        dcanvas.coords("plabel1",dwidth/2.75,dheight/8.00)

        r2 = 25
        x11 = dwidth/63
        x21 = dwidth/1.021
        y11 = dheight/2.8
        y21 = dheight/0.850


        dcanvas.coords("ppoly2",x11 + r2,y11,
        x11 + r2,y11,
        x21 - r2,y11,
        x21 - r2,y11,     
        x21,y11,     
        #--------------------
        x21,y11 + r2,     
        x21,y11 + r2,     
        x21,y21 - r2,     
        x21,y21 - r2,     
        x21,y21,
        #--------------------
        x21 - r2,y21,     
        x21 - r2,y21,     
        x11 + r2,y21,
        x11 + r2,y21,
        x11,y21,
        #--------------------
        x11,y21 - r2,
        x11,y21 - r2,
        x11,y11 + r2,
        x11,y11 + r2,
        x11,y11,
        )

        dcanvas.coords("pline1", dwidth/22.00, dheight/1.24, dwidth/1.060, dheight/1.24)
        dcanvas.coords("pline2", dwidth/22.00, dheight/1.13, dwidth/1.060, dheight/1.13)
        dcanvas.coords("pline3", dwidth/22.00, dheight/1.015, dwidth/1.060, dheight/1.015)
        dcanvas.coords("pline4", dwidth/22.00, dheight/1.24, dwidth/22.00, dheight/1.015)
        dcanvas.coords("pline5", dwidth/1.060, dheight/1.24, dwidth/1.060, dheight/1.015)
        dcanvas.coords("pline6", dwidth/5.00, dheight/1.24, dwidth/5.00, dheight/1.015)
        dcanvas.coords("pline7", dwidth/2.50, dheight/1.24, dwidth/2.50, dheight/1.015)
        dcanvas.coords("pline8", dwidth/1.80, dheight/1.24, dwidth/1.80, dheight/1.015)
        dcanvas.coords("pline9", dwidth/1.40, dheight/1.24, dwidth/1.40, dheight/1.015)
        dcanvas.coords("pline10", dwidth/1.20, dheight/1.24, dwidth/1.20, dheight/1.015)

        dcanvas.coords("pimage1",dwidth/5.29,dheight/2.15)
        dcanvas.coords("pimage2",dwidth/2.05,dheight/2.15)

        dcanvas.coords("plabel2",dwidth/5.60,dheight/1.60)
        dcanvas.coords("plabel3",dwidth/2.09,dheight/1.60)
        dcanvas.coords("plabel4",dwidth/10.55,dheight/1.21)
        dcanvas.coords("plabel5",dwidth/3.60,dheight/1.21)
        dcanvas.coords("plabel6",dwidth/2.15,dheight/1.21)
        dcanvas.coords("plabel7",dwidth/1.63,dheight/1.21)
        dcanvas.coords("plabel8",dwidth/1.35,dheight/1.21)
        dcanvas.coords("plabel9",dwidth/1.17,dheight/1.21)

        dcanvas.coords("pcombo1",dwidth/1.18,dheight/1.10)
        dcanvas.coords("pbutton1",dwidth/1.28,dheight/1.45)

    pro_canvas=Canvas(pro_frame, bg='#2f516f', width=1325, height=600, scrollregion=(0,0,700,1000))

    pro_frame.grid_rowconfigure(0,weight=1)
    pro_frame.grid_columnconfigure(0,weight=1)

    vertibar=Scrollbar(pro_frame, orient=VERTICAL)
    vertibar.grid(row=0,column=1,sticky='ns')
    vertibar.config(command=pro_canvas.yview)
    
    pro_canvas.bind("<Configure>", pro_responsive_widgets)
    pro_canvas.config(yscrollcommand=vertibar.set)
    pro_canvas.grid(row=0,column=0,sticky='nsew')

    
    pro_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("ppoly1"))
    
    label_1 = Label(pro_canvas,width=23,height=1,text="PRODUCT AND SERVICES", font=('arial 25'),background="#1b3857",fg="white") 
    window_label_1 = pro_canvas.create_window(480, 85, anchor="nw", window=label_1, tags=("plabel1"))

    pro_canvas.create_line(0,0,0,0,fill='gray',width=1,tags=("phline"))

    pro_canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("ppoly2"))


    image_1 = Image.open("images/lowstock.png")
    resize_image = image_1.resize((90,90))
    image_1 = ImageTk.PhotoImage(resize_image)
    btlogo = Label(pro_canvas, width=90, height=90, background="#1b3857", image = image_1) 
    window_image = pro_canvas.create_window(0, 0, anchor="nw", window=btlogo,tags=('pimage1'))
    btlogo.photo = image_1

    label_2 = Label(pro_canvas,width=14,height=1,text="LOW STOCK : ", font=('arial 18'),background="#1b3857",fg="white") 
    window_label_2 = pro_canvas.create_window(0, 0, anchor="nw", window=label_2,tags=('plabel2'))

    image_2 = Image.open("images/outofstock.png")
    resize_image_1 = image_2.resize((90,90))
    image_2 = ImageTk.PhotoImage(resize_image_1)
    btlogo_1 = Label(pro_canvas, width=90, height=90, background="#1b3857", image = image_2) 
    window_image_1 = pro_canvas.create_window(0, 0, anchor="nw", window=btlogo_1,tags=('pimage2'))
    btlogo_1.photo = image_2

    label_2 = Label(pro_canvas,width=15,height=1,text="OUT OF STOCK : ", font=('arial 18'),background="#1b3857",fg="white") 
    window_label_2 = pro_canvas.create_window(0, 0, anchor="nw", window=label_2,tags=('plabel3'))


    pro_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('pline1'))
    pro_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('pline2'))
    pro_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('pline3'))
    pro_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('pline4'))
    pro_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('pline5'))
    pro_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('pline6'))
    pro_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('pline7'))
    pro_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('pline8'))
    pro_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('pline9'))
    pro_canvas.create_line(0, 0, 0, 0, fill='gray',width=1,tags=('pline10'))


    label_2 = Label(pro_canvas,width=9,height=1,text="TYPE", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_2 = pro_canvas.create_window(0, 0, anchor="nw", window=label_2,tags=('plabel4'))

    label_3 = Label(pro_canvas,width=5,height=1,text="NAME", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_3 = pro_canvas.create_window(0, 0, anchor="nw", window=label_3,tags=('plabel5'))

    label_4 = Label(pro_canvas,width=5,height=1,text="SKU", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = pro_canvas.create_window(0, 0, anchor="nw", window=label_4,tags=('plabel6'))

    label_4 = Label(pro_canvas,width=8,height=1,text="HSN/SAC", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = pro_canvas.create_window(0, 0, anchor="nw", window=label_4,tags=('plabel7'))

    label_4 = Label(pro_canvas,width=11,height=1,text="QUANTITY", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = pro_canvas.create_window(0, 0, anchor="nw", window=label_4,tags=('plabel8'))

    label_4 = Label(pro_canvas,width=11,height=1,text="ACTION", font=('arial 10'),background="#1b3857",fg="white") 
    window_label_4 = pro_canvas.create_window(0, 0, anchor="nw", window=label_4,tags=('plabel9'))

   
    # Define the style for combobox widget
    # style= ttk.Style(canvas)
    # style.theme_use('clam')
    # style.configure("TCombobox", fieldbackground= "#2f516f", background= "#2f516f")

    cus_comb_1 = ttk.Combobox(pro_canvas,font=('arial 10'),foreground="white")
    cus_comb_1['values'] = ("Actions","Edit","Delete")
    cus_comb_1.current(0)
    window_cus_comb_1 = pro_canvas.create_window(1135, 560, anchor="nw", width=110,height=30,window=cus_comb_1,tags=('pcombo1'))


    def add_product():
        pro_frame.grid_forget()
        pro_frame_1 = Frame(tab3_4)
        pro_frame_1.grid(row=0,column=0,sticky='nsew')

        def pro_responsive_widgets_1(event):
            dwidth = event.width
            dheight = event.height
            dcanvas = event.widget
            
            r1 = 25
            x1 = dwidth/63
            x2 = dwidth/1.021
            y1 = dheight/14 
            y2 = dheight/3.505

            dcanvas.coords("appoly1",x1 + r1,y1,
            x1 + r1,y1,
            x2 - r1,y1,
            x2 - r1,y1,     
            x2,y1,     
            #--------------------
            x2,y1 + r1,     
            x2,y1 + r1,     
            x2,y2 - r1,     
            x2,y2 - r1,     
            x2,y2,
            #--------------------
            x2 - r1,y2,     
            x2 - r1,y2,     
            x1 + r1,y2,
            x1 + r1,y2,
            x1,y2,
            #--------------------
            x1,y2 - r1,
            x1,y2 - r1,
            x1,y1 + r1,
            x1,y1 + r1,
            x1,y1,
            )

            dcanvas.coords("aplabel1",dwidth/3,dheight/8.24)
            dcanvas.coords("aphline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

            r2 = 25
            x11 = dwidth/63
            x21 = dwidth/1.021
            y11 = dheight/2.8
            y21 = dheight/0.60


            dcanvas.coords("appoly2",x11 + r2,y11,
            x11 + r2,y11,
            x21 - r2,y11,
            x21 - r2,y11,     
            x21,y11,     
            #--------------------
            x21,y11 + r2,     
            x21,y11 + r2,     
            x21,y21 - r2,     
            x21,y21 - r2,     
            x21,y21,
            #--------------------
            x21 - r2,y21,     
            x21 - r2,y21,     
            x11 + r2,y21,
            x11 + r2,y21,
            x11,y21,
            #--------------------
            x11,y21 - r2,
            x11,y21 - r2,
            x11,y11 + r2,
            x11,y11 + r2,
            x11,y11,
            )

            r2 = 25
            x11 = dwidth/7
            x21 = dwidth/2.07
            y11 = dheight/2.0
            y21 = dheight/1.1


            dcanvas.coords("appoly3",x11 + r2,y11,
            x11 + r2,y11,
            x21 - r2,y11,
            x21 - r2,y11,     
            x21,y11,     
            #--------------------
            x21,y11 + r2,     
            x21,y11 + r2,     
            x21,y21 - r2,     
            x21,y21 - r2,     
            x21,y21,
            #--------------------
            x21 - r2,y21,     
            x21 - r2,y21,     
            x11 + r2,y21,
            x11 + r2,y21,
            x11,y21,
            #--------------------
            x11,y21 - r2,
            x11,y21 - r2,
            x11,y11 + r2,
            x11,y11 + r2,
            x11,y11,
            )

            dcanvas.coords("aplabel2",dwidth/3.9,dheight/1.75)
            dcanvas.coords("aplabel3",dwidth/6.30,dheight/1.54)
            dcanvas.coords("apbutton1",dwidth/4.1,dheight/1.30)

            r2 = 25
            x11 = dwidth/1.93
            x21 = dwidth/1.15
            y11 = dheight/2.0
            y21 = dheight/1.1


            dcanvas.coords("appoly4",x11 + r2,y11,
            x11 + r2,y11,
            x21 - r2,y11,
            x21 - r2,y11,     
            x21,y11,     
            #--------------------
            x21,y11 + r2,     
            x21,y11 + r2,     
            x21,y21 - r2,     
            x21,y21 - r2,     
            x21,y21,
            #--------------------
            x21 - r2,y21,     
            x21 - r2,y21,     
            x11 + r2,y21,
            x11 + r2,y21,
            x11,y21,
            #--------------------
            x11,y21 - r2,
            x11,y21 - r2,
            x11,y11 + r2,
            x11,y11 + r2,
            x11,y11,
            )

            dcanvas.coords("aplabel4",dwidth/1.58,dheight/1.75)
            dcanvas.coords("aplabel5",dwidth/1.85,dheight/1.54)
            dcanvas.coords("apbutton2",dwidth/1.6,dheight/1.30)

            r2 = 25
            x11 = dwidth/7
            x21 = dwidth/2.07
            y11 = dheight/1.0
            y21 = dheight/0.719


            dcanvas.coords("appoly5",x11 + r2,y11,
            x11 + r2,y11,
            x21 - r2,y11,
            x21 - r2,y11,     
            x21,y11,     
            #--------------------
            x21,y11 + r2,     
            x21,y11 + r2,     
            x21,y21 - r2,     
            x21,y21 - r2,     
            x21,y21,
            #--------------------
            x21 - r2,y21,     
            x21 - r2,y21,     
            x11 + r2,y21,
            x11 + r2,y21,
            x11,y21,
            #--------------------
            x11,y21 - r2,
            x11,y21 - r2,
            x11,y11 + r2,
            x11,y11 + r2,
            x11,y11,
            )

            dcanvas.coords("aplabel6",dwidth/3.9,dheight/0.95)
            dcanvas.coords("aplabel7",dwidth/6.30,dheight/0.88)
            dcanvas.coords("apbutton3",dwidth/4.1,dheight/0.80)

            r2 = 25
            x11 = dwidth/1.93
            x21 = dwidth/1.15
            y11 = dheight/1.0
            y21 = dheight/0.719


            dcanvas.coords("appoly6",x11 + r2,y11,
            x11 + r2,y11,
            x21 - r2,y11,
            x21 - r2,y11,     
            x21,y11,     
            #--------------------
            x21,y11 + r2,     
            x21,y11 + r2,     
            x21,y21 - r2,     
            x21,y21 - r2,     
            x21,y21,
            #--------------------
            x21 - r2,y21,     
            x21 - r2,y21,     
            x11 + r2,y21,
            x11 + r2,y21,
            x11,y21,
            #--------------------
            x11,y21 - r2,
            x11,y21 - r2,
            x11,y11 + r2,
            x11,y11 + r2,
            x11,y11,
            )

            dcanvas.coords("aplabel8",dwidth/1.58,dheight/0.95)
            dcanvas.coords("aplabel9",dwidth/1.85,dheight/0.88)
            dcanvas.coords("apbutton4",dwidth/1.6,dheight/0.80)
            dcanvas.coords("apbutton5",dwidth/23,dheight/3.415)


        p_canvas_1=Canvas(pro_frame_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,1000))

        pro_frame_1.grid_columnconfigure(0,weight=1)
        pro_frame_1.grid_rowconfigure(0,weight=1)
        
        vertibar=Scrollbar(pro_frame_1, orient=VERTICAL)
        vertibar.grid(row=0,column=1,sticky='ns')
        vertibar.config(command=p_canvas_1.yview)

        p_canvas_1.bind("<Configure>", pro_responsive_widgets_1)
        p_canvas_1.config(yscrollcommand=vertibar.set)
        p_canvas_1.grid(row=0,column=0,sticky='nsew')
        
        
        p_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("appoly1"))

        label_1 = Label(p_canvas_1,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1, tags=("aplabel1"))

        p_canvas_1.create_line(0, 0, 0, 0, fill='gray',width=1, tags=("aphline"))

        p_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=("appoly2"))

        p_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=("appoly3"))

        label_1 = Label(p_canvas_1,width=10,height=1,text="Inventory", font=('arial 20'),background="#2f516f",fg="white") 
        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel2'))

        label_1 = Label(p_canvas_1,width=45,height=2,text="Inventory is the goods available for sale and raw materials \nused to produce goods available for sale.", font=('arial 12'),background="#2f516f",fg="white") 
        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel3'))

        def inv_add_item():
            pro_frame_1.grid_forget()
            pro_frame_2 = Frame(tab3_4)
            pro_frame_2.grid(row=0,column=0,sticky='nsew')

            def pro_responsive_widgets_2(event):
                dwidth = event.width
                dheight = event.height
                dcanvas = event.widget
            
                r1 = 25
                x1 = dwidth/63
                x2 = dwidth/1.021
                y1 = dheight/14 
                y2 = dheight/3.505

                dcanvas.coords("ippoly1",x1 + r1,y1,
                x1 + r1,y1,
                x2 - r1,y1,
                x2 - r1,y1,     
                x2,y1,     
                #--------------------
                x2,y1 + r1,     
                x2,y1 + r1,     
                x2,y2 - r1,     
                x2,y2 - r1,     
                x2,y2,
                #--------------------
                x2 - r1,y2,     
                x2 - r1,y2,     
                x1 + r1,y2,
                x1 + r1,y2,
                x1,y2,
                #--------------------
                x1,y2 - r1,
                x1,y2 - r1,
                x1,y1 + r1,
                x1,y1 + r1,
                x1,y1,
                )

                dcanvas.coords("iplabel1",dwidth/3,dheight/8.24)
                dcanvas.coords("iphline",dwidth/21,dheight/4.67,dwidth/1.055,dheight/4.67)

                r2 = 25
                x11 = dwidth/63
                x21 = dwidth/1.021
                y11 = dheight/2.8
                y21 = dheight/0.29


                dcanvas.coords("ippoly2",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                r2 = 25
                x11 = dwidth/24
                x21 = dwidth/1.050
                y11 = dheight/2.1
                y21 = dheight/1.35


                dcanvas.coords("ippoly3",x11 + r2,y11,
                x11 + r2,y11,
                x21 - r2,y11,
                x21 - r2,y11,     
                x21,y11,     
                #--------------------
                x21,y11 + r2,     
                x21,y11 + r2,     
                x21,y21 - r2,     
                x21,y21 - r2,     
                x21,y21,
                #--------------------
                x21 - r2,y21,     
                x21 - r2,y21,     
                x11 + r2,y21,
                x11 + r2,y21,
                x11,y21,
                #--------------------
                x11,y21 - r2,
                x11,y21 - r2,
                x11,y11 + r2,
                x11,y11 + r2,
                x11,y11,
                )

                dcanvas.coords("iplabel2",dwidth/2.5,dheight/1.77)
                dcanvas.coords("ipbutton1",dwidth/1.8,dheight/1.77)

                dcanvas.coords("iplabel3",dwidth/23.2,dheight/1.23)
                dcanvas.coords("iplabel4",dwidth/23.3,dheight/1.02)
                dcanvas.coords("iplabel5",dwidth/1.9,dheight/1.02)
                dcanvas.coords("iplabel6",dwidth/1.9,dheight/0.92)
                dcanvas.coords("iplabel7",dwidth/27,dheight/0.865)
                dcanvas.coords("iplabel8",dwidth/1.915,dheight/0.865)
                dcanvas.coords("iplabel9",dwidth/50,dheight/0.76)
                dcanvas.coords("iplabel10",dwidth/2.95,dheight/0.76)
                dcanvas.coords("iplabel11",dwidth/1.54,dheight/0.76)
                dcanvas.coords("iplabel12",dwidth/38,dheight/0.675)
                dcanvas.coords("iplabel13",dwidth/26.8,dheight/0.606)
                dcanvas.coords("iplabel14",dwidth/28.3,dheight/0.538)
                dcanvas.coords("iplabel15",dwidth/1.9,dheight/0.538)
                dcanvas.coords("iplabel16",dwidth/28.4,dheight/0.485)
                dcanvas.coords("iplabel17",dwidth/29.3,dheight/0.438)
                dcanvas.coords("iplabel18",dwidth/28,dheight/0.401)
                dcanvas.coords("iplabel19",dwidth/1.91,dheight/0.401)
                dcanvas.coords("iplabel20",dwidth/28,dheight/0.37)
                dcanvas.coords("iplabel21",dwidth/26,dheight/0.35)
                dcanvas.coords("iplabel22",dwidth/1.9,dheight/0.35)

                dcanvas.coords("ipentry1",dwidth/23.2,dheight/1.165)
                dcanvas.coords("ipentry2",dwidth/23.2,dheight/0.975)
                dcanvas.coords("ipentry3",dwidth/1.9,dheight/0.975)
                dcanvas.coords("ipentry4",dwidth/1.9,dheight/0.83)
                dcanvas.coords("ipentry5",dwidth/23.2,dheight/0.73)
                dcanvas.coords("ipentry6",dwidth/1.52,dheight/0.73)
                dcanvas.coords("ipentry7",dwidth/23.2,dheight/0.59)
                dcanvas.coords("ipentry8",dwidth/23.2,dheight/0.525)
                dcanvas.coords("ipentry9",dwidth/23.2,dheight/0.43)
                dcanvas.coords("ipentry10",dwidth/23.2,dheight/0.394)
                dcanvas.coords("ipentry11",dwidth/23.2,dheight/0.344)

                dcanvas.coords("ipcombo1",dwidth/23.2,dheight/0.83)
                dcanvas.coords("ipcombo2",dwidth/23.2,dheight/0.654)
                dcanvas.coords("ipcombo3",dwidth/1.9,dheight/0.525)
                dcanvas.coords("ipcombo4",dwidth/23.2,dheight/0.474)
                dcanvas.coords("ipcombo5",dwidth/1.89,dheight/0.394)
                dcanvas.coords("ipcombo6",dwidth/23.2,dheight/0.364)
                dcanvas.coords("ipcombo7",dwidth/1.89,dheight/0.344)

                dcanvas.coords("ipcbutton1",dwidth/23.2,dheight/0.51)
                dcanvas.coords("ipcbutton2",dwidth/23.2,dheight/0.385)

                dcanvas.coords("ipbutton2",dwidth/2.45,dheight/0.654)
                dcanvas.coords("ipbutton3",dwidth/2.45,dheight/0.474)
                dcanvas.coords("ipbutton4",dwidth/2.45,dheight/0.364)
                dcanvas.coords("ipbutton5",dwidth/2.38,dheight/0.325)

                dcanvas.coords("iphline1",dwidth/21,dheight/0.448,dwidth/1.055,dheight/0.448)

                try:
                    dcanvas.coords("ipdate1",dwidth/2.9,dheight/0.73)
                except:
                    pass


            p_canvas_2=Canvas(pro_frame_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))

            pro_frame_2.grid_columnconfigure(0,weight=1)
            pro_frame_2.grid_rowconfigure(0,weight=1)
        
            vertibar=Scrollbar(pro_frame_2, orient=VERTICAL)
            vertibar.grid(row=0,column=1,sticky='ns')
            vertibar.config(command=p_canvas_2.yview)

            p_canvas_2.bind("<Configure>", pro_responsive_widgets_2)
            p_canvas_2.config(yscrollcommand=vertibar.set)
            p_canvas_2.grid(row=0,column=0,sticky='nsew')


            p_canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('ippoly1'))

            label_1 = Label(p_canvas_2,width=30,height=1,text="PRODUCT / SERVICE INFORMATION", font=('arial 20'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel1'))

            p_canvas_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('iphline'))

            p_canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#1b3857",tags=('ippoly2'))

            p_canvas_2.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=('ippoly3'))

            label_1 = Label(p_canvas_2,width=10,height=2,text="INVENTORY", font=('arial 20'),background="#2f516f",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel2'))

            btn_item_1=Button(p_canvas_2,text='Choose Type', width=15,height=1,foreground="white",background="#2f516f",font='arial 20',  command=add_product)
            window_btn_item_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=btn_item_1, tags=('ipbutton1'))

            label_1 = Label(p_canvas_2,width=5,height=1,text="Name", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel3'))

            entry_inv_item_1=Entry(p_canvas_2,width=200,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_1 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_1, tags=('ipentry1'))

            label_1 = Label(p_canvas_2,width=4,height=1,text="SKU", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel4'))

            str_inv_item_1 = StringVar()
            entry_inv_item_2=Entry(p_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_inv_item_1)
            str_inv_item_1.set('  Eg: N41554')
            window_entry_entry_inv_item_2 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_2, tags=('ipentry2'))

            label_1 = Label(p_canvas_2,width=9,height=1,text="HSN Code", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel5'))

            entry_inv_item_2=Entry(p_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_2 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_2, tags=("ipentry3"))

            label_1 = Label(p_canvas_2,width=30,height=1,text="Not sure about HSN Code..? Click here", font=('arial 12'),background="#1b3857",fg="skyblue") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel6'))

            label_1 = Label(p_canvas_2,width=5,height=1,text="Unit", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1, tags=('iplabel7'))

            comb_inv_item_1 = ttk.Combobox(p_canvas_2, font=('arial 10'),foreground="white")
            comb_inv_item_1['values'] = ("Choose...","BAG Bags","BAL Bale BOU","BDL Bundles","BKL Buckles","BOX Box","BTL Bottles","CAN Cans","CTN Cartons","CCM Cubic centimeters","CBM Cubic meters","CMS Centimeters","DRM Drums","DOZ Dozens","GGK Great gross GYD","GRS GrossGMS","KME Kilometre","KGS Kilograms","KLR Kilo litre","MTS Metric ton","MLT Mili litre","MTR Meters","NOS Numbers","PAC Packs","PCS Pieces","PRS Pairs","QTL Quintal","ROL Rolls","SQY Square Yards","SET Sets","SQF Square feet","SQM Square meters","TBS Tablets","TUB Tubes","TGM Ten Gross","THD Thousands","TON Tonnes","UNT Units","UGS US Gallons","YDS Yards",)
            comb_inv_item_1.current(0)
            window_comb_inv_item_1 = p_canvas_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_item_1, tags=('ipcombo1'))

            label_1 = Label(p_canvas_2,width=9,height=1,text="Category", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel8'))

            entry_inv_item_3=Entry(p_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_3 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_3,tags=('ipentry4'))

            label_1 = Label(p_canvas_2,width=24,height=1,text="Initial quantity on hand", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel9'))

            entry_inv_item_4=Entry(p_canvas_2,width=60,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_4 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_4,tags=('ipentry5'))

            label_1 = Label(p_canvas_2,width=10,height=1,text="As of date", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel10'))
  
            label_1 = Label(p_canvas_2,width=14,height=1,text="Low stock alert", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel11'))

            entry_inv_item_6=Entry(p_canvas_2,width=60,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_6 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_6,tags=('ipentry6'))

            label_1 = Label(p_canvas_2,width=22,height=1,text="Inventory asset account", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(35, 910, anchor="nw", window=label_1,tags=('iplabel12'))

            comb_inv_item_2 = ttk.Combobox(p_canvas_2, font=('arial 10'),foreground="white")
            comb_inv_item_2['values'] = ("Inventory Asset",)
            comb_inv_item_2.current(0)
            window_comb_inv_item_2 = p_canvas_2.create_window(0, 0, anchor="nw", width=480, height=30,window=comb_inv_item_2,tags=('ipcombo2'))

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
                chkbtn_inv_1_1 = Checkbutton(canvas, text = "Is sub-account", variable = chk_str_inv_1_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                chkbtn_inv_1_1.select()
                window_chkbtn_inv_1_1 = canvas.create_window(709, 500, anchor="nw", window=chkbtn_inv_1_1)

                comb_inv_1_3 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_inv_1_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                comb_inv_1_3.current(0)
                window_comb_inv_1_3 = canvas.create_window(710, 530, anchor="nw", width=540, height=30,window=comb_inv_1_3)

                label_1 = Label(canvas,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(705, 600, anchor="nw", window=label_1)

                comb_inv_1_4 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_inv_1_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                comb_inv_1_4.current(0)
                window_comb_inv_1_4 = canvas.create_window(710, 630, anchor="nw", width=540, height=30,window=comb_inv_1_4)

                inv_bac_btn_1_1=Button(canvas,text='Back', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=inv_add_item)
                window_inv_bac_btn_1_1 = canvas.create_window(450, 800, anchor="nw", window=inv_bac_btn_1_1)

                inv_sub_btn_1_1=Button(canvas,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                window_inv_sub_btn_1_1 = canvas.create_window(685, 800, anchor="nw", window=inv_sub_btn_1_1)

                

            asset_btn=Button(p_canvas_2,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=inv_acc_create_1)
            window_asset_btn = p_canvas_2.create_window(0, 0, anchor="nw", window=asset_btn,tags=('ipbutton2'))

            label_1 = Label(p_canvas_2,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel13'))

            entry_inv_item_7=Entry(p_canvas_2,width=200,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_7 = p_canvas_2.create_window(0, 0, anchor="nw", height=60,window=entry_inv_item_7,tags=('ipentry7'))

            label_1 = Label(p_canvas_2,width=15,height=1,text="Sales price/rate", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel14'))
            
            entry_inv_item_8=Entry(p_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_8 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_8,tags=('ipentry8'))

            chk_str_inv_item = StringVar()
            chkbtn_inv_item_1 = Checkbutton(p_canvas_2, text = "Inclusive of tax", variable = chk_str_inv_item, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
            chkbtn_inv_item_1.select()
            window_chkbtn_inv_item_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=chkbtn_inv_item_1,tags=('ipcbutton1'))

            label_1 = Label(p_canvas_2,width=4,height=1,text="Tax", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel15'))

            comb_inv_item_3 = ttk.Combobox(p_canvas_2, font=('arial 10'),foreground="white")
            comb_inv_item_3['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
            comb_inv_item_3.current(0)
            window_comb_inv_item_3 = p_canvas_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_item_3,tags=('ipcombo3'))

            label_1 = Label(p_canvas_2,width=15,height=1,text="Income account", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel16'))

            comb_inv_item_4 = ttk.Combobox(p_canvas_2, font=('arial 10'),foreground="white")
            comb_inv_item_4['values'] = ("Choose...","Billable Expense Income","Product Sales","Sales","Sales-Hardware","Sales-Software","Sales-Support and Maintanance","Sales of Product Income","Uncategorised Income",)
            comb_inv_item_4.current(0)
            window_comb_inv_item_4 = p_canvas_2.create_window(0, 0, anchor="nw", width=480, height=30,window=comb_inv_item_4,tags=('ipcombo4'))

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
                chkbtn_inv_2_1 = Checkbutton(canvas, text = "Is sub-account", variable = chk_str_inv_2_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                chkbtn_inv_2_1.select()
                window_chkbtn_inv_2_1 = canvas.create_window(709, 500, anchor="nw", window=chkbtn_inv_2_1)

                comb_inv_2_3 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_inv_2_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                comb_inv_2_3.current(0)
                window_comb_inv_2_3 = canvas.create_window(710, 530, anchor="nw", width=540, height=30,window=comb_inv_2_3)

                label_1 = Label(canvas,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(705, 600, anchor="nw", window=label_1)

                comb_inv_2_4 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_inv_2_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                comb_inv_2_4.current(0)
                window_comb_inv_2_4 = canvas.create_window(710, 630, anchor="nw", width=540, height=30,window=comb_inv_2_4)

                inv_bac_btn_2_1=Button(canvas,text='Back', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=inv_add_item)
                window_inv_bac_btn_2_1 = canvas.create_window(450, 800, anchor="nw", window=inv_bac_btn_2_1)

                inv_sub_btn_2_1=Button(canvas,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                window_inv_sub_btn_2_1 = canvas.create_window(685, 800, anchor="nw", window=inv_sub_btn_2_1)


            account_btn=Button(p_canvas_2,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=inv_inc_acc_1)
            window_account_btn = p_canvas_2.create_window(0, 0, anchor="nw", window=account_btn,tags=('ipbutton3'))

            p_canvas_2.create_line(0, 0, 0, 0, fill='gray',width=1, tags=('iphline1'))

            label_1 = Label(p_canvas_2,width=22,height=1,text="Purchasing information", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel17'))

            entry_inv_item_9=Entry(p_canvas_2,width=200,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_9 = p_canvas_2.create_window(0, 0, anchor="nw", height=60,window=entry_inv_item_9,tags=('ipentry9'))

            label_1 = Label(p_canvas_2,width=5,height=1,text="Cost", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel18'))
            
            entry_inv_item_10=Entry(p_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_10 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_10,tags=('ipentry10'))

            chk_str_inv_item_1 = StringVar()
            chkbtn_inv_item_2 = Checkbutton(p_canvas_2, text = "Inclusive of purchase tax", variable = chk_str_inv_item_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
            chkbtn_inv_item_2.select()
            window_chkbtn_inv_item_2 = p_canvas_2.create_window(0, 0, anchor="nw", window=chkbtn_inv_item_2,tags=('ipcbutton2'))

            label_1 = Label(p_canvas_2,width=12,height=1,text="Purchase tax", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(700, 1530, anchor="nw", window=label_1,tags=('iplabel19'))

            comb_inv_item_5 = ttk.Combobox(p_canvas_2, font=('arial 10'),foreground="white")
            comb_inv_item_5['values'] = ("Choose...","28.0% GST (28%)","28.0% IGST (28%)","18.0% GST (18%)","18.0% IGST (18%)","15.0% ST (100%)","14.5% ST (100%)","14.00% ST (100%)","14.0% VAT (100%)","12.36% ST (100%)","12.0% GST (12%)","12.0% IGST (12%)","6.0% GST (6%)","6.0% IGST (6%)","5.0% GST (5%)","5.0% IGST (5%)","5.0% VAT (100%)","4.0% VAT (100%)","3.0% GST (3%)","3.0% IGST (3%)","2.0% CST (100%)","0.25% GST (O.25%)","0.25% IGST (0.25%)","0% GST (0%)","0% IGST (0%)","Exempt GST (0%)","Exempt IGST (0%)","Out of Scope(0%)",)
            comb_inv_item_5.current(0)
            window_comb_inv_item_5 = p_canvas_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_item_5,tags=('ipcombo5'))

            label_1 = Label(p_canvas_2,width=15,height=1,text="Expense account", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel20'))

            comb_inv_item_6 = ttk.Combobox(p_canvas_2, font=('arial 10'),foreground="white")
            comb_inv_item_6['values'] = ("Cost of sales",)
            comb_inv_item_6.current(0)
            window_comb_inv_item_6 = p_canvas_2.create_window(0, 0, anchor="nw", width=480, height=30,window=comb_inv_item_6,tags=('ipcombo6'))

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
                chkbtn_inv_3_1 = Checkbutton(canvas, text = "Is sub-account", variable = chk_str_inv_3_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                chkbtn_inv_3_1.select()
                window_chkbtn_inv_3_1 = canvas.create_window(709, 500, anchor="nw", window=chkbtn_inv_3_1)

                comb_inv_3_3 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_inv_3_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                comb_inv_3_3.current(0)
                window_comb_inv_3_3 = canvas.create_window(710, 530, anchor="nw", width=540, height=30,window=comb_inv_3_3)

                label_1 = Label(canvas,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(705, 600, anchor="nw", window=label_1)

                comb_inv_3_4 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_inv_3_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                comb_inv_3_4.current(0)
                window_comb_inv_3_4 = canvas.create_window(710, 630, anchor="nw", width=540, height=30,window=comb_inv_3_4)

                inv_bac_btn_3_1=Button(canvas,text='Back', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=inv_add_item)
                window_inv_bac_btn_3_1 = canvas.create_window(450, 800, anchor="nw", window=inv_bac_btn_3_1)

                inv_sub_btn_3_1=Button(canvas,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                window_inv_sub_btn_3_1 = canvas.create_window(685, 800, anchor="nw", window=inv_sub_btn_3_1)


            expense_btn=Button(p_canvas_2,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=inv_exp_acc_1)
            window_expense_btn = p_canvas_2.create_window(0, 0, anchor="nw", window=expense_btn,tags=('ipbutton4'))

            label_1 = Label(p_canvas_2,width=15,height=1,text="Reverse Charge %", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel21'))

            str_inv_item_2 = StringVar()
            entry_inv_item_11=Entry(p_canvas_2,width=90,justify=LEFT,background='#2f516f',foreground="white",textvariable=str_inv_item_2)
            str_inv_item_2.set(' 0')
            window_entry_entry_inv_item_11 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_11,tags=('ipentry11'))

            label_1 = Label(p_canvas_2,width=15,height=1,text="Preferred Supplier", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = p_canvas_2.create_window(0, 0, anchor="nw", window=label_1,tags=('iplabel22'))

            comb_inv_item_7 = ttk.Combobox(p_canvas_2, font=('arial 10'),foreground="white")
            comb_inv_item_7['values'] = ("Select Supplier",)
            comb_inv_item_7.current(0)
            window_comb_inv_item_7 = p_canvas_2.create_window(0, 0, anchor="nw", width=540, height=30,window=comb_inv_item_7,tags=('ipcombo7'))

            inv_sub_btn1=Button(p_canvas_2,text='SUBMIT', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
            window_inv_sub_btn1 = p_canvas_2.create_window(0, 0, anchor="nw", window=inv_sub_btn1,tags=('ipbutton5'))

            entry_inv_item_5=DateEntry(p_canvas_2,width=60,justify=LEFT,background='#2f516f',foreground="white")
            window_entry_entry_inv_item_5 = p_canvas_2.create_window(0, 0, anchor="nw", height=30,window=entry_inv_item_5,tags=('ipdate1'))


        p_btn_1=Button(p_canvas_1,text='Add Item', width=20,height=1,foreground="white",background="blue",font='arial 12',command=inv_add_item)
        window_p_btn_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=p_btn_1,tags=('apbutton1'))

        p_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=("appoly4"))

        label_1 = Label(p_canvas_1,width=11,height=1,text="Non-Inventory", font=('arial 20'),background="#2f516f",fg="white") 
        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel4'))

        label_1 = Label(p_canvas_1,width=46,height=2,text="A non-inventory is a type of product that is procured, sold, \nconsumed in production but we do not keep inventories for it.", font=('arial 12'),background="#2f516f",fg="white") 
        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel5'))

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
            window_entry_non_item_1 = canvas.create_window(55, 530, anchor="nw", height=30,window=entry_non_item_1)

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
            chkbtn_non_item = Checkbutton(canvas, text = "I sell this product/service to my customers.", variable = chk_str_non_item, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
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
            chkbtn_non_item_1 = Checkbutton(canvas, text = "Inclusive of tax", variable = chk_str_non_item_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
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
                comb_non_2_2['values'] = ("Discounts/Refunds Given","Non-Profit Income","Other Primary Income","Revenue-General","Sales-Retail","Sales-Wholesale","Sales of Product Income","Service/Fee Income","Unapplied Cash Payment Inncome",)
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
                chkbtn_non_2_1 = Checkbutton(canvas, text = "Is sub-account", variable = chk_str_non_2_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                chkbtn_non_2_1.select()
                window_chkbtn_non_2_1 = canvas.create_window(709, 500, anchor="nw", window=chkbtn_non_2_1)

                comb_non_2_3 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_non_2_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                comb_non_2_3.current(0)
                window_comb_non_2_3 = canvas.create_window(710, 530, anchor="nw", width=540, height=30,window=comb_non_2_3)

                label_1 = Label(canvas,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(705, 600, anchor="nw", window=label_1)

                comb_non_2_4 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_non_2_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
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
            chkbtn_non_pitem = Checkbutton(canvas, text = "I Purchase this product/service from Supplier.", variable = chk_str_non_pitem, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
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
            chkbtn_non_item_2 = Checkbutton(canvas, text = "Inclusive of purchase tax", variable = chk_str_non_item_2, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
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
                comb_non_3_2['values'] = ("Advertising/Promotional","Amortisation Expense","Auto","Bad Debts","Bank Charges","Borrowing Cost","Charitable Contributions","Commision and Fees","Cost of Labour","Dues and Subscriptions","Equipment Rental","Finance Costs","Income Tax Expense","Insurance","Interest Paid","Legal and Professional Fees","Loss on Discontinued Operations, Net of Tax","Management Compensation","Meals and Entertainment","Office/General Administrative Expenses","Other Miscellaneous Service Cost","Other Selling Expenses","Payroll Expenses","Rent or Lease of Building","Repair and Maintanance","Shipping and Delivery Expense","Shipping, Freight and Delivery","Supplies and Materials","Taxes Paid","Travel Expenses-Gereral and Admin Expenses","Travel Expenses-Selling Expense","Unapplied Cash Bill Payment Expense","Utilities",)
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
                chkbtn_non_3_1 = Checkbutton(canvas, text = "Is sub-account", variable = chk_str_non_3_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                chkbtn_non_3_1.select()
                window_chkbtn_non_3_1 = canvas.create_window(709, 500, anchor="nw", window=chkbtn_non_3_1)

                comb_non_3_3 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_non_3_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                comb_non_3_3.current(0)
                window_comb_non_3_3 = canvas.create_window(710, 530, anchor="nw", width=540, height=30,window=comb_non_3_3)

                label_1 = Label(canvas,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(705, 600, anchor="nw", window=label_1)

                comb_non_3_4 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_non_3_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
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

        p_btn_2=Button(p_canvas_1,text='Add Item', width=20,height=1,foreground="white",background="blue",font='arial 12',command=non_add_item)
        window_p_btn_2 = p_canvas_1.create_window(0, 0, anchor="nw", window=p_btn_2,tags=('apbutton2'))

        p_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=("appoly5"))

        label_1 = Label(p_canvas_1,width=10,height=1,text="Services", font=('arial 20'),background="#2f516f",fg="white") 
        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel6'))

        label_1 = Label(p_canvas_1,width=45,height=2,text="A service is a transaction in which no physical goods are \ntransferred from the seller to the buyer.", font=('arial 12'),background="#2f516f",fg="white") 
        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel7'))

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
            chkbtn_ser_item = Checkbutton(canvas, text = "I sell this product/service to my customers.", variable = chk_str_ser_item, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
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
            chkbtn_ser_item_1 = Checkbutton(canvas, text = "Inclusive of tax", variable = chk_str_ser_item_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
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

            def ser_inc_acc_1():
                pro_frame_4.grid_forget()
                pro_frame_4_1 = Frame(tab3_4)
                pro_frame_4_1.grid(row=0,column=0,sticky='nsew')
                canvas=Canvas(pro_frame_4_1, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))
                
                vertibar=Scrollbar(pro_frame_4_1, orient=VERTICAL)
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

                comb_ser_2_1 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_ser_2_1['values'] = ("Account Receivable(Debtors)","Current Assets","Bank","Fixed Assets","Non-Current Assets","Accounts Payable(Creditors)","Credit Card","Current Liabilities","Non-Current Liabilities","Equity","Income","Other Income","Cost of Goods Sold","Expenses","Other Expenses",)
                comb_ser_2_1.current(0)
                window_comb_ser_2_1 = canvas.create_window(55, 330, anchor="nw", width=540, height=30,window=comb_ser_2_1)

                label_1 = Label(canvas,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(710, 300, anchor="nw", window=label_1)

                entry_ser_2_2=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_ser_2_2 = canvas.create_window(710, 330, anchor="nw", height=30,window=entry_ser_2_2)

                label_1 = Label(canvas,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(54, 400, anchor="nw", window=label_1)

                comb_ser_2_2 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_ser_2_2['values'] = ("Account Receivable(Debtors)",)
                comb_ser_2_2.current(0)
                window_comb_ser_2_2 = canvas.create_window(55, 430, anchor="nw", width=540, height=30,window=comb_ser_2_2)

                label_1 = Label(canvas,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(705, 400, anchor="nw", window=label_1)

                entry_ser_2_4=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_ser_2_4 = canvas.create_window(710, 430, anchor="nw", height=30,window=entry_ser_2_4)

                ser_text_2 = Text(canvas,width=67, height=14, background='black',foreground='white')
                ser_text_2.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                window_ser_text_2 = canvas.create_window(55, 500, anchor="nw",window=ser_text_2)

                chk_str_ser_2_1 = StringVar()
                chkbtn_ser_2_1 = Checkbutton(canvas, text = "Is sub-account", variable = chk_str_ser_2_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                chkbtn_ser_2_1.select()
                window_chkbtn_ser_2_1 = canvas.create_window(709, 500, anchor="nw", window=chkbtn_ser_2_1)

                comb_ser_2_3 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_ser_2_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                comb_ser_2_3.current(0)
                window_comb_ser_2_3 = canvas.create_window(710, 530, anchor="nw", width=540, height=30,window=comb_ser_2_3)

                label_1 = Label(canvas,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(705, 600, anchor="nw", window=label_1)

                comb_ser_2_4 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_ser_2_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                comb_ser_2_4.current(0)
                window_comb_ser_2_4 = canvas.create_window(710, 630, anchor="nw", width=540, height=30,window=comb_ser_2_4)

                ser_bac_btn_2_1=Button(canvas,text='Back', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=ser_add_item)
                window_ser_bac_btn_2_1 = canvas.create_window(450, 800, anchor="nw", window=ser_bac_btn_2_1)

                ser_sub_btn_2_1=Button(canvas,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                window_ser_sub_btn_2_1 = canvas.create_window(685, 800, anchor="nw", window=ser_sub_btn_2_1)

            income_ser_btn=Button(canvas,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=ser_inc_acc_1)
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
            comb_ser_iitem_7['values'] = ("Choose...","Stock Broking","Genral Insurance","Courier","Advertsing Agency","Consulting Engineer","Custom House Agent","Steamer Agent","Clearing and Forwarding","Man power Recruiting","Air Travel Agent","Tour operator","Rent a Cab","Architect","Interior Director","Management Consultment","Chartered Accountant","Cost Accountant","Company Scretary","Real Estate Agent","Security Agency","Credit Rating Agency","Market Research Agency","Underwriter","Beauty Parlor","Cargo Handling","Cable Operators","Dry Cleaning","Event Management","Fashion Designer","Life Insurance","Scientific and Technical Consultancy","Photography","Convention Services","Video Tape Production","Sound Recording","Broadcating","Insurance Auxilary Service","banking and Other Financial","Port Services","Authorised Service Station","Health Club and Fitness Centres","Rail Travel Agent","Storage and Warehousing","Business Auxilary","Commercial Coaching","Erection or Installation","Franchise Service","Internet Cafe","Maintanance or Repair","Technical Testing","Technical Inspection","Foreign Exchange Broking","Port","Airport Services","Air Transport","Business Exhibition","Goods Transport","Construction of Commerce Complex","Intellectual Property Service","Opinion Poll Service","Outdoor Catering","Television and Radio Program Production","Survey and Exploration of Minerals","Pandal and Shamiana","Travel Agent","Forward Contract Brokerage","Transport Through Pipeline","Site Preparation","Dredging","Survey and Map Making","Cleaning Service","Clubs and Association Service","Packaging Service","Mailing List Compilation","Residential Complex Construction","Share Transfer Agent","ATM Maintanance","Recovery Agent","Sale of Space for Advertisement","Sponsorship","International Air Travel","Containerised Rail Transport","Business Support Service","Action Service","Public Relation Management","Ship Management","Internet Telephony","Cruise Ship Tour","Credit Card","Telecommunication Service","Mining of Minerals, Oil or Gas","Recting Immovable Property","Works Contract","Development of Consent","Asset Management","Design Services","Information Technology Services","ULIP Management","Stock Exchange Service","Service for Transaction in Goods","Clearing House Services","Supply of Tangiable","Online Inforamtion Retrieval","Mandap keeper",)
            comb_ser_iitem_7.current(0)
            window_comb_ser_iitem_7 = canvas.create_window(900, 1210, anchor="nw", width=345, height=30,window=comb_ser_iitem_7)

            canvas.create_line(55, 1275, 1260, 1275, fill='gray',width=1)

            label_1 = Label(canvas,width=25,height=1,text="Purchasing information", font=('arial 12'),background="#1b3857",fg="white") 
            window_label_1 = canvas.create_window(26, 1300, anchor="nw", window=label_1)

            chk_str_ser_pitem = StringVar()
            chkbtn_ser_pitem = Checkbutton(canvas, text = "I Purchase this product/service from Supplier.", variable = chk_str_ser_pitem, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
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
            chkbtn_sser_item_2 = Checkbutton(canvas, text = "Inclusive of Tax", variable = chk_str_sser_item_2, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
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

            def ser_exp_acc_1():
                pro_frame_4.grid_forget()
                pro_frame_4_2 = Frame(tab3_4)
                pro_frame_4_2.grid(row=0,column=0,sticky='nsew')
                canvas=Canvas(pro_frame_4_2, bg='#2f516f', width=953, height=600, scrollregion=(0,0,700,2050))
                
                vertibar=Scrollbar(pro_frame_4_2, orient=VERTICAL)
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

                comb_ser_3_1 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_ser_3_1['values'] = ("Account Receivable(Debtors)","Current Assets","Bank","Fixed Assets","Non-Current Assets","Accounts Payable(Creditors)","Credit Card","Current Liabilities","Non-Current Liabilities","Equity","Income","Other Income","Cost of Goods Sold","Expenses","Other Expenses",)
                comb_ser_3_1.current(0)
                window_comb_ser_3_1 = canvas.create_window(55, 330, anchor="nw", width=540, height=30,window=comb_ser_3_1)

                label_1 = Label(canvas,width=5,height=1,text="*Name", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(710, 300, anchor="nw", window=label_1)

                entry_ser_3_2=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_ser_3_2 = canvas.create_window(710, 330, anchor="nw", height=30,window=entry_ser_3_2)

                label_1 = Label(canvas,width=10,height=1,text="*Detail Type", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(54, 400, anchor="nw", window=label_1)

                comb_ser_3_2 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_ser_3_2['values'] = ("Account Receivable(Debtors)",)
                comb_ser_3_2.current(0)
                window_comb_ser_3_2 = canvas.create_window(55, 430, anchor="nw", width=540, height=30,window=comb_ser_3_2)

                label_1 = Label(canvas,width=10,height=1,text="Description", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(705, 400, anchor="nw", window=label_1)

                entry_ser_3_4=Entry(canvas,width=90,justify=LEFT,background='#2f516f',foreground="white")
                window_entry_ser_3_4 = canvas.create_window(710, 430, anchor="nw", height=30,window=entry_ser_3_4)

                ser_text_3 = Text(canvas,width=67, height=14, background='black',foreground='white')
                ser_text_3.insert(END, 'Use Cash and Cash Equivalents to track cash or assets that can be converted into cash immediately. For example, marketable securities and Treasury bills.')
                window_ser_text_3 = canvas.create_window(55, 500, anchor="nw",window=ser_text_3)

                chk_str_ser_3_1 = StringVar()
                chkbtn_ser_3_1 = Checkbutton(canvas, text = "Is sub-account", variable = chk_str_ser_3_1, onvalue = 1, offvalue = 0, font=("arial", 12),background="#1b3857",foreground="white",selectcolor="#2f516f")
                chkbtn_ser_3_1.select()
                window_chkbtn_ser_3_1 = canvas.create_window(709, 500, anchor="nw", window=chkbtn_ser_3_1)

                comb_ser_3_3 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_ser_3_3['values'] = ("Deferred CGST","Deferred GST Input Credit","Deferred IGST","Deferred Krishi Kalyan Cess Input Credit","Deferred Service Tax Input Credit","Deferred SGST","Deferred VAT Input Credit","GST Refund","Inventory Asset","Paid Insurance","Service Tax Refund","TDS Receivable","Uncategorised Asset","Accumulated Depreciation","Building and Improvements","Furniture and Equipment","Land","Leasehold Improvements","CGST Payable","CST Payable","CST Suspense","GST Payable","GST Suspense","IGST Payable","Input CGST","Input CGST Tax RCM","Input IGST","Input IGST Tax RCM","Input Krishi Kalyan Cess","Input Krishi Kalyan Cess RCM","Input Service Tax","Input Service Tax RCM","Input SGST","Input SGST Tax RCM","Input VAT 14%","Input VAT 4%","Input VAT 5%","Krishi Kalyan Cess Payable","Krishi Kalyan Cess Suspense","Output CGST","Output CGST Tax RCM","Output CST 2%","Output IGST","Output IGST Tax RCM","Output Krishi Kalyan Cess","Output Krishi Kalyan Cess RCM","Output Service Tax","Output Sevice Tax RCM","Output SGST","Output SGST Tax RCM","Output VAT 14%","Output VAT 4%","Output VAT 5%","Service Tax Payable","service Tax Suspense","SGST Payable","SGST Suspense","Swachh Barath Cess Payable" ,"Swachh Barath Cess Suspense" ,"TDS Payable" ,"VAT Payable","VAT Suspense","Opening Balance","Equity",)
                comb_ser_3_3.current(0)
                window_comb_ser_3_3 = canvas.create_window(710, 530, anchor="nw", width=540, height=30,window=comb_ser_3_3)

                label_1 = Label(canvas,width=15,height=1,text="Default Tax Code", font=('arial 12'),background="#1b3857",fg="white") 
                window_label_1 = canvas.create_window(705, 600, anchor="nw", window=label_1)

                comb_ser_3_4 = ttk.Combobox(canvas, font=('arial 10'),foreground="white")
                comb_ser_3_4['values'] = ("18.0% IGST","14.00% ST","0% IGST","Out of Scope","0% GST","14.5% ST","14.0% VAT","6.0% IGST","28.0% IGST","15.0% ST","28.0% GST","12.0% GST","18.0% GST","3.0% GST","0.2% IGST","5.0% GST","6.0% GST","0.2% GST","Exempt IGST","3.0% IGST","4.0% VAT","5.0% IGST","12.36% ST","5.0% VAT","Exempt GST","12.0% IGST","2.0% CST",)
                comb_ser_3_4.current(0)
                window_comb_ser_3_4 = canvas.create_window(710, 630, anchor="nw", width=540, height=30,window=comb_ser_3_4)

                ser_bac_btn_3_1=Button(canvas,text='Back', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=ser_add_item)
                window_ser_bac_btn_3_1 = canvas.create_window(450, 800, anchor="nw", window=ser_bac_btn_3_1)

                ser_sub_btn_3_1=Button(canvas,text='Create', width=20,height=2,foreground="white",background="#1b3857",font='arial 12')
                window_ser_sub_btn_3_1 = canvas.create_window(685, 800, anchor="nw", window=ser_sub_btn_3_1)

            expense_ser_btn=Button(canvas,text='+', width=5,height=1,foreground="white",background="#1b3857",font='arial 12',command=ser_exp_acc_1)
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

        p_btn_3=Button(p_canvas_1,text='Add Item', width=20,height=1,foreground="white",background="blue",font='arial 12',command=ser_add_item)
        window_p_btn_3 = p_canvas_1.create_window(0, 0, anchor="nw", window=p_btn_3,tags=('apbutton3'))

        p_canvas_1.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,smooth=True,fill="#2f516f",tags=("appoly6"))

        label_1 = Label(p_canvas_1,width=10,height=1,text="Bundle", font=('arial 20'),background="#2f516f",fg="white") 
        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel8'))

        label_1 = Label(p_canvas_1,width=46,height=2,text="A bundle is a group of software programs or hardware \ndevices that are grouped together and sold as one.", font=('arial 12'),background="#2f516f",fg="white") 
        window_label_1 = p_canvas_1.create_window(0, 0, anchor="nw", window=label_1,tags=('aplabel9'))

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


        p_btn_4=Button(p_canvas_1,text='Add Item', width=20,height=1,foreground="white",background="blue",font='arial 12',command=bun_add_item)
        window_p_btn_4 = p_canvas_1.create_window(0, 0, anchor="nw", window=p_btn_4,tags=('apbutton4'))

        def pro_back_1():
            pro_frame_1.grid_forget()
            pro_frame.grid(row=0,column=0,sticky='nsew')

        pbck_btn1=Button(p_canvas_1,text='← Back', bd=0, foreground="white",background="#2f516f",font='arial 10 bold',activebackground="#1b3857",command=pro_back_1)
        window_pbck_btn1 = p_canvas_1.create_window(0, 0, anchor="nw", window=pbck_btn1,tags=('apbutton5'))


    pbtn1=Button(pro_canvas,text='Add Products', width=20,height=2,foreground="white",background="#1b3857",font='arial 12',command=add_product)
    window_pbtn1 = pro_canvas.create_window(1050, 430, anchor="nw", window=pbtn1,tags=('pbutton1'))

    

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