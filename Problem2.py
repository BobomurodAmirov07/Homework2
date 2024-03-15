class Computer:
    def __init__(self, name, RAM, price, processor):
        self.name = name
        self.RAM = RAM
        self.price = price
        self.processor = processor

    def info(self):
        print(f"Name {self.name}\nRAM {self.RAM}\nPrice {self.price}\nProcessor {self.processor}\n")


lst = list()

for i in range(4):
    C = Computer(input("Enter computer's name: "), int(input("Enter computer's RAM: ")), input("Enter computer's price: "), input("Enter computer's processor: "))
    print()
    lst.append([C.name, C.RAM, C.price, C.processor])

for i in lst:
    C = Computer(i[0], i[1], i[2], i[3])
    C.info()

print("-----------------------------------------")

for i in lst:
    if i[1] >= 4 and i[1] <= 16:
        print(i)