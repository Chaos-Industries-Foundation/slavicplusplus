import os
keywords = {
        "точный_указ": "const",
        "цифра": "int",
        "ничего_не_знаю": "void",
        "булев": "bool",
        "для": "for",
        "пока": "while",
        "возвращати": "return",
        "молвить": "printf",
        "истина": "true",
        "ложь": "false",
        "царь_батюшка_главный": "main",
        "#подключати": "#include",
        "буква": "char",
        "#признавати": "#define",
        "узнать": "scanf"
        }
# Запрашиваем имя файла
file_name = input("Введите название файла: ")

try:
    # Открываем файл и читаем содержимое
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.read()
except FileNotFoundError:
    print(f'Файл "{file_name}" не найден.')
    exit()

# Разделяем строки текста
lines = data.split('\n')

# Обрабатываем каждую строку отдельно
processed_lines = []
for line in lines:
    for rus_word, eng_word in keywords.items():
        if rus_word in line:
            line = line.replace(rus_word, eng_word)
    processed_lines.append(line)

# Объединяем обработанные строки обратно в один блок текста
output_data = "\n".join(processed_lines)

# Печатаем итоговый вариант программы
with open(f"{file_name}_temp.c", "w") as o:
    o.write(output_data)
os.system(f"g++ -o {file_name.split('.')[0]} {file_name}_temp.c")
