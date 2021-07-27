import re

b = "МОУ Андийская СОШ №1"
a = "МКОУ АНДИЙСКАЯ СОШ №1 "



#a = filtr.sub("[^А-Яа-я0-9.№]|(РД)","", a)
#b = filtr.sub("[^А-Яа-я0-9.№]|(РД)","", a)

filtr = "[^А-Яа-я0-9]|(МКОУ)|(МОУ)|(МБОУ)"

a = re.sub(filtr, "", str(a))
b = re.sub(filtr, "", str(b))

if a.lower() in b.lower():
    print(True)
else: print(False)