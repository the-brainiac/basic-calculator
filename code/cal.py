from tkinter import *
import tkinter.messagebox as tmsg

def button1(n):
	new=eqn.get()+n
	# if len(new)>25:
	# 	tmsg.showinfo("Limit Exceed","Can't Enter More Numbers limit exceed")
	# else:
	# 	eqn.set(new)
	eqn.set(new)
def cal_clear():
	eqn.set('')
	l1=Label(root,text='',font='lucida 15 normal',width=20,pady=15,borderwidth=2,relief=SUNKEN).grid(row=0,column=0)
def cal_cut():
	new=eqn.get()
	new=new[:len(new)-1]
	eqn.set(new)

def result():
	str=eqn.get()
	try:
		res=eval(str)
	except:
		res = "Can't devide by zero" 
	l1=Label(root,text=(res),font='lucida 15 normal',width=20,pady=15,borderwidth=2,relief=SUNKEN).grid(row=0,column=0)

root=Tk()
root.geometry('280x250')
root.title("Calculator")
root.minsize(280,250)
root.maxsize(280,250)
# root.iconbitmap("/home/brainiac/Tkinter/calc.ico")
# root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='calc1.png'))

eqn=StringVar()
eqn.set('')
l1=Label(root,text='',font='lucida 15 normal',width=20,pady=15,borderwidth=2,relief=SUNKEN).grid(row=0,column=0)
e1=Entry(root,font='lucida 14 normal',width=22,textvariable=eqn).grid(row=1,column=0)
frame=Frame(root)
Button(frame,text='9',width=5,command=lambda: button1('9')).grid(row=3,column=0)
Button(frame,text='8',width=5,command=lambda: button1('8')).grid(row=3,column=1)
Button(frame,text='7',width=5,command=lambda: button1('7')).grid(row=3,column=2)
Button(frame,text='6',width=5,command=lambda: button1('6')).grid(row=4,column=0)
Button(frame,text='5',width=5,command=lambda: button1('5')).grid(row=4,column=1)
Button(frame,text='4',width=5,command=lambda: button1('4')).grid(row=4,column=2)
Button(frame,text='3',width=5,command=lambda: button1('3')).grid(row=5,column=0)
Button(frame,text='2',width=5,command=lambda: button1('2')).grid(row=5,column=1)
Button(frame,text='1',width=5,command=lambda: button1('1')).grid(row=5,column=2)
Button(frame,text='.',width=5,command=lambda: button1('.')).grid(row=6,column=0)
Button(frame,text='0',width=5,command=lambda: button1('0')).grid(row=6,column=1)
Button(frame,text='+',width=5,command=lambda: button1('+')).grid(row=6,column=2)
Button(frame,text='/',width=5,command=lambda: button1('/')).grid(row=3,column=3)
Button(frame,text='*',width=5,command=lambda: button1('*')).grid(row=4,column=3)
Button(frame,text='-',width=5,command=lambda: button1('-')).grid(row=5,column=3)
Button(frame,text='=',width=5,bg='grey',command=result).grid(row=6,column=3)
Button(frame,text='C',width=5,command=cal_clear).grid(row=2,column=0)
Button(frame,text='❎',width=5,command=cal_cut).grid(row=2,column=1)
Button(frame,text='(',width=5,command=lambda: button1('(')).grid(row=2,column=2)
Button(frame,text=')',width=5,command=lambda: button1(')')).grid(row=2,column=3)
frame.grid(row=2,column=0)
root.mainloop()
