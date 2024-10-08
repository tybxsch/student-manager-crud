from utils.arquivos.ler_json import ler_json
from utils.arquivos.escrever_json import escrever_json
from utils.identificador_unico import identificador_unico_baseado_em_timestemp
from utils.constants import INVALID_CODE


class EntidadeController:
    def __init__(self, nome_entidade):
        self.nome_entidade = nome_entidade
        self.entidades = ler_json(nome_entidade)

    def escrever_json(self):
        escrever_json(self.entidades, self.nome_entidade)

    def gerar_identificador_unico(self):
        return identificador_unico_baseado_em_timestemp()

    def validar_codigo_existente(self, codigo):
        for entidade in self.entidades:
            if str(entidade["codigo"]) == str(codigo):
                return True
        print(INVALID_CODE)
        return False

    def criar_entidade(self, entidade):
        self.entidades.append(entidade)
        self.escrever_json()

    def ler_entidade(self):
        if not self.entidades:
            print("\nNão há dados cadastrados")
        else:
            print("\nLista:")
            for entidade in self.entidades:
                if isinstance(entidade, dict):
                    entidade_formatada = ", ".join(
                        f"{chave}: {valor}" for chave, valor in entidade.items()
                    )
                    print(entidade_formatada)
                else:
                    print(entidade)

    def atualizar_entidade(self, codigo, novos_dados):
        for entidade in self.entidades:
            if str(entidade["codigo"]) == str(codigo):
                entidade.update(novos_dados)
                self.escrever_json()
                return
        print(INVALID_CODE)

    def deletar_entidade(self, codigo):
        for entidade in self.entidades:
            if str(entidade["codigo"]) == str(codigo):
                self.entidades.remove(entidade)
                self.escrever_json()
                return
        print(INVALID_CODE)
