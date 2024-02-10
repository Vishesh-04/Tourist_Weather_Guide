# Import necessary modules and classes
from uagents import Context
from messages.query_messages import QueryUserRequest, QueryTemperatureResponse, TemperatureStatus

# Import the colorama library for cross-platform colored output
from colorama import Fore, Style

# Import the 'agent' object from the 'temperature_query' module
from agents.temperature_query.temperature_query import agent as query_agent

# Import Tkinter for the chatbot
import tkinter as tk
from tkinter import scrolledtext

class TemperatureChatbot:
    def __init__(self, query_agent):
        self.query_agent = query_agent

        # Create the main Tkinter window
        self.root = tk.Tk()
        self.root.title("Temperature Query Chatbot")

        # Create a scrolled text widget for displaying the chat messages
        self.chat_display = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=50, height=20)
        self.chat_display.pack(padx=10, pady=10)

        # Create an entry widget for location input
        self.location_entry = tk.Entry(self.root, width=40)
        self.location_entry.pack(pady=10)
        self.location_entry.insert(0, "Default Location")

        # Create an entry widget for minimum temperature input
        self.min_temperature_entry = tk.Entry(self.root, width=40)
        self.min_temperature_entry.pack(pady=10)
        self.min_temperature_entry.insert(0, "0.0")

        # Create an entry widget for maximum temperature input
        self.max_temperature_entry = tk.Entry(self.root, width=40)
        self.max_temperature_entry.pack(pady=10)
        self.max_temperature_entry.insert(0, "100.0")

        # Create a button to send user input
        self.send_button = tk.Button(self.root, text="Send", command=self.send_user_input)
        self.send_button.pack()

        # Set up the interval handler for sending periodic temperature queries
        self.root.after(5000, self.send_periodic_query)  # Default period: 5000 milliseconds

    def send_user_input(self):
        # Get user input from the entry widgets
        location = self.location_entry.get().strip()
        min_temperature = float(self.min_temperature_entry.get())
        max_temperature = float(self.max_temperature_entry.get())

        # Display user input in the chat display
        self.display_message(f"User: Location={location}, Min Temperature={min_temperature}, Max Temperature={max_temperature}")

        # Use the 'send_message' method of the 'query_agent' to send the message
        query_agent.send_message(QueryUserRequest(location=location, min_temperature=min_temperature, max_temperature=max_temperature))

    def send_periodic_query(self):
        # Send a QueryUserRequest periodically with default values
        query_agent.send_message(QueryUserRequest(location="Default Location", min_temperature=0.0, max_temperature=100.0))

        # Schedule the next periodic query
        self.root.after(5000, self.send_periodic_query)  # Default period: 5000 milliseconds

    def display_message(self, message):
        # Display a message in the chat display
        self.chat_display.insert(tk.END, message + "\n")
        self.chat_display.see(tk.END)

# Define a message handler for handling QueryTemperatureResponse messages
@query_agent.on_message(QueryTemperatureResponse)
async def handle_query_response(ctx: Context, _, msg: QueryTemperatureResponse):
    # Display the response from the agent in the chatbot
    temperature = msg.temp
    if msg.status == TemperatureStatus.COLD:
        ctx.logger.warning(f"{Fore.BLUE}{msg.status.value} at {Fore.BLUE}{msg.time}!! Current Temperature is {Fore.BLUE}{temperature}°C{Style.RESET_ALL}.")
    elif msg.status == TemperatureStatus.HOT:
        ctx.logger.warning(f"{Fore.RED}{msg.status.value} at {Fore.RED}{msg.time}!! Current Temperature is {Fore.RED}{temperature}°C{Style.RESET_ALL}.")
    else:
        ctx.logger.info(f"{Fore.GREEN}{msg.status.value} at {Fore.GREEN}{msg.time}!! Current Temperature is {Fore.GREEN}{msg.temp}°C{Style.RESET_ALL}.")

    # Display the response in the chatbot
    chatbot.display_message(f"Agent: {msg.status.value} at {msg.time}!! Current Temperature is {temperature}°C")

# Entry point for the script
if __name__ == "__main__":
    # Create an instance of the TemperatureChatbot
    chatbot = TemperatureChatbot(query_agent)

    # Run the query agent and Tkinter chatbot
    query_agent.run()
    chatbot.root.mainloop()
