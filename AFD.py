import graphviz

class AFD:
    def __init__(self, Q, Sigma, q0, F, delta):
        self.Q = Q               
        self.Sigma = Sigma        
        self.q0 = q0              
        self.F = F                
        self.delta = delta        

    def desenhar(self, nome="AFD"):
        dot = graphviz.Digraph(nome, format="png")
        dot.attr(rankdir="LR")

       
        dot.node("", shape="none")

        for estado in self.Q:
            if estado in self.F:
                dot.node(estado, shape="doublecircle")
            else:
                dot.node(estado, shape="circle")

        
        dot.edge("", self.q0)

       
        for (estado, simbolo), novo_estado in self.delta.items():
            dot.edge(estado, novo_estado, label=simbolo)

        dot.render(nome, view=True)

    def simular(self, cadeia):
        estado_atual = self.q0
        for simbolo in cadeia:
            if (estado_atual, simbolo) in self.delta:
                estado_atual = self.delta[(estado_atual, simbolo)]
            else:
                return False  
        return estado_atual in self.F


def main():
    print("=== Definição do AFD ===")

    
    Q = input("Conjunto de estados (separados por espaço): ").split()

    
    Sigma = input("Alfabeto (símbolos separados por espaço): ").split()

    
    q0 = input("Estado inicial: ").strip()

    
    F = input("Estados de aceitação (separados por espaço): ").split()

    
    print("Defina as transições no formato (estado simbolo novo_estado). Digite 'fim' para encerrar.")
    delta = {}
    while True:
        linha = input("δ: ")
        if linha.lower() == "fim":
            break
        partes = linha.split()
        if len(partes) != 3:
            print("Formato inválido! Use: estado simbolo novo_estado")
            continue
        estado, simbolo, novo_estado = partes
        delta[(estado, simbolo)] = novo_estado

    
    afd = AFD(Q, Sigma, q0, F, delta)

    
    afd.desenhar("AFD_Gerado")

    while True:
        cadeia = input("\nDigite uma cadeia (ou 'sair' para encerrar): ")
        if cadeia.lower() == "sair":
            break
        if afd.simular(cadeia):
            print(f"Cadeia '{cadeia}' -> ACEITA")
        else:
            print(f"Cadeia '{cadeia}' -> REJEITA")


if __name__ == "__main__":
    main()
