class Agent:
    def __init__(self, agent_id, strategy):
        self.agent_id = agent_id
        self.strategy = strategy
        self.score = 0

    def act(self, view):
        return self.strategy.move(view)

    def add_score(self, points):
        self.score += points