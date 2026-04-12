from history import GlobalHistory
from match import Match

class Simulation:
    def __init__(self, population, horizon, total_games):
        self.population = population
        self.horizon = horizon
        self.total_games = total_games
        self.history = GlobalHistory()
        self.game_count = 0

    def run(self):
        raise NotImplementedError

    def reset_scores(self):
        for agent in self.population.agents:
            agent.score = 0


class AxelrodSimulation(Simulation):
    def run(self):
        self.reset_scores()
        agents = self.population.agents

        for i in range(len(agents)):
            for j in range(i, len(agents)):
                for _ in range(200):
                    match = Match(agents[i], agents[j], self.history, self.horizon)
                    match.play()
                    self.game_count += 1

# random partitions
class EdwardSimulation(Simulation):
    def run(self):
        self.reset_scores()

        for _ in range(self.total_games):
            agent_i, agent_j = self.population.get_random_pair()
            match = Match(agent_i, agent_j, self.history, self.horizon)
            match.play()
            self.game_count += 1


"""
import random

# equal random samples
class EdwardSimulation(Simulation):
    def run(self):
        self.reset_scores()

        agents = self.population.agents
        n = len(agents)

        pairs = []
        for i in range(n):
            for j in range(i, n):
                pairs.append((i, j))

        num_pairs = len(pairs)
        base_games = self.total_games // num_pairs
        extra_games = self.total_games % num_pairs

        pair_targets = {pair: base_games for pair in pairs}

        extra_pairs = random.sample(pairs, extra_games)
        for pair in extra_pairs:
            pair_targets[pair] += 1

        match_list = []
        for (i, j), count in pair_targets.items():
            for _ in range(count):
                match_list.append((agents[i], agents[j]))

        random.shuffle(match_list)

        # strategy-pair counter
        strategy_pair_counts = {
            ("AlwaysCooperate", "AlwaysCooperate"): 0,
            ("AlwaysCooperate", "AlwaysDefect"): 0,
            ("AlwaysCooperate", "TitForTat"): 0,
            ("AlwaysDefect", "AlwaysDefect"): 0,
            ("AlwaysDefect", "TitForTat"): 0,
            ("TitForTat", "TitForTat"): 0,
        }

        for agent_i, agent_j in match_list:
            s1 = type(agent_i.strategy).__name__
            s2 = type(agent_j.strategy).__name__
            key = tuple(sorted([s1, s2]))
            strategy_pair_counts[key] += 1

            match = Match(agent_i, agent_j, self.history, self.horizon)
            match.play()
            self.game_count += 1

        print("\nStrategy pair counts:")
        for key, count in strategy_pair_counts.items():
            print(f"{key}: {count}")

# equal partitions
class EdwardSimulation(Simulation):          
    def run(self):
        agents = self.population.agents
        n = len(agents)

        num_pairs = n * (n + 1) // 2
        if self.total_games % num_pairs != 0:
            raise ValueError("total_games must be divisible by number of pairs")

        target = self.total_games // num_pairs

        pair_counts = {}
        for i in range(n):
            for j in range(i, n):
                pair_counts[(i, j)] = 0

        while True:
            if all(count == target for count in pair_counts.values()):
                break

            i = random.randint(0, n - 1)
            j = random.randint(i, n - 1)

            key = (i, j)

            if pair_counts[key] >= target:
                continue

            match = Match(agents[i], agents[j], self.history, self.horizon)
            match.play()

            pair_counts[key] += 1
            self.game_count += 1
"""