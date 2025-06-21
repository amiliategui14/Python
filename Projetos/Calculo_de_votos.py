# Tabela de candidatos
candidatos = {
    1: "José",
    2: "Maria",
    3: "Ana",
    4: "Luna"

}

# Inicializando contadores
votos = {
    "José": 0,
    "Maria": 0,
    "Ana": 0,
    "Luna": 0,
    "Nulo": 0,
    "Branco": 0
}

print("Códigos de votação:")
print("1 - josé\n2 - João\n3 - Maria\n4 - Voto Nulo\n6 - Voto Branco\n0 - Fim dos votos")

# Leitura dos votos
while True:
    try:
        voto = int(input("Digite o código de voto: "))
        if voto == 0:
            break
        elif voto in [1, 2, 3, 4]:
            votos[candidatos[voto]] += 1
        elif voto == 5:
            votos["Nulo"] += 1
        elif voto == 6:
            votos["Branco"] += 1
        else:
            print("Codigo inválido! Tente novamente.")
    except ValueError:
        print("Entrada inválida! Digite apenas números.")

# Total de votos
total_votos = sum(votos.values())

# Cálculo das porcentagens
percent_nulo = (votos["Nulo"] / total_votos) * 100 if total_votos > 0 else 0
percent_branco = (votos["Branco"] / total_votos) * 100 if total_votos > 0 else 0

# Mostrando os resultados
print("\nRESULTADO DA ELEIÇÃO:")
for nome in candidatos.values():
    print(f"{nome}: {votos[nome]} voto(s)")
print(f"Votos nulos: {votos['Nulo']}")
print(f"Votos em branco: {votos['Branco']}")
print(f"Percentual de votos nulos: {percent_nulo:.2f}%")
print(f"Percentual de votos em branco: {percent_branco:.2f}%")

# Descobrindo o vencedor
vencedor = max(candidatos.values(), key=lambda nome: votos[nome])
print(f"\nCandidato vencedor: {vencedor}")