from pronto import *
from math import log

# Importing ontology
tron = Ontology('tribolium.obo')

# Generating ic_dict, will be replaced
ic_dict = dict()
#ic_list = dict()
root = 'TrOn:0000001'  # Ontology root term
ic_dict[root] = 1.0

def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result

def getMuFromNode(node):
    if node in ic_dict:
        return (ic_dict[node], len(tron[node].children))
    parentIC_list = []
    for p in tron[node].parents:
        ic, childcount = getMuFromNode(p.id)
        parentIC_list.append(ic / childcount)
    ic_dict[node] = multiplyList(parentIC_list)
    return (ic_dict[node], len(tron[node].children))

def getICFromNode(node):
    node_mu = getMuFromNode(node)[0]
    ic = -log(node_mu, 10)
    return ic



