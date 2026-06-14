from model.FraseDiariaModel import FraseDiariaModel
class FraseDiariaDao:
    def __init__(self):
        self.fraseDiarias = {
            1: {"frase": "A vida é bela!", "data": "2026-06-01"},
            2: {"frase": "Cada dia é uma nova oportunidade.", "data": "2026-06-02"},
            3: {"frase": "Sorria para a vida!", "data": "2026-06-03"}
        }
 #FRASES ESPECIFICAS
    def obterFrase(self, data):
        for frase_info in self.fraseDiarias.values():
            if frase_info["data"] == data:
                return frase_info
        return None

#TODAS AS FRASES
    def listarFrases(self):
        listaFrases = list(self.fraseDiarias.values())
        return listaFrases
