import os
from dotenv import load_dotenv

from agent import root_agent

import vertexai 
from vertexai import agent_engines

# Load environment variables
load_dotenv(override=True)

MODEL=os.getenv("GEMINI_MODEL")
PROJECT_ID=os.getenv("GOOGLE_CLOUD_PROJECT")
LOCATION=os.getenv("GOOGLE_CLOUD_LOCATION")
STAGING_BUCKET = os.getenv("STAGING_BUCKET")

vertexai.init(project=PROJECT_ID, location=LOCATION, staging_bucket=STAGING_BUCKET) 

app = agent_engines.AdkApp(agent=root_agent, enable_tracing=True) 

remote_agent = agent_engines.create(
    app,
    display_name="Alphabet Earnings MultiAgent",
    requirements=["google-cloud-aiplatform[adk, agent_engines]==1.126.1", "google-adk==1.18.0"],
    extra_packages = ["alphabet_earnings_agent/"],
    env_vars = {
                "GOOGLE_CLOUD_AGENT_ENGINE_ENABLE_TELEMETRY": "true",
                "OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT": "true",
                }
)
