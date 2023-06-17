# def wealth_distribution(some_population, some_wealth):
#     is_equal_distribution_possible = True
#     some_population.sort()
#     for element in range(len(some_population)):
#         difference = 0
#         if some_population[element] < some_wealth:
#             difference = some_wealth - some_population[element]
#             if some_population[some_population.index(max(some_population))] >= difference + some_wealth:
#                 some_population[element] = some_wealth
#                 some_population[some_population.index(max(some_population))] -= difference
#             else:
#                 is_equal_distribution_possible = False
#     if is_equal_distribution_possible:
#         result = some_population
#     else:
#         result = "No equal distribution possible"
#     return result


def wealth_distribution (some_population, some_wealth):
    for element in range(len(some_population)):
        wealthiest = max(some_population)
        poorest = min(some_population)
        take_from = some_population.index(wealthiest)
        give_to = some_population.index(poorest)
        some_population[give_to] += some_wealth - poorest
        some_population[take_from] -= some_wealth - poorest

    if min(some_population) >= some_wealth:
        result = some_population
    else:
        result = "No equal distribution possible"
    return result

population_input = [int(number) for number in input().split(", ")]
minimum_wealth = int(input())
print(wealth_distribution(population_input, minimum_wealth))








