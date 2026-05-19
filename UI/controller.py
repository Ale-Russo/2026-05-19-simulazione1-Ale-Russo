import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDGenre(self):
        generi = self._model.getAllGeneri()
        for g in generi:
            self._view._ddGenre.options.append(ft.dropdown.Option(text = g["Name"],
                                                                  key = g["GenreId"]))

    def handleCreaGrafo(self, e):
        self._view._txt_result.options.clear()
        genere = self._view._ddGenre.value
        if genere is None:
            self._view._txt.result.options.append(ft.Text("Inserire um genere.", color="red"))
            self._view.update_page()
            return

        self._model.creaGrafo(genere)
        self._view._ddArtist.options.clear()
        for a in self._model._graph.nodes:
            self._view._ddArtist.options.append(ft.dropdown.Option(text = a.Name,
                                                                   key = str(a.ArtistId)))
        self._view.update_page()


    def handleCreaGrafo(self,e):
        pass

    def handleCammino(self,e):
        pass