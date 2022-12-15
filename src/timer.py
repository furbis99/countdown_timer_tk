import time
from tkinter import * 
from tkinter import messagebox
# from playsound import playsound



class TimerCloock(object):


    def __init__(self):
        # settings Frame
        root = Tk()
        root.title('Timer')
        root.geometry("400x600")
        root.config(bg="#000")
        root.resizable(False,False)

        #Image
        image1 = PhotoImage(file="eggs.png")
        self.button2 = Button(root,image=image1,bg="#000",bd=0)
        self.button2.place(x=7,y=300)

        image2 = PhotoImage(file="face.png")
        self.button3 = Button(root,image=image2,bg="#000",bd=0)
        self.button3.place(x=140,y=300)

        image3 = PhotoImage(file="brush.png")
        self.button4 = Button(root,image=image3,bg="#000",bd=0)
        self.button4.place(x=270,y=300)

        heading = Label(root,text="Timer",font = "arial 40 bold",bg ="#000" , fg = "#ea3548")
        heading.pack(pady=10)

        # Clock Current Time
        Label(root,font="arial 13 bold",text="Current time: ",bg="papaya whip").place(x= 65, y = 70)
        self.current_time = Label(root,font="arial 13 bold",text="",fg="#000",bg="#fff")
        self.current_time.place(x=180,y=70)
        self.clock()


        # Timer 
        self.hrs = StringVar()
        Entry(root,textvariable=self.hrs,width=2,font="arial 50",bg="#000",fg="#fff").place(x=30,y=155)
        Label(root,text="hours",font="arial 12",bg="#000",fg="#fff").place(x=105,y=200)
        self.hrs.set("00")
        # Min
        self.min = StringVar()
        Entry(root,textvariable=self.min,width=2,font="arial 50",bg="#000",fg="#fff").place(x=150,y=155)
        Label(root,text="min",font="arial 12",bg="#000",fg="#fff").place(x=225,y=200)
        self.min.set("00")
        # Sec
        self.sec = StringVar()
        Entry(root,textvariable=self.sec,width=2,font="arial 50",bg="#000",fg="#fff").place(x=270,y=155)
        Label(root,text="sec",font="arial 12",bg="#000",fg="#fff").place(x=345,y=200)
        self.sec.set("00")

        #Button
        self.button = Button(root,text="Start",font="arial 10 bold",bg="#ea3548",fg="#fff",width=20,height=2,bd=0)
        self.button.pack(padx = 5, pady = 40,side = BOTTOM)
        root.mainloop() 

        # Image
        




    def clock(self):

        clock_time = time.strftime('%I:%M:%S %p')
        self.current_time.config(text = clock_time)
        self.current_time.after(1000,self.clock)