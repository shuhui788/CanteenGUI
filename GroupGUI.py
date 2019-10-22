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
        tk.Tk.__init__(self)
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
        tk.Button(self, text="Calculate the estimated waiting time", width = 40,
                  command=lambda: master.switch_frame(WaitT)).pack()
        tk.Button(self, text="View operating hours", width = 40,
                  command=lambda: master.switch_frame(OperT)).pack()
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
                  command=lambda: master.switch_frame(mc)).pack()
        tk.Button(self, text="Subway", width = 40,
                  command=lambda: master.switch_frame(subway)).pack()
        tk.Button(self, text="The Sandwich Guys", width = 40,
                  command=lambda: master.switch_frame(sandwich)).pack()
        tk.Button(self, text="Return to Home Page", width = 40,
                  command=lambda: master.switch_frame(HomePage)).pack()

def qTiming(pax, time, multiplier): # multiplier is different for different stalls
    # TODO need to see what happens when bad input
    time_to_wait = 0
    if time == "morning":
        time_to_wait = pax * 1 # least in the morning
    elif time == "afternoon":
        time_to_wait = pax * 3 # most in the afternoon
    elif time == "evening":
        time_to_wait = pax * 2 # second most in evening
    return time_to_wait


class miniwok(tk.Frame):
    def openMiniwokMenu(self): # placed above the def __init__ so that it can be referenced by the View Menu Button
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
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="Mini Wok", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text = "View Menu", width = 40, command = lambda: self.openMiniwokMenu()).pack()
        tk.Button(self, text= "Calculate Q timings", width = 40, command = lambda: master.switch_frame(miniwokQCalc)).pack()
        tk.Button(self, text="Return to Home Page",
                  command=lambda: master.switch_frame(HomePage)).pack(side=tk.BOTTOM)
class miniwokQCalc(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        entry = tk.Entry(self, text = "Please input the number of people queuing: ")
        entry.pack()
        pax = entry.get()
        calculation = tk.Button(self, text = "Calculate Q timing", command = lambda: qTiming(pax, "morning", 3)).pack()
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
        tk.Button(self, text="Return to Home Page",
                 command=lambda: master.switch_frame(HomePage)).pack(side=tk.BOTTOM)


class mc(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="McDonald's", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
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
        tk.Button(self, text="Return to Home Page",
                  command=lambda: master.switch_frame(HomePage)).pack(side=tk.BOTTOM)

class subway(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="Subway", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        with open('menu information.txt') as menu:
                if day == 'Sunday' or 'Saturaday':
                    if time1<1100 and time1>1800:
                        tk.Label(self, text="The stall is closed now.", font=('Helvetica', 18, "bold")).pack(side="top")
                    else:
                        for i,line in enumerate(menu.readlines()):
                            if i>=30 and i<=33:
                                menusub = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
                else:
                    if time1<800 and time1>2100:
                        tk.Label(self, text="The stall is closed now.", font=('Helvetica', 18, "bold")).pack(side="top")
                    else:
                        for i,line in enumerate(menu.readlines()):
                            if i>=30 and i<=33:
                                menusub = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
        tk.Button(self, text="Return to Home Page",
                  command=lambda: master.switch_frame(HomePage)).pack(side=tk.BOTTOM)

class sandwich(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="The Sandwich Guys", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        with open('menu information.txt') as menu:
            if time1<830 and time1>1730:
                tk.Label(self, text="The stall is closed now.", font=('Helvetica', 18, "bold")).pack(side="top")
            else:
                for i,line in enumerate(menu.readlines()):
                    if i>=36 and i<=37:
                        menusandwich = tk.Message(self, text=line, font=('Helvetica', 10),width=10000).pack(side="top")
        tk.Button(self, text="Return to Home Page",
                  command=lambda: master.switch_frame(HomePage)).pack(side=tk.BOTTOM)


class WaitT(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="Calculation of estimated waiting time", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Return to Home Page",
                  command=lambda: master.switch_frame(HomePage)).pack()

class OperT(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self)
        tk.Label(self, text="View the operating hours", font=('Helvetica', 18, "bold")).pack(side="top")
        scrollbar=tk.Scrollbar(self)
        scrollbar.pack(side = tk.RIGHT, fill = 'y')
        mylist = tk.Listbox(self, yscrollcommand = scrollbar.set)
        operating = "operating time.txt"
        file2 = open(operating,'r')
        for line in file2:
            lines = line
            mylist.insert(tk.END, lines)
        mylist.pack(fill='both')
        scrollbar.config(command = mylist.yview)
        tk.Button(self, text="Return to Home Page",
                  command=lambda: master.switch_frame(HomePage)).pack()


class dateT(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="Set system date and time", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Return to Home Page",
                  command=lambda: master.switch_frame(HomePage)).pack()


m = NTUsystem()
m.title('NTU Canteen System')
m.mainloop()
