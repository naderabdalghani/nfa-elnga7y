LAST_USED_STATE_INDEX = -1


class State:
    def __init__(self, symbol, input_dict=None):
        self.symbol = symbol
        self.input_dict = input_dict


class Automaton:
    def __init__(self, states=None):
        self.states = states

    def print_to_file(self):
        pass

