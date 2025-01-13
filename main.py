import os
from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio

# Retrieve OpenAI API key
os.environ["OPENAI_API_KEY"] = ("OPENAI_API_KEY")

async def execute_task():
    """Executes the agent's task."""
    agent = Agent(
        #task="Go to https://www.youtube.com/@HarvestersTV, click on the first video and play it",
        task="Go to British Airways website, search for a return flight from London to New York, Depart 20/01/2025 return 30/01/2025 and return the cheapest flight.",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    try:
        result = await agent.run()
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Main function."""
    asyncio.run(execute_task())

if __name__ == "__main__":
    main()
