from nltk import CFG

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