# UAgents-weather

## Project Description

The TemperatureX Web Application is a Flask-based Temperature Alert Agent built using Fetch.AI's uAgent library that provides a simple interface for users to input their desired location and temperature range and then displays real-time temperature status updates on the webpage, i.e., sends alert/notification to the user when the current temperature in their chosen location goes below the minimum or above the maximum threshold they've set. 

## How to Run the Project

### Step 1: Prerequisites
Before starting, you'll need the following:

> Python (3.8+ is recommended)

> Poetry (a packaging and dependency management tool for Python)

### Step 2: Clone or download this repository to your local machine:

```bash
   git clone https://github.com/Vishesh-04/Tourist_Weather_Guide.git
   ```

### Step 3: Set up .env file
To run the demo, you need API key from:

[WeatherAPI](https://www.weatherapi.com/) &rarr;

> Visit WeatherAPI.

> Sign up or log in.

> Go to Dashboards in the left hand column and click on Generate API

> Once generated, copy the API key

Once you have the weather key, create a .env file in the hackAI_temp_agent/src directory.

```bash
   export WEATHER_API_KEY="{GIVE THE API KEY}"
   ```

### Step 4: To use the environment variables from .env and install the project:
Open New Terminal,

```bash
   cd src
   .env
   poetry install
   ```

### Step 5: Navigate to shell
```bash
   poetry shell
   ```

### Step 6: Run the main script
To run the project and its agents:

```bash
   python main.py
   ```
### You need to look for the following output in the logs:

Enter the location for temperature query: {Enter the location whose temperature updates you want to receive}

Enter the minimum acceptable temperature: {Enter the minimum threshold temperature}

Enter the maximum acceptable temperature: {Enter the maximum threshold temperature}

### Once you hit enter, a request will be sent to the query agent every half an hour and you will be able to see your results in the console!

For example, 

Enter the location for temperature query: Goa

Enter the minimum acceptable temperature: 30

Enter the maximum acceptable temperature: 50

### The result you should be able to see is,

<span style="color: yellow;">WARNING:</span> [temperature_query]: Temperature Alert: It's Cold at 2023-10-10 20:28!! Current Temperature is 27.0°C

## Special Considerations 

The application uses the uagents library for agent-based communication. Ensure that you have this library properly installed and configured in your project.
