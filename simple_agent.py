import os

from agents import Agent, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel, Runner
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://openrouter.ai/api/v1"
)

model = OpenAIChatCompletionsModel(
    model="google/gemini-2.0-flash-exp:free",
    openai_client=provider
)

run_config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)

agent = Agent(
    instructions="You are a helpful AI assistant that provides clear and accurate responses to user queries.",
    name="Assistant"
)

result = Runner.run_sync(agent, "Hello, how are you?", run_config=run_config)

print(result.final_output)