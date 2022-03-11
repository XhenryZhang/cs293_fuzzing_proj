To Install Grammarinator:

pip install grammarinator
grammarinator-generate -p json_generator/JSONUnparser.py -l json_generator/JSONUnlexer.py -r json -d 100 -n 100

This generates 100 json strings based on json.g4. Visit https://github.com/renatahodovan/grammarinator for official documentation.
ANTLRv4 grammars for Grammarinator in this project were taken off https://github.com/antlr/grammars-v4.

To run the generators based on Fuzzingbook implementations, use the command:
py fuzzingbook_generators/run_all_generators.py <number of runs> [json|xml] <output folder prefix>

This command outputs 3 folders:
 - <prefix>_basic_[json|xml]_corpus
 - <prefix>_coverage_[json|xml]_corpus
 - <prefix>_prob_[json|xml]_corpus

Folders correspond to the type of Grammar fuzzer used to generate the outputs. See the report for more details on the reasoning behind
each type of generator.