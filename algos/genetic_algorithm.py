import random

import numpy as np


class GeneticAlgorithm:

    def __init__(self, eval_fn, crossover_fn=None, mutation_fn=None, parents_ratio=0.5, mutation_ratio=1):
        self._eval_fn = eval_fn
        self._crossover_fn = crossover_fn
        self._mutation_fn = mutation_fn
        self._parents_ratio = parents_ratio
        self._mutation_ratio = mutation_ratio

    def _crossover(self, current_pop):
        if self._crossover_fn is None:
            return current_pop

        pop_size = len(current_pop)

        sorted_pop = sorted(current_pop, key=self._eval_fn, reverse=True)

        nb_parents = int(pop_size * self._parents_ratio)
        parent_candidates = sorted_pop[: nb_parents]

        parents_1 = [parent_candidates[idx] for idx in np.random.choice(nb_parents, nb_parents // 2, replace=True)]
        parents_2 = [parent_candidates[idx] for idx in np.random.choice(nb_parents, nb_parents // 2, replace=True)]

        childs = [self._crossover_fn(parent_1, parent_2) for parent_1, parent_2 in zip(parents_1, parents_2)]

        new_pop = parent_candidates + childs + current_pop[nb_parents: pop_size - len(childs)]

        return new_pop

    def _mutation(self, current_pop):
        if self._mutation_fn is None:
            return current_pop

        nb_mutations = int(len(current_pop) * self._mutation_ratio)

        mutations_idx = np.random.choice(range(len(current_pop)), nb_mutations, replace=True)

        for mutation_idx in mutations_idx:
            current_pop[mutation_idx] = self._mutation_fn(current_pop[mutation_idx])

        return current_pop

    def _step(self, current_pop):
        current_pop = self._crossover(current_pop)
        current_pop = self._mutation(current_pop)
        return current_pop

    def run(self, initial_pop, iterations=1000):
        current_pop = initial_pop
        for _ in range(iterations):
            current_pop = self._step(current_pop)

        return current_pop


if __name__ == "__main__":
    seed=1
    np.random.seed(seed)
    random.seed(seed)

    pop_size = 50
    bag_size = 10
    max_weight = 100
    nb_possible_items = 10
    items = []
    bags = []

    for i in range(nb_possible_items):
        weight = random.randint(1, 30)
        value = random.randint(0, 10)
        items.append({'weight': weight, 'value': value})

    for _ in range(pop_size):
        bag = []
        for _ in range(bag_size):
            item_id = random.randint(0, nb_possible_items - 1)
            bag.append(items[item_id])
        bags.append(bag)


    def evaluate(bag):
        current_value = 0
        current_weight = 0
        for item in bag:
            current_weight += item['weight']
            if current_weight > max_weight:
                return current_value
            current_value += item['value']
        return current_value


    def crossover(bag1, bag2):
        return bag1[:len(bag1) // 2] + bag2[:len(bag2) // 2]


    def mutation(bag):
        item_idx = random.randint(0, len(bag) - 1)
        if random.randint(0, 1) == 0:
            if len(bag) > 1:
                bag.pop(item_idx)
        else:
            added_item = items[random.randint(0, nb_possible_items - 1)]
            bag.insert(item_idx, added_item)
        return bag


    gen_algo = GeneticAlgorithm(eval_fn=evaluate, crossover_fn=crossover, mutation_fn=mutation)

    for iteration in range(100):
        scores = map(evaluate, bags)

        max_score = max(scores)

        print('iteration', str(iteration), max_score)

        bags = gen_algo._step(bags)
