import os

from dotenv import load_dotenv

load_dotenv()


def check_and_load(key: str) -> str:
    """
    해당 Key로 이루어진 환경 변수가 존재하는지 확인하고,
    만약 없다면 오류를 일으킵니다.
    :param key: 환경 변수 이름
    :returns: 환경 변수의 값
    """
    if key in os.environ:
        return os.environ[key]
    else:
        raise Exception(f"{key} is not set")


#: Github Actions
GITHUB_EVENT_NAME = check_and_load("GITHUB_EVENT_NAME")
