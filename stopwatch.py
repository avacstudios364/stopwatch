from tkinter import *
import time
import tkinter.messagebox

root = Tk()
root.minsize(500,200)
root.title('Stopwatch')

#declare variables
hour = StringVar() 
minute = StringVar()
second = StringVar()

#setting the default values as 0
hour.set('00')
minute.set('00')
second.set('00')

systemfont = ('Arial', 18, '')

# use of Entry(to get input from users)
hourEntry = Entry(root, width = 2, font = systemfont, textvariable = hour)
hourEntry.place(x = 50, y = 50)

minuteEntry = Entry(root, width = 2, font = systemfont, textvariable = minute)
minuteEntry.place(x = 150, y = 50)

secondEntry = Entry(root, width = 2, font = systemfont, textvariable = second)
secondEntry.place(x = 250, y = 50)


def submit():
    try:
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        print('Please input and number')

    while temp > -1 :
        mins,secs = divmod(temp, 60)
        hours = 00
        if mins > 60:
            hours, mins = divmod(mins, 60)
            
        hour.set('{00:2d}'.format(hours))
        minute.set('{00:2d}'.format(mins))
        second.set('{00:2d}'.format(secs))
        root.update()
        time.sleep(1)
        if temp == 0:
            tkinter.messagebox.showinfo('Finished','The timer is finished')
        temp -= 1

settimerbtn = Button(root, text = 'Start countdown', font = systemfont, border = 5, command = submit)
settimerbtn.place(x = 50, y = 100)


root.mainloop()
