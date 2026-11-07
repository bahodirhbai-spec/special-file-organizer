import os
import shutil
import shutil
# Kategoriyalar lug'ati
CATEGORIES = {
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images",
    ".pdf": "Documents", ".docx": "Documents", ".txt": "Documents",
    ".zip": "Archives",
}

path = input("Enter path: ").strip()

# Kiritilgan yo'l mavjudligini tekshirish
if not os.path.exists(path) or not os.path.isdir(path):
    print("Xato: Bunday papka mavjud emas!")
else:
    files = os.listdir(path)

    moved_count = 0
    for file in files:
        file_path = os.path.join(path, file)

        # 1. Muhim: Agar bu papkaning o'zi bo'lsa, uni tashlab o'tamiz (o'zini o'ziga ko'chirmaslik uchun)
        if os.path.isdir(file_path):
            continue

        filename, extension = os.path.splitext(file)
        extension = extension.lower()

        # 2. Kategoriyani aniqlash
        if extension in CATEGORIES:
            folder_name = CATEGORIES[extension]
        else:
            folder_name = "Other"

        # 3. Kategoriya papkasining to'liq yo'li
        folder_path = os.path.join(path, folder_name)

        # 4. Papka mavjud bo'lmasa yaratamiz
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # 5. Faylni tegishli papkaga ko'chirish
        destination_path = os.path.join(folder_path, file)
        
        # Agar bir xil nomli fayl oldindan mavjud bo'lsa ustma-ust yozilib ketishining oldini olish
        if not os.path.exists(destination_path):
            shutil.move(file_path, destination_path)
            moved_count += 1

    print(f"Jarayon yakunlandi! Ko'chirilgan fayllar soni: {moved_count}")