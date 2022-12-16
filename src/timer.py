from tkinter import * 
from tkinter import messagebox
import time
# from playsound import playsound

#TODO: add playsound to the aplication

class TimerCloock(object):

    def __init__(self):
        # settings Frame
        self.root = Tk()
        self.root.title('Timer')
        self.root.geometry("400x600")
        self.root.config(bg="#000")
        self.root.resizable(False,False)

        #Images
        image1 = PhotoImage(file="eggs.png")
        self.button2 = Button(self.root,image=image1,bg="#000",bd=0,command=self.eggs)
        self.button2.place(x=7,y=300)

        image2 = PhotoImage(file="face.png")
        self.button3 = Button(self.root,image=image2,bg="#000",bd=0,command=self.face)
        self.button3.place(x=140,y=300)

        image3 = PhotoImage(file="brush.png")
        self.button4 = Button(self.root,image=image3,bg="#000",bd=0,command=self.brush)
        self.button4.place(x=270,y=300)

        heading = Label(self.root,text="Timer",font = "arial 40 bold",bg ="#000" , fg = "#ea3548")
        heading.pack(pady=10)

        # Clock Current Time
        Label(self.root,font="arial 13 bold",text="Current time: ",bg="papaya whip").place(x= 65, y = 70)
        self.current_time = Label(self.root,font="arial 13 bold",text="",fg="#000",bg="#fff")
        self.current_time.place(x=180,y=70)
        self.clock()

        # Timer 
        self.hrs = StringVar()
        Entry(self.root,textvariable=self.hrs,width=2,font="arial 50",bg="#000",fg="#fff").place(x=30,y=155)
        Label(self.root,text="hours",font="arial 12",bg="#000",fg="#fff").place(x=105,y=200)
        self.hrs.set("00")
        # Min
        self.min = StringVar()
        Entry(self.root,textvariable=self.min,width=2,font="arial 50",bg="#000",fg="#fff").place(x=150,y=155)
        Label(self.root,text="min",font="arial 12",bg="#000",fg="#fff").place(x=225,y=200)
        self.min.set("00")
        # Sec
        self.sec = StringVar()
        Entry(self.root,textvariable=self.sec,width=2,font="arial 50",bg="#000",fg="#fff").place(x=270,y=155)
        Label(self.root,text="sec",font="arial 12",bg="#000",fg="#fff").place(x=345,y=200)
        self.sec.set("00")

        #Button
        self.button = Button(self.root,text="Start",font="arial 10 bold",bg="#ea3548",fg="#fff",width=20,height=2,bd=0,command=self.start_timer)
        self.button.pack(padx = 5, pady = 40,side = BOTTOM)
        self.root.mainloop() 

    #* Functions
    def clock(self):

        """Set the current time"""

        clock_time = time.strftime('%I:%M:%S %p')
        self.current_time.config(text = clock_time)
        self.current_time.after(1000,self.clock)

    def brush(self):
        """Set the timer for brush"""
        self.hrs.set("00")
        self.min.set("02")
        self.sec.set("00")

    def face(self):
        """Set the timer for face"""
        self.hrs.set("00")
        self.min.set("15")
        self.sec.set("00")

    def eggs(self):
        """Set the timer for eggs"""
        self.hrs.set("00")
        self.min.set("10")
        self.sec.set("00")

    def start_timer(self):
        """Function that manages the timer control"""

        times = int(self.hrs.get())*3600 + int(self.min.get())*60 + int(self.sec.get()) #sets the time in seconds
        while  times > -1:
            min, second = times//60 , times % 60
            
            hour = 0
            if min >60:
                hour, min = min//60,min%60
            
            self.sec.set(second)
            self.min.set(min)
            self.hrs.set(hour)

            self.root.update()
            time.sleep(1)

            if (times == 0):
                self.hrs.set("00")
                self.min.set("00")
                self.sec.set("00")
                messagebox.showinfo(message="Time Out",title="Time is up")

            times -= 1