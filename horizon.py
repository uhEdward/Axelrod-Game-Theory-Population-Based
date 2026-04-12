class Horizon:
    name = "Unknown"
    description = "No description provided"

    def get_view(self, i, j, history):
        raise NotImplementedError


class AxelrodHorizon(Horizon):
    name = "Pairwise"
    description = "Agents only see history with the current opponent"

    def get_view(self, i, j, history):
        pair_history = history.get_pair(i, j)

        if i < j:
            pair_view = pair_history
        else:
            pair_view = [(b, a) for (a, b) in pair_history]

        return {
            "pair": pair_view,
            "opponent_history": []
        }


class EdwardHorizon(Horizon):
    name = "Global"
    description = "Agents see the opponent's interactions with everyone else"

    def get_view(self, i, j, history):
        opponent_history = []

        for (a, b), interactions in history.get_all().items():
            if j in (a, b) and i not in (a, b):
                for move_a, move_b in interactions:
                    if j == a:
                        opponent_history.append((move_a, move_b))
                    else:
                        opponent_history.append((move_b, move_a))

        return {
            "pair": [],
            "opponent_history": opponent_history
        }