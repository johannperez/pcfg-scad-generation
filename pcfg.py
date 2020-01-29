from nltk import PCFG, Nonterminal
from nltk.parse.generate import generate
from nltk.text import Text
import random
from copy import deepcopy

pgrammar = PCFG.fromstring("""
S -> Pendant [1]
Pendant -> Concatenated [.3] | Intersected [.1]  | Mirror [.4] | Hull [.2]
Figure -> 3DFigure [.3] | Concatenated [.2] | Intersected [.1] | Mirror [.2] | Hull [.2]
Mirror -> 'mirror' '[' Figure ']' [1]
Extrude -> 'extrude' '[' 2DFiguresArray ']' [1]
Hull -> 'hull' '[' Figure ']' [1]
Concatenated -> 'concat' '[' FiguresArray ']' [1]
Overlapped -> 'overlap' '[' 2DFiguresArray ']' [1]
Intersected -> 'intersect' '[' FiguresArray ']' [1]
FiguresArray -> Figure [0.4] | Figure FiguresArray [0.6]
3DFigure -> 3DPrimitive [.5] | Extrude [.5]
3DFiguresArray -> 3DFigure [.4] | 3DFigure 3DFiguresArray [.6]
2DFiguresArray -> 2DFigure [0.4] | 2DFigure 2DFiguresArray [0.6]
2DFigure -> Overlapped [.3] | 2DPrimitive [.7]
Primitive -> 3DPrimitive [0.5] | 2DPrimitive [0.5]
3DPrimitive ->  'cube' [.5]  | 'sphere' [.5]
2DPrimitive -> 'square' [0.3333] | 'circle' [0.3333] | 'polygon' [.3333]
""")

print(pgrammar)

# def RandomizedGrammar():
#     new_grammar = deepcopy(pgrammar)

#     pendant_productions = new_grammar.productions(lhs=Nonterminal("Pendant"))

#     remaining_probability = 1

#     for prod in pendant_productions:
#         r = random.random()
#         probability = remaining_probability * r
#         remaining_probability = remaining_probability - probability
        

#     return new_grammar

# RandomizedGrammar()


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