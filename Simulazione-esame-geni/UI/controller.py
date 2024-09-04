import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        self._model.buildGraph()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(
            ft.Text(f"Creato grafo con {self._model.getNumNodi()} vertici e {self._model.getNumArchi()} archi"))


        self._view.txt_result.controls.append(ft.Text(f"Informazioni sui pesi degli archi: "
                                                      f"Valore minimo {self._model.calcolaMin()} e massimo {self._model.calcolaMax()}"))

        self._view.update_page()

    """def handle_countedges(self, e):
        soglia = self._view.txt_name.value
        try:
            sogliaIns = float(soglia)
        except ValueError:
            self._view.txt_result2.controls.clear()
            self._view.txt_result2.controls.append(ft.Text(f"Il numero inserito non è valido"))
            self._view.update_page()
            return
        min = self._model.calcolaMin()
        max = self._model.calcolaMax()
        if sogliaIns > min and sogliaIns < max:
            self._view.txt_result2.controls.clear()
            numMag, numMin = self._model.contaValoriSoglia(sogliaIns)
            self._view.txt_result2.controls.append(ft.Text(f"Numero archi con peso maggiore della soglia: {numMag}"))
            self._view.txt_result2.controls.append(ft.Text(f"Numero archi con peso minore della soglia: {numMin}"))
            self._view.update_page()
        else:
            self._view.txt_result2.controls.clear()
            self._view.txt_result2.controls.append(ft.Text(f"Il numero inserito non rispetta il valore min e max"))
            self._view.update_page()
            return"""

    def handle_countedges(self, e):
        threshold = float(self._view.txt_name.value)
        if threshold < self._model.calcolaMin() or threshold > self._model.calcolaMax():
            self._view.create_alert("Valore di soglia non valida!")
            return
        count_bigger, count_smaller = self._model.contaValoriSoglia(threshold)
        self._view.txt_result2.controls.append(ft.Text(f"Numero archi con peso maggiore della soglia: {count_bigger}"))
        self._view.txt_result2.controls.append(ft.Text(f"Numero archi con peso minore della soglia: {count_smaller}"))
        self._view.update_page()

    def handle_search(self, e):
        pass