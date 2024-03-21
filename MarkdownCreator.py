import tkinter as tk
from tkinter import filedialog
import os

def text_to_markdown(text):
    lines = text.strip().split('\n')
    markdown_lines = []
    for line in lines:
        if line.startswith('Секция') or any(line.startswith(prefix) for prefix in ["1.", "2.", "3.", "4."]):
            section_title = line.replace(':', '').split(' ', 1)[1]
            markdown_lines.append(f'## {section_title}\n')
        else:
            markdown_lines.append(f'{line}\n')
    return ''.join(markdown_lines)

def convert_file_to_markdown(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text_from_file = file.read()
        markdown_content = text_to_markdown(text_from_file)
        output_md_file_path = os.path.splitext(filepath)[0] + '_converted.md'
        with open(output_md_file_path, 'w', encoding='utf-8') as md_file:
            md_file.write(markdown_content)
        file_path_label.config(text=f"Файл сохранен как: {output_md_file_path}")
    except Exception as e:
        file_path_label.config(text="Ошибка при обработке файла: " + str(e))

def open_file_dialog():
    filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filepath:
        file_path_label.config(text=f"Обрабатывается файл: {filepath}")
        convert_file_to_markdown(filepath)

root = tk.Tk()
root.title("Конвертер TXT в Markdown")

open_file_button = tk.Button(root, text="Открыть TXT файл", command=open_file_dialog)
open_file_button.pack(pady=10)

file_path_label = tk.Label(root, text="Путь к файлу не выбран")
file_path_label.pack(pady=5)

root.mainloop()
