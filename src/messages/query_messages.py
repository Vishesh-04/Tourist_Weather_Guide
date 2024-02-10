# Import necessary modules and classes
from enum import Enum
from uagents import Model

# Define an enumeration for temperature statuses
class TemperatureStatus(str, Enum):
    COLD = "Temperature Alert: It's Cold"
    HOT = "Temperature Alert: It's Hot"
    NORMAL = "Temperature is Normal"

# Define a data model class for querying user requests
class QueryUserRequest(Model):
    
    # Define attributes for the query user request
    location: str                   # Location for weather query
    max_temperature: float          # Maximum acceptable temperature
    min_temperature: float          # Minimum acceptable temperature

# Define a data model class for query temperature responses
class QueryTemperatureResponse(Model):
    
    # Define attributes for the query temperature response
    status: TemperatureStatus       # The temperature status based on the query
    time: str                       # The time when the temperature was queried
    temp: float                     # The temperature value returned in the response
