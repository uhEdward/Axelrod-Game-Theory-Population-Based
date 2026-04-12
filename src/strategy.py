class Strategy:
    def move(self, view):
        raise NotImplementedError
      
class AlwaysCooperate(Strategy):
    def move(self, view):
        return "C"
    
class AlwaysDefect(Strategy):
    def move(self, view):
        return "D"

class TitForTat(Strategy):
    def move(self, view):
        pair_history = view["pair"]
        opponent_history = view["opponent_history"]

        if pair_history:
            return pair_history[-1][1]

        if opponent_history:
            return opponent_history[-1][0]

        return "C"