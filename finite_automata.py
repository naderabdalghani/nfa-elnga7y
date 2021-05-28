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


def do_operation(operands, operation):
    global LAST_USED_STATE_INDEX
    states = []
    if operation == '.':
        if isinstance(operands[0], Automaton) and isinstance(operands[1], Automaton):
            states = operands[0].states
            LAST_USED_STATE_INDEX += 1
            states[-1].input_dict = {'Epsilon': [operands[1].states[0].symbol]}
            states += operands[1].states
        elif isinstance(operands[0], Automaton):
            states = operands[0].states
            LAST_USED_STATE_INDEX += 1
            states[-1].input_dict = {'Epsilon': ['S' + str(LAST_USED_STATE_INDEX)]}
            states.append(State('S' + str(LAST_USED_STATE_INDEX),
                                {operands[1]: ['S' + str(LAST_USED_STATE_INDEX + 1)]}))
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX)))
        elif isinstance(operands[1], Automaton):
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX),
                                {operands[0]: ['S' + str(LAST_USED_STATE_INDEX + 1)]}))
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX),
                                {'Epsilon': [operands[1].states[0].symbol]}))
            states += operands[1].states
        else:
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX),
                                {operands[0]: ['S' + str(LAST_USED_STATE_INDEX + 1)]}))
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX),
                                {'Epsilon': ['S' + str(LAST_USED_STATE_INDEX + 1)]}))
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX),
                                {operands[1]: ['S' + str(LAST_USED_STATE_INDEX + 1)]}))
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX)))
        return Automaton(states)
