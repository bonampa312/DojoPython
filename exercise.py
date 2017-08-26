from tkinter import*

root = Tk()
root.geometry("1200x600+0+0")
root.title("Dojo python")

text_input = StringVar()
operator = ""

Tops = Frame(root, width=1200, height = 90, bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)


frame = Frame(root, width=1200, height = 600, bg="powder blue", relief=SUNKEN)
frame.pack(side=TOP)

lblinfo = Label(Tops, font=("SHOWCARD GOTHIC", 50, 'bold'), text="dojo python")
lblinfo.grid(row=0,column=0)

def btnClick(num):
	global operator
	operator = operator + str(num)
	text_input.set(operator)

def btnEval():
	global operator
	result = str(eval(operator))
	text_input.set(result)

txtDisplay = Entry(frame, font=("SHOWCARD GOTHIC", 50, 'bold'), textvariable=text_input, bg="black")
txtDisplay.grid(columnspan = 4)

btn1 = Button(frame, font=("SHOWCARD GOTHIC", 20, 'bold'), command = lambda:btnClick(1).grid(row=2,column=0))
btn2 = Button(frame, font=("SHOWCARD GOTHIC", 20, 'bold'), command = lambda:btnClick(2).grid(row=2,column=1))
Addition = Button(frame, font=("SHOWCARD GOTHIC", 20, 'bold'), command = lambda:btnClick('+').grid(row=2,column=2))
Equals = Button(frame, font=("SHOWCARD GOTHIC", 20, 'bold'), command = btnEval().grid(row=2,column=3))

root.mainloop()