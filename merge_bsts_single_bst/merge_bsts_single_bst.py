from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        # Mapear raízes para árvores e coletar valores de filhos
        root_to_tree = {}
        child_values = set()

        for tree in trees:
            root_to_tree[tree.val] = tree
            if tree.left:
                child_values.add(tree.left.val)
            if tree.right:
                child_values.add(tree.right.val)

        # Encontrar a raiz final
        final_root = None
        for tree in trees:
            if tree.val not in child_values:
                if final_root is not None:
                    return None
                final_root = tree
        # Verificar se há mais de uma raiz possível
        if final_root is None:
            return None

        # Remover a raiz final do mapeamento
        root_to_tree.pop(final_root.val, None)

        def validate_and_merge(node: TreeNode, min_val: float, max_val: float) -> bool:
            if node is None:
                return True

            # Verificar a propriedade BST
            if not (min_val < node.val < max_val):
                return False
            
            # Tentar mesclar subárvores se os filhos forem raízes de outras árvores
            if node.left:
                # Tentar mesclar subárvores se os filhos forem raízes de outras árvores
                if node.left.val in root_to_tree:
                    subtree = root_to_tree.pop(node.left.val)
                    node.left = subtree
                # Validar a subárvore esquerda
                if not validate_and_merge(node.left, min_val, node.val):
                    return False
            
            # Tentar mesclar subárvores se os filhos forem raízes de outras árvores
            if node.right:
                if node.right.val in root_to_tree:
                    subtree = root_to_tree.pop(node.right.val)
                    node.right = subtree
                
                if not validate_and_merge(node.right, node.val, max_val):
                    return False
            
            return True

        # Iniciar a validação e mesclagem a partir da raiz final
        if not validate_and_merge(final_root, float('-inf'), float('inf')):
            return None

        # Se ainda houver árvores não mescladas, retornar None
        if root_to_tree:
            return None 
        return final_root