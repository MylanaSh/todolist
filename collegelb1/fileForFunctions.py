import normalnieFunctions as nf
from normalnieFunctions import songs, information_about_authors

nf.create_file("../collegelb1/songs.json", songs)
nf.create_file("../collegelb1/infoaut.csv", information_about_authors)


while True:
    print("\nМеню:")
    print("1. Пошук найпопулярнішого жанру")
    print("2. Пошук найпопулярнішої пісні")
    print("3. Додавання пісні")
    print("4. Пошук інформації про автора за назвою пісні")
    print("5. Додавання інформації про автора")
    print("6. Вийти")

    menu = input("Оберіть опцію (1-6): ")

    match menu:
        case '1':
            popular_genre, _ = nf.fpgs(songs)
            print(f"Найпопулярніший жанр: {popular_genre}")
        case '2':
            _, popular_song = nf.fpgs(songs)
            print(
                f"Найпопулярніша пісня: {popular_song[0]} - {popular_song[1]} ({popular_song[2]}) з {popular_song[3]} прослуховуваннями")
        case '3':
            song_add = tuple(input("Введіть Title, Author, Genre, Plays через кому: ").split(','))
            nf.append_file("../collegelb1/songs.json", song_add)
            nf.append_file("../collegelb1/songs.txt", song_add)
            print("Пісню додано.")
        case '4':
            song_title = input("Введіть назву пісні: ")
            print(nf.authorinfo_by_song(song_title, songs, information_about_authors))
        case '5':
            author_info_add = tuple(input("Введіть Name, City, Active через кому: ").split(','))
            nf.append_information_about_authors("../collegelb1/infoaut.csv", author_info_add)
            print("Інформацію про автора додано.")
        case '6':
            print("До побачення!")
            break
        case _:
            print("Помилка, спробуйте ще раз.")
