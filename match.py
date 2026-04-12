class Match:
    def __init__(self, agent_i, agent_j, history, horizon):
        self.agent_i = agent_i
        self.agent_j = agent_j
        self.history = history
        self.horizon = horizon

    def play(self):
        i = self.agent_i.agent_id
        j = self.agent_j.agent_id

        view_i = self.horizon.get_view(i, j, self.history)
        view_j = self.horizon.get_view(j, i, self.history)

        move_i = self.agent_i.act(view_i)
        move_j = self.agent_j.act(view_j)

        payoff_i, payoff_j = self.get_payoff(move_i, move_j)

        self.agent_i.add_score(payoff_i)
        self.agent_j.add_score(payoff_j)

        self.history.update(i, j, move_i, move_j)

    def get_payoff(self, move_i, move_j):
        if move_i == "C" and move_j == "C":
            return 3, 3
        elif move_i == "C" and move_j == "D":
            return 0, 5
        elif move_i == "D" and move_j == "C":
            return 5, 0
        else:
            return 1, 1