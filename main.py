import pandas as pd


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


feedback = Feedback(pd.read_csv("arquivos/Avaliação01 - Página1.csv", delimiter=';')['Nota'], pd.read_csv("arquivos/Avaliação01 - Página1.csv", delimiter=';')['Comentario'])
nps = AnalisandoFeedback(feedback).calcular_nps()

print(nps)