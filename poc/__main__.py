import argparse
import os
import yaml
import json

from .event import event, run_event


# fmt: off
parser = argparse.ArgumentParser()
parser.add_argument("--config-path", type=str, required=True)
# fmt: on


@event("push")
def push_event():
    print("push event")

def main(args):
    run_event()
    return 0


args = parser.parse_args()
exit(main(args))
