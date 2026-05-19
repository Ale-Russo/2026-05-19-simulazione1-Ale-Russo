from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._artisti = DAO.getAllArtists()
        self._pop = DAO.getPopularity()
        self._idMapArtisti = {}
        self._popMap = {}
        for a in self._artisti:
            self._idMapArtisti[a.ArtistId] = a
        for p in self._pop:
            self._popMap[p[0]] = p[1]



    def getAllGeneri(self):
        return DAO.getAllGeneri()

    def getAllNodes(self, GenreId, idMapA):
        artisti = DAO.getAllNodes(GenreId,idMapA)
        return artisti

    def creaGrafo(self,GenreId):
        self._graph.clear()
        nodi_validi = self.getAllNodes(GenreId, self._idMapArtisti)
        self._graph.add_nodes_from(nodi_validi)



