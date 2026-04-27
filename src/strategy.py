# src/strategy.py

class Strategy:
    registry = []

    name = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls is not Strategy:
            if cls.name is None:
                cls.name = cls.__name__
            Strategy.registry.append(cls)

    def move(self, view):
        raise NotImplementedError

    @classmethod
    def all(cls):
        return cls.registry.copy()

    @classmethod
    def names(cls):
        return [strategy_cls.name for strategy_cls in cls.registry]


class AlwaysCooperate(Strategy):
    name = "AlwaysCooperate"

    def move(self, view):
        return "C"


class AlwaysDefect(Strategy):
    name = "AlwaysDefect"

    def move(self, view):
        return "D"


class Alternating(Strategy):
    name = "Alternating"

    def __init__(self):
        self.move_count = 0

    def move(self, view):
        move = "C" if self.move_count % 2 == 0 else "D"
        self.move_count += 1
        return move


class TitForTat(Strategy):
    name = "TitForTat"

    def move(self, view):
        pair_history = view["pair"]
        opponent_history = view["opponent_history"]

        if pair_history:
            return pair_history[-1][1]
        if opponent_history:
            return opponent_history[-1][0]
        return "C"
