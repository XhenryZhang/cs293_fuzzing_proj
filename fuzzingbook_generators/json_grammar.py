from fuzzingbook.Grammars import Grammar, srange, is_valid_grammar
import string

# bnf is a metasyntax for specifying context free grammars
JSON_GRAMMAR_EBNF: Grammar = {
    "<start>": ["<values>"],
    "<values>": ["<value1>", "<basic>"],
    "<basic>": ["<string>", "<number>", "true", "false", "null"],
    "<value1>": ["<obj>", "<arr>"],
    "<obj>": ["{ <pair>(, <pair>)* }", "{}"],
    "<pair>": ["<string>: <values>"],
    "<arr>": ["[]", "[<values>(, <values>)*]"],
    "<string>": ["\"(<character>)*\""],
    "<character>": srange(string.ascii_letters),
    "<number>": ["<sign>?<integer>(.<integer>)?"],
    "<sign>": ["-"],
    "<integer>": ["<digit>+"],
    "<digit>": srange(string.digits)
}

assert is_valid_grammar(JSON_GRAMMAR_EBNF)