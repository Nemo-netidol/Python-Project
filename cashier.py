
from tkinter import *
import os
from tkinter import ttk

def mainpagedestroy():
   main_page0.destroy()

def main_page1():
   var1 = IntVar()
   var2 = IntVar()
   var3 = IntVar()
   var4 = IntVar()
   var5 = IntVar()
   var6 = IntVar()
   var7 = IntVar()
   var8 = IntVar()
   var001 = IntVar()

   var1.set(0)
   var2.set(0)
   var3.set(0)
   var4.set(0)
   var5.set(0)
   var6.set(0)
   var7.set(0)
   var8.set(0)
   var001.set(0)

   stre1 = StringVar()
   stre1.set("0")

   stre2 = StringVar()
   stre2.set("0")

   stre3 = StringVar()
   stre3.set("0")

   stre4 = StringVar()
   stre4.set("0")

   stre5 = StringVar()
   stre5.set("0")

   stre6 = StringVar()
   stre6.set("0")

   stre7 = StringVar()
   stre7.set("0")

   stre8 = StringVar()
   stre8.set("0")

   var01 = StringVar()
   var01.set("0")

   stre01 = StringVar()
   stre01.set("0")

   den1 = StringVar()
   den1.set("0")


   def check():
       if var1.get() == 1:
           entry1.configure(state="normal")
           stre1.set("1")
       elif var1.get() == 0:
           entry1.configure(state="disabled")
           stre1.set("0")
       if var2.get() == 1:
           entry2.configure(state="normal")
           stre2.set("1")
       elif var2.get() == 0:
           entry2.configure(state="disabled")
           stre2.set("0")
       if var3.get() == 1:
           entry3.configure(state="normal")
           stre3.set("1")
       elif var3.get() == 0:
           entry3.configure(state="disabled")
           stre3.set("0")
       if var4.get() == 1:
           entry4.configure(state="normal")
           stre4.set("1")
       elif var4.get() == 0:
           entry4.configure(state="disabled")
           stre4.set("0")
       if var5.get() == 1:
           entry5.configure(state="normal")
           stre5.set("1")
       elif var5.get() == 0:
           entry5.configure(state="disabled")
           stre5.set("0")
       if var6.get() == 1:
           entry6.configure(state="normal")
           stre6.set("1")
       elif var6.get() == 0:
           entry6.configure(state="disabled")
           stre6.set("0")
       if var7.get() == 1:
           entry7.configure(state="normal")
           stre7.set("1")
       elif var7.get() == 0:
           entry7.configure(state="disabled")
           stre7.set("0")
       if var8.get() == 1:
           entry8.configure(state="normal")
           stre8.set("1")
       elif var8.get() == 0:
           entry8.configure(state="disabled")
           stre8.set("0")
       if var01.get() == 1:
           entry01.configure(state="normal")
           stre01.set("1")
       elif var01.get() == 0:
           entry01.configure(state="disabled")
           stre01.set("0")
       if var001.get() == 1:
           entryd1.configure(state="normal")
           den1.set("1")
       elif var001.get() == 0:
           entryd1.configure(state="disabled")
           den1.set("0")

   var001 = IntVar()
   var002 = IntVar()
   var003 = IntVar()
   var004 = IntVar()
   var005 = IntVar()
   var006 = IntVar()
   var007 = IntVar()

   var001.set("0")
   var002.set("0")
   var003.set("0")
   var004.set("0")
   var005.set("0")
   var006.set("0")
   var007.set("0")

   den1 = StringVar()
   den1.set("0")
   den2 = StringVar()
   den2.set("0")
   den3 = StringVar()
   den3.set("0")
   den4 = StringVar()
   den4.set("0")
   den5 = StringVar()
   den5.set("0")
   den6 = StringVar()
   den6.set("0")
   den7 = StringVar()
   den7.set("0")


   def desert():
       if var001.get() == 1:
           entryd1.configure(state="normal")
           den1.set("1")
       elif var001.get() == 0:
           entryd1.configure(state="disabled")
           den1.set("0")
       if var002.get() == 1:
           entryd2.configure(state="normal")
           den2.set("1")
       elif var002.get() == 0:
           entryd2.configure(state="disabled")
           den2.set("0")
       if var003.get() == 1:
           entryd3.configure(state="normal")
           den3.set("1")
       elif var003.get() == 0:
           entryd3.configure(state="disabled")
           den3.set("0")
       if var004.get() == 1:
           entryd4.configure(state="normal")
           den4.set("1")
       elif var004.get() == 0:
           entryd4.configure(state="disabled")
           den4.set("0")
       if var005.get() == 1:
           entryd5.configure(state="normal")
           den5.set("1")
       elif var005.get() == 0:
           entryd5.configure(state="disabled")
           den5.set("0")
       if var005.get() == 1:
           entryd5.configure(state="normal")
           den5.set("1")
       elif var005.get() == 0:
           entryd5.configure(state="disabled")
           den5.set("0")
       if var006.get() == 1:
           entryd6.configure(state="normal")
           den6.set("1")
       elif var006.get() == 0:
           entryd6.configure(state="disabled")
           den6.set("0")
       if var007.get() == 1:
           entryd7.configure(state="normal")
           den7.set("1")
       elif var007.get() == 0:
           entryd7.configure(state="disabled")
           den7.set("0")

   var01 = IntVar()
   var02 = IntVar()
   var03 = IntVar()
   var04 = IntVar()
   var05 = IntVar()

   var01.set("0")
   var02.set("0")
   var03.set("0")
   var04.set("0")
   var05.set("0")

   stre01 = StringVar()
   stre01.set("0")
   stre02 = StringVar()
   stre02.set("0")
   stre03 = StringVar()
   stre03.set("0")
   stre04 = StringVar()
   stre04.set("0")
   stre05 = StringVar()
   stre05.set("0")

   moneycome = IntVar()
   moneycome.set("0")
   change = IntVar()
   change.set("-----")
   vat_value = IntVar()
   vat_value.set("--")
   # total_value = StringVar()
   # total_value.set("--")
   change = StringVar()



   def water():
       if var01.get() == 1:
           entry01.configure(state="normal")
           stre01.set("1")
       elif var01.get() == 0:
           entry01.configure(state="disabled")
           stre01.set("0")
       if var02.get() == 1:
           entry02.configure(state="normal")
           stre02.set("1")
       elif var02.get() == 0:
           entry02.configure(state="disabled")
           stre02.set("0")
       if var03.get() == 1:
           entry03.configure(state="normal")
           stre03.set("1")
       elif var03.get() == 0:
           entry03.configure(state="disabled")
           stre03.set("0")
       if var04.get() == 1:
           entry04.configure(state="normal")
           stre04.set("1")
       elif var04.get() == 0:
           entry04.configure(state="disabled")
           stre04.set("0")
       if var05.get() == 1:
           entry05.configure(state="normal")
           stre05.set("1")
       elif var05.get() == 0:
           entry05.configure(state="disabled")
           stre05.set("0")

   def menuclear():
       entry1.configure(state="disabled")
       stre1.set("0")
       var1.set("0")
       entry2.configure(state="disabled")
       stre2.set("0")
       var2.set("0")
       entry3.configure(state="disabled")
       stre3.set("0")
       var3.set("0")
       entry4.configure(state="disabled")
       stre4.set("0")
       var4.set("0")
       entry5.configure(state="disabled")
       stre5.set("0")
       var5.set("0")
       entry6.configure(state="disabled")
       stre6.set("0")
       var6.set("0")
       entry7.configure(state="disabled")
       stre7.set("0")
       var7.set("0")
       entry8.configure(state="disabled")
       stre8.set("0")
       var8.set("0")
       entry01.configure(state="disabled")
       stre01.set("0")
       var01.set("0")
       entry02.configure(state="disabled")
       stre02.set("0")
       var02.set("0")
       entry03.configure(state="disabled")
       stre03.set("0")
       var03.set("0")
       entry04.configure(state="disabled")
       stre04.set("0")
       var04.set("0")
       entry05.configure(state="disabled")
       stre05.set("0")
       var05.set("0")
       entryd1.configure(state="disabled")
       den1.set("0")
       var001.set("0")
       entryd2.configure(state="disabled")
       den2.set("0")
       var002.set("0")
       entryd3.configure(state="disabled")
       den3.set("0")
       var003.set("0")
       entryd4.configure(state="disabled")
       den4.set("0")
       var004.set("0")
       entryd5.configure(state="disabled")
       den5.set("0")
       var005.set("0")
       entryd6.configure(state="disabled")
       den6.set("0")
       var006.set("0")
       entryd7.configure(state="disabled")
       den7.set("0")
       var007.set("0")
       total_value.set("0")
       vat_value.set("---")
       total_value.set("---")
       moneycome.set("0")
       change.set("-----")


   def tote_up():

       m1 = float(stre1.get()) * 9.99 + float(stre2.get()) * 8.99 + float(stre3.get()) * 49.99 + float(stre4.get()) * 12.99\
            + float(stre5.get()) * 2.99 + float(stre6.get()) * 65.99 + float(stre7.get()) * 15.99 + float(stre8.get()) * 25.99\
            + float(stre01.get()) * 0.99 + float(stre02.get()) * 2.99 + float(stre03.get()) *3.5 + float(stre04.get()) * 4.99\
            + float(stre05.get()) * 3.99 + float(den1.get()) * 2.99 + float(den2.get()) * 5.99 + float(den3.get()) * 5.99\
            + float(den4.get()) * 2.99 + float(den5.get()) * 9.99 + float(den6.get()) * 1.99 + float(den7.get()) * 1.69
       total_value.set(f'{m1: .2f}')
       cash = m1 + (7/100*m1)
       credit = m1 + (9/100*m1)
       paypal = m1 + (8/100*m1)
       eth = m1 + (10/100*m1)
       doge = m1 + (10/100*m1)
       global cashchange
       cashchange = float(moneycome.get()) - cash
       #change.set(f'${cashchange: .2f}')
       if payment_select.get() == "Cash":
           vat_value.set("7%")
           total_value.set(f'{cash: .2f}')
       elif payment_select.get() == "Credit card":
           total_value.set(f'{credit: .2f}')
           vat_value.set("9%")
       elif payment_select.get() == "PayPal":
           total_value.set(f'{paypal: .2f}')
           vat_value.set("8%")
       elif payment_select.get() == "Ethereum (ETH)":
           vat_value.set("10%")
           total_value.set(f'{eth: .2f}')
       elif payment_select.get() == "Doge Coin (DOGE)":
           vat_value.set("10%")
           total_value.set(f'{doge: .2f}')
       elif payment_select.get() == "Select the payment":
           vat_value.set("Please select the payment")
           total_value.set("#@!&")
           change.set("-----")


   def calbtn():
       global m1
       m1 = float(stre1.get()) * 9.99 + float(stre2.get()) * 8.99 + float(stre3.get()) * 49.99 + float(
           stre4.get()) * 12.99 \
            + float(stre5.get()) * 2.99 + float(stre6.get()) * 65.99 + float(stre7.get()) * 15.99 + float(
           stre8.get()) * 25.99 \
            + float(stre01.get()) * 0.99 + float(stre02.get()) * 2.99 + float(stre03.get()) * 3.5 + float(
           stre04.get()) * 4.99 \
            + float(stre05.get()) * 3.99 + float(den1.get()) * 2.99 + float(den2.get()) * 5.99 + float(
           den3.get()) * 5.99 \
            + float(den4.get()) * 2.99 + float(den5.get()) * 9.99 + float(den6.get()) * 1.99 + float(den7.get()) * 1.69

       cash = m1 + (7/100*m1)
       credit = m1 + (9/100*m1)
       paypal = m1 + (8/100*m1)
       eth = m1 + (10/100*m1)
       doge = m1 + (10/100*m1)

       cashchange = (moneycome.get()) - cash
       creditchange = moneycome.get() - credit
       palchange = moneycome.get() - paypal
       ethchange = moneycome.get() - eth
       dogechange = moneycome.get() - doge
       if m1 < 0.01:
           change.set("Please choose the menu")
       elif moneycome.get() == 0:
           change.set("Fill the money first!")
       elif payment_select.get() == "Cash":
           change.set(f'{cashchange: .2f}')
       elif payment_select.get() == "Credit card":
           change.set(f'{creditchange: .2f}')
       elif payment_select.get() == "PayPal":
           change.set(f'{palchange: .2f}')
       elif payment_select.get() == "Ethereum (ETH)":
           change.set(f'{ethchange: .2f}')
       elif payment_select.get() == "Doge Coin (DOGE)":
           change.set(f'{dogechange: .2f}')
       elif total_value.get() < 0.01:
           change.set("Please choose the menu")

   def billbill():
       total_value = StringVar()

       m1 = float(stre1.get()) * 9.99 + float(stre2.get()) * 8.99 + float(stre3.get()) * 49.99 + float(
           stre4.get()) * 12.99 \
            + float(stre5.get()) * 2.99 + float(stre6.get()) * 65.99 + float(stre7.get()) * 15.99 + float(
           stre8.get()) * 25.99 \
            + float(stre01.get()) * 0.99 + float(stre02.get()) * 2.99 + float(stre03.get()) * 3.5 + float(
           stre04.get()) * 4.99 \
            + float(stre05.get()) * 3.99 + float(den1.get()) * 2.99 + float(den2.get()) * 5.99 + float(
           den3.get()) * 5.99 \
            + float(den4.get()) * 2.99 + float(den5.get()) * 9.99 + float(den6.get()) * 1.99 + float(den7.get()) * 1.69
       servicecharge = int(m1) + int(0.1 * m1)
       order = int(stre1.get()) + int(stre2.get()) + int(stre3.get()) + int(stre4.get()) + int(stre5.get())\
               + int(stre6.get()) + int(stre7.get()) + int(stre8.get()) + int(stre01.get()) + int(stre02.get())\
               + int(stre03.get()) + int(stre04.get()) + int(stre05.get()) + int(den1.get()) + int(den2.get())\
               + int(den3.get()) + int(den6.get()) + int(den7.get()) + int(den4.get()) + int(den5.get())
       Line = ""


       receipt.delete(1.0, END)
       receipt.insert(END, Line)
       receipt.insert(END,"******************************************************************************************************\n")
       receipt.insert(END, "\t\t          Thank you for using our service!\n")
       receipt.insert(END, "******************************************************************************************************\n")
       receipt.insert(END, f"\nNumber of order: {    order}\t\t\n ")
       receipt.insert(END, f"Almomnd Tofu\t\t\t\t  {stre1.get()}\t\t   $ {int(stre1.get()) * 9.99}\n")
       receipt.insert(END, f"Bamboo Shoot Soup\t\t\t\t  {stre2.get()}\t\t   $ {int(stre2.get()) * 8.99}\n")
       receipt.insert(END, f"Crab Roe Tofu\t\t\t\t  {stre3.get()}\t\t   $ {int(stre3.get()) * 49.99}\n")
       receipt.insert(END, f"Cream Stew\t\t\t\t  {stre4.get()}\t\t   $ {int(stre4.get()) * 12.99}\n")
       receipt.insert(END, f"Fullmoon Egg\t\t\t\t  {stre5.get()}\t\t   $ {int(stre5.get()) * 2.99}\n")
       receipt.insert(END, f"Golden Crab\t\t\t\t  {stre6.get()}\t\t   $ {int(stre6.get()) * 65.99}\n")
       receipt.insert(END, f"Goulash\t\t\t\t  {stre7.get()}\t\t   $ {int(stre7.get()) * 15.99}\n")
       receipt.insert(END, f"Mattsutake Meat Rolls\t\t\t\t  {stre8.get()}\t\t   $ {int(stre8.get()) * 25.99}\n")
       receipt.insert(END, f"Mineral water\t\t\t\t  {stre01.get()}\t\t   $ {int(stre01.get()) * 0.99}\n")
       receipt.insert(END, f"Soft drink\t\t\t\t  {stre02.get()}\t\t   $ {int(stre02.get()) * 2.99}\n")
       receipt.insert(END, f"All kind of juice\t\t\t\t  {stre03.get()}\t\t   $ {int(stre03.get()) * 3.5}\n")
       receipt.insert(END, f"Tropical smoothy\t\t\t\t  {stre04.get()}\t\t   $ {int(stre04.get()) * 4.99}\n")
       receipt.insert(END, f"Holy water\t\t\t\t  {stre05.get()}\t\t   $ {int(stre05.get()) * 3.99}\n")

       receipt.insert(END, f"Sunsettia\t\t\t\t  {den1.get()}\t\t   $ {int(den1.get()) * 2.99}\n")
       receipt.insert(END, f"Tea Break Pancake\t\t\t\t  {den2.get()}\t\t   $ {int(den2.get()) * 5.99}\n")
       receipt.insert(END, f"Teyvat's honey Toast\t\t\t\t  {den3.get()}\t\t   $ {int(den3.get()) * 5.99}\n")
       receipt.insert(END, f"Doina's Special\t\t\t\t  {den4.get()}\t\t   $ {int(den4.get()) * 2.99}\n")
       receipt.insert(END, f"Banoffe pie\t\t\t\t  {den5.get()}\t\t   $ {int(den5.get()) * 9.99}\n")
       receipt.insert(END, f"Mint Jelly\t\t\t\t  {den6.get()}\t\t   $ {int(den6.get()) * 1.99}\n")
       receipt.insert(END, f"Ice Cream\t\t\t\t  {den7.get()}\t\t   $ {int(den7.get()) * 1.69}\n\n")
       receipt.insert(END,  "Total: " + total_entry.get() + "           "+ "Change: " + change.get())
# "Total: " + total_value.get() + "           " + change.get()



       receipt.configure(font='arial 10 bold')




   def reset123():
       receipt.delete(1.0, END)

#####################################################################################################################
   vat_value = StringVar()
   total_value = IntVar()
   global main_page0
   main_page0 = Toplevel(root)
   main_page0.title("Cashier manager 1.0")
   ##
   width = root.winfo_screenwidth()
   height = root.winfo_screenheight()
   main_page0.geometry("%dx%d" % (width, height))
   ##
   frame1 = Frame(main_page0, relief="groove", bd=15)
   frame1.pack(side=TOP)
   l1 = Label(frame1, text="            Cashier management system            ", font=('bold', 50))
   l1.grid(row=0, column=0)
   bottom_frame2 = Frame(main_page0, width=450, height=650, bd=10, relief="raise")
   bottom_frame2_top = Frame(bottom_frame2, width=450, height=325, relief="groove", bd=5)
   bottom_frame2_top.pack()

   bottom_frame2_food = Frame(bottom_frame2_top, width=450, height=325, relief="groove", bd=5)
   bottom_frame2_food.grid(row=0, column=0, columnspan=2)
   Label(bottom_frame2_food, text="                   Food                   ", font=("Calibri", 30, "bold")).pack()

   ###############################################################################################################

   checkbox1 = Checkbutton(bottom_frame2_top, text="Almond Tofu\t         $9.99", font=("Calibri", 13), variable=var1
                           , onvalue=1, offvalue=0, command=check)
   checkbox1.grid(row=1, column=0, sticky='w')
   entry1 = Entry(bottom_frame2_top, state="disabled", width=10, textvariable=stre1, justify='center')
   entry1.grid(row=1, column=1)

   checkbox2 = Checkbutton(bottom_frame2_top, text="Bamboo Shoot Soup\t         $8.99", font=("Calibri", 13),
                           variable=var2, onvalue=1, offvalue=0, command=check)
   checkbox2.grid(row=2, column=0, sticky='w')
   entry2 = Entry(bottom_frame2_top, width=10, text="0", state="disabled", textvariable=stre2, justify='center')
   entry2.grid(row=2, column=1)

   checkbox3 = Checkbutton(bottom_frame2_top, text="Crab Roe Tofu\t         $49.99", font=("Calibri", 13),
                           variable=var3, command=check, onvalue=1, offvalue=0)
   checkbox3.grid(row=3, column=0, sticky='w')
   entry3 = Entry(bottom_frame2_top, state="disabled", width=10, textvariable=stre3, justify='center')
   entry3.grid(row=3, column=1)

   checkbox4 = Checkbutton(bottom_frame2_top, text="Cream Stew\t         $12.99", font=("Calibri", 13), variable=var4,
                           command=check, onvalue=1, offvalue=0)
   checkbox4.grid(row=4, column=0, sticky='w')
   entry4 = Entry(bottom_frame2_top, state="disabled", width=10, textvariable=stre4, justify='center')
   entry4.grid(row=4, column=1)

   checkbox5 = Checkbutton(bottom_frame2_top, text="Fullmoon Egg\t         $2.99", font=("Calibri", 13), variable=var5,
                           command=check, onvalue=1, offvalue=0)
   checkbox5.grid(row=5, column=0, sticky='w')
   entry5 = Entry(bottom_frame2_top, state="disabled", width=10, textvariable=stre5, justify='center')
   entry5.grid(row=5, column=1)

   checkbox6 = Checkbutton(bottom_frame2_top, text="Golden Crab\t         $65.99", font=("Calibri", 13), variable=var6
                           , command=check, onvalue=1, offvalue=0)
   checkbox6.grid(row=6, column=0, sticky='w')
   entry6 = Entry(bottom_frame2_top, state="disabled", width=10, textvariable=stre6, justify='center')
   entry6.grid(row=6, column=1)

   checkbox7 = Checkbutton(bottom_frame2_top, text="Goulash\t\t         $15.99", font=("Calibri", 13), variable=var7,
                           command=check, onvalue=1, offvalue=0)
   checkbox7.grid(row=7, column=0, sticky='w')
   entry7 = Entry(bottom_frame2_top, state="disabled", width=10, textvariable=stre7, justify='center')
   entry7.grid(row=7, column=1)

   checkbox8 = Checkbutton(bottom_frame2_top, text="Matsutake Meat Rolls       $25.99", font=("Calibri", 13)
                           , variable=var8,
                           command=check, onvalue=1, offvalue=0)
   checkbox8.grid(row=8, column=0, sticky='w')
   entry8 = Entry(bottom_frame2_top, state="disabled", width=10, textvariable=stre8, justify='center')
   entry8.grid(row=8, column=1)


##################################################################################################################


   bottom_frame2_low = Frame(bottom_frame2, width=450, height=325, relief="groove", bd=5)
   bottom_frame2_low.pack()
   bottom_frame2.pack(side=LEFT)
   ##



   drinkLabel = Frame(bottom_frame2_low, width=450, height=325, relief="groove", bd=5)
   drinkLabel.grid(row=0, column=0, columnspan=2)
   Label(drinkLabel, text="                   Drink                   ", font=("Calibri", 30, "bold")).pack()


   checkbox01 = Checkbutton(bottom_frame2_low, text="Mineral water\t         $0.99", font=("Calibri", 13),
                            variable=var01, onvalue=1, offvalue=0, command=water)
   checkbox01.grid(row=1, column=0, sticky='w')
   entry01 = Entry(bottom_frame2_low, state="disabled", width=10, textvariable=stre01, justify='center')
   entry01.grid(row=1, column=1)
   checkbox02 = Checkbutton(bottom_frame2_low, text="Soft drink\t\t         $2.99", font=("Calibri", 13)
                            , variable=var02, onvalue=1, offvalue=0, command=water)
   checkbox02.grid(row=2, column=0, sticky='w')
   entry02 = Entry(bottom_frame2_low, state="disabled", width=10, textvariable=stre02, justify='center')
   entry02.grid(row=2, column=1)

   checkbox03 = Checkbutton(bottom_frame2_low, text="All kind of juice\t         $3.5", font=("Calibri", 13)
                            , variable=var03, onvalue=1, offvalue=0, command=water)
   checkbox03.grid(row=3, column=0, sticky='w')
   entry03 = Entry(bottom_frame2_low, state="disabled", width=10, textvariable=stre03, justify='center')
   entry03.grid(row=3, column=1)

   checkbox04 = Checkbutton(bottom_frame2_low, text="tropical smoothy\t         $4.99", font=("Calibri", 13)
                            , variable=var04, onvalue=1, offvalue=0, command=water)
   checkbox04.grid(row=4, column=0, sticky='w')
   entry04 = Entry(bottom_frame2_low, state="disabled", width=10, textvariable=stre04, justify='center')
   entry04.grid(row=4, column=1)

   checkbox05 = Checkbutton(bottom_frame2_low, text="Holy water\t         $3.99", font=("Calibri", 13), variable=var05
                            , onvalue=1, offvalue=0, command=water)
   checkbox05.grid(row=5, column=0, sticky='w')
   entry05 = Entry(bottom_frame2_low, state="disabled", width=10, textvariable=stre05, justify='center')
   entry05.grid(row=5, column=1)
#################################################################################################################
   frame3 = Frame(main_page0, width=450, height=650, bd=10, relief="raise", pady=-11)
   frame3.pack(side=LEFT)
   bottom_frame3_top = Frame(frame3, width=450, height=350, relief="raise")
   bottom_frame3_top.grid(row=0, column=0)
   bottom_frame3_low = Frame(frame3, width=450, height=300, pady=10)
   bottom_frame3_low.grid(row=1, column=0)


   desertframe = Frame(frame3, width=450, height=350, relief="groove", bd=5)
   desertframe.grid(row=0, column=0)
   desertlabelframe = Frame(desertframe, width=450, height=350, relief="groove", bd=5)
   desertlabelframe.grid(row=0, column=0, columnspan=2)
   Label(desertlabelframe, text="                   Desert                   ", font=("Calibri", 30, "bold")).pack()

   # checkbox1 = Checkbutton(bottom_frame2_top, text="Almond Tofu\t         100$", font=("Calibri", 13), variable=var1
   #                         , onvalue=1, offvalue=0, command=check)
   # checkbox1.grid(row=1, column=0, sticky='w')
   # entry1 = Entry(bottom_frame2_top, state="disabled", width=10, textvariable=stre1, justify='center')
   # entry1.grid(row=1, column=1)

   checkboxd1 = Checkbutton(desertframe, text="Sunsettia\t\t         $2.99", font=("Calibri", 13), variable=var001
                            , onvalue=1, offvalue=0, command=desert)
   checkboxd1.grid(row=2, column=0, sticky='w')
   entryd1 = Entry(desertframe, state="disabled", width=10, textvariable=den1, justify='center')
   entryd1.grid(row=2, column=1)

   checkboxd2 = Checkbutton(desertframe, text="Tea Break Pancake\t         $5.99", font=("Calibri", 13), variable=var002
                           , onvalue=1, offvalue=0, command=desert)
   checkboxd2.grid(row=3, column=0, sticky='w')
   entryd2 = Entry(desertframe, state="disabled", width=10, textvariable=den2, justify='center')
   entryd2.grid(row=3, column=1)

   checkboxd3 = Checkbutton(desertframe, text="Teyvat's honey toast         $5.99", font=("Calibri", 13)
                            , variable=var003, onvalue=1, offvalue=0, command=desert)
   checkboxd3.grid(row=4, column=0, sticky='w')
   entryd3 = Entry(desertframe, state="disabled", width=10, textvariable=den3, justify='center')
   entryd3.grid(row=4, column=1)

   checkboxd4 = Checkbutton(desertframe, text="Diona's special\t         $2.99", font=("Calibri", 13), variable=var004
                           , onvalue=1, offvalue=0, command=desert)
   checkboxd4.grid(row=5, column=0, sticky='w')
   entryd4 = Entry(desertframe, state="disabled", width=10, textvariable=den4, justify='center')
   entryd4.grid(row=5, column=1)

   checkboxd5 = Checkbutton(desertframe, text="Banoffe pie\t         $9.99", font=("Calibri", 13), variable=var005
                           , onvalue=1, offvalue=0, command=desert)
   checkboxd5.grid(row=6, column=0, sticky='w')
   entryd5 = Entry(desertframe, state="disabled", width=10, textvariable=den5, justify='center')
   entryd5.grid(row=6, column=1)

   checkboxd6 = Checkbutton(desertframe, text="Mint Jelly\t\t         $1.99", font=("Calibri", 13), variable=var006
                           , onvalue=1, offvalue=0, command=desert)
   checkboxd6.grid(row=7, column=0, sticky='w')
   entryd6 = Entry(desertframe, state="disabled", width=10, textvariable=den6, justify='center')
   entryd6.grid(row=7, column=1)

   checkboxd7 = Checkbutton(desertframe, text="Ice cream\t\t         $1.69", font=("Calibri", 13), variable=var007
                           , onvalue=1, offvalue=0, command=desert)
   checkboxd7.grid(row=8, column=0, sticky='w')
   entryd7 = Entry(desertframe, state="disabled", width=10, textvariable=den7, justify='center')
   entryd7.grid(row=8, column=1)



   buttonframe = Frame(desertframe, width=450, height=80)
   buttonframe.grid(row=9, column=0, columnspan=2)
   clearbutton = Button(buttonframe, text="Clear", font=("Calibri", 15, "bold"), relief="raised", bd=5, padx=7,
                        pady=2, command=menuclear, width=6, height=1)
   clearbutton.pack(side=LEFT, padx=5, pady=5)

   billbutton = Button(buttonframe, text="Create a bill", font=("Calibri", 15, "bold"), relief="raised", bd=5, padx=7,
                       pady=2, command=billbill, width=10, height=1)
   billbutton.pack(side=LEFT, padx=5, pady=5)

   calculatebutton = Button(buttonframe, text="Tote up", font=("Calibri", 15, "bold"), relief="raised", bd=5,
                            padx=7, command=tote_up, width=6, height=1, pady=2)
   calculatebutton.pack(side=RIGHT, padx=2, pady=2)
   Label(buttonframe, text='').pack()


#####################################################################################################################

   subframe3bottom = Frame(bottom_frame3_low, width=450, height=400, pady=13)
   subframe3bottom.pack(side=TOP)
   payment_select = ttk.Combobox(subframe3bottom,
                                 values=["Select the payment", "Cash", "Credit card", "PayPal", "Ethereum (ETH)",
                                         "Doge Coin (DOGE)"], state="readonly")
   payment_select.current(0)
   payment_select.grid(row=0, column=1, padx=5)
   payment_label = Label(subframe3bottom, text="Payment", font=("Calibri", 20, "bold"))
   payment_label.grid(row=0, column=0)
   vat = Label(subframe3bottom, text="VAT", font=("Calibri", 18, "bold"))
   vat.grid(row=2, column=0)
   vat_entry = Entry(subframe3bottom, textvariable=vat_value, width=23, justify='center')
   vat_entry.grid(row=2, column=1)
   total = Label(subframe3bottom, text="Total", font=("Calibri", 18, "bold"))
   total.grid(row=4, column=0)
   total_entry = Entry(subframe3bottom, textvariable=total_value, width=23, justify='center')
   total_entry.grid(row=4, column=1)
   vat_value.set("---")
   total_value.set("---")


   subframe3bottom2 = Frame(bottom_frame3_low, width=450, height=400, pady=10)
   subframe3bottom2.pack(side=BOTTOM)
   p1 = Label(subframe3bottom2, text="Receive", font=("Calibri", 15, "bold"))
   p1.grid(row=0, column=0)
   p1entry = Entry(subframe3bottom2, width=15, textvariable=moneycome, justify='center')
   p1entry.grid(row=0, column=1, padx=5)
   p2 = Label(subframe3bottom2, text="Change", font=("Calibri", 15, "bold"))
   p2.grid(row=0, column=2)
   p2entry = Entry(subframe3bottom2, width=22, textvariable=change, justify='center')
   p2entry.grid(row=0, column=3, padx=5)
   calbtn = Button(subframe3bottom2, text="Calculate", font=("Calibri", 10, "bold"), relief="groove", command=calbtn)
   calbtn.grid(row=0, column=4, padx=11)
   ##
   bottom_frame4 = Frame(main_page0, width=450, height=650, bd=10, relief="raise")
   bottom_frame4.pack(side=LEFT)
   receipt_label = Label(bottom_frame4, text="                 Receipt                 ", relief="groove", bd=7, font='Calibri 30 bold')
   receipt_label.pack()
   bottom_frame4_top = Frame(bottom_frame4, width=450, height=400, relief="ridge", bd=10)
   bottom_frame4_top.pack(side=TOP)
   bottom_frame4_low = Frame(bottom_frame4, width=450, height=400, relief="raise", bd=10)
   bottom_frame4_low.pack(side=BOTTOM)

   receipt = Text(bottom_frame4_top, width=450, relief="raise", bd=5, height=25)
   receipt.pack()

   deletebutton = Button(bottom_frame4_low, text="Delete", command=reset123, relief="groove", font=("Calibri", 20, "bold"), width=15)
   deletebutton.pack(side=RIGHT)
   exitbutton = Button(bottom_frame4_low, text="Exit", command=mainpagedestroy, relief="groove", font=("Calibri", 20, "bold"), width=15)
   exitbutton.pack(side=LEFT)
   ##

def destroy():
   screen_0.destroy()
   page2.destroy()
   main_page1()

def  destroy_1():
   screen_1.destroy()
def destroy_2():
   screen_2.destroy()
def login_sus():
   global screen_0
   screen_0 = Toplevel(root)
   screen_0.geometry("150x100")
   screen_0.title("Sucess!")
   screen_0.config(bg="#E5E4CD")
   Label(screen_0, text="Login sucess", font=(("Calibri", 13)), bg="#E5E4CD", fg="#31c923").pack()
   Label(screen_0, text="").pack()
   Button(screen_0, text="Ok", command=destroy, width=10).pack()
def error_1():
   global screen_1
   screen_1 = Toplevel(root)
   screen_1.geometry("400x100")
   screen_1.title("System message")
   Label(screen_1, text="System cannot able to recognise this password,\n"
                        " please try again", font=(("Calibri", 13))).pack()
   Label(screen_1, text="").pack()
   Button(screen_1, text="Ok", command=destroy_1, width=10).pack()
def user_not_found():
   global screen_2
   screen_2 = Toplevel(root)
   screen_2.geometry("150x100")
   screen_2.title("User not found!")
   Label(screen_2, text="User not found:(", font=(("Calibri", 13))).pack()
   Label(screen_2, text="").pack()
   Button(screen_2, text="Ok", command=destroy_2, width=10).pack()
def r_login():
   user_1 = r_username.get()
   password_1 = r_password.get()
   user_entry.delete(0, END)
   password_entry.delete(0, END)

   list_of_file = os.listdir()
   if user_1 in list_of_file:
       file1 = open(user_1, "r")
       verify = file1.read().splitlines()
       if password_1 in verify:
           login_sus()
       else:
           error_1()
   else:
       user_not_found()

def login():
   global page2
   global r_username
   global r_password
   global password_entry
   global user_entry
   page2 = Toplevel(root)
   page2.config(bg="#E5E4CD")
   page2.title("Login page")
   page2.geometry("300x200")
   Label(page2, text="Please fill the required fields below", font=(("Calibri", 13)), bg="#E5E4CD", fg="#2f658e").pack(pady=3)
   ##String Var
   r_username = StringVar()
   r_password = StringVar()
   ############
   Label(page2, text="Username", bg="#E5E4CD").pack()
   user_entry = Entry(page2, text=r_username, bg="#f0f0f0")
   user_entry.pack()
   Label(page2, text=" ", bg="#E5E4CD").pack()
   Label(page2, text="Password", bg="#E5E4CD").pack()
   password_entry = Entry(page2, textvariable=r_password, show="*", bg="#f0f0f0")
   password_entry.pack()
   Button(page2, text="Login", width=10, command=r_login).pack(pady=10)


def reg_click():
   user_info = username.get()
   password_info = password.get()

   file = open(user_info, "w")
   file.write(user_info + "\n")
   file.write(password_info)
   file.close()
   alpha.delete(0, END)
   beta.delete(0, END)

   reg = Label(page1, text="Registration Successfully!", fg="green", font=(("Calibri", 13)))
   reg.pack()
def register():
   global page1
   page1 = Toplevel(root)
   page1.title("Register page")
   page1.geometry("300x200")
   page1.config(bg="#E5E4CD")
   ##String Var
   global username
   global password
   global alpha
   global beta
   username = StringVar()
   password = StringVar()
   ###########
   Label(page1, text="Please fill the required fields below", font=("Calibri", 13), bg="#E5E4CD").pack(pady=3)
   Label(page1, text="Create a Username*", bg="#E5E4CD", fg="#f74231").pack()
   alpha = Entry(page1, textvariable=username, bg="#f0f0f0")
   alpha.pack()
   Label(page1, text="  ", bg="#E5E4CD").pack()
   Label(page1, text="Create a Password*", bg="#E5E4CD", fg="#f74231").pack()
   beta = Entry(page1, textvariable=password, bg="#f0f0f0")
   beta.pack()

   Button(page1, text="Register", width=10, command=reg_click).pack(pady=10)



def main_page():
   global root
   root = Tk()
   root.geometry("380x300")
   root.config(bg='#E5E4CD')
   root.title("Cashier management system")
   Label(text="Cashier management system 1.0", width="300", height="2", font=("Calibri", 15), bg='#E5E4CD').pack()
   Label(text=" ", bg='#E5E4CD').pack()
   Button(text="Login", height="2", width="15", command=login).pack()
   Label(text=" ", bg='#E5E4CD').pack()
   Button(text="Register", height="2", width="15", command=register).pack()
   Label(text=" ", bg='#E5E4CD').pack()
   Button(text="Admin", command=main_page1, height="2", width="15").pack()


   root.mainloop()

main_page()

