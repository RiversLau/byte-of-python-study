name = 'RiversLau'

if name.startswith("Ri"):
    print('Yes, ths string start with "Ri"')

if 'a' in name:
    print("Yes, it contains string 'a'")

if name.find('ver') != -1:
    print("Yes, it contains string 'ver'")

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
