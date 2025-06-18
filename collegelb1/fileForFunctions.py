import normalnieFunctions as nf
from normalnieFunctions import songs, information_about_authors

nf.create_file("../collegelb1/songs.json", songs)
nf.create_file("../collegelb1/infoaut.csv", information_about_authors)


while True:
    print("\nМеню:")
    print("1. Список пісень і авторів")
    print("2. інформація про авторів")
    print("3. Пошук найпопулярнішого жанру")
    print("4. Пошук найпопулярнішої пісні")
    print("5. Додавання пісні")
    print("6. Пошук інформації про автора за назвою пісні")
    print("7. Додавання інформації про автора")
    print("8. Вийти")

    menu = input("Оберіть опцію (1-8): ")

    match menu:
        case '1':
            for t in songs:
                print({t[0]}, {t[1]})
        case '2':
            print(information_about_authors)
        case '3':
            _, popular_song = nf.fpgs(songs)
            print(
                f"Найпопулярніша пісня: {popular_song[0]} - {popular_song[1]} ({popular_song[2]}) з {popular_song[3]} прослуховуваннями")
        case '4':
            popular_genre, _ = nf.fpgs(songs)
            print(f"Найпопулярніший жанр: {popular_genre}")
        case '5':
            song_title = input("Введіть назву пісні: ")
            print(nf.authorinfo_by_song(song_title, songs, information_about_authors))
        case '6':
            author_info_add = tuple(input("Введіть Name, City, Active через кому: ").split(','))
            nf.append_information_about_authors("csv.csv", author_info_add)
            print("Інформацію про автора додано.")
        case '7':
            song_add = tuple(input("Введіть Title, Author, Genre, Plays через кому: ").split(','))
            nf.append_file("songs.json", song_add)
            nf.append_file("songs.txt", song_add)
            print("Пісню додано.")
        case '8':
            print("До побачення!")
            break
        case _:
            print("Помилка, спробуйте ще раз.")
