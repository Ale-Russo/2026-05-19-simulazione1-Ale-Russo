from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._artisti = DAO.getAllArtists()
        self._pop = []
        self._idMapArtisti = {}
        self._popMap = {}
        for a in self._artisti:
            self._idMapArtisti[a.ArtistId] = a
        self._clientiArtisti = {}
        self._prova = []


    def getAllGeneri(self):
        return DAO.getAllGeneri()

    def getAllNodes(self, GenreId, idMapA):
        artisti = DAO.getAllNodes(GenreId,idMapA)
        return artisti

    def addAllEdges(self, Artisti):
        for i in range(len(Artisti)):
            artista1 = Artisti[i]
            id1 = artista1.ArtistId
            if id1 in self._popMap:
                pop1 = self._popMap[id1]
            else:
                continue
            clienti1 = self._clientiArtisti[id1]
            for j in range(i+1, len(Artisti)):
                artista2 = Artisti[j]
                id2 = artista2.ArtistId
                if artista1 == artista2:
                    continue
                if id2 in self._popMap:
                    pop2 = self._popMap[id2]
                else:
                    continue
                clienti2 = self._clientiArtisti[id2]
                if len(clienti1.intersection(clienti2)) > 0:
                        peso = pop1 + pop2
                        if pop1 > pop2:
                            self._graph.add_edge(artista1, artista2, weight=peso)
                        elif pop1 == pop2:
                            self._graph.add_edge(artista1, artista2, weight=peso)
                            self._graph.add_edge(artista2, artista1, weight=peso)
                        else:
                            self._graph.add_edge(artista2, artista1, weight=peso)


    def creaGrafo(self,GenreId):
        self._graph.clear()
        self._pop = DAO.getPopularity(GenreId)
        for p in self._pop:
            self._popMap[p["ArtistId"]] = int(p["Popolarita"])
        self._prova = DAO.getAcquisti(GenreId)
        for coppia in self._prova:
            if coppia[1] in self._clientiArtisti:
                self._clientiArtisti[coppia[1]].add(coppia[0])
            else:
                self._clientiArtisti[coppia[1]] = {coppia[0]}
        nodi_validi = self.getAllNodes(GenreId, self._idMapArtisti)
        self._graph.add_nodes_from(nodi_validi)
        self.addAllEdges(nodi_validi)



