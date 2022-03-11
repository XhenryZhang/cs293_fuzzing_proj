from fuzzingbook.ProbabilisticGrammarFuzzer import ProbabilisticGrammarFuzzer, ProbabilisticGrammarMiner, invert_probs, is_valid_probabilistic_grammar
from fuzzingbook.Grammars import convert_ebnf_grammar
from fuzzingbook.Parser import EarleyParser
from json_grammar import JSON_GRAMMAR_EBNF
from basic_generator import run_generator as basic_gen

# fuzzing
def run_generator(num_trials, grammar):
    bnf = convert_ebnf_grammar(grammar)
    #print(bnf)
    expansion_counter = ProbabilisticGrammarMiner(EarleyParser(bnf))
    half = num_trials // 2
    
    # run basic generator and invert probabilities
    fuzzed = basic_gen(half, grammar)
    prob_bnf = expansion_counter.mine_probabilistic_grammar(fuzzed)
    #print("finished mining")
    
    inv_prob_bnf = invert_probs(prob_bnf)
    #print(inv_prob_bnf)

    assert is_valid_probabilistic_grammar(inv_prob_bnf)
    
    # run generator on the least generated parts
    inv_generator = ProbabilisticGrammarFuzzer(inv_prob_bnf, min_nonterminals = 5,
                                               max_nonterminals = 100)
    
    for i in range(half):
        fuzzed.append(inv_generator.fuzz())
        
    print(fuzzed)
    return fuzzed
    
    
if __name__ == '__main__':
    run_generator(100, JSON_GRAMMAR_EBNF)
    