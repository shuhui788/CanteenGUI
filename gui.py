import tkinter as tk
import datetime
today = datetime.datetime.now()
now = str(today)
hour = int(now[11:13])
minute = int(now[14:16])
sec = int(now[17:19])
time1 = int(now[11:13]+now[14:16])
day = today.strftime('%A')

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
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="Mini Wok", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        with open('menu information.txt') as menu:
                if day == 'Sunday':
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
                                menuminiwok = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
        tk.Button(self, text="Calculate the estimated waiting time", width = 40,
                  command=lambda: master.switch_frame(WaitTMiniwok)).pack()
        tk.Button(self, text="View operating hours", width = 40,
                  command=lambda: master.switch_frame(Oper1)).pack()
        tk.Button(self, text="Return", width = 40,
                  command=lambda: master.switch_frame(ViewS)).pack(side=tk.BOTTOM)

class chicken(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="Chicken Rice", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        with open('menu information.txt') as menu:
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
                                menuchicken = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
        tk.Button(self, text="Calculate the estimated waiting time", width = 40,
                  command=lambda: master.switch_frame(WaitTChicken)).pack()
        tk.Button(self, text="View operating hours", width = 40,
                  command=lambda: master.switch_frame(Oper2)).pack()
        tk.Button(self, text="Return", width = 40,
                 command=lambda: master.switch_frame(ViewS)).pack(side=tk.BOTTOM)


class mac(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="McDonald's", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        hour = datetime.datetime.now().hour # displays the current 24 hour format. Rounds down. e.g. 3:37PM will be 15
        if (day != 'Sunday' and 21 < hour < 9) or (day == 'Sunday' and 11 < hour < 6): # if it's currently the closing hours
            tk.Label(self, text="We're sorry, MacDonalds is closed", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        with open('menu information.txt') as menu:
            if day == 'Sunday':
                for i,line in enumerate(menu.readlines()):
                    if hour>=10 and hour<11:
                        if i>=16 and i<=20:
                            menumc = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
                    elif hour>=11 and hour<22:
                        if i>=23 and i<=27:
                            menumc = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
                    else:
                        tk.Label(self, text="McDonald's is closed now.", font=('Helvetica', 18)).pack()
            else:
                for i,line in enumerate(menu.readlines()):
                    if hour>=7 and hour<11:
                        if i>=16 and i<=20:
                            menumc = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
                    elif hour>=11 and hour<24:
                        if i>=23 and i<=27:
                            menumc = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
                    else:
                        tk.Label(self, text="McDonald's is closed now.", font=('Helvetica', 18)).pack()
        tk.Button(self, text="Calculate the estimated waiting time", width = 40,
                  command=lambda: master.switch_frame(WaitTMacs)).pack()
        tk.Button(self, text="View operating hours", width = 40,
                  command=lambda: master.switch_frame(Oper3)).pack()
        tk.Button(self, text="Return", width=40,
                  command=lambda: master.switch_frame(ViewS)).pack(side=tk.BOTTOM)




def qTiming(pax, time, textBox):
    # TODO need to see what happens when bad input
    time_to_wait = 0
    multiplier = 2 # multiplier exists only to inflate the time taken for queueing
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
            time_to_wait = "Stall is closed till"
        string_output = str(time_to_wait) + " minutes of waiting time."
        textBox.insert(0, string_output)
        return time_to_wait
    except ValueError: # arises when user inputs a non number into the textbox
        textBox.delete(0, 'end') # deletes the incorrect user input, end references the last string series input into the entry box
        textBox.insert(0, 'Please type the numerical form of people queuing: ')


def timeOfDayDecider(opening, closing): # takes the current system time and decides whether it's morning, afternoon or evening
    # used in the qTiming function to show how much a group of ppl will need to queue for a stall
    hour = datetime.datetime.now().hour # returns the 24 hour form of what hour it is right now
    # please note the hour will be rounded down from whatever time it is now
    # if it's 1230, the hour will be 12
    time = None
    if 0 <= hour <= opening:
        time = "closed"
    elif opening <= hour <= 12:
        time = "morning"
    elif 12 <= hour <= 17:
        time = "afternoon"
    elif 17 <= hour <= closing:
        time = "evening"
    return time

# def OCR():


class WaitTMiniwok(tk.Frame): # Frame that displays waitings times for a specific length of queue
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')


        opening = 6
        closing = 22 # edit this per restaurant

        entry = tk.Entry(self, width = 50)
        entry.pack()
        calculationButton = tk.Button(self, text="Calculate Q timing", command=lambda: qTiming(entry.get(), timeOfDayDecider(opening, closing), calcDisplay)).pack() # int(entry.get()) is the received input from the top entrybox after the user input is keyed in
        calcDisplay = tk.Entry(self, text = "", width = 50)
        calcDisplay.pack()
        # KK NVM the only thing the button should do is execute func to send output to the texbox
        returnButton = tk.Button(self, text="Return", width=40,
                  command=lambda: master.switch_frame(miniwok)).pack(side=tk.BOTTOM)

class WaitTChicken(tk.Frame): # Frame that displays waitings times for a specific length of queue
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')


        opening = 6
        closing = 22 # edit this per restaurant

        entry = tk.Entry(self, width = 50)
        entry.pack()
        calculationButton = tk.Button(self, text="Calculate Q timing", command=lambda: qTiming(entry.get(), timeOfDayDecider(opening, closing), calcDisplay)).pack() # int(entry.get()) is the received input from the top entrybox after the user input is keyed in
        calcDisplay = tk.Entry(self, text = "", width = 50)
        calcDisplay.pack()
        # KK NVM the only thing the button should do is execute func to send output to the texbox
        returnButton = tk.Button(self, text="Return", width=40,
                  command=lambda: master.switch_frame(chicken)).pack(side=tk.BOTTOM)

class WaitTMacs(tk.Frame): # Frame that displays waitings times for a specific length of queue
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')


        opening = 6
        closing = 22 # edit this per restaurant

        entry = tk.Entry(self, width = 50)
        entry.pack()
        calculationButton = tk.Button(self, text="Calculate Q timing", command=lambda: qTiming(entry.get(), timeOfDayDecider(opening, closing), calcDisplay)).pack() # int(entry.get()) is the received input from the top entrybox after the user input is keyed in
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
