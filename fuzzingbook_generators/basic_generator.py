from fuzzingbook.GrammarFuzzer import GrammarFuzzer
from fuzzingbook.Grammars import convert_ebnf_grammar, Grammar
from json_grammar import JSON_GRAMMAR_EBNF

# build grammar
def run_generator(num_trials: int, grammar: Grammar):
    bnf = convert_ebnf_grammar(grammar)
    generator = GrammarFuzzer(bnf, min_nonterminals = 5,
                 max_nonterminals = 100)
    
    fuzzed = [generator.fuzz() for i in range(num_trials)]
    #print(fuzzed)
    return fuzzed

if __name__ == '__main__':
    run_generator(10, JSON_GRAMMAR_EBNF)