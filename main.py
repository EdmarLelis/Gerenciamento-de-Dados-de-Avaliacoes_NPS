import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mapatches


class Feedback:
    def __init__(self, nota, comentario):
        self.comentario = comentario
        self.nota = nota


class AnalisandoFeedback:
    def __init__(self, feedback):
        self.feedback = feedback

    def calcular_nps(self):
        detractors = sum(1 for f in self.feedback.nota if f <= 6)
        promoters = sum(1 for f in self.feedback.nota if f >= 9)

        return ((promoters/len(self.feedback.nota)*100) - (detractors/len(self.feedback.nota)*100))


class NpsGrafico:
    def __init__(self, nps, NPS_ZONAS, NPS_VALORES, NPS_CORES):
        self.nps = nps
        self.NPS_ZONAS = NPS_ZONAS
        self.NPS_VALORES = NPS_VALORES
        self.NPS_CORES = NPS_CORES

    def criando_grafico(self):
        fig, ax = plt.subplots(figsize=(10, 2))

        for i, zona in enumerate(self.NPS_ZONAS):
            ax.barh([0], width=self.NPS_VALORES[i + 1] - self.NPS_VALORES[i], left=self.NPS_VALORES[i], color=self.NPS_CORES[i])

        ax.barh([0], width=1.2, left=self.nps, color='black')
        plt.show()


feedback = Feedback(pd.read_csv("arquivos/Avaliação01 - Página1.csv", delimiter=';')['Nota'], pd.read_csv("arquivos/Avaliação01 - Página1.csv", delimiter=';')['Comentario'])
nps = AnalisandoFeedback(feedback).calcular_nps()
