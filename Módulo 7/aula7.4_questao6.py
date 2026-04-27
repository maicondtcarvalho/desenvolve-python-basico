arquivo = open("spotify-2023.csv", "r", encoding="latin-1")
linhas = arquivo.readlines()
arquivo.close()

for i in range(5):
    print(linhas[i], end="")

melhores_por_ano = {}

for linha in linhas[1:]:
    if linha.startswith('"'):
        continue

    partes = linha.strip().split(",")

    if len(partes) < 9:
        continue

    if '"' in partes[1]:
        continue

    try:
        track_name = partes[0]
        artista = partes[1]
        released_year = int(partes[3])
        streams = int(partes[8])

        if released_year >= 2012 and released_year <= 2022:
            if released_year not in melhores_por_ano:
                melhores_por_ano[released_year] = [track_name, artista, released_year, streams]
            else:
                if streams > melhores_por_ano[released_year][3]:
                    melhores_por_ano[released_year] = [track_name, artista, released_year, streams]

    except:
        continue

resultado = []

for ano in range(2012, 2023):
    if ano in melhores_por_ano:
        resultado.append(melhores_por_ano[ano])

print("\nLista final:")
print(resultado)