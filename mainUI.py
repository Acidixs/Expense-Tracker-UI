import tkinter as tk
import json

class App:
    def __init__(self, master, num=1, total=0):
        self.master = master
        master.geometry("500x650")
        master.resizable(width=False, height=True)
        master.title("Expense tracker")
        
        self.all_entries = []
        self.dateEntry_list = []
        self.nameEntry_list = []
        self.priceEntry_list = []
        self.priceEntry_list = []

        self.num = num
        self.total = total
        self.frame = tk.Frame(root)
        self.frame.grid()
        self.create_widgets()
        self.new_item()


    def create_widgets(self):
        
        self.dateLabel = tk.Label(self.frame, text="date", font=("verdana", 15), padx=25)
        self.dateLabel.grid(column=0, row=0)

        self.itemLabel = tk.Label(self.frame, text="name", font=("verdana", 15), padx=25)
        self.itemLabel.grid(column=1, row=0)

        self.priceLabel = tk.Label(self.frame, text="price", font=("verdana", 15), padx=25)
        self.priceLabel.grid(column=2, row=0)

        self.newItemBtn = tk.Button(self.frame, text="new item", fg="green", font=("verdana", 10), pady=5, padx=5, command=self.new_item)
        self.newItemBtn.grid(column=1, row=999)

        self.totalLabel = tk.Label(self.frame, text=(f"total: {self.total}$"), font=("verdana", 14))
        self.totalLabel.grid(column=1, row=1000)

        self.saveBtn = tk.Button(self.frame, text="Save", font=("verdana", 10), fg="green", padx=4, pady=4, command=self.save_items)
        self.saveBtn.grid(column=1, row= 1001)

        self.loadBtn = tk.Button(self.frame, text="Load", font=("verdana", 10), fg="blue", padx=4, pady=4, command=self.load_items)
        self.loadBtn.grid(column=1, row=1002)

        self.resetBtn = tk.Button(self.frame, text="Reset", fg="red", font=("verdana", 10), command=self.reset_tracker)
        self.resetBtn.grid(column=1, row=1003)



    def new_item(self):


        self.dateEntry = tk.Entry(self.frame, font=("verdana", 10))
        self.dateEntry.grid(column=0, row=self.num, padx=1, pady=1)

        self.itemEntry = tk.Entry(self.frame, font=("verdana", 10))
        self.itemEntry.grid(column=1, row=self.num, padx=1, pady=1)

        self.priceEntry = tk.Entry(self.frame, font=("verdana", 10))
        self.priceEntry.grid(column=2, row=self.num, padx=1, pady=1)

        self.num += 1
        self.dateEntry_list.append(self.dateEntry)
        self.nameEntry_list.append(self.itemEntry)
        self.priceEntry_list.append(self.priceEntry)
        self.all_entries.extend((self.dateEntry, self.itemEntry, self.priceEntry))
        
        # update total expense
        self.update_total()

    def get_total(self):
        sumtotal = 0

        for e in self.priceEntry_list:
            if e.get():
                cash = e.get()
                cash = int(cash)
                sumtotal += cash
        return sumtotal

    def update_total(self):
        self.total = self.get_total()
        self.totalLabel.config(text=(f"total: {self.total}$"))

    def reset_tracker(self):
        for e in self.all_entries:
            e.destroy()
        self.all_entries.clear()
        self.priceEntry_list.clear()
        self.dateEntry_list.clear()
        self.nameEntry_list.clear()
        self.new_item()
    
    def save_items(self):

        l = []
        count = 1

        for (date, name, price) in zip(self.dateEntry_list, self.nameEntry_list, self.priceEntry_list):
            if date.get():
                date = str(date.get())
            if name.get():
                name = str(name.get())
            if price.get():
                price = str(price.get())

                itemDict = {"id": count, "date": date, "name": name, "price": price}

                l.append(itemDict)
                count += 1

                with open("items.txt", "w+") as f:
                    json.dump(l, f, indent=4)
    
    def load_items(self):
        self.reset_tracker()

        with open("items.txt", "r") as f:
            data = json.load(f)
            for v in data:
                date = v["date"]
                name = v["name"]
                price = v["price"]

                print(date, name, price)
            
                self.dateEntry = tk.Entry(self.frame, font=("verdana", 10))
                self.dateEntry.grid(column=0, row=self.num, padx=1, pady=1)
                self.dateEntry.insert(0, date)

                self.itemEntry = tk.Entry(self.frame, font=("verdana", 10))
                self.itemEntry.grid(column=1, row=self.num, padx=1, pady=1)
                self.itemEntry.insert(0, name)

                self.priceEntry = tk.Entry(self.frame, font=("verdana", 10))
                self.priceEntry.grid(column=2, row=self.num, padx=1, pady=1)
                self.priceEntry.insert(0, price)

                self.num += 1

                self.dateEntry_list.append(self.dateEntry)
                self.nameEntry_list.append(self.itemEntry)
                self.priceEntry_list.append(self.priceEntry)
                self.all_entries.extend((self.dateEntry, self.itemEntry, self.priceEntry))
                        


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

