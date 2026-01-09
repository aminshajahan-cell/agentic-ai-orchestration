import asyncio
from dotenv import load_dotenv
import agents

load_dotenv()

async def run_orchestration(user_request: str):
    planner = agents.planner_agent()
    executor = agents.executor_agent()
    reviewer = agents.reviewer_agent()

    print("\n Planner Agent working...\n")
    plan_response = await planner.run(user_request)
    plan = plan_response.messages[-1].contents[0].text
    print("PLAN:\n", plan)

    print("\n Executor Agent working...\n")
    exec_response = await executor.run(
        f"Use this plan to generate the output:\n{plan}"
    )
    draft = exec_response.messages[-1].contents[0].text
    print("DRAFT OUTPUT:\n", draft)

    print("\n Reviewer Agent working...\n")
    review_response = await reviewer.run(
        f"Review and improve the following content:\n{draft}"
    )
    final_output = review_response.messages[-1].contents[0].text
    print("\n FINAL OUTPUT:\n")
    print(final_output)


if __name__ == "__main__":
    user_request = input("\n Enter your request: ")
    asyncio.run(run_orchestration(user_request))

