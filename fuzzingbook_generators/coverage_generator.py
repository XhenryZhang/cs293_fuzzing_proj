from fuzzingbook.GrammarCoverageFuzzer import GrammarCoverageFuzzer
from fuzzingbook.Grammars import convert_ebnf_grammar
from json_grammar import JSON_GRAMMAR_EBNF

# fuzzing
def run_generator(num_trials, grammar):
    bnf = convert_ebnf_grammar(grammar)
    generator = GrammarCoverageFuzzer(bnf, min_nonterminals = 5,
                                           max_nonterminals = 100, start_symbol = "<start>")
    fuzzed = []
    
    for i in range(num_trials):
        fuzzed.append(generator.fuzz())
        
        # reset coverage after coverage becomes full
        if len(generator.max_expansion_coverage(symbol = "<start>")) == len(generator.expansion_coverage()):
            # print('resetting')
            generator.reset_coverage()
            
    print(fuzzed)
    return fuzzed

if __name__ == '__main__':
    run_generator(100, JSON_GRAMMAR_EBNF)