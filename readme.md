# Tresdé - Context Free Grammar

## Table of contents

## Project description

TODO

### Desicions


#### Grammar 


#### Parser

ShiftReduceParser vs RecursiveDescentParser ?

ShiftReduceParser is not being able to parse current grammar, if we activate tracing then it'll fail with:

```
Traceback (most recent call last):
  File "/Users/johann/Projects/DataScience/GSL Pro/code/parser.py", line 11, in <module>
    for t in r:
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/nltk/parse/shiftreduce.py", line 98, in parse
    while self._reduce(stack, remaining_text):
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/nltk/parse/shiftreduce.py", line 197, in _reduce
    self._trace_reduce(stack, production, remaining_text)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/nltk/parse/shiftreduce.py", line 258, in _trace_reduce
    rhs = " ".join(production.rhs())
TypeError: sequence item 0: expected str instance, Nonterminal found
```

** IMPORTANT ** https://stackoverflow.com/questions/39187042/nltk-cfg-recursion-depth-error


#### 3d generation

## References

 - https://pypi.org/project/OpenPySCAD/
 - http://www.nltk.org/howto/grammar.html
 - http://www.nltk.org/howto/parse.html
 - http://ce.sharif.edu/courses/94-95/1/ce414-2/resources/root/Text%20Books/Automata/John%20E.%20Hopcroft,%20Rajeev%20Motwani,%20Jeffrey%20D.%20Ullman-Introduction%20to%20Automata%20Theory,%20Languages,%20and%20Computations-Prentice%20Hall%20(2006).pdf
  - http://ce.sharif.edu/courses/94-95/1/ce414-2/resources/root/Text%20Books/Compiler%20Design/Alfred%20V.%20Aho,%20Monica%20S.%20Lam,%20Ravi%20Sethi,%20Jeffrey%20D.%20Ullman-Compilers%20-%20Principles,%20Techniques,%20and%20Tools-Pearson_Addison%20Wesley%20(2006).pdf

