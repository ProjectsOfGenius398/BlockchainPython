from tkinter import *
from web3 import Web3
from PIL import ImageTk, Image

root = Tk()
root.title("Account Details")

ganache_url = 'http://127.0.0.1:7545'

web3 = Web3(Web3.HTTPProvider(ganache_url))

img = ImageTk.PhotoImage(Image.open("image.png"))
panel = Label(root, image=img, bg='white')
panel.pack(side="top")

frame = Frame(
    root,
    bg='white',
    padx=5,
    pady=5
)
# create the labels to hold the account numbers
Label(frame,text="Account 1 ", fg='black',bg='white').grid(row=0,column=0, sticky=W, pady=10)
Label(frame,text="Account 2 ", fg='black',bg='white').grid(row=1,column=0,sticky=W,pady=10)
Label(frame,text="Account 3 ", fg='black',bg='white').grid(row=2,column=0, sticky=W, pady=10)
Label(frame,text="Account 4 ", fg='black',bg='white').grid(row=3,column=0, sticky=W, pady=10)
Label(frame,text="Account 5 ", fg='black',bg='white').grid(row=4,column=0, sticky=W, pady=10)
Label(frame,text="Account 6 ", fg='black',bg='white').grid(row=5,column=0, sticky=W, pady=10)

#Create entry elements to get the use input for account addresses 
account1=Entry(frame)
account2=Entry(frame)
account3=Entry(frame)
account4=Entry(frame)
account5=Entry(frame)
account6=Entry(frame)
#place the entry elements on the root window
account1.grid(row=0, column=1,padx=10, pady=20)
account2.grid(row=1, column=1,padx=10, pady=20)
account3.grid(row=2, column=1,padx=10, pady=20)
account4.grid(row=3, column=1,padx=10, pady=20)
account5.grid(row=4, column=1,padx=10, pady=20)
account6.grid(row=5, column=1,padx=10, pady=20)

#create thee text box
result=Text(root, height=10, width=45)
#define a function CHECK_BALANCE() and add the code inside it.
def thenIwillShowTheTruePowerOfTheDarkSideOfTheForce():
    accountNo=[]   
    accountNo.append(account1.get())
    accountNo.append(account2.get())
    accountNo.append(account3.get())
    accountNo.append(account4.get())
    accountNo.append(account5.get())
    accountNo.append(account6.get())
count=1

frame.pack()

#Create a button element to call the CHECK_BALANCE()


    

result.pack(pady=5)
root.mainloop()
