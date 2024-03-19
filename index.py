
# import tkinter as tk

# def increase_number():
#     current_number = int(label.cget("text"))
#     label.config(text=str(current_number + 1))

# def decrease_number():
#     current_number = int(label.cget("text"))
#     label.config(text=str(current_number - 1))

# window = tk.Tk()

# label = tk.Label(window, text="0", font=("Arial", 20))
# label.pack()

# plus_button = tk.Button(window, text="+", command=increase_number)
# plus_button.pack(side=tk.LEFT, padx=10)

# minus_button = tk.Button(window, text="-", command=decrease_number)
# minus_button.pack(side=tk.RIGHT, padx=10)

# window.mainloop()

# 



import tkinter as tk
import requests
import http.client
import json


##sending sms
conn = http.client.HTTPSConnection("CLIENT CONNECTION LINK")
def sendSMS(message):
     payload = json.dumps({
                "messages": [
                    {
                        "destinations": [{"to":"phone number"}],
                        "from": "ServiceSMS",
                        "text": message
                    }
                ]
                })
     conn.request("POST", "/sms/2/text/advanced", payload, headers)
     res = conn.getresponse()
     data = res.read()
     print(data.decode("utf-8"))
                       

headers = {
    'Authorization': 'App API KEY',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}



class ItemCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Item Counter App")

        self.beans_count = 5
        self.milk_count = 5
        self.rice_count = 5

        self.create_table()

    def create_table(self):
        # Create header labels
        tk.Label(self.root, text="Item").grid(row=0, column=0)
        tk.Label(self.root, text="Count").grid(row=0, column=1)
        tk.Label(self.root, text="Actions").grid(row=0, column=2, columnspan=2)

        # Create table rows
        self.create_row("Beans", 1, self.beans_count)
        self.create_row("Milk", 2, self.milk_count)
        self.create_row("Rice", 3, self.rice_count)

    def create_row(self, item_name, row_number, count):
        # Item label
        tk.Label(self.root, text=item_name).grid(row=row_number, column=0)

        # Count label
        count_label = tk.Label(self.root, text=count)
        count_label.grid(row=row_number, column=1)

        # Plus button
        plus_button = tk.Button(self.root, text="+", command=lambda: self.update_count(item_name, count_label, 1))
        plus_button.grid(row=row_number, column=2)

        # Minus button
        minus_button = tk.Button(self.root, text="-", command=lambda: self.update_count(item_name, count_label, -1))
        minus_button.grid(row=row_number, column=3)

    def update_count(self, item_name, count_label, change):
        # Update count based on the button pressed
        if item_name == "Beans":
            self.beans_count = max(0, self.beans_count + change)
            count_label.config(text=self.beans_count)
            if self.beans_count < 5:
                message = f"you are almost out of {item_name}. You have {self.beans_count} left"
                sendSMS(message)
                
                
                # print(f"you are almost out of {item_name}")
            elif self.beans_count > 5:
                 message = f"you have enough {item_name}"
                 sendSMS(message)
                
                # print(f"you have enough {item_name}")
                
        elif item_name == "Milk":
            self.milk_count = max(0, self.milk_count + change)
            count_label.config(text=self.milk_count)
            if self.milk_count < 5:
                message = f"you are almost out of {item_name}. You have {self.milk_count} left"
                sendSMS(message)
                
                
                # print(f"you are almost out of {item_name}")
            elif self.milk_count > 5:
                 message = f"you have enough {item_name}"
                 sendSMS(message)
                
        elif item_name == "Rice":
            self.rice_count = max(0, self.rice_count + change)
            count_label.config(text=self.rice_count)
            if  self.rice_count < 5:
                message = f"you are almost out of {item_name}. You have { self.rice_count} left"
                sendSMS(message)
                
                
                # print(f"you are almost out of {item_name}")
            elif  self.rice_count > 5:
                 message = f"you have enough {item_name}"
                 sendSMS(message)
                

# Create the main window
root = tk.Tk()
app = ItemCounterApp(root)

# Run the Tkinter event loop
root.mainloop()
