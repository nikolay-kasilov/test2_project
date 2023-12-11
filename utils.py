import json
from typing import Union

PATH = 'tasks.json'


def write_tasks(tasks: dict[str, Union[str, int]], path=PATH):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)


def read_tasks(path=PATH) -> dict[str, Union[str, int]]:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def filter_task(tasks: list[dict[str, Union[str, int]]], priority: int) -> list[dict[str, Union[str, int]]]:
    return [
        task
        for task in tasks
        if task.get('priority') == priority
    ]
