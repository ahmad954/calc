from tkinter import*


a=Tk() 
#





p= Entry(a,width=50,fg="blue",bg="#fdffbc")
p.grid(row=0,column=0,padx=60,pady=70,columnspan=6)

p.get()

def myclick(number):
     gg=p.get()
     p.delete(0,END)
     p.insert(0,str(gg)+str(number))
    
    

def myclick2(number):



     p.delete(0,END)
    
    
def myclick3(number):

     f=p.get()
     global fn_num
     global math
     math="0"
     fn_num = int(f)
     p.delete(0,END)

def myclick5(number):

     f=p.get()
     global fn_num
     global math
     math="1"
     fn_num = int(f)
     p.delete(0,END)

def myclick6(number):
     f=p.get()
     global fn_num
     global math
     math="2"
     fn_num = int(f)
     p.delete(0,END)


def myclick7(number):
     f=p.get()
     global fn_num
     global math
     math="3"
     fn_num = int(f)
     p.delete(0,END)



def myclick4(number):
    f2=p.get()
    p.delete(0,END)
    if math=="0":
     p.insert(0,fn_num + int(f2))

    if math=="1":
     p.insert(0,fn_num - int(f2))

    if math=="2":

     p.insert(0,fn_num * int(f2))
    if math=="3":

     p.insert(0,fn_num / int(f2))





    
#dont forget spell (lambda)
#b=BUTTON
b0 = Button(a,text="0",command=lambda:myclick(0),padx=30,pady=30,fg="#dddddd",bg="#30475e")
b0.grid(row=1,column=0)
b1 = Button(a,text="1",command=lambda:myclick(1),padx=30,pady=30,fg="#dddddd",bg="#30475e")
b1.grid(row=1,column=1)
b2 = Button(a,text="2",command=lambda:myclick(2),padx=30,pady=30,fg="#dddddd",bg="#30475e")
b2.grid(row=1,column=2)
b3 = Button(a,text="3",command=lambda:myclick(3),padx=30,pady=30,fg="#dddddd",bg="#30475e")
b3.grid(row=1,column=3)

bplus = Button(a,text="+",command=lambda:myclick3("+"),padx=30,pady=30,fg="#dddddd",bg="#30475e")
bplus.grid(row=2,column=3)

bequal = Button(a,text="=",command=lambda:myclick4("="),padx=50,width=50,pady=30,fg="#dddddd",bg="#30475e")
bequal.grid(row=4,column=0,columnspan=6)

bclear = Button(a,text="c",command=lambda:myclick2("c"),padx=30,pady=30,fg="#dddddd",bg="#30475e")
bclear.grid(row=3,column=3)




b4 = Button(a,text="4",command=lambda:myclick(4),padx=30,pady=30,fg="#dddddd",bg="#30475e")
b4.grid(row=2,column=0)
b5 = Button(a,text="5",command=lambda:myclick(5),padx=30,pady=30,fg="#dddddd",bg="#30475e")
b5.grid(row=2,column=1)
b6 = Button(a,text="6",command=lambda:myclick(6),padx=30,pady=30,fg="#dddddd",bg="#30475e")
b6.grid(row=2,column=2)


b7 = Button(a,text="7",command=lambda:myclick(7),padx=30,pady=30,fg="#dddddd",bg="#30475e")
b7.grid(row=3,column=0)
b8 = Button(a,text="8",command=lambda:myclick(8),padx=30,pady=30,fg="#dddddd",bg="#30475e")
b8.grid(row=3,column=1)
b9 = Button(a,text="9",command=lambda:myclick(9),padx=30,pady=30,fg="#dddddd",bg="#30475e")
b9.grid(row=3,column=2)


br=Button(a,text="*",command=lambda:myclick6("*"),padx=70,pady=30,fg="#dddddd",bg="#30475e")
br.grid(row=3,column=5)

bx=Button(a,text="/",command=lambda:myclick7("/"),padx=70,pady=30,fg="#dddddd",bg="#30475e")
bx.grid(row=2,column=5)


bd=Button(a,text="-",command=lambda:myclick5("-"),padx=70,pady=30,fg="#dddddd",bg="#30475e")
bd.grid(row=1,column=5)




































a.title("calcutr")

a.mainloop()