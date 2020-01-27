# from cfg import grammar
from pcfg import pgrammar, GenerateRandomSample
from nltk.parse import ShiftReduceParser, RecursiveDescentParser
from nltk.tree import Tree, ParentedTree
from copy import deepcopy
import openpyscad as ops
import random

def IsTerminal(tree):
    return type(tree) == str

def IsOverlapped(tree):
    return tree.label() == 'Overlapped'

def IsMirrored(tree):
    return tree.label() == 'Mirror'    

def IsHull(tree):
    return tree.label() == 'Hull'

def IsExtruded(tree):
    return tree.label() == 'Extrude'    

def IsIntersected(tree):
    return tree.label() == 'Intersected'    

def GenerateOverlappedTreeCadModel(tree:ParentedTree):
    element = ops.Union()
    for i in range(0, len(tree)):
        cadFigure = GenerateCadFile(tree[i])
        if cadFigure != None:
            element.append(cadFigure)
    return element

def GenerateIntersectedCadModel(tree:ParentedTree):
    element = ops.Intersection()
    for i in range(0, len(tree)):
        cadFigure = GenerateCadFile(tree[i])
        if cadFigure != None:
            element.append(cadFigure)
    return element

def GenerateMirroredCadModel(tree:ParentedTree):
    cadFigure = GenerateCadFile(tree[2])
    cadFigure2 = deepcopy(cadFigure)
    cadFigure = cadFigure.mirror([1,0,0])
    result = ops.Union()
    result.append(cadFigure)
    result.append(cadFigure2)
    return result

def GenerateExtrudedCadModel(tree:ParentedTree):
    cadFigure = GenerateCadFile(tree[2])
    return cadFigure.linear_extrude(height=10, twist=120)

def GenerateHullCadModel(tree:ParentedTree):
    cadFigure = GenerateCadFile(tree[2])
    return cadFigure.hull()

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

def GenerateSphere():
    return ops.Sphere(5).translate([(random.random()-0.5)*10, (random.random()-0.5)*10, (random.random()-0.5)*10])

def GenerateCircleModel():
    return ops.Cylinder(2)
    # primitive = ops.Difference()
    # primitive.append(ops.Circle(6))
    # primitive.append(ops.Circle(5))
    # return primitive

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
        elif IsMirrored(tree):
            return GenerateMirroredCadModel(tree)
        elif IsExtruded(tree):
            return GenerateExtrudedCadModel(tree)
        elif IsIntersected(tree):
            return GenerateIntersectedCadModel(tree)
        elif IsHull(tree):
            return GenerateHullCadModel(tree)
        else:
            return GenerateCadFile(tree[0])
    elif tree == 'circle':
        return GenerateCircleModel().translate([6,4,0])
    elif tree == 'square':
        return GenerateSquareModel()
    elif tree == 'sphere':
        return GenerateSphere()



def Process(str, file):
    sr = RecursiveDescentParser(pgrammar)
    r = list(sr.parse(str.split()))
    if len(r) > 0:
        cadResult = GenerateCadFile(ParentedTree.convert(r[0]))
        cadResult.write(file)
    else:
        print("************* " + str)

Process('extrude [ mirror [ concat [ circle square circle square ] ] ]', 'output5.scad')

for i in range(1,50):
    Process(GenerateRandomSample(pgrammar), './out/output' + str(i) + '.scad')