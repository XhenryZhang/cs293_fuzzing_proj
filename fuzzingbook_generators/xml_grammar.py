from fuzzingbook.Grammars import Grammar, srange, is_valid_grammar
import string

# bnf is a metasyntax for specifying context free grammars
XML_GRAMMAR_EBNF: Grammar = {
    "<start>": ["<xml-tree>"],
    "<xml-tree>": ["<text>",
                   "<xml-open-tag><xml-tree><xml-close-tag>",
                   "<xml-openclose-tag>",
                   "(<combine>)+"],
    "<combine>": ["<text>",
                   "<xml-open-tag><xml-tree><xml-close-tag>",
                   "<xml-openclose-tag>"],
    "<xml-open-tag>":      ["<<id>>", "<<id> <xml-attribute>>"],
    "<xml-openclose-tag>": ["<<id>/>", "<<id> <xml-attribute>/>"],
    "<xml-close-tag>":     ["</<id>>"],
    "<xml-attribute>":     ["(<id>=<id>)+"],
    "<id>":                ["(<letter>)+"],
    "<text>":              ["(<letter_space>)+"],
    "<letter>":            srange(string.ascii_letters + string.digits +
                                  "\"" + "'" + "."),
    "<letter_space>":      srange(string.ascii_letters + string.digits +
                                  "\"" + "'" + " " + "\t"),
}

assert is_valid_grammar(XML_GRAMMAR_EBNF)