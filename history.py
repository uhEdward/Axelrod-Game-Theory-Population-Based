class GlobalHistory:
    def __init__(self):
        # key = pair of agents, value = array of their history
        self.history = {}

    def update(self, i, j, move_i, move_j):
        key = (min(i, j), max(i, j))

        if key not in self.history:
            self.history[key] = []

        if i < j:
            self.history[key].append((move_i, move_j))
        else:
            self.history[key].append((move_j, move_i))

    def get_pair(self, i, j):
        key = (min(i, j), max(i, j))
        return self.history.get(key, [])

    def get_last_k(self, i, j, k):
        pair_history = self.get_pair(i, j)
        return pair_history[-k:]

    def get_all(self):
        return self.history