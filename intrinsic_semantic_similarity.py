from pronto import *
from math import log
from intrinsic_IC_calculation import getICFromNode

# Importing ontology
tron = Ontology('tribolium.obo')

ic_dict = dict()
#ic_list = dict()
root = 'TrOn:0000001'  # Ontology root term
ic_dict[root] = 1.0

def getSemanticSimilarity(term_a, term_b):
    term_a_parents = tron[term_a].rparents()
    term_b_parents = tron[term_b].rparents()
    common_ancesters = list(set(term_a_parents) & set(term_b_parents))

    common_ancesters_IC = dict()
    for ancester in common_ancesters:
        IC = getICFromNode(ancester.id)
        common_ancesters_IC[ancester.id] = IC
    mica = max(common_ancesters_IC.values())
    term_a_IC = getICFromNode(term_a)
    term_b_IC = getICFromNode(term_b)
    max_IC = max(term_a_IC, term_b_IC)
    semantic_similarity = mica/max_IC
    return semantic_similarity



