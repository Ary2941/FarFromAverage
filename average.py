
# cesar's cypher

message = str(input("write me some message!: "))
factor = int(input("write me the key: "))

lista = []
for item in message:
    lista += [(ord(item)+factor) % 127]

newmessage = ""
for item in lista:
    newmessage += chr(item)

print(newmessage)
