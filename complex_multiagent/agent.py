import os
from dotenv import load_dotenv
from google.adk.agents import LlmAgent, ParallelAgent, SequentialAgent
from google.adk.tools import google_search

from alphabet_earnings_agent.agent import root_agent as vertex_ai_search_agent

load_dotenv(override=True)
GEMINI_MODEL = os.getenv("GEMINI_MODEL")

# Google Search Agent
google_search_agent = LlmAgent(
    name="GoogleSearchAgent",
    model=GEMINI_MODEL,
    instruction="""You are a helpful assistant that uses the Google Search tool to answer questions.
          When a user asks a question, use the `Google Search` tool to find the answer.
          Output *only* the relevant information found by the tool.
          """,
    description="Searches for information using Google Search.",
    tools=[google_search],
    output_key="google_search_results",
)

# Parallel Search Agent
parallel_search_agent = ParallelAgent(
    name="ParallelSearchAgent",
    sub_agents=[vertex_ai_search_agent, google_search_agent],
    description="Performs parallel searches using Vertex AI Search and Google Search.",
)

# This new agent will receive the outputs from the ParallelAgent.
# The `output_key` values from the parallel branches are used as placeholders in this supervisor's instruction.
supervisor_agent = LlmAgent(
    name="SupervisorAgent",
    model=GEMINI_MODEL,
    instruction="""You are a supervisor agent. Your job is to compare and synthesize the results from two different search tools.

    Here are the results from Vertex AI Search:
    {vertex_ai_search_results}

    Here are the results from Google Search:
    {google_search_results}

    Analyze both sets of results and provide a comprehensive, single answer to the user's original query.
    If the results are different, point out the discrepancies.
    If they are similar, combine them into a more complete response.
    Always state that data from Vertex AI Search is more reliable since its enterprise-based data vs a google seearch.
    """,
    description="Compares search results and synthesizes a final answer.",
)


# The root_agent is now a Sequential Agent
# It first runs the parallel search, then passes its combined
# output to the supervisor agent for the final comparison.
root_agent = SequentialAgent(
    name="SupervisedSearchChain",
    sub_agents=[parallel_search_agent, supervisor_agent],
    description="A chain that performs parallel searches and then has a supervisor compare the results."
)
