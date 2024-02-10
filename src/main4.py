from tkinter import *
import threading
import time
from uagents import Context
from messages.query_messages import QueryUserRequest, QueryTemperatureResponse, TemperatureStatus
from colorama import Fore, Style
from agents.temperature_query.temperature_query import agent as query_agent

# Global variable to store the input
global_input = None

# Function to handle user input and update global variable
def handle_input():
    global global_input
    while True:
        time.sleep(0.1)  # Small delay to prevent busy-waiting
        user_input = e.get().strip()
        if user_input:
            global_input = user_input
            e.delete(0, END)

# Function to simulate sending the updated input
def send_input():
    global global_input
    while True:
        time.sleep(0.1)  # Small delay to prevent busy-waiting
        if global_input:
            txt.insert(END, f"\nYou: {global_input}")
            bot_response = generate_response(global_input)
            txt.insert(END, f"\nBot: {bot_response}")
            global_input = None

# Function to run the chatbot logic
def generate_response(user_input):
    query_location = user_input
    query_min_temperature = float(input("Enter the minimum acceptable temperature: "))
    query_max_temperature = float(input("Enter the maximum acceptable temperature: "))
    query_period = float(3600)

    # Define an interval handler for sending periodic temperature queries
    @query_agent.on_interval(period=query_period, messages=QueryUserRequest)
    async def handle_interval(ctx: Context):
        # Send a QueryUserRequest to query the temperature in specified location with specified temperature thresholds
        await ctx.send(query_agent.address,
                       QueryUserRequest(location=query_location, min_temperature=query_min_temperature,
                                        max_temperature=query_max_temperature))

    # Define a message handler for handling QueryTemperatureResponse messages
    @query_agent.on_message(QueryTemperatureResponse)
    async def handle_query_response(ctx: Context, _, msg: QueryTemperatureResponse):
        # Assuming that msg.temp contains the temperature value
        temperature = msg.temp

        # Check the temperature status and log appropriate messages
        if msg.status == TemperatureStatus.COLD:
            ctx.logger.warning(
                f"{Fore.BLUE}{msg.status.value} at {Fore.BLUE}{msg.time}!! Current Temperature is {Fore.BLUE}{temperature}°C{Style.RESET_ALL}.")

        elif msg.status == TemperatureStatus.HOT:
            ctx.logger.warning(
                f"{Fore.RED}{msg.status.value} at {Fore.RED}{msg.time}!! Current Temperature is {Fore.RED}{temperature}°C{Style.RESET_ALL}.")

        else:
            ctx.logger.info(
                f"{Fore.GREEN}{msg.status.value} at {Fore.GREEN}{msg.time}!! Current Temperature is {Fore.GREEN}{msg.temp}°C{Style.RESET_ALL}.")

    # Entry point for the script
    if __name__ == "__main__":
        # Run the query agent
        query_agent.run()

# Create a Tkinter window
root = Tk()
root.title("Chatbot")

# Create a text area to display output
txt = Text(root, wrap=WORD, width=60, height=10)
txt.grid(row=0, column=0, padx=10, pady=10)

# Create an entry field for user input
e = Entry(root, width=60)
e.grid(row=1, column=0, padx=10, pady=5)

# Start two separate threads for handling input and sending input
input_thread = threading.Thread(target=handle_input)
send_thread = threading.Thread(target=send_input)
input_thread.start()
send_thread.start()

# Start the Tkinter event loop
root.mainloop()
