report_books=["Rising up by Micheal Paul in 2020. With 20 Chapters",
"Up in the sun by Fred J in 2022. With 25 Chapters",
"Purple Flower by Chidimma Frances in 2019. With 50 Chapters",
"In the Rain by Loveth Paul in 2016, With 35 Chapters",
"Miracle in Nigeria by Chizaram in 2021. With 20 Chapters",
"Fight for Freedom by Peter Obi in 2023. With 20 Chapters"]

class Library():
    def __init__(self):
        print("Welcome to my Bookstore")
    def report(self,reports):
        self.reports=reports

        return reports


class BookPrice():
    def __init__(self, price):
        self.price = price
        self.many_books = int(input("How many books do you want"))
        self.total = (self.price * self.many_books)
        print(f"Total amount is {self.total}")
        self.rec_amount = int(input(f"Enter amount for {self.many_books} books"))

        self.change = 0

    def rec(self):
        self.change = self.rec_amount - self.total

        if self.total >= self.price:
            print("Recieved processing your other")
            print(f"Cost of book {self.price}. Amount recieved {self.rec_amount}.How many books {self.many_books}. Total {self.total}. Your remaining balance is {self.change}")

        else:
            print("Nope")

lib = Library()
start = True
while start:
    choice = input("What do you want to do? 'report', 'buy books' or 'borrow books'").lower()
    if choice == 'report':

        print(lib.report(report_books))
    elif choice == "buy books":
        which = int(input("Number of book you want from 0"))
        print(lib.report(report_books[which]))
        BookPrice(20).rec()
        print(f" {lib.report(report_books[which])} Nice choice. Enjoy!")
        again = input("Do you want to buy more? y/n").lower()
        if again != "y":
            start = False