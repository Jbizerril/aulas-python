# Coletar as informações do usuário
extensao_pista = float(input("Extensão da pista (km): "))
numero_voltas = int(input("Número de voltas: "))
consumo_base = float(input("Consumo de combustível (litros por km): "))
clima = input("Condições climáticas (ensolarado/chuvoso/nublado/ventania): ").strip().lower()
estrategia = input("Estratégia do piloto (agressiva/conservadora/regular): ").strip().lower()
desgaste_pneus = input("Desgaste dos pneus alto? (s/n): ").strip().lower()

# Ajustar consumo baseado nas condições climáticas, 
consumo_clima = {
    "ensolarado": 0.95,
    "chuvoso": 1.2,
    "nublado": 1.05,
    "ventania": 0.9 if input("Vento a favor ou contra? (favor/contra): ").strip().lower() == "favor" else 1.1
}
consumo_por_km = consumo_base * consumo_clima.get(clima, 1)

# Ajustar consumo baseado na estratégia do piloto
estrategia_piloto = {
    "agressiva": 1.2,
    "conservadora": 0.9,
    "regular": 1  # Sem alteração no consumo, não faria sentido todo mundo estar muito rápido ou lento, quis a opção 'padrão' também
}
consumo_por_km *= estrategia_piloto.get(estrategia, 1)

# Ajustar consumo por desgaste dos pneus, não sei como se dá numa corrida de f1, acredito que seja maior, ja que trocam pneus diretos, mas fiz um desgaste baixo, só para ter
if desgaste_pneus == 's':
    consumo_por_km *= 1.05

# Calcular a quantidade de combustível necessária
distancia_total = extensao_pista * numero_voltas
combustivel_necessario = distancia_total * consumo_por_km

# Exibir o resultado
print(f"\nQuantidade de combustível necessária: {combustivel_necessario:.2f} litros")