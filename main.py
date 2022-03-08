




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import logging
import checkfile
from checkfile import search_my_file
logging.basicConfig(filename="pdf.log",level=logging.DEBUG,format="%(asctime)s %(levelname)s %(message)s")
#logger=logging.getLogger(__name__)

#create a gui window
win=tk.Tk()
#image1 = Image.open("C:\myproject\water.png")
#image1 = ImageTk.resize((10, 5), Image.ANTIALIAS)
win.title("PDF MERGER")
win.geometry("900x360")

#create labels and entry field
path_label=ttk.Label(win,text="enter the directory path",font=("green",14,"bold"),)
path_label.grid(row=0,column=0)
path_var=tk.StringVar()
path_entry=ttk.Entry(win,width=70,textvariable=path_var)
path_entry.grid(row=0,column=1)

#create buttons and its func
def action():
    logging.info("submit button clicked")
    try:
        res_output.delete(0.0,END)
        result=checkfile.search_my_file(path_var.get(),".pdf")
        print(result)
        logging.info("inserting files in the field")
        for i in result:
            res_output.insert(END,f"{i}\n")
    except:
        pass

def clear_action():
    logging.info("clear Button clicked")
    try:
        res_output.delete(0.0,END)
        path_entry.delete((0.0,END))
    except:
        pass1
def merge_action():
    logging.info("merge button is clicked")
    try:
        final_output.delete(0.0, END)
        result=checkfile.merge_pdf(path_var.get())
        try:
            final_output.insert(END,f"{result}\n")
        except Exception as e:
            logging.error("error in inserting the merged file loc"+str(e))
    except Exception as e:
        logging.error("error occured in merge_action")
        logging.exception(e)






sub_button=Button(win,width=16,height=2,text="submit",command=action)
sub_button.grid(row=1,column=1)

clear_button=Button(win,width=16,height=2,text="clear",command=clear_action)
clear_button.grid(row=2,column=1)

merge_button=Button(win,width=16,height=2,text="merge",command=merge_action)
merge_button.grid(row=2,column=1)

#create result field
res_label=ttk.Label(win,text="your pdf files",font=16)
res_label.grid(row=1,column=0)

final_label=ttk.Label(win,text="your merged pdf files are available at",font=16)
final_label.grid(row=3,column=0)

res_output=Text(win,width=70,height=30,background="light pink",foreground="black")
res_output.grid(row=2,column=0)

final_output=Text(win,width=30,height=10,background="light pink",foreground="black")
final_output.grid(row=3,column=1)



win.mainloop()