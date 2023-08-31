s1 = "Hello"
print(s1)

str = """dfhdgsjhfznbh
fhggfdfsnmfsf
bhgghrbgfdnhkjfdh"""
print(str)

str = "Welcome \\to python \n and \t datascience"
print(str)

str = "python"
print("The lenght of the str=",len(str))
print(str[0])
print(str[1:3])
print(str*3)
s1="trfgyt"
s2="fdrs"
print(s1+s2)

#str = input("Enter any string:")
#sub = input("Enter any substring:")
#if sub in str:
 #   print(sub, "is found in main string")
#else:
 #   print(sub, "is not found in the main string")

s1="box"
s2="boy"
if(s1==s2):
    print("Both are same")
else:
    print("Both are not same")


str = "welcome to Python"
print(str.capitalize())
print(str.casefold())
print(str.center(100))
print(str.count("o"))
print(str.encode(encoding='ascii',errors='ignore'))
print(str.expandtabs(tabsize=6))
print(str.find("lo"))
print(str.format(str))
print('______________________________________________________________')
d={101:'sharvee', 102:'vinay',103:'poonam'}
print(str.format_map(d))



print(str.index('l'))
s1 = 'sdfsfjrhguytyrtnbbjh5464131dtfhjbhj'
print(s1.isalnum())
print(s1.isalpha())
print(s1.isascii())
print(s1.isdecimal())
print(s1.isdecimal())
print(s1.isdigit())
print(s1.isidentifier())
print(s1.islower())
print(s1.isupper())
print(s1.istitle())
print(s1.isnumeric())
print(s1.isprintable())
print(s1.istitle())
print(s1.isupper())
print(s1.islower())
s1='%'
s2 = 'data'
print(s1.join(s2))

s1='welcome'
print(s1.find('e'))
print(s1.rindex('e'))
print(s1.rfind('e'))
print(s1.swapcase())
print(s1.title())
print(s1.zfill(10))
print(s1.splitlines())