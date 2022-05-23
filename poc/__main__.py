import os
import yaml
import json

from .event import event, run_event


@event("push")
def push_event():
    print("push event")

def main():
    run_event()
    return 0


exit(main())
