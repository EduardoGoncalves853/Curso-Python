# "r" - read
# "w" - write
# "r+"- read/write
# "x" - create
# "a" - append

# films = open("Curso-Python/class-06-files/films.txt", "r+", encoding="utf-8")
try:
    with open("Curso-Python/class-06-files/files/films.txt", "r+", encoding="utf-8") as list_films:
        print(list_films.read())
        print(list_films.tell())
        array_films = list_films.readlines()
        # list_films.write("Piratas do Caribe\n")

        list_films.seek(0)
        for film in array_films:
            print(film.upper())
except FileNotFoundError:
    print("arquivo não encontrado!")

