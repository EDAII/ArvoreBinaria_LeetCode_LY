from io import StringIO
import sys
import os

path = os.path.join(os.path.dirname(__file__), "self-balancing-tree.py")

print("Teste 1: Inserção simples")
sys.stdin = StringIO("3\n5 3 7\n2\n")
exec(open(path).read())

print("\nTeste 2: Rotação")
sys.stdin = StringIO("2\n1 2\n3\n")
exec(open(path).read())

print("\nTeste 3: Inserção balanceada")
sys.stdin = StringIO("3\n10 5 15\n12\n")
exec(open(path).read())

