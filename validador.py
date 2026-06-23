#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
analise_vendas.py

Script de validação de dados de vendas para integração com Jenkins.
Utiliza dados internos (hardcoded) e aplica regras de validação.
"""

import sys


def obter_dados_vendas():
    """Retorna a lista de vendas definida internamente."""
    vendas = [
        {"produto": "Notebook", "quantidade": 2, "valor": 4500.00, "status": "pago"},
        {"produto": "Mouse", "quantidade": 10, "valor": 50.00, "status": "pago"},
        {"produto": "Teclado", "quantidade": -1, "valor": 200.00, "status": "pendente"},
        {"produto": "Monitor", "quantidade": 3, "valor": -1500.00, "status": "pago"},
        {"produto": "Webcam", "quantidade": 5, "valor": 120.00, "status": "cancelado"},
        {"produto": "Fone", "quantidade": 0, "valor": 80.00, "status": "pago"},
    ]
    return vendas


def validar_venda(venda):
    """
    Valida uma venda conforme as regras:
      - quantidade > 0
      - valor > 0
      - status em ['pago', 'pendente']
    Retorna uma lista de erros encontrados.
    """
    erros = []
    produto = venda.get("produto", "DESCONHECIDO")
    quantidade = venda.get("quantidade")
    valor = venda.get("valor")
    status = venda.get("status")

    if not isinstance(quantidade, (int, float)) or quantidade <= 0:
        erros.append({
            "produto": produto,
            "campo": "quantidade",
            "valor": quantidade,
            "mensagem": "A quantidade deve ser maior que zero.",
        })

    if not isinstance(valor, (int, float)) or valor <= 0:
        erros.append({
            "produto": produto,
            "campo": "valor",
            "valor": valor,
            "mensagem": "O valor deve ser maior que zero.",
        })

    if status not in ("pago", "pendente"):
        erros.append({
            "produto": produto,
            "campo": "status",
            "valor": status,
            "mensagem": "O status deve ser 'pago' ou 'pendente'.",
        })

    return erros


def main():
    vendas = obter_dados_vendas()

    total_registros = len(vendas)
    vendas_validas = 0
    valor_total_validas = 0.0
    todos_os_erros = []

    print("=" * 80)
    print("INÍCIO DA VALIDAÇÃO DE VENDAS")
    print("=" * 80)

    for venda in vendas:
        erros_da_venda = validar_venda(venda)

        if erros_da_venda:
            todos_os_erros.extend(erros_da_venda)
        else:
            vendas_validas += 1
            valor_total_validas += venda.get("valor", 0.0)

    if todos_os_erros:
        print("\nERROS ENCONTRADOS:")
        print("-" * 60)
        for erro in todos_os_erros:
            print(
                f"Produto: {erro['produto']:<10} | "
                f"Campo: {erro['campo']:<10} | "
                f"Valor: {erro['valor']!s:<15} | "
                f"Motivo: {erro['mensagem']}"
            )

    print("\n" + "=" * 60)
    print("RESUMO")
    print("=" * 60)
    print(f"Total de registros:    {total_registros}")
    print(f"Vendas válidas:        {vendas_validas}")
    print(f"Valor total válidas:   R$ {valor_total_validas:,.2f}")
    print(f"Erros encontrados:     {len(todos_os_erros)}")
    print("=" * 60)

    if todos_os_erros:
        print("\nFalha na validação: foram encontrados erros.")
        sys.exit(1)

    print("\nValidação concluída com sucesso.")
    sys.exit(0)


if __name__ == "__main__":
    main()
