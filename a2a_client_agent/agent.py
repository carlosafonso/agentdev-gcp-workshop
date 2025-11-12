import os
from dotenv import load_dotenv

from google.adk.agents import LlmAgent
from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent


load_dotenv(override=True)

alphabet_earnings_search_agent = RemoteA2aAgent(
    name="alphabet_earnings_search_agent",
    description="Answers questions about Alphabet Earnings.",
    agent_card=(
        f"http://127.0.0.1:8001{AGENT_CARD_WELL_KNOWN_PATH}"
    ),
)

root_agent = LlmAgent(
    model=os.getenv("GEMINI_MODEL"),
    name="root_agent",
    instruction="""
      You are a helpful assistant that can answer questions about Alphabet Earnings.
      You delegate answering the questions to the alphabet_earnings_search_agent.

      Follow these steps:
      1. If the user asks a question related to earnings at Alphabet, delegate it to the alphabet_earnings_search_agent.
      2. If the question is not related to earnings at Alphabet do not answer it, and politely tell the user that you cannot help them.

      Always answer in spanish.
    """,
    sub_agents=[alphabet_earnings_search_agent],
)
