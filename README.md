# SimpleScript Programming Language

SimpleScript is an interpreted, BACIC-like programming language built with Python. It is small, clean, and powerful. 
The language itself is straightforward and allows for cleaner-looking mathematical operations and data processing.

## Installation

Ensure Python 3 is installed on your system. SimpleScript does not use any external libraries.
This makes it entirely portable since it does not require the installation of any third-party libraries. **TL;DR: all you need is Python 3 installed on your system.** Nothing else is needed to write and execute SimpleScript programs.

## How To Use

You can use Python to launch the interactive shell. This will allow you to play with the SimpleSCript language in your terminal. You can use the shell to test expressions. 
In your BASH terminal, run the `shell.py` script using Python. 

```BASH
python shell.py  # Launches the interactive SimpleScript shell
```

## All Supported Operators

Here is a table including all supported mathematical operations in SimpleScript. Most are similar to Python or BASIC's implementations, but I've made some small changes which hopefully improve the look and feel of larger mathematical expressions.

| Operation | SimpleScript Command | Description | Notes |
|---|---|---|---|
| Addition | + | Performs addition |  |
| Subtraction | - | Performs subtraction |  |
| Multiplication | * | Performs multiplication |  |
| Division | / | Performs typical floating division | Cannot divide by 0 |
| Integer Division | &#124; | Performs division using integers | Cannot divide by 0 |
| Power | ^ | Raises expression to a power | Supports negative powers |
| Modulo | % | Returns remainder of division |  |

All these operations can be performed on both numeric values and sub-expressions, including variables. Variables are executed before any other numeric operation, so you can actually assign variables _while performing numeric operations_ on other values. 

## Examples Of Math Operations

Basic arithmetic operations can be performed directly on numbers, variables, and other values. Mathematical operations all return their associated value. Anytime a floating point operation is introduced, the data type returned will be a float. 

```php
$ (2 + 1) | (4 - 1)
$ 1
```

```php
$ 10 % 5
$ 0
```

```php
$ 1 + 2 - 3 * 4 / 5
$ 0.6000000000000001
```

```php
$ ((1 + 2) * 3 ^ 2) / 2
$ 13.5
```

```php
$ 10 | 2 + (8 ^ 2) - 6
$ 63
```

As you'd expect, division by zero is not allowed. If you try, the interpreter will inform you that the operation you're trying to execute is invalid. It will even highlight the error in your file. Negative powers are valid operations that will evaluate to the same result as would a similar BASIC operation.

```php
$ 12345 / 0

Traceback (most recent call last):
File <stdin>, line 1, in <program>
File <stdin>, on line 1
12345 / 0
        ^
```

```php
$ 98765 / (4 - 5 + 1)

Traceback (most recent call last):
File <stdin>, line 1, in <program>
File <stdin>, on line 1
98765 / (4 - 5 + 1)
         ^^^^^^^^^
```

Operations that eventually evaluate into zero are also not allowed, as seen in the above example. In this case, the entire sub-expression is highlighted by the interpreter. This hopefully provides enough tracing and error information to fix the issue in your program. The stack trace will always be displayed in error messages.e," there is a great deal that can be improved upon. I, for one, am less-than-satisfied with much of the variable and function mechanisms of SimpleScript.

## Language Grammars

The SimpleScript language is built around the grammar of BASIC. The grammar was used in the creation of the Lexer and the Parser. It served to inform the design and development of the creation of the abstract syntax trees and their tokens.

```text
statements  : NEWLINE* statement (NEWLINE+ statement)* NEWLINE*

statement		: KEYWORD:RETURN expr?
						: KEYWORD:CONTINUE
						: KEYWORD:BREAK
						: expr

expr        : KEYWORD:VAR IDENTIFIER EQ expr
            : comp-expr ((KEYWORD:AND|KEYWORD:OR) comp-expr)*

comp-expr   : NOT comp-expr
            : arith-expr ((EE|LT|GT|LTE|GTE) arith-expr)*

arith-expr  :	term ((PLUS|MINUS) term)*

term        : factor ((MUL|DIV) factor)*

factor      : (PLUS|MINUS) factor
            : power

power       : call (POW factor)*

call        : atom (LPAREN (expr (COMMA expr)*)? RPAREN)?

atom        : INT|FLOAT|STRING|IDENTIFIER
            : LPAREN expr RPAREN
            : list-expr
            : if-expr
            : for-expr
            : while-expr
            : func-def

list-expr   : LSQUARE (expr (COMMA expr)*)? RSQUARE

if-expr     : KEYWORD:IF expr KEYWORD:THEN
              (statement if-expr-b|if-expr-c?)
            | (NEWLINE statements KEYWORD:END|if-expr-b|if-expr-c)

if-expr-b   : KEYWORD:ELIF expr KEYWORD:THEN
              (statement if-expr-b|if-expr-c?)
            | (NEWLINE statements KEYWORD:END|if-expr-b|if-expr-c)

if-expr-c   : KEYWORD:ELSE
              statement
            | (NEWLINE statements KEYWORD:END)

for-expr    : KEYWORD:FOR IDENTIFIER EQ expr KEYWORD:TO expr 
              (KEYWORD:STEP expr)? KEYWORD:THEN
              statement
            | (NEWLINE statements KEYWORD:END)

while-expr  : KEYWORD:WHILE expr KEYWORD:THEN
              statement
            | (NEWLINE statements KEYWORD:END)

func-def    : KEYWORD:FUN IDENTIFIER?
              LPAREN (IDENTIFIER (COMMA IDENTIFIER)*)? RPAREN
              (ARROW expr)
            | (NEWLINE statements KEYWORD:END)
```

This grammar was lifted from [davidcallanan/py-myopl-code](https://github.com/davidcallanan/py-myopl-code/blob/master/ep14/grammar.txt) as they already had the most accurate and feature-rich BASIC grammar I could find online. This grammar is completely barebones; all BASIC implementations would be identical. This was lifted to save me the hastle of drafting the initial grammar myself, a task only POWs and grammar enthusiasts enjoy.

## Backend Architecture

The process of building and interpreting a programming language from scratch can be split into three main components. Each component produces their own deliverable that is used as an input for the following process.

- Lexing: Turns text strings into a list of tokens
- Parsing: Turns the list of tokens into an abstract syntax tree (AST)
- Interpreting: Evaluates every node of the AST to return a result

The three components are named accordingly in the `bin/` directory. They are: `lexer.py`, `parser.py`, and `interpreter.py`. These three components are the backbone of (most) programming languages.

## Related Readings

Here are some of the best physical and digital resources I could find on the subject of creating an interpreter for a programming language from scratch:

* [Language Implementation Patterns: Create Your Own Domain-Specific and General Programming Languages (Pragmatic Programmers)](https://www.amazon.ca/gp/product/193435645X/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=193435645X&linkCode=as2&tag=russblo0b-20&linkId=MP4DCXDV6DJMEJBL)
* [Writing Compilers and Interpreters: A Software Engineering Approach](https://www.amazon.ca/gp/product/0470177071/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0470177071&linkCode=as2&tag=russblo0b-20&linkId=UCLGQTPIYSWYKRRM)
* [Modern Compiler Implementation in Java](https://www.amazon.ca/gp/product/052182060X/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=052182060X&linkCode=as2&tag=russblo0b-20&linkId=ZSKKZMV7YWR22NMW)
* [Modern Compiler Design](https://www.amazon.com/gp/product/1461446988/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1461446988&linkCode=as2&tag=russblo0b-20&linkId=PAXWJP5WCPZ7RKRD)
* [Compilers: Principles, Techniques, and Tools (2nd Edition)](https://www.amazon.ca/gp/product/0321486811/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0321486811&linkCode=as2&tag=russblo0b-20&linkId=GOEGDQG4HIHU56FQ)
* [The "Let’s Build A Simple Interpreter" Blog Series](https://ruslanspivak.com/lsbasi-part1/)
* [The "Make YOUR OWN Programming Language" Video Series](https://www.youtube.com/playlist?list=PLZQftyCk7_SdoVexSmwy_tBgs7P0b97yD)
* [Introduction to Programming Languages/Interpreted Programs](https://en.wikibooks.org/wiki/Introduction_to_Programming_Languages/Interpreted_Programs)

Hopefully these help inform similar projects in the future. While SimpleScript is "complete," there is a great deal that can be improved upon. I, for one, am less-than-satisfied with much of the variable and function mechanisms of SimpleScript.

---

<p align="center"><img src="https://img.shields.io/badge/license-GNU-red.svg" /> <img src="https://img.shields.io/badge/maintainer-FlatlanderWoman-informational.svg" /> <img src="https://img.shields.io/badge/version-v1.0-yellow.svg" /></p>
