from tkinter import *
from PIL import ImageTk, Image
from tkinter import messageBox
from web3 import Web3

root = Tk()
root.title("Crypto")
root.configure(background="white")
infura_url='https://sepolia.infura.io/v3/b7bb76f13f004cc9a6eadfb0c9381796'
web3_infura_connection=Web3(Web3.HTTPProvider(infura_url))

image_logo=ImageTk.PhotoImage(Image.open("logo.jpg"))
image_label=Label(root,image=image_logo)
image_label.pack(side="top")

frame=Frame(root,bg='white',padx=5,pady=5)
Label(frame,text="Account 1 ", fg='black',bg='white').grid(row=0,column=0, sticky=W, pady=10)
Label(frame,text="Account 2 ", fg='black',bg='white').grid(row=1,column=0, sticky=W, pady=10)
Label(frame,text="Private Key ",fg='black',bg='white').grid(row=2,column=1,sticky=W,pady=10)
Label(frame,text="ETH:", fg='black',bg='white').grid(row=3, column=0, sticky=W, pady=10)
Label(frame,text="Gas Price: ", fg='black', bg='white').grid(row=4, column=0, sticky=W, pady=10)
Label(frame,text="Gas >imit: ", fg='black', bg='white').grid(row=5, column=0, sticky=W, pady=10)

account1=Entry(frame)
account2=Entry(frame)
private_key=Entry(frame)
amount=Entry(frame)
gas_Price=Entry(frame)
gas_limit=Entry(frame)

account1.grid(row=0, column=1, pady=10, padx=20)
account2.grid(row=1, column=1, pady=10, padx=20)
private_key.grid(row=2, column=1, pady=10, padx=20)
amount.grid(row=3, column=1, pady=10, padx=20)
gas_Price.grid(row=4, column=1, pady=10, padx=20)
gas_limit.grid(row=5, column=1, pady=10, padx=20)

def MoneyMoneyMoney():
	account1_id=account1.get()
	account2_id=account2.get()
	key=private_key.get()
	eth_amount=amount.get()
	Gfee=gas_Price.get()
	Glimit=gas_limit.get()

	nonce=web3_infura_connection.getTransactionCount(account1_id)
	transaction={
		'nonce':nonce,
		'to':account2_id,
		'value':web3_infura_connection.toWei(eth_amount,'ether'),
		'gas':int(Glimit),
		'gasPrice':web3_infura_connection,toWei(gas_Price, 'gwei')
	}

	signed_transaction=web3_infura_connection.eth.account.signTransaction(transaction, key)
	transaction=web3_infura_connection.eth.sendRawTransaction(signed_transaction.rawTransaction)
	print("Transaction Successful, id= ", transaction_hash.hex())

	messageBox.showInfo('Transaction info: ','Transaction complete')

frame.pack()
transfer_eth=Button(root, text='Transfer eth', command=MoneyMoneyMoney, highlightbackground='white', width=15)
transfer_eth.pack()
root.mainloop()
