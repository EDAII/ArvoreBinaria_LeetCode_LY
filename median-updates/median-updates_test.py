from io import StringIO
import sys
import os

path = os.path.join(os.path.dirname(__file__), "median-updates.py")

print("Teste 1: Adições simples")
sys.stdin = StringIO("3\na 1\na 2\na 3\n")
exec(open(path).read())

print("\nTeste 2: Adição e remoção")
sys.stdin = StringIO("3\na 5\na 10\nr 5\n")
exec(open(path).read())

print("\nTeste 3: Elemento único")
sys.stdin = StringIO("1\na 42\n")
exec(open(path).read())

