import os
from pathlib import Path

def count_lines(filepath: str) -> int:
    """Подсчёт количества строк в файле"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)

def main():
    # Получаем пути из переменных окружения
    data_dir = os.getenv('DATA_DIR')
    dataset_path = os.getenv('DATASET_PATH')
    result_dir = os.getenv('RESULT_DIR')
    result_path = os.getenv('RESULT_PATH')

    # Проверяем, что все переменные заданы
    if None in (data_dir, dataset_path, result_dir, result_path):
        raise ValueError("Не все необходимые переменные окружения заданы!")

    # Формируем полные пути
    input_file = Path(data_dir) / dataset_path
    output_file = Path(result_dir) / result_path

    # Создаём директорию для результатов, если её нет
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Подсчитываем строки и записываем результат
    line_count = count_lines(input_file)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(str(line_count))

    print(f"Успешно обработано! Количество строк: {line_count}")

if __name__ == "__main__":
    main()
