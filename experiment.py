from population import Population
from simulation import AxelrodSimulation, EdwardSimulation
from horizon import AxelrodHorizon, EdwardHorizon
from agent import Agent
from strategy import AlwaysCooperate, AlwaysDefect, TitForTat


def compute_scores(population):
    scores = {
        "AlwaysCooperate": 0,
        "AlwaysDefect": 0,
        "TitForTat": 0
    }

    for agent in population.agents:
        key = type(agent.strategy).__name__
        scores[key] += agent.score

    return [
        scores[k]
        for k in ["AlwaysCooperate", "AlwaysDefect", "TitForTat"]
    ]


def create_axelrod_population():
    agents = [
        Agent(0, AlwaysCooperate()),
        Agent(1, AlwaysDefect()),
        Agent(2, TitForTat())
    ]
    return Population(agents)


def create_edward_population(k):
    agents = [
        Agent(i, strat())
        for i, strat in enumerate(
            [AlwaysCooperate, AlwaysDefect, TitForTat] * k
        )
    ]
    return Population(agents)

def run_experiment(k):
    axelrod_population = create_axelrod_population()
    edward_population = create_edward_population(k)

    n_ax = axelrod_population.size()
    ax_total_games = (n_ax * (n_ax + 1) // 2) * 200

    ax_horizon = AxelrodHorizon()
    ed_horizon = EdwardHorizon()

    axelrod = AxelrodSimulation(
        axelrod_population,
        ax_horizon,
        ax_total_games
    )

    edward = EdwardSimulation(
        edward_population,
        ed_horizon,
        ax_total_games
    )

    axelrod.run()
    axelrod_scores = compute_scores(axelrod_population)

    edward.run()
    edward_scores = compute_scores(edward_population)

    return (
        axelrod_scores,
        edward_scores,
        axelrod.game_count,
        edward.game_count,
        ed_horizon.name,
        ed_horizon.description
    )