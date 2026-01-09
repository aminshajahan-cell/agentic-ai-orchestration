import os
from dotenv import load_dotenv
from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient

load_dotenv()

def _create_chat_client():
    return OpenAIChatClient(
        base_url=os.getenv("GITHUB_ENDPOINT"),
        api_key=os.getenv("OPENAI_API_KEY"),
        model_id=os.getenv("GITHUB_MODEL_ID"),
    )

def planner_agent():
    return ChatAgent(
        chat_client=_create_chat_client(),
        instructions=(
            "You are a Planner Agent. "
            "Break the user request into clear step-by-step actions."
        ),
    )

def executor_agent():
    return ChatAgent(
        chat_client=_create_chat_client(),
        instructions=(
            "You are an Executor Agent. "
            "Execute the plan and generate the required content."
        ),
    )

def reviewer_agent():
    return ChatAgent(
        chat_client=_create_chat_client(),
        instructions=(
            "You are a Reviewer Agent. "
            "Review the output, fix errors, and improve clarity."
        ),
    )
