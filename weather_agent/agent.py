
from google.adk.agents import LlmAgent

GEMINI_MODEL = "gemini-2.5-flash"

#Python tool
def get_weather(city: str) -> str:
    """Gets the weather for a given city.

    Args:
        city: The city to get the weather for.

    Returns:
        The weather forecast for the given city.
    """
    if "tokyo" in city.lower():
        return "The weather in Tokyo is 75 degrees and sunny."
    elif "london" in city.lower():
        return "The weather in London is 60 degrees and cloudy."
    else:
        return f"I don't have the weather for {city}."

# Agent Definition
root_agent = LlmAgent(
    name="weather_agent",
    model=GEMINI_MODEL,
    instruction="""You are a helpful assistant that uses the get_weather tool to answer questions about the weather.
          When a user asks for the weather, use the `get_weather` tool to find the answer.
          Output *only* the relevant information found by the tool.
          """,
    description="Gets the weather for a given city.",
    tools=[get_weather],
)
