from tkinter import *
from tkinter import ttk
/*test for comment*/
top = Tk()
top.geometry("1170x730")
top.title("Utility GUI Calculator")
# top.config(bg='#e7e8d1')


def cal():
   e1.delete(0, END)
   value1 = float(cb1.get()) * float(cb1x.get())
   value2 = float(cb2.get()) * float(cb2x.get())
   value3 = float(cb3.get()) * float(cb3x.get())
   value4 = float(cb4.get()) * float(cb4x.get())
   value5 = float(cb5.get()) * float(cb5x.get())
   value6 = float(cb6.get()) * float(cb6x.get())
   value7 = float(cb7.get()) * float(cb7x.get())
   value8 = float(cb8.get()) * float(cb8x.get())
   value9 = float(cb9.get()) * float(cb9x.get())
   value10 = float(cb10.get()) * float(cb10x.get())
   value11 = float(cb11.get()) * float(cb11x.get())
   value12 = float(cb12.get()) * float(cb12x.get())
   value13 = float(cb13.get()) * float(cb13x.get())
   value14 = float(cb14.get()) * float(cb14x.get())
   value15 = float(cb15.get()) * float(cb15x.get())

   creditvalue = float(cb1x.get()) + float(cb2x.get()) + float(cb3x.get()) + float(cb3x.get()) + float(cb5x.get()) +\
                 float(cb6x.get()) + float(cb7x.get()) + float(cb8x.get()) + float(cb9x.get()) + float(cb10x.get()) +\
                float(cb11x.get()) + float(cb12x.get()) + float(cb13x.get()) + float(cb14x.get()) + float(cb15x.get())

   valuemax = (value1 + value2 + value3 + value4 + value5 + value6 + value7 + value8 + value9 + value10 + value11
               + value12 + value13 + value14 + value15) / creditvalue
   e1.insert(0, f'{valuemax:.2f}')

frame1 = Frame(top, width=2000)
frame1.pack(side=LEFT)
g = LabelFrame(frame1, text='GPAX Calculator', font='18', fg='#486a7e')
g.pack(fill="both", expand="yes", padx=8)

l1 = Label(g, text='Subject1')
l1.grid()

cb1 = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4"], width=5)
cb1.grid()
cb1.current(0)

l1x = Label(g, text='Credit1')
l1x.grid(column=3, row=0)

cb1x = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2"], width=5)
cb1x.grid(column=3, row=1)
cb1x.current(0)
#sub2
l2 = Label(g, text='Subject2')
l2.grid(column=0, row=2)

cb2 = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4"], width=5)
cb2.grid(column=0, row=3)
cb2.current(0)


l2x = Label(g, text='Credit2')
l2x.grid(column=3, row=2)

cb2x = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2"], width=5)
cb2x.grid(column=3, row=3)
cb2x.current(0)
#sub3
l3 = Label(g, text='Subject3')
l3.grid(column=0, row=4)

cb3 = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4"], width=5)
cb3.grid(column=0, row=5)
cb3.current(0)

l3x = Label(g, text='Credit3')
l3x.grid(column=3, row=4)

cb3x = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2"], width=5)
cb3x.grid(column=3, row=5)
cb3x.current(0)
#sub4
l4 = Label(g, text='Subject4')
l4.grid(column=0, row=6)

cb4 = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4"], width=5)
cb4.grid(column=0, row=7)
cb4.current(0)

l4x = Label(g, text='Credit4')
l4x.grid(column=3, row=6)

cb4x = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2"], width=5)
cb4x.grid(column=3, row=7)
cb4x.current(0)
#sub5
l5 = Label(g, text='Subject5')
l5.grid(column=0, row=8)

cb5 = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4"], width=5)
cb5.grid(column=0, row=9)
cb5.current(0)

l5x = Label(g, text='Credit5')
l5x.grid(column=3, row=8)

cb5x = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2"], width=5)
cb5x.grid(column=3, row=9)
cb5x.current(0)

#sub6
l6 = Label(g, text='Subject6')
l6.grid(column=0, row=10)

cb6 = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4"], width=5)
cb6.grid(column=0, row=11)
cb6.current(0)

l6x = Label(g, text='Credit6')
l6x.grid(column=3, row=10)

cb6x = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2"], width=5)
cb6x.grid(column=3, row=11)
cb6x.current(0)
#sub7
l7 = Label(g, text='Subject7')
l7.grid(column=0, row=12)

cb7 = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4"], width=5)
cb7.grid(column=0, row=13)
cb7.current(0)

l7x = Label(g, text='Credit7')
l7x.grid(column=3, row=12)

cb7x = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2"], width=5)
cb7x.grid(column=3, row=13)
cb7x.current(0)
#sub8
l8 = Label(g, text='Subject8')
l8.grid(column=0, row=14)

cb8 = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4"], width=5)
cb8.grid(column=0, row=15)
cb8.current(0)

l8x = Label(g, text='Credit8')
l8x.grid(column=3, row=14)

cb8x = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2"], width=5)
cb8x.grid(column=3, row=15)
cb8x.current(0)
#sub9
l9 = Label(g, text='Subject9')
l9.grid(column=0, row=16)

cb9 = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4"], width=5)
cb9.grid(column=0, row=17)
cb9.current(0)

l9x = Label(g, text='Credit9')
l9x.grid(column=3, row=16)

cb9x = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2"], width=5)
cb9x.grid(column=3, row=17)
cb9x.current(0)
#sub10
l10 = Label(g, text='Subject10')
l10.grid(column=0, row=18)

cb10 = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4"], width=5)
cb10.grid(column=0, row=19)
cb10.current(0)

l10x = Label(g, text='Credit10')
l10x.grid(column=3, row=18)

cb10x = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2"], width=5)
cb10x.grid(column=3, row=19)
cb10x.current(0)
#sub11
l11 = Label(g, text='Subject11')
l11.grid(column=0, row=20)

cb11 = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4"], width=5)
cb11.grid(column=0, row=21)
cb11.current(0)

l11x = Label(g, text='Credit11')
l11x.grid(column=3, row=20)

cb11x = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2"], width=5)
cb11x.grid(column=3, row=21)
cb11x.current(0)
#sub12
l12 = Label(g, text='Subject12')
l12.grid(column=0, row=22)

cb12 = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4"], width=5)
cb12.grid(column=0, row=23)
cb12.current(0)

l12x = Label(g, text='Credit12')
l12x.grid(column=3, row=22)

cb12x = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2"], width=5)
cb12x.grid(column=3, row=23)
cb12x.current(0)
#sub13
l13 = Label(g, text='Subject13')
l13.grid(column=0, row=24)

cb13 = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4"], width=5)
cb13.grid(column=0, row=25)
cb13.current(0)

l13x = Label(g, text='Credit13')
l13x.grid(column=3, row=24)

cb13x = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2"], width=5)
cb13x.grid(column=3, row=25)
cb13x.current(0)
#sub14
l14 = Label(g, text='Subject14')
l14.grid(column=0, row=26)

cb14 = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4"], width=5)
cb14.grid(column=0, row=27)
cb14.current(0)

l14x = Label(g, text='Credit14')
l14x.grid(column=3, row=26)

cb14x = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2"], width=5)
cb14x.grid(column=3, row=27)
cb14x.current(0)
#sub15
l15 = Label(g, text='Subject15')
l15.grid(column=0, row=28)

cb15 = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2", "2.5", "3", "3.5", "4"], width=5)
cb15.grid(column=0, row=29)
cb15.current(0)
cb15.current(0)

l15x = Label(g, text='Credit15')
l15x.grid(column=3, row=28, padx=10, pady=3)

cb15x = ttk.Combobox(g, values=["0", "0.5", "1", "1.5", "2"], width=5)
cb15x.grid(column=3, row=29, padx=10, pady=3)
cb15x.current(0)

e1 = Entry(g, width=10)
e1.grid(ipady=5, column=1, row=30, sticky="news", columnspan=2)

b1 = Button(g, text='Grade is', command=cal, height=1, width=6)
b1.grid(pady=3, column=0, row=30)


frame2 = Frame(top, width=150)
frame2.pack(side=LEFT)
frame2up = LabelFrame(frame2, width=200, text='Temperature Converter', font=18, fg='#b85042')
frame2up.pack(ipadx=5, side=TOP, pady=5)
# Label(frame2, text='Also here').pack(side=LEFT)


def reset():
   c.set(0)
   color = "#672146"
   if float(c.get()) == 0:
       c["fg"] = color
       r_value["fg"] = color
       f_value["fg"] = color
       kelvin_value["fg"] = color
       temp.set(f'{float(c.get()) + 273.15: .2f}K')
       temp1.set(f'{(float(c.get()) * 9/5) + 32: .2f}F')
       temp2.set(f'{(float(c.get()) * 9/5) + 491.67: .2f}R')
def drag(e):
   kel = float(c.get()) + 273.15
   temp.set(f'{kel: .2f}K')
   color = ""
   if kel <= 273.15:
       color = "#00609f"
   elif kel >= 373.15:
       color = "#f00"
   else:
       color = "#672146"
   kelvin_value["fg"] = color
   fra = (float(c.get()) * 9/5) + 32
   temp1.set(f'{fra: .2f}F')
   if fra >= 212:
       color = "#f00"
   elif fra <= 32:
       color = "#00609f"
   else:
       color = "#672146"
   f_value["fg"] = color
   rank = (float(c.get()) * 9/5) + 491.67
   temp2.set(f'{rank: .2f}R')
   if rank >= 671.641:
       color = "#f00"
   elif rank <= 492:
       color = "#00609f"
   else:
       color = "#672146"
   r_value["fg"] = color

   cel = float(c.get())
   if cel >= 100:
       color = "#f00"
   elif cel <= 0:
       color = "#00609f"
   elif cel > 0:
       color = '#672146'
   elif cel == 1:
       color = '#672146'
   c["fg"] = color


lb1 = Label(frame2up, text="Celcius (°C)", font=("Arial", 15))
lb1.grid(row=1, column=0, padx=2,  pady=2, sticky='sw')
#Scale
c = Scale(frame2up, from_=-500, to=500, orient=HORIZONTAL, length=300, width=20)
c.grid(row=1, column=1)
c.set(0)
c.bind('<B1-Motion>', drag)
c.bind('<Button-1>', drag)
#unit temp
temp = StringVar()
temp1 = StringVar()
temp2 = StringVar()
#kelvin
kelvin_label = Label(frame2up, text='Kelvin: ', font=("Arial", 15))
kelvin_label.grid(row=2, column=0, padx=5, pady=5)
kelvin_value = Label(frame2up, textvariable=temp)
kelvin_value.grid(row=2, column=1)
#fahrenheit
f_label = Label(frame2up, text='Fahrenheit:', font=("Arial", 15))
f_label.grid(row=3, column=0)
f_value = Label(frame2up, textvariable=temp1)
f_value.grid(row=3, column=1, pady=2)
#Rankine
r_label = Label(frame2up, text='Rankine:', font=("Arial", 15))
r_label.grid(row=4, column=0, pady=5, padx=5)
r_value = Label(frame2up, textvariable=temp2)
r_value.grid(row=4, column=1, pady=2)

b_reset = Button(frame2up, text='Reset Temp', command=reset)
b_reset.grid(column=2, row=4)

###################################################################################################################

def tick():
    if male.get() == 1:
        agebox.configure(state="normal")
        heightbox.configure(state="normal")
        femalebox.configure(state="disabled")
        weightbox.configure(state="normal")
        age.set("")
        height.set("")
        weight.set("")
    elif male.get() == 0:
        agebox.configure(state="disabled")
        heightbox.configure(state="disabled")
        femalebox.configure(state="normal")
        weightbox.configure(state="disabled")
        age.set('0')
        height.set("0")
        weight.set("0")
        bmr.set('')
        tdee.set('')

def tack():
    if female.get() == 1:
        agebox.configure(state="normal")
        heightbox.configure(state="normal")
        malebox.configure(state="disabled")
        weightbox.configure(state="normal")
        age.set("")
        height.set("")
        weight.set("")
    elif female.get() == 0:
        agebox.configure(state="disabled")
        heightbox.configure(state="disabled")
        malebox.configure(state="normal")
        weightbox.configure(state="disabled")
        age.set('0')
        height.set("0")
        weight.set("0")
        bmr.set('')
        tdee.set('')

def clearbtn():
    if male.get() or female.get() == 1:
        bmr.set('')
        age.set('')
        weight.set('')
        height.set('')
        actbox.set("Please select your lately activity")
        tdee.set('')
    if male.get() or female.get() == 0:
        actbox.set("Please select your lately activity")
        tdee.set('')

frame2mid = LabelFrame(frame2, text='BMR&TDEE Calculator', font=18, fg='#924d54')
frame2mid.pack(padx=5, ipadx=5, pady=10)

frame2mid_1 = Frame(frame2mid)
frame2mid_1.pack()
label11 = Label(frame2mid_1, text='\tBasal Metabolic Rate & Total Daily Energy Expenditure\t', font=30)
label11.grid(row=0, column=0, sticky='sw')
frame2mid_2 = Frame(frame2mid)
frame2mid_2.pack()
sex = Label(frame2mid_2, text='Sex     ', font=("Times New Roman", 15))
sex.grid(row=1, column=0, sticky='sw', pady=5)

male = IntVar()
female = IntVar()

malebox = Checkbutton(frame2mid_2, text='Male       ', variable=male, font=("Times New Roman", 15), command=tick)
malebox.grid(row=1, column=1, pady=5)
malebox.deselect()
femalebox = Checkbutton(frame2mid_2, text='Female', variable=female, font=("Times New Roman", 15), command=tack)
femalebox.grid(row=1, column=2, pady=5)
femalebox.deselect()

age = IntVar()
height = IntVar()
weight = IntVar()

frame2mid_3 = Frame(frame2mid, width=150)
frame2mid_3.pack()
agelabel = Label(frame2mid_3, text='Age:', font=("Times New Roman", 15))
agelabel.grid(row=0, column=0)
agebox = Entry(frame2mid_3, textvariable=age, width=8, justify='center')
agebox.grid(row=0, column=1, padx=8, pady=10)
agebox.configure(state='disabled')
heightlabel = Label(frame2mid_3, text='Height:', font=("Times New Roman", 15))
heightlabel.grid(row=0, column=2)
heightbox = Entry(frame2mid_3, textvariable=height, width=8, justify='center')
heightbox.grid(row=0, column=3, padx=8)
heightbox.configure(state='disabled')

frame2mid_4 = Frame(frame2mid, width=150)
frame2mid_4.pack()

weightlabel = Label(frame2mid_4, text='Weight:  ', font=("Times New Roman", 15))
weightlabel.grid(row=0, column=0, padx=5, pady=10)

weightbox = Entry(frame2mid_4, textvariable=weight, width=10, justify='center')
weightbox.grid(row=0, column=1)
weightbox.configure(state='disabled')

actlabel = Label(frame2mid_4, text='Activity ', font=("Times New Roman", 15))
actlabel.grid(row=0, column=2)
actbox = ttk.Combobox(frame2mid_4, values=["Little to no exercise", "light exercise 1-3 days / week",
                                           "Moderate exercise 3-5 days / week", "Heavy exercise 6-7 days/ week"], width=40, state="readonly")
actbox.set("Please select your lately activity")
actbox.grid(row=0, column=3)

# blank1 = Label(frame2mid_4, text='').grid(row=0, column=2)

frame2mid_5 = Frame(frame2mid)
frame2mid_5.pack()

bmr = IntVar()
tdee = IntVar()

bmrlabel = Label(frame2mid_5, text='BMR:', font=("Times New Roman", 15))
bmrlabel.grid(row=0, column=0)
bmrbox = Entry(frame2mid_5, textvariable=bmr, justify='center')
bmrbox.grid(row=0, column=1, padx=7)
bmr.set("")

tdeelabel = Label(frame2mid_5, text='TDEE:', font=("Times New Roman", 15))
tdeelabel.grid(row=0, column=2)
tdeebox = Entry(frame2mid_5, textvariable=tdee, justify='center')
tdeebox.grid(row=0, column=3, padx=7)
tdee.set("")

def calme():
    if male.get() ==1 :
        answer1 = 88.362 + (13.397 * weight.get()) + (4.799 * height.get()) - (5.677 * age.get())
        bmrbox.delete(0, END)
        bmrbox.insert(0, f'{answer1: .2f}')
    elif female.get() == 1:
        answer2 = 447.593 + (9.247 * weight.get()) + (3.098 * height.get()) - (4.330 * age.get())
        bmrbox.delete(0, END)
        bmrbox.insert(0, f'{answer2: .2f}')

    answer1 = 88.362 + (13.397 * weight.get()) + (4.799 * height.get()) - (5.677 * age.get())
    a1 = answer1 * 1.2
    a2 = answer1 * 1.375
    a3 = answer1 * 1.55
    a4 = answer1 * 1.725

    if actbox.get() == "Little to no exercise" and male.get() == 1:
            tdeebox.delete(0, END)
            tdeebox.insert(0, f'{answer1 * 1.2: .2f}')
            bmrbox.delete(0, END)
            bmrbox.insert(0, f'{answer1: .2f}')
    elif actbox.get() == "Little to no exercise" and female.get() == 1:
            tdeebox.delete(0, END)
            tdeebox.insert(0, f'{answer2 * 1.2: .2f}')
            bmrbox.delete(0, END)
            bmrbox.insert(0, f'{answer2: .2f}')
    elif actbox.get() == "light exercise 1-3 days / week" and male.get() == 1:
            tdeebox.delete(0, END)
            tdeebox.insert(0, f'{answer1 * 1.375: .2f}')
            bmrbox.delete(0, END)
            bmrbox.insert(0, f'{answer1: .2f}')
    elif actbox.get() == "light exercise 1-3 days / week" and female.get() == 1:
            tdeebox.delete(0, END)
            tdeebox.insert(0, f'{answer2 * 1.375: .2f}')
            bmrbox.delete(0, END)
            bmrbox.insert(0, f'{answer2: .2f}')
    elif actbox.get() == "Moderate exercise 3-5 days / week" and male.get() == 1:
            tdeebox.delete(0, END)
            tdeebox.insert(0, f'{answer1 * 1.55: .2f}')
            bmrbox.delete(0, END)
            bmrbox.insert(0, f'{answer1: .2f}')
    elif actbox.get() == "Moderate exercise 3-5 days / week" and female.get() == 1:
            tdeebox.delete(0, END)
            tdeebox.insert(0, f'{answer2 * 1.55: .2f}')
            bmrbox.delete(0, END)
            bmrbox.insert(0, f'{answer2: .2f}')
    elif actbox.get() == "Heavy exercise 6-7 days/ week" and male.get() == 1:
            tdeebox.delete(0, END)
            tdeebox.insert(0, f'{answer1 * 1.725: .2f}')
            bmrbox.delete(0, END)
            bmrbox.insert(0, f'{answer1: .2f}')
    elif actbox.get() == "Heavy exercise 6-7 days/ week" and female.get() == 1:
            tdeebox.delete(0, END)
            tdeebox.insert(0, f'{answer2 * 1.725: .2f}')
            bmrbox.delete(0, END)
            bmrbox.insert(0, f'{answer2: .2f}')


    # elif female.get() == 1:
    #     answer2 = 447.593 + (9.247 * weight.get()) + (3.098 * height.get()) - (4.330 * age.get())
    #     bmrbox.delete(0, END)
    #     bmrbox.insert(0, f'{answer2: .2f}')




frame2mid_6 = Frame(frame2mid)
frame2mid_6.pack()
calbtn = Button(frame2mid_6, text='Calculate', width=12, height='2', relief='groove', command=calme)
calbtn.grid(row=0, column=0, padx=8, pady=10)
clearbtn = Button(frame2mid_6, text='CLear', width=12, height='2', relief='groove', command=clearbtn)
clearbtn.grid(row=0, column=1, padx=8, pady=10)

tcasframe = LabelFrame(frame2, text='GAT&PAT Score Calculator', fg='#561d5e', font='3')
tcasframe.pack(ipadx=50, ipady=4)

tcaslabel = Frame(tcasframe)
tcaslabel.pack()
tlabel = Label(tcaslabel, text='GAT&PAT Score (KMITL 64)', font=("Times New Roman", 15))
tlabel.pack(pady=5)

gp = Frame(tcasframe)
gp.pack()

gatlabel = Label(gp, text='GAT: ', font=("Times New Roman", 15))
gatlabel.grid(row=0, column=0, pady=5)

gatget = Entry(gp, width=8, justify='center')
gatget.grid(row=0, column=1, padx=5)

patlabel = Label(gp, text='PAT1: ', font=("Times New Roman", 15))
patlabel.grid(row=0, column=3, padx=5, pady=5)

patget = Entry(gp, width=8, justify='center')
patget.grid(row=0, column=4, padx=5)

pat2label = Label(gp, text='PAT2: ', font=("Times New Roman", 15))
pat2label.grid(row=0, column=5, padx=5)

pat2get = Entry(gp, width=8, justify='center')
pat2get.grid(row=0, column=6, padx=5)


scoreframe = Frame(tcasframe, width=150)
scoreframe.pack()

scorelabel = Label(scoreframe, text='Score: ', font=("Times New Roman", 15))
scorelabel.grid(row=0, column=0, pady=10)

sentry = Entry(scoreframe, width=20, justify='center')
sentry.grid(row=0, column=1, ipady=5, pady=10, ipadx=10)

def scorecal():
    if gatget.get() == '' and patget.get() == '' and pat2get.get() == '':
        sentry.delete(0, END)
        textext = "Please insert some data"
        sentry.insert(0, textext)
    elif int(gatget.get()) > 0 and int(patget.get()) > 0 and int(pat2get.get()) > 0:
        gatgo = (int(gatget.get())) * 10
        patgo = (int(patget.get())) * 50
        pat2go = (int(pat2get.get())) * 40
        allsum = gatgo + patgo + pat2go
        sentry.delete(0, END)
        sentry.insert(0, f'{allsum: .2f}')

def delscore():
    sentry.delete(0,  END)
    patget.delete(0,  END)
    gatget.delete(0,  END)
    pat2get.delete(0,  END)



btnscore = Button(scoreframe, text='Calculate!', width=10, height=3, relief='groove', command=scorecal)
btnscore.grid(row=0, column=3, padx=10)

delscore = Button(scoreframe, text='Clear', width=10, height=3, relief='groove', command=delscore)
delscore.grid(row=0, column=4, padx=10)

frame3 = Frame(top)
frame3.pack(side=LEFT, padx=5)


frameshape = LabelFrame(frame3, width=500, height=500, text="Geometry Area Calculator", fg='#D99D31', font='3')
frameshape.pack(padx=5, ipadx=5)



def shapeselecter():
    if shapeselect.get() == "Select the Geometry shape":
        widthentry.configure(state='disabled')
        heightentry.configure(state='disabled')
        baseentry.configure(state='disabled')
        lengthentry.configure(state='disabled')
        radiusentry.configure(state='disabled')
        

def shapecal():
    textlol = "insert some value to make a calculation"
    if shapeselect.get() == "Square" and widthentry.get() == '':
        textlol = " insert some value to make a calculation"
        ansentry.delete(0, END)
        ansentry.insert(0, textlol)
    elif shapeselect.get() == "Square":
        ans1 = int(widthentry.get())*int(widthentry.get())
        ansentry.delete(0, END)
        ansentry.insert(0, ans1)


    elif shapeselect.get() == "Triangle" and baseentry.get() == '' and heightentry.get() == '':
        textlol = " insert some value to make a calculation!!!"
        ansentry.delete(0, END)
        ansentry.insert(0, textlol)
    elif shapeselect.get() == "Triangle":
        ans2 = int(baseentry.get()) * int(heightentry.get()) * 1/2
        ansentry.delete(0, END)
        ansentry.insert(0, ans2)


    elif shapeselect.get() == "Circle" and radiusentry.get() == '':
        textlol = " insert some value to make a calculation"
        ansentry.delete(0, END)
        ansentry.insert(0, textlol)
    elif shapeselect.get() == "Circle":
        ans3 = 22/7 * (int(radiusentry.get()))**2
        ans31 = f'{ans3: .2f}'
        ansentry.delete(0, END)
        ansentry.insert(0, ans31)


    elif shapeselect.get() == "Cylinder" and radiusentry.get() == '' or heightentry.get() == '':
        textlol = "insert some value to make a calculation"
        ansentry.delete(0, END)
        ansentry.insert(0, textlol)
    elif shapeselect.get() == "Cylinder":
        ans4 = int(2*22/7) * (int(radiusentry.get()))**2 + (int(heightentry.get()) * int(int(22/7)*radiusentry.get()))
        ansentry.delete(0, END)
        ansentry.insert(0, ans4)
       
    elif shapeselect.get() == "Cube" and widthentry.get() == '':
        textlol = " insert somevalue to make a calculation"
        ansentry.delete(0, END)
        insert = ansentry.insert(0, textlol)
    elif shapeselect.get() == "Cube":
        ans4 = 6*(int(widthentry.get()))**2
        ansentry.delete(0, END)
        ansentry.insert(0, ans4)
    elif shapeselect.get() == "Select the Geometry shape":
        ansentry.configure(state='disabled')
    elif shapeselect.get() == "Circle":
        ansnew = 22/7 * int((radiusentry.get())**2)
        ansentry.delete(0, END)
        ansentry.insert(0, ansnew)


shapearea1 = Frame(frameshape)
shapearea1.pack()
shapeselect = ttk.Combobox(shapearea1,
                                 values=["Select the Geometry shape", "Square", "Triangle", "Circle", "Cylinder",
                                         "Cube"], state="readonly", width=30, height=10, justify
                           ='center')
shapeselect.pack(padx=5, pady=8)
shapeselect.current(0)



shapearea2 = Frame(frameshape)
shapearea2.pack(pady=10)

widthlabel = Label(shapearea2, text='Width: ', font=("Courier New", 18))
widthlabel.grid(row=0, column=0)
widthentry = Entry(shapearea2, width=8, justify='center')
widthentry.grid(row=0, column=1, padx=3, pady=10, ipadx=10, ipady=4)

heightlab = Label(shapearea2, text='Height: ', font=("Courier New", 18))
heightlab.grid(row=1, column=0, padx=10)
heightentry = Entry(shapearea2, width=8, justify='center')
heightentry.grid(row=1, column=1, padx=3, pady=10, ipadx=10, ipady=4)

baselabel = Label(shapearea2, text='Base: ', font=("Courier New", 18))
baselabel.grid(row=2, column=0)
baseentry = Entry(shapearea2, width=8, justify='center')
baseentry.grid(row=2, column=1, padx=3, pady=10, ipadx=10, ipady=4)

lengthlabel = Label(shapearea2, text='Length: ', font=("Courier New", 18))
lengthlabel.grid(row=3, column=0, padx=5)
lengthentry = Entry(shapearea2, width=8, justify='center')
lengthentry.grid(row=3, column=1, padx=3, pady=10, ipadx=10, ipady=4)

radiuslabel = Label(shapearea2, text='Radius:', font=('Courier New', 18))
radiuslabel.grid(row=4, column=0)
radiusentry = Entry(shapearea2, width=8, justify='center')
radiusentry.grid(row=4, column=1, padx=3, pady=10, ipadx=10, ipady=4)

ansentry = Entry(shapearea2, width=30, justify='center')
ansentry.grid(row=5, column=0, columnspan=2, ipadx=20, ipady=6, pady=10)

shapebtn = Button(shapearea2, text='Calculate area!', font=('Courier New', 12), command=shapecal)
shapebtn.grid(row=6, column=0, columnspan=2, padx=5, pady=5, ipadx=5, ipady=10)

creditframe = LabelFrame(frame3, text='Credit', font=18, fg='#ff0051')
creditframe.pack()
Label(creditframe, text='\nUtility  GUI Calculator', font=("Times New Roman", 10)).pack()
Label(creditframe, text='Created by Nakorn Boonprasong', font=("Courier New", 10)).pack(padx=10, pady=5)
Label(creditframe, text='6/19/2021').pack()
Label(creditframe, text='Matthayom Watnairong School', font=("Courier New", 10)).pack(pady=5)
Label(creditframe, text='MATH-SCI Program', font=("Courier New", 10)).pack(pady=5)
Label(creditframe, text='', font=("Courier New", 10)).pack(pady=5)
top.mainloop()
