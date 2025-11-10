from typing import List, Optional

from merge_bsts_single_bst import TreeNode, Solution

def construir_arvore(valores: List[Optional[int]]) -> Optional[TreeNode]:
    if not valores:
        return None

    raiz = TreeNode(valores[0])

    if len(valores) > 1 and valores[1] is not None:
        raiz.left = TreeNode(valores[1])

    if len(valores) > 2 and valores[2] is not None:
        raiz.right = TreeNode(valores[2])

    return raiz


def arvore_para_lista(raiz: Optional[TreeNode]) -> List[Optional[int]]:
    if raiz is None:
        return []

    resultado: List[Optional[int]] = []
    fila = [raiz]
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


class MergeBSTTester:
    def testar(self, descricao: str, arvores_input: List[List[Optional[int]]]):
        print(f"Teste: {descricao}")
        print(f"Árvores (entrada): {arvores_input}")

        arvores = [construir_arvore(valores) for valores in arvores_input]
        resultado = Solution().canMerge(arvores)
        lista_resultado = arvore_para_lista(resultado)

        print(f"Resultado (lista por níveis): {lista_resultado if lista_resultado else '[]'}")
        print("-" * 40)


def main():
    tester = MergeBSTTester()

    casos_teste = [
        ("Exemplo 1", [[2, 1], [3, 2, 5], [5, 4]]),
        ("Exemplo 2", [[5, 3, 8], [3, 2, 6]]),
        ("Exemplo 3", [[5, 4], [3]]),
    ]

    for descricao, arvores_input in casos_teste:
        tester.testar(descricao, arvores_input)


if __name__ == "__main__":
    main()

