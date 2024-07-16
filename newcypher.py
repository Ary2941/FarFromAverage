
# 9's cypher (the maximum that one letter can vary is 9)

message = str(input("write me some message!: "))
factor = int(input("write me the key: "))

xfactor = str(factor)

if len(message) > len(xfactor):
    print (len(message) // len(xfactor))

    print(len(message)%len(xfactor))

    xfactor = xfactor*(len(message) // len(xfactor)) + xfactor[:(len(message)%len(xfactor))]
print(xfactor.split())






lista = []
for item in range(len(message)):
    lista += [(ord(message[item])+int(xfactor[item])) % 127]

newmessage = ""
for item in lista:
    newmessage += chr(item)

if len(message) == len(xfactor):
    print(xfactor)



print(newmessage)
