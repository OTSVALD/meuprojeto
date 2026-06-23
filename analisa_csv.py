import csv

arquivo = r"C:\Users\Usuário\Desktop\vendas.csv"
erros = 0
total_valor = 0
vendas_validas = 0

with open(arquivo, encoding="utf-8") as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        produto = linha["produto"]
        qtd = int(linha["quantidade"])
        valor = float(linha["valor"])
        status = linha["status"]

        if qtd &lt;= 0:
            print(f"Erro: {produto} - quantidade invalida ({qtd})")
            erros += 1
        if valor &lt;= 0:
            print(f"Erro: {produto} - valor invalido ({valor})")
            erros += 1
        if status not in ("pago", "pendente"):
            print(f"Erro: {produto} - status invalido ({status})")
            erros += 1
        if qtd > 0 and valor > 0 and status in ("pago", "pendente"):
            vendas_validas += 1
            total_valor += valor * qtd

print(f"\nVendas validas: {vendas_validas}")
print(f"Valor total: R$ {total_valor:.2f}")
print(f"Erros: {erros}")

if erros > 0:
    exit(1)
else:
    exit(0)
