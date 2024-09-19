#String="fundamentos con"
text1 ="fundamentos con"
text2 ="python"
result = text1 + text2
print(result)

name = "yenifer"
lastName = "perdomo"
fullName = name + " " +lastName
print(fullName)

# format string
price = 97
text3 = f"the price is {price:2f}dollars"
print(text3)

# math operacion
text4 = f" la multiplicacion es {20*59}"
print(text4)

# string capitalize()
text5 = "python es un lenguaje de alto nivel de programacion"
result1 = text5.capitalize()
print(result1)

# string casefold()
title = " cien años  de soledad"
titleConvert = title.casefold()
print(titleConvert)
#Strig center()
fruit = "banano"
textCenter = fruit.center(20,"-")
print(textCenter)


#string count ()
title1 = "i love apples, apple are my favorite fruit"
result2 =title1.count("apple")
print(result2)

#String endswith
text6 = "curso  fundamentos  con python"
result3 = text6.endswith(".")
print(result3)

#String expandtabs
letter = "F\tu\tp"
letterSpaces = letter.expandtabs(2)
print(letterSpaces)

#String find
text7 = "hola, bienvenidos a colombia."
result4 =text7.find("bienvenidos")
print(result4)

#funcion title
text8 = "welcome to my world"
result5 = text8.title()
print(result5)
#funcion isalnum
alphanumeric = "python312"
result6 = alphanumeric.isalnum()
print(result6)

#funcion isalpha
letters = "space x "
result7 = letters.isalpha()
print(result7)