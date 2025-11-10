from typing import List, Optional

from recover_tree_preorder_tranversal import TreeNode, Solution


def arvore_para_lista_nivel(raiz: Optional[TreeNode]) -> List[Optional[int]]:
    if raiz is None:
        return []

    resultado: List[Optional[int]] = []
    fila: List[Optional[TreeNode]] = [raiz]
    indice = 0

    while indice < len(fila):
        nodo = fila[indice]
        indice += 1

        if nodo is None:
            resultado.append(None)
            continue

        resultado.append(nodo.val)
        fila.append(nodo.left)
        fila.append(nodo.right)

    while resultado and resultado[-1] is None:
        resultado.pop()

    return resultado


class RecoverTreeTester:
    def testar(self, descricao: str, traversal: str):
        print(f"Teste: {descricao}")
        print(f"Traversal (entrada): {traversal}")

        resultado = Solution().recoverFromPreorder(traversal)
        lista_nivel = arvore_para_lista_nivel(resultado)
        lista_formatada = [("null" if valor is None else valor) for valor in lista_nivel]

        print(f"Resultado (ordem por níveis): {lista_formatada if lista_formatada else '[]'}")
        print("-" * 40)


def main():
    tester = RecoverTreeTester()

    casos_teste = [
        ("Exemplo 1", "1-2--3--4-5--6--7"),
        ("Exemplo 2", "1-2--3---4-5--6---7"),
        ("Exemplo 3", "1-401--349---90--88"),
    ]

    for descricao, traversal in casos_teste:
        tester.testar(descricao, traversal)


if __name__ == "__main__":
    main()

