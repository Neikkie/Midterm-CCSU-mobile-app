# import
from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
from tkmacosx import Button

# Window setup

window = Tk()
window.title('CCSU Mobile App')
window.geometry('500x650')
window.resizable(0,0)
window.configure(bg='#99BBDD')


# make white in logo transparent and show it
img = Image.open('logo1.png')

# PILLOW>=10 changed ANTIALIAS; this keeps it compatible
try:
    img = img.resize((100, 100), Image.Resampling.LANCZOS)
except AttributeError:
    img = img.resize((100, 100), Image.ANTIALIAS)
img = img.convert('RGBA')
image_data = list(img.get_flattened_data())

newData = []
for item in image_data:
    # if pixel is white, make it transparent; else keep it
    if item[:3] == (255,255,255):
        newData.append((255,255,255,0))
    else:
        newData.append(item)

img.putdata(newData)
img.save('transparent.png')

logo = Image.open('transparent.png')
logo = ImageTk.PhotoImage(logo)
logoLabel = Label(window, image=logo, bg='#99B9DB')
logoLabel.place(x=1, y=1)

#------------------------------
data =pd.read_csv('CCSU_Fall_2026_Academic_Calendar.csv')

# Label used to display results
lb=Label(window, justify='left', bg='#99B9DB', fg= 'black', anchor='nw', font=('Arial', 10), wraplength=400)
lb.place(relx=0.5, y=230, anchor='n')

#----------------------------
# BUTTON 1: Calendar
def calendar():
    df=pd.DataFrame(data, columns=['CalendarDate'])
    selected_rows =df[~df['CalendarDate'].isnull()]
    calendar_text = '\n'.join(selected_rows['CalendarDate'].astype(str))
    lb.config(text=calendar_text)


# button 2: buildings
def building():
    df=pd.DataFrame(data, columns=['Buildings'])
    selected_rows =df[~df['Buildings'].isnull()]
    buildings_text = '\n'.join(selected_rows['Buildings'].astype(str))
    lb.config(text=buildings_text)


# button 3: faculty
def faculty():
    df =pd.DataFrame(data, columns=['FacultyName'])
    selected_rows =df[~df['FacultyName'].isnull()]
    faculty_text = '\n'.join(selected_rows['FacultyName'].astype(str))
    lb.config(text=faculty_text)


# button 4: School of Business
def school_of_business():
    departments = (
        'School of Business Departments:\n'
        '- Accounting:\n'
        '- Finance:\n'
        '- Management & Organization:\n'
        '- Marketing:\n'
        '- Management Information Systems (MIS):\n'
        '- Business Analytics:\n'
    )
    lb.config(text=departments)


# button 5: MIS Department
def mis_department():
    departments = (
        'MIS Department Core Courses:\n'
        '- Intro to MIS:\n'
        '- Database Management:\n'
        '- System Analysis & Design:\n'
        '- Business Analytics / Data Visualization:\n'
        '- Networks & Information Security:\n'
        '- Project Management:\n'
        '- Python for Business Applications:\n'

    )
    lb.config(text=departments)



# ----------------------------------------
button1 =Button(window, text='Calendar', command=calendar, bg='dark blue', fg='white', highlightbackground='dark blue')
button1.place(x=50, y=135)

button2 =Button(window, text='Buildings', command=building, bg='dark blue', fg='white')
button2.place(x=175, y=135)

button3= Button(window, text='Faculty', command=faculty, bg='dark blue', fg='white')
button3.place(x=300, y=135)

button4 = Button(window, text='School of business', command=school_of_business, bg='dark blue', fg='white')
button4.place(x=50, y=175)

button5 = Button(window, text='MIS Department', command= mis_department, background='dark blue', fg='white')
button5.place(x=240, y=175)


window.mainloop()