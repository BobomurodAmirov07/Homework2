class Book:
    def __init__(self, name, author, price, publishing):
        self.name = name
        self.author = author
        self.price = price
        self.publishing = publishing

    def grt_info(self):
        print(f"Book's name is {self.name}\nBook's author is {self.author}\nBook's price is {self.price}\nBook's publishing is {self.publishing}")


lst = list()

for i in range(2):
    B = Book(input("Enter book's name: "), input("Enter book's author: "), input("Enter book's price: "), input("Enter book's publishing: "))
    print()
    lst.append([B.name, B.author, B.price, B.publishing])

s = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

for i in lst:
    B = Book(i[0], i[1], i[2], i[3])
    B.grt_info()

print("-----------------------------------------")

for i in lst:
    for j in s:
        if str(i[-1]).startswith(j):
            print(" ".join(i))