"""
AES-шифрование/дешифрование файлов с помощью библиотеки cryptography
Принцип работы:
1. Генерируем ключ один раз и сохраняем его в key.key
2. Пользователь выбирает: шифрование или дешифрование
3. Скрипт читает файл, шифрует или дешифрует его
4. Результат сохраняется в новом файле
"""

from cryptography.fernet import Fernet
import os

# Функция для генерации ключа (если его ещё нет)
def generate_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as f:
            f.write(key)
        print("✅ Ключ сгенерирован и сохранён в key.key")
    else:
        print("🔑 Ключ уже существует, используем key.key")

# Функция для шифрования файла
def encrypt_file(filename):
    with open("key.key", "rb") as f:
        key = f.read()
    fernet = Fernet(key)

    with open(filename, "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    out_file = filename + ".enc"
    with open(out_file, "wb") as f:
        f.write(encrypted)
    print(f"✅ Файл зашифрован: {out_file}")

# Функция для дешифрования файла
def decrypt_file(filename):
    with open("key.key", "rb") as f:
        key = f.read()
    fernet = Fernet(key)

    with open(filename, "rb") as f:
        encrypted = f.read()

    try:
        decrypted = fernet.decrypt(encrypted)
    except:
        print("❌ Ошибка: не удалось расшифровать файл. Проверьте ключ и файл.")
        return

    if filename.endswith(".enc"):
        out_file = filename.replace(".enc", "")
    else:
        out_file = filename + ""

    with open(out_file, "wb") as f:
        f.write(decrypted)
    print(f"✅ Файл расшифрован: {out_file}")

# --- Основная логика ---
def main():
    generate_key()
    print("\nВыберите действие:")
    print("1 — Шифровать файл")
    print("2 — Дешифровать файл")
    choice = input("Введите 1 или 2: ").strip()

    file_name = input("Введите имя файла (с расширением) или полный путь к нему (если файл не в одной папке с вашим проектом): ").strip()

    if not os.path.exists(file_name):
        print("❌ Файл не найден.")
        return

    if choice == "1":
        encrypt_file(file_name)
    elif choice == "2":
        decrypt_file(file_name)
    else:
        print("❌ Неверный выбор.")

if __name__ == "__main__":
    main()