import agent


def first_example():
    AmiAgent = agent.Agent()
    AmiAgent.set_option(1, 1)
    AmiAgent.set_option(2, 2)
    AmiAgent.set_option(3, 3)
    AmiAgent.set_option(4, 4)
    AmiAgent.set_option(5, 5)

    TamiAgent = agent.Agent()
    TamiAgent.set_option(1, 3)
    TamiAgent.set_option(2, 1)
    TamiAgent.set_option(3, 2)
    TamiAgent.set_option(4, 5)
    TamiAgent.set_option(5, 4)

    RamiAgent = agent.Agent()
    RamiAgent.set_option(1, 3)
    RamiAgent.set_option(2, 5)
    RamiAgent.set_option(3, 5)
    RamiAgent.set_option(4, 1)
    RamiAgent.set_option(5, 1)


if __name__ == '__main__':
    AmiAgent = agent.Agent()
    AmiAgent.set_option(1, 1)
    AmiAgent.set_option(2, 2)
    AmiAgent.set_option(3, 3)
    AmiAgent.set_option(4, 4)
    AmiAgent.set_option(5, 5)

    TamiAgent = agent.Agent()
    TamiAgent.set_option(1, 3)
    TamiAgent.set_option(2, 1)
    TamiAgent.set_option(3, 2)
    TamiAgent.set_option(4, 5)
    TamiAgent.set_option(5, 4)

    RamiAgent = agent.Agent()
    RamiAgent.set_option(1, 3)
    RamiAgent.set_option(2, 5)
    RamiAgent.set_option(3, 5)
    RamiAgent.set_option(4, 1)
    RamiAgent.set_option(5, 1)

    list1 = [AmiAgent, TamiAgent, RamiAgent]
    list2 = [1, 2, 3, 4, 5]
    result = agent.isParetoImprovement(list1, 7, 1)
    print(result)


    result1 = agent.isParetoOptimal(list1, 5, list2)
    print(result1)

    AmiAgent = agent.Agent()
    AmiAgent.set_option(1, 2)
    AmiAgent.set_option(2, 0)
    AmiAgent.set_option(3, 0)
    AmiAgent.set_option(4, 2)

    TamiAgent = agent.Agent()
    TamiAgent.set_option(1, 1)
    TamiAgent.set_option(2, 1)
    TamiAgent.set_option(3, 1)
    TamiAgent.set_option(4, 1)

    print("--------------------------")
    list1 = [AmiAgent, TamiAgent, RamiAgent]
    list2 = [1, 2, 3, 4]
    result = agent.isParetoImprovement(list1, 3, 2)
    print(result)


    result1 = agent.isParetoOptimal(list1, 1, list2)
    print(result1)

    print("--------------------------")

    AmiAgent = agent.Agent()
    AmiAgent.set_option(1, 1)
    AmiAgent.set_option(2, 3)

    TamiAgent = agent.Agent()
    TamiAgent.set_option(1, 2)
    TamiAgent.set_option(2, 2)

    RamiAgent = agent.Agent()
    RamiAgent.set_option(1, 3)
    RamiAgent.set_option(2, 1)


    list1 = [AmiAgent, TamiAgent, RamiAgent]
    list2 = [1, 2]

    result1 = agent.isParetoOptimal(list1, 1, list2)
    print(result1)

    result1 = agent.isParetoOptimal(list1, 2, list2)
    print(result1)

    print("--------------------------")

    AmiAgent = agent.Agent()
    AmiAgent.set_option(1, 1)
    AmiAgent.set_option(2, 3)
    AmiAgent.set_option(3, 3)

    TamiAgent = agent.Agent()
    TamiAgent.set_option(1, 2)
    TamiAgent.set_option(2, 2)
    TamiAgent.set_option(3, 3)

    RamiAgent = agent.Agent()
    RamiAgent.set_option(1, 3)
    RamiAgent.set_option(2, 1)
    RamiAgent.set_option(3, 3)

    list1 = [AmiAgent, TamiAgent, RamiAgent]
    list2 = [1, 2, 3]

    result1 = agent.isParetoOptimal(list1, 3, list2)
    print(result1)
    result1 = agent.isParetoOptimal(list1, 2, list2)
    print(result1)
    result1 = agent.isParetoOptimal(list1, 1, list2)
    print(result1)


    print("--------------------------")

    AmiAgent = agent.Agent()
    AmiAgent.set_option(1, 1)
    AmiAgent.set_option(2, 2)
    AmiAgent.set_option(3, 3)
    AmiAgent.set_option(4, 4)
    AmiAgent.set_option(5, 5)

    TamiAgent = agent.Agent()
    TamiAgent.set_option(1, 3)
    TamiAgent.set_option(2, 1)
    TamiAgent.set_option(3, 2)
    TamiAgent.set_option(4, 5)
    TamiAgent.set_option(5, 4)

    RamiAgent = agent.Agent()
    RamiAgent.set_option(1, 3)
    RamiAgent.set_option(2, 5)
    RamiAgent.set_option(3, 5)
    RamiAgent.set_option(4, 1)
    RamiAgent.set_option(5, 1)


    list1 = [AmiAgent, TamiAgent, RamiAgent]
    list2 = [1, 2, 3, 4, 5]

    result1 = agent.isParetoOptimal(list1, 1, list2)
    print(result1)
    result1 = agent.isParetoOptimal(list1, 2, list2)
    print(result1)
    result1 = agent.isParetoOptimal(list1, 3, list2)
    print(result1)
    result1 = agent.isParetoOptimal(list1, 4, list2)
    print(result1)
    result1 = agent.isParetoOptimal(list1, 5, list2)
    print(result1)

