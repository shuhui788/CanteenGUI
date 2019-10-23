import tkinter as tk
import datetime
import time as TIME
today = datetime.datetime.now()
now = str(today)
hour = int(now[11:13])
minute = int(now[14:16])
sec = int(now[17:19])
time1 = int(now[11:13]+now[14:16]) # time1 is the current 24 hour time
day = today.strftime('%A')


miniwok_open = 0
miniwok_close = 0

chicken_open = 0
chicken_close = 0

macs_open = 0
macs_close = 0
# the above are the open and close timings, are assigned their values in their Stall Classes

def stallIsClosedlabel(opening, closing, display_text): # adds text into a label saying that the stall is closed during the closing hours
    if opening< time1 <closing:
        print("") # do nothing
    else: # if stall is closed
        display_text.set("Stall is closed")


def qTiming(pax, time, textBox):
    time_to_wait = 0
    multiplier = 0.7 # multiplier exists only to deflate the time taken for queueing, can edit according to preference
    try:
        pax = int(pax) # pax comes as a string input from the textbox, here converted to int form
        textBox.delete(0, 'end')
        if time == "morning":
            time_to_wait = pax * 1 * multiplier  # least in the morning
        elif time == "afternoon":
            time_to_wait = pax * 3 * multiplier  # most in the afternoon
        elif time == "evening":
            time_to_wait = pax * 2 * multiplier  # second most in evening
        elif time == "closed":
            time_to_wait = "Stall is closed"
        if time == "closed":
            string_output = str(time_to_wait)
        else:
            string_output = str(int(time_to_wait)) + " minutes of waiting time." # time to wait is made to be be an int first because the multiplier converts it to float
        textBox.insert(0, string_output)

    except ValueError: # arises when user inputs a non number into the textbox
        textBox.delete(0, 'end') # deletes the incorrect user input, end references the last string series input into the entry box
        textBox.insert(0, 'Please type the numerical form of people queuing: ')


def timeOfDayDecider(opening, closing): # takes the current system time and decides whether it's morning, afternoon or evening
    # used in the qTiming function to show how much a group of ppl will need to queue for a stall
    time = None
    if 0 <= time1  <= opening or opening == 0: # the second part is due to some stalls being closed on sunday, during which their stallname_open value will be set to 0
        time = "closed"
    elif opening <= time1 <= 1200:
        time = "morning"
    elif 1200 <= time1  <= 1700:
        time = "afternoon"
    elif 1700 <= time1  <= closing:
        time = "evening"
    return time


class NTUsystem(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self) # init function of tk.Tk. is being called, therefore constructing everything in it
        self._frame = None
        self.switch_frame(HomePage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class HomePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Real Time NTU Canteen System", font=('Helvetica', 20, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="View Stalls", width = 40,
                  command=lambda: master.switch_frame(ViewS)).pack()
        tk.Button(self, text="Set date and time", width = 40,
                  command=lambda: master.switch_frame(dateT)).pack()
        tk.Button(self, text="Exit", width = 40, command=self.destroy).pack()

class ViewS(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self, text="View Stalls", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Mini Wok", width = 40,
                  command=lambda: master.switch_frame(miniwok)).pack()
        tk.Button(self, text="Chicken Rice", width = 40,
                  command=lambda: master.switch_frame(chicken)).pack()
        tk.Button(self, text="McDonald's", width = 40,
                  command=lambda: master.switch_frame(mac)).pack()
        tk.Button(self, text="Return to Home Page", width = 40,
                  command=lambda: master.switch_frame(HomePage)).pack()

class miniwok(tk.Frame):
    def __init__(self, master):
        global miniwok_open
        global miniwok_close # opening and closing times for miniwok. declared as global here to be used by multiple classes and functions
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)

        tk.Label(self, text="Mini Wok", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        display_text = tk.StringVar()
        weAreClosedLabel = tk.Label(self, textvariable = display_text, font=('Helvetica', 18)).pack() # display_text will be empty unless stall is closed
        if day == 'Sunday':
            miniwok_open = 0
            display_text.set("Stall is closed today")
        elif day == "Saturday":
            miniwok_open = 830
            miniwok_close = 1700
            stallIsClosedlabel(830, 1700, display_text)
        else:
            miniwok_open = 830
            miniwok_close = 2130
            stallIsClosedlabel(830, 2130, display_text)

        with open('menu information.txt') as menu:
            for i, line in enumerate(menu.readlines()): # displays the part of the menu that belongs to miniwok
                if i >= 1 and i <= 5:
                    menuminiwok = tk.Message(self, text=line, font=('Helvetica', 10), width=10000).pack(side="top")
                '''if day == 'Sunday':
                    tk.Label(self, text="The stall is closed today.", font=('Helvetica', 18, "bold")).pack(side="top")
                elif day == 'Saturday':
                    if time1>1700 and time1<830:
                        tk.Label(self, text="The stall is closed now.", font=('Helvetica', 18, "bold")).pack(side="top")
                    else:
                        for i,line in enumerate(menu.readlines()):
                            if i>=1 and i<=5:
                                menuminiwok = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
                else:
                    if time1>2130 and time1<830:
                        tk.Label(self, text="The stall is closed now.", font=('Helvetica', 18, "bold")).pack(side="top")
                    else:
                        for i,line in enumerate(menu.readlines()):
                            if i>=1 and i<=5:
                                menuminiwok = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")''' # This codeblock can be removed if we want show the menu when the stall is closed
                # ... however if we use it need to fix some of the if conditions cos (time1>2130 and time1<830) can never be true
        tk.Button(self, text="Calculate the estimated waiting time", width = 40,
                  command=lambda: master.switch_frame(WaitTMiniwok)).pack()
        tk.Button(self, text="View operating hours", width = 40,
                  command=lambda: master.switch_frame(Oper1)).pack()
        tk.Button(self, text="Return", width = 40,
                  command=lambda: master.switch_frame(ViewS)).pack(side=tk.BOTTOM)

class chicken(tk.Frame):
    def __init__(self, master):
        global chicken_open
        global chicken_close
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="Chicken Rice", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        display_text = tk.StringVar()
        weAreClosedLabel = tk.Label(self, textvariable=display_text, font=('Helvetica', 18)).pack()
        if day == 'Sunday':
            chicken_open = 'stallclosessunday'
            display_text.set("Stall is closed today")
        elif day == "Saturday":
            chicken_open = 830
            chicken_close = 1700
            stallIsClosedlabel(830, 1700, display_text)
        else:
            chicken_open = 830
            chicken_close = 2130
            stallIsClosedlabel(830, 2130, display_text)
        with open ('menu information.txt') as menu:
            for i, line in enumerate(menu.readlines()):
                if i >= 1 and i <= 5:
                    menuchicken = tk.Message(self, text=line, font=('Helvetica', 10), width=10000).pack(side="top")
        '''with open('menu information.txt') as menu:
                if day == 'Sunday':
                    tk.Label(self, text="The stall is closed today.", font=('Helvetica', 18, "bold")).pack(side="top")
                elif day == 'Saturday':
                    if time1>1700 and time1<830:
                        tk.Label(self, text="The stall is closed now.", font=('Helvetica', 18, "bold")).pack(side="top")
                    else:
                        for i,line in enumerate(menu.readlines()):
                            if i>=1 and i<=5:
                                menuchicken = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
                else:
                    if time1>2130 and time1<830:
                        tk.Label(self, text="The stall is closed now.", font=('Helvetica', 18, "bold")).pack(side="top")
                    else:
                        for i,line in enumerate(menu.readlines()):
                            if i>=1 and i<=5:
                                menuchicken = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")''' # This codeblock can be removed if we want show the menu when the stall is closed
                                # ... same as in the miniwok class need to fix some of the errors in the if conditions if we do decide to use it
        tk.Button(self, text="Calculate the estimated waiting time", width = 40,
                  command=lambda: master.switch_frame(WaitTChicken)).pack()
        tk.Button(self, text="View operating hours", width = 40,
                  command=lambda: master.switch_frame(Oper2)).pack()
        tk.Button(self, text="Return", width = 40,
                 command=lambda: master.switch_frame(ViewS)).pack(side=tk.BOTTOM)


class mac(tk.Frame):
    def __init__(self, master):
        global macs_open
        global  macs_close
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="McDonald's", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        display_text = tk.StringVar()
        weAreClosedLabel = tk.Label(self, textvariable=display_text, font=('Helvetica', 18)).pack()
        if day == 'Sunday':
            macs_open = 1000
            macs_close = 2200
            stallIsClosedlabel(1000, 2200, display_text)
        elif day == "Saturday":
            macs_open = 700
            macs_close = 2359
            stallIsClosedlabel(700, 2359, display_text)
        else:
            macs_open = 700
            macs_close = 2359
            stallIsClosedlabel(700, 2359, display_text)
        with open('menu information.txt') as menu: # if mcdonalds is closed, show the previous menu for lunch&dinner
            if day == 'Sunday':
                for i,line in enumerate(menu.readlines()):
                    if 1000 < time1 < 1200: # if between 10AM and 12PM
                        if 16<= i <=20: # print the morning section of the macs menu
                            menumc = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
                    else: # if between 12PM and 10PM, or after close print the afternoon section of the macs menu. There will still be a label at the top ...
                        # ... saying that the stall is closed
                        if 23<= i <=27:
                            menumc = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
            else:
                for i,line in enumerate(menu.readlines()):
                    if 700<= time1 <=1100: # if during morning time from monday to saturday
                        if 16<= i <=20:
                            menumc = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
                    else:
                        if 23<= i <=27:
                            menumc = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")

        tk.Button(self, text="Calculate the estimated waiting time", width = 40,
                  command=lambda: master.switch_frame(WaitTMacs)).pack()
        tk.Button(self, text="View operating hours", width = 40,
                  command=lambda: master.switch_frame(Oper3)).pack()
        tk.Button(self, text="Return", width=40,
                  command=lambda: master.switch_frame(ViewS)).pack(side=tk.BOTTOM)





class WaitTMiniwok(tk.Frame): # Frame that displays waitings times for a specific length of queue
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        entry = tk.Entry(self, width = 50)
        entry.pack()
        calculationButton = tk.Button(self, text="Insert no. pax and calculate Q timing", command=lambda: qTiming(entry.get(),
                                                                                                                  timeOfDayDecider(miniwok_open, miniwok_close),
                                                                                                                  calcDisplay)).pack()
        calcDisplay = tk.Entry(self, text = "", width = 50)
        calcDisplay.pack()
        # KK NVM the only thing the button should do is execute func to send output to the texbox
        returnButton = tk.Button(self, text="Return", width=40,
                  command=lambda: master.switch_frame(miniwok)).pack(side=tk.BOTTOM)

class WaitTChicken(tk.Frame): # Frame that displays waitings times for a specific length of queue
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        entry = tk.Entry(self, width = 50)
        entry.pack()
        calculationButton = tk.Button(self, text="Insert no. pax and calculate Q timing", command=lambda: qTiming(entry.get(),
                                                                                                                  timeOfDayDecider(chicken_open, chicken_close),
                                                                                                                  calcDisplay)).pack()
        calcDisplay = tk.Entry(self, text = "", width = 50)
        calcDisplay.pack()
        returnButton = tk.Button(self, text="Return", width=40,
                  command=lambda: master.switch_frame(chicken)).pack(side=tk.BOTTOM)

class WaitTMacs(tk.Frame): # Frame that displays waitings times for a specific length of queue
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        entry = tk.Entry(self, width = 50)
        entry.pack()
        calculationButton = tk.Button(self, text="Insert no. pax and calculate Q timing", command=lambda: qTiming(entry.get(),
                                                                                                                  timeOfDayDecider(macs_open, macs_close),
                                                                                                                  calcDisplay)).pack()
        calcDisplay = tk.Entry(self, text = "", width = 50)
        calcDisplay.pack()
        # KK NVM the only thing the button should do is execute func to send output to the texbox
        returnButton = tk.Button(self, text="Return", width=40,
                  command=lambda: master.switch_frame(mac)).pack(side=tk.BOTTOM)
class Oper1(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="View the operating hours", font=('Helvetica', 18, "bold")).pack(side="top")
        with open('operating time.txt') as oper:
            for i,line in enumerate(oper.readlines()):
                if i>=1 and i<=6:
                    mini = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
        tk.Button(self, text="Return", width = 40,
                  command=lambda: master.switch_frame(miniwok)).pack()
#operating hours for mini wok

class Oper2(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="View the operating hours", font=('Helvetica', 18, "bold")).pack(side="top")
        with open('operating time.txt') as oper:
            for i,line in enumerate(oper.readlines()):
                if i>=9 and i<=14:
                    chick = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
        tk.Button(self, text="Return", width = 40,
                  command=lambda: master.switch_frame(chicken)).pack()
#operating hours for chicken rice

class Oper3(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="View the operating hours", font=('Helvetica', 18, "bold")).pack(side="top")
        with open('operating time.txt') as oper:
            for i,line in enumerate(oper.readlines()):
                if i>=17 and i<=22:
                    mc_message = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
                    # do not rename the above mc_message variable to mac, that'll cause an error in the switch_frame.
        tk.Button(self, text="Return", width=40,
                  command=lambda: master.switch_frame(mac)).pack()
#operating hours for mcdonald

class dateT(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="Set system date and time", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Return to Home Page", width = 40,
                  command=lambda: master.switch_frame(HomePage)).pack()


m = NTUsystem()
m.title('NTU Canteen System')
m.mainloop()
