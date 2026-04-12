import matplotlib.pyplot as plt

def plot_scores(axelrod_scores, edward_scores, strategies, k, horizon_name, horizon_desc):
    x = range(len(strategies))

    bars1 = plt.bar(x, axelrod_scores, width=0.4, label="Axelrod")
    bars2 = plt.bar([i + 0.4 for i in x], edward_scores, width=0.4, label="Edward")

    plt.xticks([i + 0.2 for i in x], strategies)
    plt.legend()

    plt.title("Strategy Performance Comparison")

    plt.suptitle(
        f"Edward: {3*k} agents ({k} per strategy)\n"
        f"Horizon: {horizon_name}\n"
        f"{horizon_desc}",
        fontsize=10,
        y=0.98
    )
    
    for bar in bars1:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/2,
            height,
            f'{height:.0f}',
            ha='center',
            va='bottom'
        )

    for bar in bars2:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/2,
            height,
            f'{height:.0f}',
            ha='center',
            va='bottom'
        )

    plt.show()