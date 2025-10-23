import json
import csv


def authorinfo_by_song(song_title, songs, authors_info):
    author_name = None
    for title, author, genre, plays in songs:
        if title.lower() == song_title.lower():
            author_name = author
            break

    if not author_name:
        return f"Пісню '{song_title}' не знайдено."

    for info in authors_info:
        if info[0].lower() == author_name.lower():
            return f"Інформація про автора '{author_name}': Місто - {info[1]}, Активність - {info[2]}"

    return f"Інформація про автора '{author_name}' не знайдена."


def create_file(fileName, text):
    try:
        with open(fileName, 'w', encoding='utf-8') as file:
            if fileName.endswith(".json"):
                songs_json = []
                for t in text:
                    name, author, genre, plays = t
                    songs_json.append({
                        "Title": name,
                        "Author": author,
                        "Genre": genre,
                        "Plays": plays
                    })
                json.dump(songs_json, file, indent=2)

            if fileName.endswith(".csv"):
                for t in text:
                    file.write(f"Name: {t[0]} / City: {t[1]} / Active: {t[2]} | \n")

            if fileName.endswith(".txt"):
                for t in text:
                    file.write(f"Title: {t[0]} | Author: {t[1]} | Genre: {t[2]} | Plays: {t[3]} | \n")
        print(f"Файл {fileName} записано")

    except FileNotFoundError:
        print(f"Файл {fileName} не знайдено")


def fpgs(songs):
    genreplays = {}
    mpsong = tuple()

    for title, author, genre, plays in songs:
        if genre not in genreplays:
            genreplays[genre] = 0
        genreplays[genre] += plays

        if not mpsong:
            mpsong = (title, author, genre, plays)
        elif plays > mpsong[3]:
            mpsong = (title, author, genre, plays)

    mpgenre = max(genreplays, key=genreplays.get)

    return mpgenre, mpsong


def append_file(fileName, text):
    try:
        if fileName.endswith(".json"):
            with open(fileName, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = {}
            title = text[0]
            data[title] = {
                "Author": text[1],
                "Genre": text[2],
                "Plays": int(text[3])
            }
            with open(fileName, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2)

        elif fileName.endswith(".txt"):
            with open(fileName, 'a', encoding='utf-8') as file:
                file.write(f"Title: {text[0]} | Author: {text[1]} | Genre: {text[2]} | Plays: {text[3]} |\n")
        print(f"Файл {fileName} записано")
    except FileNotFoundError:
        print(f"Файл {fileName} не знайдено")


def append_information_about_authors(fileName, text):
    try:
        with open(fileName, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            formatted_row = [f"Name: {text[0]} / City: {text[1]} / Active: {text[2]} |"]
            writer.writerow(formatted_row)
        print(f"Файл {fileName} записано")
    except FileNotFoundError:
        print(f"Файл {fileName} не знайдено")

songs = [
    ("Are You Ready For Me", "Pretty Vicious", "Grunge", 8558614),
    ("The Funeral Of Hearts", "HIM", "Metal", 20589444),
    ("Girls, Girls, Girls", "Motley Crue", "Rock", 335166996),
    ("Gorgeous Nightmare", "Escape The Fate", "Metal", 19959997)
]

information_about_authors = [
    ["Pretty Vicious", "Merthyr Tydfil, Wales", "2014-2019"],
    ["HIM", "Helsinki, Finland", "1991-1993, 1995-2017"],
    ["Motley Crue", "Los-Angeles, USA", "1981-now"],
    ["Escape The Fate", "Las-Vegas, USA", "2004-now"]
]

for t in songs:
    print({t[0]} , {t[1]})

create_file("../collegelb1/songs.json", songs)
create_file("../collegelb1/infoaut.csv", information_about_authors)

popular_genre, popular_song = fpgs(songs)