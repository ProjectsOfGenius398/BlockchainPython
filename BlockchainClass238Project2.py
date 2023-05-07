import hashlib

text1="John gave me 10 dollars"
result=hashlib.sha3_256(text1.encode())
print("Text 1 sha3_256 is : ", result.hexdigest())

text2="Bob gave 5 dollars to Alex"
result=hashlib.sha3_256(text2.encode())
print("Text 2 sha3_256 is : ", result.hexdigest())

text3 = "John gave 5 dollars to Shawn on 13th October"
result=hashlib.sha3_256(text3.encode())
print("Text 3 sha3_256 is : ", result.hexdigest()) 