from model.model import Model

myModel = Model()
myModel.creaGrafo(2)
grafo = myModel._graph
print(f"Il grafo ha {len(grafo.nodes)} vertici e {len(grafo.edges)} archi.")
myModel.dettagliGrafo(grafo)
