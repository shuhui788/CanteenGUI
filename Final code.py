import tkinter as tk
import datetime
from tkinter import ttk
import time as TIME
from tkinter import messagebox

today = datetime.datetime.now()
now = str(today)
hour = str('%02d' % today.hour)
minute = str('%02d' % today.minute)
sec = int(now[17:19])
str_time1 = hour+minute # str_time1 is the current 24 hour time. Used to retain the 00 in front of hours before 1000 (10AM)
time1 = int(str_time1)
day = today.strftime('%A')


MINI_OCD = {'miniwok_open': 0, 'miniwok_close': 0}

CHIK_OCD = {'chicken_open': 0, 'chicken_close': 0}

MACS_OCD = {'macs_open': 0, 'macs_close': 0}

# the above are the open and close timings to be given values in their respective Stall Classes

def popupmessage(timestr,dayIn):#Authors: Ashwin Kurup, Ang Shu Hui, and Benedict Leong
 global str_time1
 global time1
 global day
 #global time1 and day so that they can be used at all namespace
 for i in timestr:
     if i.isalpha() == True:
         messagebox.showerror(title="Error", message="There should not have an alphabet")
         break
     elif len(timestr) != 4:
      messagebox.showerror(title="Error", message="Time should be between 0000 and 2359 in proper 24 Hour format.")
     elif int(timestr) > 2359 or int(timestr) <= 0 or int(timestr[2]) >= 6:  # last conditional exists to make sure timings like 1367 cannot be accepted
      messagebox.showerror(title="Error", message="Time should be between 0000 and 2359 in proper 24 Hour format.")

 str_time1 = timestr # str_time1 is the global variable used for all other functions. timestr is the local variable which is the value of the current 24 Hour time
 time1 = int(timestr)

 day = dayIn
    #assign user's input to the system variables

def stallIsClosedlabel(opening, closing, display_text): #Author: Ashwin Kurup
  if opening< time1 <closing:
      print("") # do nothing
  else: # if stall is closed
      display_text.set("Stall is closed")
# stallIsClosedlabel: adds text into a label saying that the stall is closed during the closing hours. 

def qTiming(pax, time, label_var): #Author: Ashwin Kurup
  time_to_wait = 0
  multiplier = 0.7 # multiplier exists only to deflate the time taken for queueing, can edit according to preference
  try:
      pax = int(pax) # pax comes as a string input from the textbox, here converted to int form
      label_var.set(" ")
      if time == "morning":
          time_to_wait = pax * 1 * multiplier  # least in the morning
      elif time == "afternoon":
          time_to_wait = pax * 3 * multiplier  # most in the afternoon
      elif time == "evening":
          time_to_wait = pax * 2 * multiplier  # second most in evening

      if time == "closed":
          string_output = "Stall is closed"
      else:
          string_output = str(int(time_to_wait)) + " minutes of waiting time."  # time to wait is made to be be an int first because the multiplier converts it to float
      label_var.set(string_output)
  except ValueError: # arises when user inputs a non number into the textbox
      label_var.set('Please type the numerical form of people queuing')


def timeOfDayDecider(opening, closing):#Author: Ashwin Kurup
# takes the current system time and decides whether it's morning, afternoon or evening
# used in the qTiming function to show how much a group of ppl will need to queue for a stall
  time = None
  if 0 <= time1  <= opening or opening == 0 or time1 >= closing: # the second part is due to some stalls being closed on sunday, during which their stallname_open value will be set to 0
      time = "closed"
      print(time1, opening)
  elif opening <= time1 <= 1200:
      time = "morning"
  elif 1200 <= time1  <= 1700:
      time = "afternoon"
  elif 1700 <= time1  <= closing:
      time = "evening"
  return time


class NTUsystem(tk.Tk):
  def __init__(self):#Author: Ang Shu Hui (reference: https://www.delftstack.com/howto/python-tkinter/how-to-switch-frames-in-tkinter/)
      tk.Tk.__init__(self) # init function of tk.Tk. is being called, therefore constructing everything in it
      self._frame = None
      self.switch_frame(HomePage)

  def switch_frame(self, frame_class):#Author: Ang Shu Hui (reference: https://www.delftstack.com/howto/python-tkinter/how-to-switch-frames-in-tkinter/)
      new_frame = frame_class(self)
      if self._frame is not None:
          self._frame.destroy()
      self._frame = new_frame
      self._frame.pack()

class HomePage(tk.Frame):
  def __init__(self, master):#Author: Ang Shu Hui
      tk.Frame.__init__(self, master)
      tk.Label(self, text="Real Time NTU Canteen System", font=('Arial', 20, "bold")).pack(side="top", fill="x", pady=5)
      tk.Label(self, text="Current time: "+day+' '+str_time1[0:2]+':'+str_time1[2:4], font=('Arial', 10)).pack()
      tk.Button(self, text="View Stalls", width = 40,
                command=lambda: master.switch_frame(ViewS)).pack()
      tk.Button(self, text="Set date and time", width = 40,
                command=lambda: master.switch_frame(dateT)).pack()
      tk.Button(self, text="Exit", width = 40, command=self.master.destroy).pack()

class ViewS(tk.Frame):
  def __init__(self, master):#Author: Ang Shu Hui
      tk.Frame.__init__(self, master)
      tk.Frame.configure(self)
      tk.Label(self, text="View Stalls", font=('Arial', 18, "bold")).pack(side="top", fill="x", pady=5)
      tk.Button(self, text="Mini Wok", width = 40,
                command=lambda: master.switch_frame(miniwok)).pack()
      tk.Button(self, text="Chicken Rice", width = 40,
                command=lambda: master.switch_frame(chicken)).pack()
      tk.Button(self, text="McDonald's", width = 40,
                command=lambda: master.switch_frame(mac)).pack()
      tk.Button(self, text="Return to Home Page", width = 40,
                command=lambda: master.switch_frame(HomePage)).pack()

class miniwok(tk.Frame):
  def __init__(self, master):#Authors: Ashwin Kurup,Ang Shu Hui
      tk.Frame.__init__(self, master)
      tk.Frame.configure(self)

      tk.Label(self, text="Mini Wok", font=('Arial', 18, "bold")).pack(side="top", fill="x", pady=5)
      display_text = tk.StringVar()
      weAreClosedLabel = tk.Label(self, textvariable = display_text, font=('Arial', 18)).pack() # display_text will be empty unless stall is closed
      if day == 'Sunday':
          MINI_OCD['miniwok_open'] = 0
          display_text.set("Stall is closed today")
      elif day == "Saturday":
          MINI_OCD['miniwok_open'] = 830
          MINI_OCD['miniwok_close'] = 1700
          stallIsClosedlabel(830, 1700, display_text)
      else:
          MINI_OCD['miniwok_open'] = 830
          MINI_OCD['miniwok_close'] = 2130
          stallIsClosedlabel(830, 2130, display_text)

      with open('menu information.txt') as menu:
          if day == 'Tuesday':
             for i, line in enumerate(menu.readlines()): # displays the part of the menu that belongs to miniwok on tue
                if i >= 30 and i <= 34:
                   menuminiwok = tk.Message(self, text=line, font=('Arial', 10), width=10000).pack(side="top")
          else:
              for i, line in enumerate(menu.readlines()): # displays the part of the menu that belongs to miniwok on weekdays except tue
                  if i >= 1 and i <= 5:
                      menuminiwok = tk.Message(self, text=line, font=('Arial', 10), width=10000).pack(side="top")

      tk.Button(self, text="Calculate the estimated waiting time", width = 40,
                command=lambda: master.switch_frame(WaitTMiniwok)).pack()
      tk.Button(self, text="View operating hours", width = 40,
                command=lambda: master.switch_frame(Oper1)).pack()
      tk.Button(self, text="Return", width = 40,
                command=lambda: master.switch_frame(ViewS)).pack(side=tk.BOTTOM)

class chicken(tk.Frame):
  def __init__(self, master):#Authors: Ashwin Kurup, Ang Shu Hui

      tk.Frame.__init__(self, master)
      tk.Frame.configure(self)
      tk.Label(self, text="Chicken Rice", font=('Arial', 18, "bold")).pack(side="top", fill="x", pady=5)
      display_text = tk.StringVar()
      weAreClosedLabel = tk.Label(self, textvariable=display_text, font=('Arial', 18)).pack()
      if day == 'Sunday':
          CHIK_OCD['chicken_open'] = 0
          display_text.set("Stall is closed today")
      elif day == "Saturday":
          CHIK_OCD['chicken_open'] = 830
          CHIK_OCD['chicken_close'] = 1700
          stallIsClosedlabel(830, 1700, display_text)
      else:
          CHIK_OCD['chicken_open'] = 830
          CHIK_OCD['chicken_close'] = 2130
          stallIsClosedlabel(830, 2130, display_text)
      with open ('menu information.txt') as menu:
          for i, line in enumerate(menu.readlines()):
              if i >= 1 and i <= 5:
                  menuchicken = tk.Message(self, text=line, font=('Arial', 10), width=10000).pack(side="top")
      tk.Button(self, text="Calculate the estimated waiting time", width = 40,
                command=lambda: master.switch_frame(WaitTChicken)).pack()
      tk.Button(self, text="View operating hours", width = 40,
                command=lambda: master.switch_frame(Oper2)).pack()
      tk.Button(self, text="Return", width = 40,
               command=lambda: master.switch_frame(ViewS)).pack(side=tk.BOTTOM)


class mac(tk.Frame):
  def __init__(self, master):#Authors: Ashwin Kurup, Ang Shu Hui

      tk.Frame.__init__(self, master)
      tk.Frame.configure(self)
      tk.Label(self, text="McDonald's", font=('Arial', 18, "bold")).pack(side="top", fill="x", pady=5)
      display_text = tk.StringVar()
      weAreClosedLabel = tk.Label(self, textvariable=display_text, font=('Arial', 18)).pack()
      if day == 'Sunday':
          MACS_OCD['macs_open'] = 1000
          MACS_OCD['macs_close'] = 2200
          stallIsClosedlabel(1000, 2200, display_text)
      elif day == "Saturday":
          MACS_OCD['macs_open'] = 700
          MACS_OCD['macs_close']= 2359
          stallIsClosedlabel(700, 2359, display_text)
      else:
          MACS_OCD['macs_open'] = 700
          MACS_OCD['macs_close'] = 2359
          stallIsClosedlabel(700, 2359, display_text)
      with open('menu information.txt') as menu: # if mcdonalds is closed, show the previous menu for lunch&dinner
          if day == 'Sunday':
              for i,line in enumerate(menu.readlines()):
                  if 1000 < time1 < 1200: # if between 10AM and 12PM
                      if 16<= i <=20: # print the morning section of the macs menu
                          menumc = tk.Message(self, text=line, font=('Arial', 10),width=10000).pack(side="top")
                  else: # if between 12PM and 10PM, or after close print the afternoon section of the macs menu. There will still be a label at the top ...
                      # ... saying that the stall is closed
                      if 23<= i <=27:
                          menumc = tk.Message(self, text=line, font=('Arial', 10),width=10000).pack(side="top")
          else:
              for i,line in enumerate(menu.readlines()):
                  if 700<= time1 <=1100: # if during morning time from monday to saturday
                      if 16<= i <=20:
                          menumc = tk.Message(self, text=line, font=('Arial', 10),width=10000).pack(side="top")
                  else:
                      if 23<= i <=27:
                          menumc = tk.Message(self, text=line, font=('Arial', 10),width=10000).pack(side="top")

      tk.Button(self, text="Calculate the estimated waiting time", width = 40,
                command=lambda: master.switch_frame(WaitTMacs)).pack()
      tk.Button(self, text="View operating hours", width = 40,
                command=lambda: master.switch_frame(Oper3)).pack()
      tk.Button(self, text="Return", width=40,
                command=lambda: master.switch_frame(ViewS)).pack(side=tk.BOTTOM)



class WaitTMiniwok(tk.Frame): # Frame that displays waitings times for a specific length of queue
  def __init__(self, master):#Authors: Ashwin Kurup, Ang Shu Hui
      tk.Frame.__init__(self, master)
      tk.Frame.configure(self)
      tk.Label(self, text="Calculate Waiting Time", font=('Arial', 18, "bold")).pack(side="top", fill="x", pady=5)
      entry = tk.Entry(self, width = 20)
      entry.pack()
      tk.Label(self,text = "Insert number of people").place(x=35,y=40)
      lable_var = tk.StringVar()
      calculationButton = tk.Button(self, text="Submit", command=lambda: qTiming(entry.get(),
                                                                                 timeOfDayDecider(MINI_OCD['miniwok_open'], MINI_OCD['miniwok_close']),
                                                                                 lable_var)).place(x=315,y=40)

      tk.Label(self, text="Estimated Waiting Time: ").pack()
      calcDisplay = tk.Label(self, textvariable=lable_var, width=50, borderwidth=2, relief="groove").pack()
      returnButton = tk.Button(self, text="Return", width=70,
                command=lambda: master.switch_frame(miniwok)).pack(side=tk.BOTTOM)

class WaitTChicken(tk.Frame): # Frame that displays waitings times for a specific length of queue
  def __init__(self, master):#Authors: Ashwin Kurup, Ang Shu Hui
      tk.Frame.__init__(self, master)
      tk.Frame.configure(self)
      tk.Label(self, text="Calculate Waiting Time", font=('Arial', 18, "bold")).pack(side="top", fill="x", pady=5)
      entry = tk.Entry(self, width = 20)
      entry.pack()
      tk.Label(self,text = "Insert number of people").place(x=35,y=40)
      lable_var = tk.StringVar()
      calculationButton = tk.Button(self, text="Submit", command=lambda: qTiming(entry.get(),
                                                                                 timeOfDayDecider(CHIK_OCD['chicken_open'], CHIK_OCD['chicken_close']),
                                                                                 lable_var)).place(x=315,y=40)
      tk.Label(self, text="Estimated Waiting Time: ").pack()
      calcDisplay = tk.Label(self, textvariable=lable_var, width=50, borderwidth=2, relief="groove").pack()
      returnButton = tk.Button(self, text="Return", width=70,
                command=lambda: master.switch_frame(chicken)).pack()

class WaitTMacs(tk.Frame): # Frame that displays waitings times for a specific length of queue
  def __init__(self, master):#Authors: Ashwin Kurup, Ang Shu Hui
      tk.Frame.__init__(self, master)
      tk.Frame.configure(self)
      tk.Label(self, text="Calculate Waiting Time", font=('Arial', 18, "bold")).pack(side="top", fill="x", pady=5)
      entry = tk.Entry(self, width = 20)
      entry.pack()
      tk.Label(self,text = "Insert number of people").place(x=35,y=40)
      lable_var = tk.StringVar()
      calculationButton = tk.Button(self, text="Submit", command=lambda: qTiming(entry.get(),
                                                                                 timeOfDayDecider(MACS_OCD['macs_open'], MACS_OCD['macs_close']),
                                                                                 lable_var), ).place(x=315,y=40)
      tk.Label(self,text = "Estimated Waiting Time: ").pack()
      calcDisplay = tk.Label(self, textvariable=lable_var, width=50, borderwidth=2, relief="groove").pack()


      returnButton = tk.Button(self, text="Return", width=70,
                command=lambda: master.switch_frame(mac)).pack(side=tk.BOTTOM)

class Oper1(tk.Frame):

  def __init__(self, master):#Author: Ang Shu Hui
      tk.Frame.__init__(self, master)
      tk.Frame.configure(self)
      tk.Label(self, text="View the operating hours", font=('Arial', 18, "bold")).pack(side="top")
      with open('operating time.txt') as oper:
          for i,line in enumerate(oper.readlines()):
              if i>=1 and i<=6:
                  mini = tk.Message(self, text=line, font=('Arial', 10),width=10000).pack(side="top")
      tk.Button(self, text="Return", width = 40,
                command=lambda: master.switch_frame(miniwok)).pack()
#operating hours for mini wok

class Oper2(tk.Frame):
  def __init__(self, master):#Author: Ang Shu Hui
      tk.Frame.__init__(self, master)
      tk.Frame.configure(self)
      tk.Label(self, text="View the operating hours", font=('Arial', 18, "bold")).pack(side="top")
      with open('operating time.txt') as oper:
          for i,line in enumerate(oper.readlines()):
              if i>=9 and i<=14:
                  chick = tk.Message(self, text=line, font=('Arial', 10),width=10000).pack(side="top")
      tk.Button(self, text="Return", width = 40,
                command=lambda: master.switch_frame(chicken)).pack()
#operating hours for chicken rice

class Oper3(tk.Frame):
  def __init__(self, master):#Author: Ang Shu Hui
    tk.Frame.__init__(self, master)
    tk.Frame.configure(self)
    tk.Label(self, text="View the operating hours", font=('Arial', 18, "bold")).pack(side="top")
    with open('operating time.txt') as oper:
       for i,line in enumerate(oper.readlines()):
          if i>=17 and i<=22:
             mc_message = tk.Message(self, text=line, font=('Arial', 10),width=10000).pack(side="top")
                  # do not rename the above mc_message variable to mac, that'll cause an error in the switch_frame.
    tk.Button(self, text="Return", width=40,
                command=lambda: master.switch_frame(mac)).pack()
#operating hours for mcdonald

#Function window for user to enter day and time
class dateT(tk.Frame):#Author: Benedict Leong
 def __init__(self, master):
    tk.Frame.__init__(self, master)
    tk.Frame.configure(self)
    tk.Label(self, text="Set user-defined day and time", font=('Arial', 18, "bold")).pack(side="top", fill="x", pady=5)
    DayOptionList = [
         "Monday",
         "Tuesday",
         "Wednesday",
         "Thursday",
         "Friday",
         "Saturday",
         "Sunday"
     ]

    daycombo = ttk.Combobox(self, values=DayOptionList, state='readonly')
    daycombo.set(DayOptionList[0])
    daycombo.pack()
    label = tk.Label (text="Enter time here (i.e 0000): ")
    label.place(x=0, y=64)
    entry = tk.Entry(self, width = 10)
    entry.pack()
    button1 = tk.Button(self, text="Submit", width=10, command=lambda: popupmessage(entry.get(), daycombo.get())).place(x= 450, y = 75, anchor = "e")
    button2 = tk.Button(self, text="Return to Home Page", width = 80, command=lambda: master.switch_frame(HomePage)).pack()


if __name__ == "__main__":
  m = NTUsystem()
  m.title('NTU Canteen System')
  m.mainloop()
