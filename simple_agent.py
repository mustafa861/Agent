import os
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner
from agents.run import RunConfig
from dotenv import load_dotenv, find_dotenv
from agents.tool import function_tool
import asyncio

load_dotenv(find_dotenv())

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider
)

run_config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True
)









async def main():
    agent = Agent(
    instructions="You are a helpful AI assistant that provides clear and accurate responses to user queries.",
    name="Assistant",
)


    result = await Runner.run(agent, "sum of 2+3", run_config=run_config)
    print(result.final_output)



if __name__ == "__main__":
    asyncio.run(main())
