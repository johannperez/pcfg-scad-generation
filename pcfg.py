from nltk import PCFG
from nltk.parse.generate import generate
from nltk.text import Text
import random

pgrammar = PCFG.fromstring("""
S -> Pendant [1]
Pendant -> Figure [1]
Figure -> Primitive [.25] | Concatenated [.14] | Intersected [.05] | Overlapped [.14] | Mirror [.14] | Extrude [.14] | Hull [.14]
Mirror -> 'mirror' '[' Figure ']' [1]
Extrude -> 'extrude' '[' Figure ']' [1]
Hull -> 'hull' '[' Figure ']' [1]
Concatenated -> 'concat' '[' FiguresArray ']' [1]
Overlapped -> 'overlap' '[' FiguresArray ']' [1]
Intersected -> 'intersect' '[' FiguresArray ']' [1]
FiguresArray -> Figure [0.7] | Figure FiguresArray [0.3]
Primitive -> 'square' [0.3333]| 'triangle' | 'circle' [0.3333] | 'sphere' [0.3333]
""")

print(pgrammar)

def generate_sample(grammar, prod, frags):        
    if prod in grammar._lhs_index: # Derivation
        derivations = grammar._lhs_index[prod]            
        derivation = weighted_choice(derivations)            
        for d in derivation._rhs:            
            generate_sample(grammar, d, frags)
    elif prod in grammar._rhs_index:
        # terminal
        frags.append(str(prod))
    else:
        frags.append(prod)

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

def GenerateRandomSample(pgrammar):
    frags = []  
    generate_sample(pgrammar, pgrammar.start(), frags)
    return ' '.join(frags)

# print(GenerateRandomSample(pgrammar))
# print(GenerateRandomSample(pgrammar))
# print(GenerateRandomSample(pgrammar))