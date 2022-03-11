from basic_generator import run_generator as run_basic
from coverage_generator import run_generator as run_coverage
from probabilistic_generator import run_generator as run_probabilistic
from json_grammar import JSON_GRAMMAR_EBNF
import sys, os, datetime

JSON = 'json'

def fuzz_and_save(generator_func, num_trials, grammar_type, folder_prefix, folder_name):
    grammar = ""
    if grammar_type == JSON:
        grammar = JSON_GRAMMAR_EBNF
        
    fuzzing_results = generator_func(num_trials, grammar)
    
    # create output directory
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, '{}_{}_{}_corpus'.format(folder_prefix, folder_name, grammar_type))
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # remove existing files in directory, output fuzzing results to directory
    for file in os.scandir(output_dir):
        os.remove(file.path)
    
    for i in fuzzing_results:
        date_time = datetime.datetime.now()
        date_time_string = 'fuzzed_{}_{}'.format(grammar_type, date_time.strftime("%m%d%Y%H%M%S%f"))
        text_file = open(os.path.join(output_dir, date_time_string), "w")
        text_file.write(i)
        text_file.close()
    
    return None

if __name__ == '__main__':
    print(f"Arguments count: {len(sys.argv)}")
    if len(sys.argv) != 4:
        print("Usage: py run_all_generators.py <number of trials> <json|xml> <output folders prefix>")
        sys.exit(1)
    
    if sys.argv[2] != JSON:
        print('invalid grammar type, only supported type is json')
        sys.exit(1)
        
    fuzz_and_save(run_basic, int(sys.argv[1]), sys.argv[2], sys.argv[3], 'basic')
    fuzz_and_save(run_coverage, int(sys.argv[1]), sys.argv[2], sys.argv[3], 'coverage')
    fuzz_and_save(run_probabilistic, int(sys.argv[1]), sys.argv[2], sys.argv[3], 'prob')
        
    
    