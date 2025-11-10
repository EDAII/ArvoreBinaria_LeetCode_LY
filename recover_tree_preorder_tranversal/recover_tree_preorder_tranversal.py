from typing import  Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        self.i = 0 
        self.S = traversal
        
        return self.dfs(0)

    def dfs(self, expected_depth: int) -> Optional[TreeNode]:
        #  Conta os hifens para determinar a profundidade atual
        peek_index = self.i
        current_depth = 0
        while peek_index < len(self.S) and self.S[peek_index] == '-':
            current_depth += 1
            peek_index += 1
        
        # Se a profundidade atual não corresponder à esperada, retorna None
        if current_depth != expected_depth:
            return None 

        self.i = peek_index
        
        # Ler o valor do nó 
        value_str = ""
        while self.i < len(self.S) and self.S[self.i].isdigit():
            value_str += self.S[self.i]
            self.i += 1
            
        if not value_str:
            return None
            
        # Criar o nó com o valor lido
        node = TreeNode(int(value_str))
        
        # Recursivamente construir os filhos esquerdo e direito
        node.left = self.dfs(expected_depth + 1)
        node.right = self.dfs(expected_depth + 1)
        
        return node