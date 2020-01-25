from cfg import grammar
from nltk.parse import ShiftReduceParser, RecursiveDescentParser
from nltk.tree import Tree, ParentedTree
import openpyscad as ops

def IsTerminal(tree):
    return type(tree) == str

def IsOverlapped(tree):
    return tree.label() == 'Overlapped'

def GenerateOverlappedTreeCadModel(tree:ParentedTree):
    element = ops.Union()
    for i in range(0, len(tree)):
        cadFigure = GenerateCadFile(tree[i])
        if cadFigure != None:
            element.append(cadFigure)
    return element

def IsConcatenated(tree:ParentedTree):
    return tree.label() == 'Concatenated'

def GenerateConcatenatedCadModel(tree:ParentedTree):
    element = ops.Union()
    offset = 0 #TODO find better way to do concatenation
    for i in range(0, len(tree)):
        cadFigure = GenerateCadFile(tree[i])
        if cadFigure != None:
            for f in cadFigure:
                element.append(f.translate([offset,0,0]))
                offset = offset + 10
    return element

def GenerateCircleModel():
    primitive = ops.Difference()
    primitive.append(ops.Circle(6))
    primitive.append(ops.Circle(5))
    return primitive

def GenerateSquareModel():
    primitive = ops.Difference()
    primitive.append(ops.Square(10))
    primitive.append(ops.Square(8).translate([1,1,0]))
    return primitive

def IsAnArray(tree:ParentedTree):
    return tree.label() == 'FiguresArray'

def GenerateArrayModel(tree:ParentedTree):
    array = []
    for i in range(0, len(tree)):
        cadFigure = GenerateCadFile(tree[i])
        if type(cadFigure) == list:
            for f in cadFigure:
                array.append(f)
        elif cadFigure != None:
            array.append(cadFigure)  
    return array 

def GenerateCadFile(tree: ParentedTree):
    if not IsTerminal(tree): 
        if IsOverlapped(tree):
            return GenerateOverlappedTreeCadModel(tree)
        elif IsConcatenated(tree):
            return GenerateConcatenatedCadModel(tree)
        elif IsAnArray(tree):
            return GenerateArrayModel(tree)                 
        else:
            return GenerateCadFile(tree[0])
    elif tree == 'circle':
        return GenerateCircleModel().translate([6,4,0])
    elif tree == 'square':
        return GenerateSquareModel()



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