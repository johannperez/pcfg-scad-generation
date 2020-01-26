from nltk import CFG, PCFG
from nltk.parse.generate import generate
from nltk.text import Text
import random

# grammar = CFG.fromstring("""
# S -> Pendant
# Pendant -> Figures ']'
# Figures ->  Primitive | Primitive ',' Figures | 'concat' '[' Figures ']' | 'overlap' '[' Figures ']' 
# Primitive -> 'square' | 'triangle' | 'circle' | 'star'
# """)

grammar = CFG.fromstring("""
S -> Pendant
Pendant -> Figure
Figure ->  Primitive | Concatenated | Overlapped
Concatenated -> 'concat' '[' FiguresArray ']'
Overlapped -> 'overlap' '[' FiguresArray ']'
FiguresArray -> Figure | Figure FiguresArray 
Primitive -> 'square' | 'triangle' | 'circle' | 'star'
""")

print(grammar)


def generate_sample(grammar, prod, frags):        
    if prod in grammar._lhs_index: # Derivation
        derivations = grammar._lhs_index[prod]            
        derivation = weighted_choice(derivations)            
        for d in derivation._rhs:            
            generate_sample(grammar, d, frags)
    elif prod in grammar._rhs_index:
        # terminal
        frags.append(str(prod))

def weighted_choice(productions):
    prods_with_probs = [(prod, prod.prob()) for prod in productions]
    total = sum(prob for prod, prob in prods_with_probs)
    r = random.uniform(0, total)
    upto = 0
    for prod, prob in prods_with_probs:
        if upto + prob >= r:
            return prod
        upto += prob
    assert False, "Shouldn't get here"

pgrammar = PCFG.fromstring("""
S -> Pendant [1]
Pendant -> Figure [1]
Figure ->  Primitive [0.5] | Concatenated [0.25] | Overlapped [0.25]
Concatenated -> 'concat' '[' FiguresArray ']' [1]
Overlapped -> 'overlap' '[' FiguresArray ']' [1]
FiguresArray -> Figure [0.7] | Figure FiguresArray [0.3]
Primitive -> 'square' [0.5]| 'triangle' | 'circle' [0.5] | 'star' 
""")

print(pgrammar)

print("---------")
frags = []  
generate_sample(pgrammar, pgrammar.start(), frags)
print( ' '.join(frags) )
print("---------")
frags = []  
generate_sample(pgrammar, pgrammar.start(), frags)
print( ' '.join(frags) )
print("---------")
frags = []  
generate_sample(pgrammar, pgrammar.start(), frags)
print( ' '.join(frags) )
print("---------")
frags = []  
generate_sample(pgrammar, pgrammar.start(), frags)
print( ' '.join(frags) )
print("---------")
frags = []  
generate_sample(pgrammar, pgrammar.start(), frags)
print( ' '.join(frags) )
# for s in generate(pgrammar, n=50):
#     print(' '.join(s))
