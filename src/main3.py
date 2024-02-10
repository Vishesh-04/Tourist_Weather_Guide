from tkinter import *
from uagents import Context
from messages.query_messages import QueryUserRequest, QueryTemperatureResponse, TemperatureStatus

# Import the colorama library for cross-platform colored output
from colorama import Fore, Style

# Import the 'agent' object from the 'temperature_query' module
from agents.temperature_query.temperature_query import agent as query_agent
# GUI
root = Tk()
root.title("Chatbot")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# Send function
def send():
	send = "You -> " + e.get()
	txt.insert(END, "\n" + send)
	user = e.get().lower()
	e.get().clear()
	txt.insert(END, "\n" + "Bot -> Enter Your Native location for temperature query:")
	send = "You -> " + e.get()
	txt.insert(END, "\n" + send)
	query_location = e.get()
	print(query_location)
	txt.insert(END, "\n" + "Bot -> Enter Destination location for temperature query:")
	send = "You -> " + e.get()
	txt.insert(END, "\n" + send)
	query_location = e.get()
	print(query_location)



# query_location = input("Enter Your location for temperature query: ")
# query_location1 = input("Enter the Destination location for temperature query: ")


		# txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that")

	e.delete(0, END)


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
	row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

txt.insert(END, "\n" + "Bot -> Hi there, how can I help?")

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
			command=send).grid(row=2, column=1)


root.mainloop()
