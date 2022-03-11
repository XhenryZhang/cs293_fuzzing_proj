/** Taken from "The Definitive ANTLR 4 Reference" by Terence Parr */

// Derived from http://json.org
grammar json;

json
   : value1
   | value2
   | value3
   | basic
   ;

basic
   : STRING
   | NUMBER
   | 'true'
   | 'false'
   | 'null'
   ;

obj
   : '{' pair (',' pair)* '}'
   | '{' '}'
   ;

pair
   : STRING ':' json
   ;

arr
   : '[' json (',' json)* ']'
   | '[' json (',' json)* ']'
   | '[' json (',' json)* ']'
   | '[' ']'
   ;

value1
   : obj
   | arr
   ;

value2
   : obj
   | arr
   ;

value3
   : obj
   | arr
   ;

STRING
   : '"' (ESC | SAFECODEPOINT)* '"'
   ;


fragment ESC
   : '\\' (["\\/bfnrt] | UNICODE)
   ;
fragment UNICODE
   : 'u' HEX HEX HEX HEX
   ;
fragment HEX
   : [0-9a-fA-F]
   ;
fragment SAFECODEPOINT
   : ~ ["\\\u0000-\u001F]
   ;

NUMBER
   : '-'? INT ('.' [0-9] +)? EXP?
   ;

fragment INT
   : '0' | [1-9] [0-9]*
   ;

// no leading zeros

fragment EXP
   : [Ee] [+\-]? INT
   ;

// \- since - means "range" inside [...]

WS
   : [ \t\n\r] + -> skip
   ;