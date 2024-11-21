from tkinter import *
window = Tk()
window.title("abhinav pradeep")
window.geometry("600x500")

def findsum():
      sum = int(n1.get())+int(n2.get())
      result.set(sum)


    
 
result = StringVar() 

lb1 = Label(window, text = "number 1: ")
lb2 = Label(window, text = "number 2: ")
lb3 = Label(window, text = "result : ")

n1 = Entry(window)
n2 = Entry(window)
n3 = Entry(window,textvariable = result)

lb1.pack()
n1.pack()
lb2.pack()
n2.pack()
lb3.pack()
n3.pack()

btn1 = Button(window,text="sum",command=findsum)
btn1.pack()
window.mainloop()