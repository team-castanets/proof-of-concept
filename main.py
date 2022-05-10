import os
import yaml
import json


TEST_README = """
## Click, clack. We are moving forward!

Review stage changed from **Dev** to **Stage**. [Workflow was triggered](https://www.google.com/search?q=%ED%9E%9D+%EC%86%8D%EC%95%98%EC%A7%80&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjG1d67gtX3AhUnl1YBHQ7TCqEQ_AUoAXoECAEQAw&cshid=1652188688866062&biw=1680&bih=898&dpr=2) for this stage.

```mermaid
flowchart LR
    Dev:::Done --> Stage{{Stage}}:::Running --> Prod:::Pending

classDef Done fill:#2da44e,stroke:#fff,color:white
classDef Running fill:#bf8700,stroke:#fff,color:white
classDef Pending fill:#888,stroke:#fff,color:white
```
### Stage Description

곧 Stage 단계 배포가 완료됩니다. 상단의 Workflow 링크를 참조해주세요.
배포가 완료되면 사내 망에서 https://staging.servicename.io 에 접근하셔서 테스트해주세요.

### Required Reviews
At least **2** approvals are needed to move this process forward.

Requested reviewers:

* @harrydrippin (MUST REVIEW)
* @FYLSunghwan
""".strip()


def main():
    event = os.environ["GITHUB_EVENT"]
    config_path = os.environ["INPUT_CONFIG_PATH"]
    workspace_path = os.environ["GITHUB_WORKSPACE"]
    job_summary_path = os.environ["GITHUB_STEP_SUMMARY"]

    with open(os.path.join(workspace_path, config_path)) as f:
        config = yaml.load(f)

    if event == "pull_request":
        with open(job_summary_path, "w") as f:
            f.write(TEST_README + '\n\n' + json.dumps(config))

    return 0


if __name__ == "__main__":
    exit(main())
