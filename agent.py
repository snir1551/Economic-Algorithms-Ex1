from typing import Dict
from typing import List


class Agent:
    def __init__(self):
        self.options: Dict[int, float] = dict()
        self.num: float = -1
        self.replay_num = 0

    def set_option(self, option: int, value: float):
        self.options.update({option: value})
        if self.num < value:
            self.num = value
            self.replay_num = 1
        elif self.num == value:
            self.replay_num += 1

    def get_num(self):
        return self.num

    def value(self, option: int) -> float:
        if self.options.get(option) is None:
            return -1
        return self.options[option]


def isParetoImprovement(agents: List[Agent], option1: int, option2: int) -> bool:
    numAgents = 0
    for x in agents:
        if x.value(option1) < x.value(option2):
            print(x.value(option1))
            return False
        elif x.value(option1) == x.value(option2):
            numAgents += 1

    if numAgents == len(agents):
        return False
    else:
        return True


def isParetoOptimal(agents: List[Agent], option: int, allOptions: List[int]) -> bool:
    equal_in_another_option = 0
    for x in agents:
        if x.value(option) < x.get_num():
            return True
        if x.replay_num > 1:
            equal_in_another_option += 1

    if equal_in_another_option == len(agents):
        return True

    return False
