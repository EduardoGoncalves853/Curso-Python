# Class-06-challenge

# Abra o arquivo de filmes e crie um array
# Passe os nomes do array para caixa alta
# Escreva (write) os nomes em um novo arquivo

try:
#* Abre o arquivo e o renomeia como list_films
# r para (read)  ler
# w para (write) escrever

   with open('Curso-Python/class-06-files/files/films.txt', 'r', encoding="utf-8") as films, \
        open('Curso-Python/class-06-files/files/upper_films.txt', 'w', encoding="utf-8") as upper_films: 
#* Converte em Upper Case
    for film in films:
      upper_films.write(film.upper())

except FileNotFoundError:
    print("arquivo não encontrado!")