# Import necessary modules and classes
from uagents import Agent, Context
from messages.query_messages import QueryUserRequest, QueryTemperatureResponse, TemperatureStatus
from uagents.setup import fund_agent_if_low
from utils import weather_api

# Create an instance of the Agent class with specific configuration
agent = Agent(name="temperature_query", port=8000, seed="temperature_query_seed", endpoint="http://127.0.0.1:8000/submit")

# Fund the agent's wallet if it has a low balance
fund_agent_if_low(agent.wallet.address())

# Define a message handler for incoming QueryUserRequest messages and specify the expected response message type
@agent.on_message(model=QueryUserRequest, replies={QueryTemperatureResponse})
async def handle_query_request(ctx: Context, sender: str, msg: QueryUserRequest):
    
    # Fetch weather data from an API based on the provided location
    api_status, api_time, api_temp = weather_api.fetch_data(msg.location)
    
    # Check if API is active or not
    if api_status is True:
        
        # Determine the temperature status based on the received data
        if api_temp <= msg.min_temperature:
            status = TemperatureStatus.COLD
            
        elif api_temp >= msg.max_temperature:
            status = TemperatureStatus.HOT
            
        else:
            status = TemperatureStatus.NORMAL           
            
    # Send a response message (QueryTemperatureResponse) back to the sender with the calculated temperature status, time, and temperature
    await ctx.send(sender, QueryTemperatureResponse(status=status, time=api_time, temp=api_temp))