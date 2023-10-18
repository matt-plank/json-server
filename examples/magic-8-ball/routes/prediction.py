import random

from simple_web.request import Request
from simple_web.response import Response
from simple_web.router import Router

CHOICES: list[str] = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
]

router = Router()


@router.get("/")
def prediction(request: Request) -> Response:
    """Magic 8-ball prediction."""
    choice: str = random.choice(CHOICES)

    return Response(
        status=200,
        headers={},
        json={"prediction": choice},
    )
