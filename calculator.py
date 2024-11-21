import tkinter as tk
from tkinter import StringVar

class Calculator:
    def __init__(self,root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.variable = ""
        self.var = StringVar()
        self.display = tk.Entry(root,textvariable=self.var, font=("Arial",20),bg="lightgreen",fg="black", bd=10,insertwidth=2,width=14,justify='right')
        self.display.grid(row=0, column=0, columnspan=4)
        self.create_buttons()
       

        
    def click_button(self,value):
        if value == "=":
            try:
               result = str(eval(self.operator))
               self.var.set(result)
               self.operator = result 
            except Exception  as e:
                self.var.set("error")
                self.operator = ""
        elif value == "C":
            self.operator = ""
            self.var.set("")
        else:
            self.operator += str(value)
            self.var.set(self.operator)
    def create_buttons(self):
        buttons = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "C", "0", "=", "/"



        ]

        row,col = 1,0
        for button in buttons:
            tk.Button(
                self.root, text=button, padx=20,pady=20,font=("arial",14),
                bg="black",fg="white",
                command=lambda b=button: self.click_button(b)
            ).grid(row=row , column = col , sticky="nsew")
            col=col+1
            if col>3:
                col = 0
                row =row+1
if __name__=="__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()




            
        
     




