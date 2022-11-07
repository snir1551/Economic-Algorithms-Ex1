from typing import Dict
from typing import List


class Agent:
    def __init__(self):
        self.options: Dict[int, float] = dict()

    def set_option(self, option: int, value: float):
        self.options.update({option: value})

    def value(self, option: int) -> float:
        if self.options.get(option) is None:
            return -1
        return self.options[option]


def isParetoImprovement(agents: List[Agent], option1: int, option2: int) -> bool:
    numAgents = 0
    for x in agents:
        if x.value(option1) < x.value(option2):
            return False
        elif x.value(option1) == x.value(option2):
            numAgents += 1

    if numAgents == len(agents):
        return False
    else:
        return True


def isParetoOptimal(agents: List[Agent], option: int, allOptions: List[int]) -> bool:
    for option_another_agent in allOptions:
        if option == option_another_agent:
            continue
        if isParetoImprovement(agents, option_another_agent, option):
            return False

    return True

