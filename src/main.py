# Import necessary modules and classes
from uagents import Context
from messages.query_messages import QueryUserRequest, QueryTemperatureResponse, TemperatureStatus

# Import the colorama library for cross-platform colored output
from colorama import Fore, Style

# Import the 'agent' object from the 'temperature_query' module
from agents.temperature_query.temperature_query import agent as query_agent

# Prompt the user for input for location, temperature thresholds, and period
query_location = input("Enter the location for temperature query: ")
query_min_temperature = float(input("Enter the minimum acceptable temperature: "))
query_max_temperature = float(input("Enter the maximum acceptable temperature: "))
# query_period = float(3600)


# Define an interval handler for sending periodic temperature queries
@query_agent.on_interval(period=3, messages=QueryUserRequest)
async def handle_interval(ctx: Context):
    # Send a QueryUserRequest to query the temperature in specified location with specified temperature thresholds
    await ctx.send(query_agent.address, QueryUserRequest(location=query_location, min_temperature=query_min_temperature,
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