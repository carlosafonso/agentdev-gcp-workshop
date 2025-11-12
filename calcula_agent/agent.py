import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StreamableHTTPConnectionParams
import os

# Load environment variables
load_dotenv(override=True)

GEMINI_MODEL = os.getenv("GEMINI_MODEL")
MCP_SERVER_URL = os.getenv("MCP_SERVER_URL")

prompt = """
  You're an assistant that helps with calculations. You handle adding and substracting. In order to do this you use the tools available.
"""

root_agent = Agent(
    model=GEMINI_MODEL,
    name='calcula_agent',
    description='A helpful calculations assistant.',
    instruction=prompt,
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPConnectionParams(
                url=f"{MCP_SERVER_URL}/mcp",
                headers={}
                ),
                )
    ],
)
