import hashlib

text="Hello World"

result=hashlib.sha3_256(text.encode())

print("The sha3_256 is : ",result.hexdigest())

