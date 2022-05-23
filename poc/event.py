import os
import logging
from typing import Callable

from .constants import GITHUB_EVENT_NAME

__EVENT_REGISTRY = {}


def event(name: str):
    def __decorator(func: Callable):
        global __EVENT_REGISTRY
        __EVENT_REGISTRY[name] = func
        return func

    return __decorator


def run_event():
    if GITHUB_EVENT_NAME not in __EVENT_REGISTRY:
        logging.error(f"{event} is not supported")
        return 1

    return __EVENT_REGISTRY[event]()
