from tkinter import*

root=Tk()
root.title("registration")
root.geometry("600x470")
root.resizable(False,False)

def register():
    print("registered")
   
Label(root,text="python Registration from",font="arial 25").pack(pady=50)
Label(text="Name",font=23).place(x=100,y=150)
Label(text="phone",font=23).place(x=100,y=200)
Label(text="Genter",font=23).place(x=100,y=250)
Label(text="Email", font=23).place(x=100,y=300)

        #entryf
nameValue=StringVar()
PhoneValue=StringVar()
genderValue=StringVar()
emailvalue=StringVar()
    
nameEntry=Entry(root,textvariable=nameValue,width=30,bd=2,font=20)
phoneEntry=Entry(root,textvariable=PhoneValue,width=30,bd=2,font=20)
genterEntry=Entry(root,textvariable=genderValue,width=30,bd=2,font=20)
emailEntry=Entry(root,textvariable=emailvalue,width=30,bd=2,font=20)

nameEntry.place(x=200,y=150)
phoneEntry.place(x=200,y=200)
genterEntry.place(x=200,y=250)
emailEntry.place(x=200,y=300)

    #check button
checkValue=IntVar
checkbtn=Checkbutton(text="remember me", variable=checkValue)
checkbtn.place(x=200,y=340)


Button(text="Register",font=20,width=11,height=2,command=register).place(x=250,y=380)

root,mainloop()