contatos = {
    "gulherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovana@gmail.com": {"nome": "Giovana", "telefone": "32344-2561"},
    "chappie@gmail.com": {"nome": "Chappei", "telefone": "3456-2589"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3000-6981", "extra": {"a": 1}},
}

telefone = contatos["giovana@gmail.com"]["telefone"]
print(telefone)

extra = contatos["melaine@gmail.com"]["extra"]["a"]
print(extra)

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

for chave, valor in contatos.items():
    print(chave,valor)