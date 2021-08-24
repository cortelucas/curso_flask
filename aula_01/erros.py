a: int = 5
b: int = 10

try:
    a.upper()
    print(b // a)
except AttributeError as e:
    print("Não posso transformar número em maiúsculo", str(e))
except ZeroDivisionError as e:
    print("Erro, tente novamente!", str(e))
