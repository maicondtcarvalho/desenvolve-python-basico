arquivo = open("meus_livros.csv", "w", encoding="utf-8")

arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")

arquivo.write("O Caçador de Pipas,Khaled Hosseini,2003,368\n")
arquivo.write("Torto Arado,Itamar Vieira Junior,2019,264\n")
arquivo.write("Dom Casmurro,Machado de Assis,1899,256\n")
arquivo.write("1984,George Orwell,1949,328\n")
arquivo.write("A Revolução dos Bichos,George Orwell,1945,152\n")
arquivo.write("Harry Potter e a Pedra Filosofal,J.K. Rowling,1997,264\n")
arquivo.write("O Pequeno Príncipe,Antoine de Saint-Exupéry,1943,96\n")
arquivo.write("Senhor dos Anéis,J.R.R. Tolkien,1954,1178\n")
arquivo.write("Percy Jackson e o Ladrão de Raios,Rick Riordan,2005,400\n")
arquivo.write("Extraordinário,R.J. Palacio,2012,320\n")

arquivo.close()

print("Arquivo meus_livros.csv criado com sucesso!")