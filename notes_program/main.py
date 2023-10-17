import json
import datetime

def load_notes():
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
        return notes
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file)

def create_note():
    title = input("Введите заголовок заметки: ")
    body = input("Напишите текст заметки: ")
    timestamp = datetime.datetime.now()
    note = {
        'id': len(notes) + 1,
        'title': title,
        'body': body,
        'timestamp': str(timestamp)
    }
    notes.append(note)
    save_notes(notes)
    print(f'Заметка {title} создана')

def display_notes():
    if len(notes) == 0:
        print("Заметок не найдено")
    else:
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Title: {note['title']}")
            print(f"Body: {note['body']}")
            print(f"Timestamp: {note['timestamp']}\n")

def edit_note():
    note_id = int(input("Введите ID заметки, которую вы хотите изменить: "))
    for note in notes:
        if note['id'] == note_id:
            note['title'] = input("Введите новый заголовок заметки: ")
            note['body'] = input("Напишите новую заметку: ")
            note['timestamp'] = str(datetime.datetime.now())
            save_notes(notes)
            return
    print("Заметка не найдена.")

def delete_note():
    note_id = int(input("Введите ID заметки, которую хотите удалить: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена.")
            return
    print("Заметка не найдена.")


notes = load_notes()
while True:
    print("1. Создать заметку")
    print("2. Показать все заметки")
    print("3. Изменить заметку")
    print("4. Удалить заметку")
    print("5. Выход")
    command = int(input("Выберите команду: "))
    if command == 1:
        create_note()
    elif command == 2:
        display_notes()
    elif command == 3:
        edit_note()
    elif command == 4:
        delete_note()
    elif command == 5:
        break
    else:
        print("Такой команды нет. Попробуйте еще раз!")


