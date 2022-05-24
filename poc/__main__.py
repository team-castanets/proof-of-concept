import argparse
import os
import yaml
import json

from .event import event, run_event
from .constants import GITHUB_EVENT_PATH


# fmt: off
parser = argparse.ArgumentParser()
parser.add_argument("--config-path", type=str, required=True)
# fmt: on


@event("push")
def push_event():
    print("push event")

def main(args):

    os.makedirs("artifacts", exist_ok=True)
    with open(GITHUB_EVENT_PATH, "r") as f:
        event_data = json.load(f)

    print(event_data)

    run_event()
    return 0


args = parser.parse_args()
exit(main(args))
