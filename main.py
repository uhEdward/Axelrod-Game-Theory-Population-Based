from src.experiment import run_experiment
from src.visualizer import plot_scores

if __name__ == "__main__":
    k =10
    ax_scores, ed_scores, ax_games, ed_games, horizon_name, horizon_desc = run_experiment(k)

    strategies = ["AlwaysCooperate", "AlwaysDefect", "TitForTat"]
    plot_scores(ax_scores, ed_scores, strategies, k, horizon_name=horizon_name, horizon_desc=horizon_desc)

    print("Axelrod games:", ax_games)
    print("Edward games:", ed_games)