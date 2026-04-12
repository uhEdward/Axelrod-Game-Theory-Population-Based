import random

class Population:
    def __init__(self, agents):
        self.agents = agents
        self.pairs = []

        n = len(agents)
        for i in range(n):
            for j in range(i, n):
                self.pairs.append((agents[i], agents[j]))

    def size(self):
        return len(self.agents)

    def get_random_pair(self):
        return random.choice(self.pairs)