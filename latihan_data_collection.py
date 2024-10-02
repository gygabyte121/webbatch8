# list

# mylist = [1, 2.0, '3', True, 1]

# mylist.append(1000)

# data = mylist[4]

# print(mylist)


# mydict = {
#     'Nama':'Jhon',
#     'pekerjaan':'IT',
#     'Hobi':['makan','tidur','jalan-jalan']}

# data = mydict['Hobi'][2]

# print(data)


class Fruit:
    def __init__(self, name, color, taste):
        self.name = name
        self.color = color
        self.taste = taste
        
    def display_info(self):
        print(f"{self.name}: Color - {self.color}, Taste - {self.taste}")

apple = Fruit("Apel", "Merah", "manis")
orange = Fruit("Jeruk","kuning","Asem") 

apple.display_info
orange.display_info