from src.experiment import run_experiment
from src.visualizer import plot_scores

if __name__ == "__main__":
    k = 1
    results = run_experiment(k)

    plot_scores(
        results["axelrod_scores"],
        results["edward_scores"],
        results["strategy_names"],
        k,
        horizon_name=results["horizon_name"],
        horizon_desc=results["horizon_desc"],
    )

    print("Axelrod games:", results["axelrod_games"])
    print("Edward games:", results["edward_games"])