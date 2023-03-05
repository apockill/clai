import os
from types import ModuleType

import openai

API_TOKEN_VAR = "OPENAI_API_TOKEN"


def initialize_api() -> ModuleType:
    try:
        api_key = os.environ[API_TOKEN_VAR]
    except KeyError:
        print(f"You must set the`{API_TOKEN_VAR}` variable in your environment!")
        exit(1)

    openai.api_key = api_key
    return openai
