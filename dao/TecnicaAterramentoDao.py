from model.TecnicaAterramentoModel import TecnicaAterramentoModel
class TecnicaAterramentoDao:
    def __init__(self):
        self.tecnicas = {
            1: {"idTecnica": 1, "tipo": "Respiração Profunda", "descricao": "Concentre-se em respirar profundamente para acalmar a mente."},
            2: {"idTecnica": 2, "tipo": "Contato com a Natureza", "descricao": "Passe um tempo ao ar livre para se reconectar com o ambiente."},
            3: {"idTecnica": 3, "tipo": "Meditação Guiada", "descricao": "Use uma meditação guiada para se centrar e encontrar equilíbrio."}
        }

    def obterTecnica(self, idTecnica):
        return self.tecnicas.get(idTecnica, None)
    
    def listarTecnicas(self):
        return list(self.tecnicas.values())