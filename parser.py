from cfg import grammar
from nltk.parse import ShiftReduceParser, RecursiveDescentParser
from nltk.tree import Tree, ParentedTree
import openpyscad as ops

def GenerateCadFile(tree: ParentedTree):
    if type(tree) != str: # not a terminal
        if tree.label() == 'Overlapped':
            element = ops.Union()
            for i in range(0, len(tree)):
                cadFigure = GenerateCadFile(tree[i])
                if cadFigure != None:
                    element.append(cadFigure)
            return element
        if tree.label() == 'Concatenated':
            element = ops.Union()
            offset = 0
            for i in range(0, len(tree)):
                cadFigure = GenerateCadFile(tree[i])
                if cadFigure != None:
                    for f in cadFigure:
                        element.append(f.translate([offset,0,0]))
                        offset = offset + 10
            return element
        elif tree.label() == 'FiguresArray':
            array = []
            for i in range(0, len(tree)):
                cadFigure = GenerateCadFile(tree[i])
                if type(cadFigure) == list:
                    for f in cadFigure:
                        array.append(f)
                elif cadFigure != None:
                    array.append(cadFigure)  
            return array                  
        else:
            return GenerateCadFile(tree[0])
    elif tree == 'circle':
        return ops.Circle(6).translate([6,4,0])
    elif tree == 'square':
        return ops.Square(10)



def Process(str, file):
    sr = RecursiveDescentParser(grammar)
    r = list(sr.parse(str.split()))
    cadResult = GenerateCadFile(ParentedTree.convert(r[0]))
    cadResult.write(file)

Process('circle', 'output1.scad')
Process('overlap [ circle square ]', 'output2.scad')
Process('concat [ circle square ]', 'output3.scad')
Process('concat [ circle circle circle circle ]', 'output4.scad')
Process('concat [ circle square circle square ]', 'output5.scad')