# src/experiment.py

from .population import Population
from .simulation import AxelrodSimulation, EdwardSimulation
from .horizon import AxelrodHorizon, EdwardHorizon
from .agent import Agent
from .strategy import Strategy


def compute_scores(population, strategy_classes):
    scores = {strategy_cls.name: 0 for strategy_cls in strategy_classes}

    for agent in population.agents:
        key = agent.strategy.name
        scores[key] += agent.score

    return [scores[strategy_cls.name] for strategy_cls in strategy_classes]


def create_axelrod_population(strategy_classes):
    agents = [
        Agent(i, strategy_cls())
        for i, strategy_cls in enumerate(strategy_classes)
    ]
    return Population(agents)


def create_edward_population(k, strategy_classes):
    agents = []
    agent_id = 0

    for strategy_cls in strategy_classes:
        for _ in range(k):
            agents.append(Agent(agent_id, strategy_cls()))
            agent_id += 1

    return Population(agents)


def run_experiment(k):
    strategy_classes = Strategy.all()

    axelrod_population = create_axelrod_population(strategy_classes)
    edward_population = create_edward_population(k, strategy_classes)

    n_ax = axelrod_population.size()
    ax_total_games = (n_ax * (n_ax + 1) // 2) * 200

    ax_horizon = AxelrodHorizon()
    ed_horizon = EdwardHorizon()

    axelrod = AxelrodSimulation(axelrod_population, ax_horizon, ax_total_games)
    edward = EdwardSimulation(edward_population, ed_horizon, ax_total_games)

    axelrod.run()
    edward.run()

    axelrod_scores = compute_scores(axelrod_population, strategy_classes)
    edward_scores = compute_scores(edward_population, strategy_classes)

    return {
        "axelrod_scores": axelrod_scores,
        "edward_scores": edward_scores,
        "strategy_names": [cls.name for cls in strategy_classes],
        "axelrod_games": axelrod.game_count,
        "edward_games": edward.game_count,
        "horizon_name": ed_horizon.name,
        "horizon_desc": ed_horizon.description,
    }