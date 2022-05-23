import os
import logging
from typing import Callable

__EVENT_REGISTRY = {}


def event(name: str):
    def __decorator(func: Callable):
        global __EVENT_REGISTRY
        __EVENT_REGISTRY[name] = func
        return func

    return __decorator


def run_event():
    event = os.environ["GITHUB_EVENT_NAME"]
    if event not in __EVENT_REGISTRY:
        logging.error(f"{event} is not supported")
        return 1

    return __EVENT_REGISTRY(event)()
