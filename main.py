import os
import asyncio
from random import randint
from dotenv import load_dotenv

from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient

# Load environment variables from .env
load_dotenv()

# -------------------------
# Tool definition
# -------------------------
def get_random_destination() -> str:
    """Get a random vacation destination."""
    destinations = [
        "Barcelona, Spain", "Paris, France", "Berlin, Germany",
        "Tokyo, Japan", "Sydney, Australia", "New York, USA",
        "Cairo, Egypt", "Cape Town, South Africa",
        "Rio de Janeiro, Brazil", "Bali, Indonesia"
    ]
    return destinations[randint(0, len(destinations) - 1)]

# -------------------------
# Main async runner
# -------------------------
async def main():
    # Initialize chat client for GitHub Models
    chat_client = OpenAIChatClient(
    base_url=os.environ.get("GITHUB_ENDPOINT"),
    api_key=os.environ.get("GITHUB_TOKEN"),
    model_id=os.environ.get("GITHUB_MODEL_ID"),
)


    # Create agent
    agent = ChatAgent(
        chat_client=chat_client,
        instructions=(
            "You are a helpful AI Agent that can help plan vacations "
            "for customers at random destinations."
        ),
        tools=[get_random_destination],
    )

    # Run agent
    response = await agent.run("Plan me a day trip")

    # Extract final message
    last_message = response.messages[-1]
    text_content = last_message.contents[0].text

    print("Travel plan:")
    print(text_content)


# Entry point
if __name__ == "__main__":
    asyncio.run(main())
