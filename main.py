"""Example of using agents with input guardrails to check for homework-related queries."""

import asyncio
from typing import Any, Dict

from dotenv import load_dotenv
from pydantic import BaseModel

from agents import Agent, InputGuardrail, GuardrailFunctionOutput, Runner

load_dotenv()


class HomeworkOutput(BaseModel):
    """Output model for homework detection results."""

    is_homework: bool
    reasoning: str


guardrail_agent = Agent(
    name="Guardrail check",
    instructions="Check if the user is asking about homework.",
    output_type=HomeworkOutput,
)

math_tutor_agent = Agent(
    name="Math Tutor",
    handoff_description="Specialist agent for math questions",
    instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
)

history_tutor_agent = Agent(
    name="History Tutor",
    handoff_description="Specialist agent for historical questions",
    instructions="You provide assistance with historical queries. Explain important events and context clearly.",
)


async def homework_guardrail(ctx: Dict[str, Any], _agent: Agent, input_data: str) -> GuardrailFunctionOutput:
    """Check if the input is related to homework.

    Args:
        ctx: Context object
        _agent: Agent object (unused)
        input_data: User input string

    Returns:
        GuardrailFunctionOutput with homework check result
    """
    result = await Runner.run(guardrail_agent, input_data, context=ctx.get("context", {}))
    final_output = result.final_output_as(HomeworkOutput)
    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=not final_output.is_homework,
    )

triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to use based on the user's homework question",
    handoffs=[history_tutor_agent, math_tutor_agent],
    input_guardrails=[
        InputGuardrail(guardrail_function=homework_guardrail),
    ],
)


async def main():
    """Run the agent system with example queries."""
    result = await Runner.run(triage_agent, "who was the first president of the united states?")
    print(result.final_output)

    result = await Runner.run(triage_agent, "what is life")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
