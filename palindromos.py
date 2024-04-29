from automata.tm.dtm import DTM

las_transiciones={
    'q0': {
        'a': ('q1', '~', 'R'),
        'b': ('q4', '~', 'R'),
        '~': ('qacc', '~', 'R')
    },
    'q1': {
        'a': ('q1', 'a', 'R'),
        'b': ('q1', 'b', 'R'),
        '~': ('q2', '~', 'L')
    },
    'q2': {
        'a': ('q3', '~', 'L'),
    },
    'q3': {
        'a': ('q3', 'a', 'L'),
        'b': ('q3', 'b', 'L'),
        '~': ('q0', '~', 'R')
    },
    'q4': {
        'a': ('q4', 'a', 'R'),
        'b': ('q4', 'b', 'R'),
        '~': ('q5', '~', 'L')
    },
    'q5': {
        'b': ('q6', '~', 'L'),
    },
    'q6': {
        'a': ('q6', 'a', 'L'),
        'b': ('q6', 'b', 'L'),
        '~': ('q0', '~', 'R')
    }
}

palindromos = DTM(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'qacc'},
    input_symbols={'a', 'b'},
    tape_symbols={'a', 'b', '~'},
    transitions=las_transiciones,
    initial_state='q0',
    blank_symbol='~',
    final_states={'qacc'}
)

