#with open("abecedario.txt", "r") as fileabc:
#   print(fileabc.read())

#with open("abecedario.txt", "w") as fileabc:
#    fileabc.write("abcdef")

#with open("abecedario.txt", "r") as fileabc:
#    print(fileabc.read())

with open("abecedario.txt", "a") as fileabc:
    print(fileabc.write("\nklmnño"))
    
with open("abecedario.txt", "r") as fileabc:
    for linea in fileabc:
        print(linea)
