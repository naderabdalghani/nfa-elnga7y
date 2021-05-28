import json

LAST_USED_STATE_INDEX = -1


class State:
    def __init__(self, symbol, input_dict=None):
        self.symbol = symbol
        self.input_dict = input_dict


class Automaton:
    def __init__(self, states=None):
        self.states = states

    def print_to_file(self):
        if self.states is None:
            return
        output_dict = {
            "startingState": self.states[0].symbol
        }
        for state in self.states:
            output_dict[state.symbol] = {
                "isTerminatingState": state == self.states[-1]
            }
            if state.input_dict is not None:
                for input_key in state.input_dict:
                    output_dict[state.symbol][input_key] = state.input_dict[input_key]
        with open('nfa.json', 'w') as f:
            json.dump(output_dict, f, indent=4)


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
    if operation == '|':
        if isinstance(operands[0], Automaton) and isinstance(operands[1], Automaton):
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX),
                                {'Epsilon': [
                                    operands[0].states[0].symbol,
                                    operands[1].states[0].symbol
                                ]}))
            LAST_USED_STATE_INDEX += 1
            operands[0].states[-1].input_dict = {'Epsilon': ['S' + str(LAST_USED_STATE_INDEX)]}
            operands[1].states[-1].input_dict = {'Epsilon': ['S' + str(LAST_USED_STATE_INDEX)]}
            states += operands[0].states + operands[1].states
            states.append(State('S' + str(LAST_USED_STATE_INDEX)))
        elif isinstance(operands[0], Automaton):
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX),
                                {'Epsilon': [
                                    operands[0].states[0].symbol,
                                    'S' + str(LAST_USED_STATE_INDEX + 1)
                                ]}))
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX),
                                {operands[1]: ['S' + str(LAST_USED_STATE_INDEX + 1)]}))
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX),
                                {'Epsilon': ['S' + str(LAST_USED_STATE_INDEX + 1)]}))
            LAST_USED_STATE_INDEX += 1
            operands[0].states[-1].input_dict = {'Epsilon': ['S' + str(LAST_USED_STATE_INDEX)]}
            states += operands[0].states
            states.append(State('S' + str(LAST_USED_STATE_INDEX)))
        elif isinstance(operands[1], Automaton):
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX),
                                {'Epsilon': [
                                    'S' + str(LAST_USED_STATE_INDEX + 1),
                                    operands[1].states[0].symbol
                                ]}))
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX),
                                {operands[0]: ['S' + str(LAST_USED_STATE_INDEX + 1)]}))
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX),
                                {'Epsilon': ['S' + str(LAST_USED_STATE_INDEX + 1)]}))
            LAST_USED_STATE_INDEX += 1
            operands[1].states[-1].input_dict = {'Epsilon': ['S' + str(LAST_USED_STATE_INDEX)]}
            states += operands[1].states
            states.append(State('S' + str(LAST_USED_STATE_INDEX)))
        else:
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX),
                                {'Epsilon': [
                                    'S' + str(LAST_USED_STATE_INDEX + 1),
                                    'S' + str(LAST_USED_STATE_INDEX + 2)
                                ]}))
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX),
                                {operands[0]: ['S' + str(LAST_USED_STATE_INDEX + 2)]}))
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX),
                                {operands[1]: ['S' + str(LAST_USED_STATE_INDEX + 2)]}))
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX),
                                {'Epsilon': ['S' + str(LAST_USED_STATE_INDEX + 2)]}))
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX),
                                {'Epsilon': ['S' + str(LAST_USED_STATE_INDEX + 1)]}))
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX)))
        return Automaton(states)
    if operation == '*':
        if isinstance(operands[0], Automaton):
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX),
                                {'Epsilon': [
                                    operands[0].states[0].symbol,
                                    'S' + str(LAST_USED_STATE_INDEX + 1)
                                ]}))
            operands[0].states[-1].input_dict = {'Epsilon': [
                'S' + str(LAST_USED_STATE_INDEX),
                'S' + str(LAST_USED_STATE_INDEX + 1)
            ]}
            states += operands[0].states
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX)))
        else:
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX),
                                {'Epsilon': [
                                    'S' + str(LAST_USED_STATE_INDEX + 1),
                                    'S' + str(LAST_USED_STATE_INDEX + 3)
                                ]}))
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX),
                                {operands[0]: ['S' + str(LAST_USED_STATE_INDEX + 1)]}))
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX),
                                {'Epsilon': [
                                    'S' + str(LAST_USED_STATE_INDEX - 2),
                                    'S' + str(LAST_USED_STATE_INDEX + 1)
                                ]}))
            LAST_USED_STATE_INDEX += 1
            states.append(State('S' + str(LAST_USED_STATE_INDEX)))
        return Automaton(states)
