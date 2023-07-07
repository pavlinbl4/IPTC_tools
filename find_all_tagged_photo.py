from tkinter import filedialog
import os
import re
import exiftool
import shutil
from datetime import datetime


def select_folder():
    return filedialog.askdirectory(initialdir='/Users/evgeniy/Pictures/Pyton_tes_images')


def check_tag(file):
    with exiftool.ExifToolHelper() as et:
        metadata = et.get_metadata(file)[0]  # extract dict from list
    return metadata.get('XMP:Tagged')


def find_image_files(path):  # this will match a file_name
    rg_pattern = r'NEF|nef|ORF|orf|JPG|jpg|DNG'
    result = []
    for root, dirs, files in os.walk(path):
        print(f"{len(files)} files in folder")
        for name in files:
            print(f'check file {name}')
            if re.search(rg_pattern, name) and check_tag(os.path.join(root, name)):
                result.append(os.path.join(root, name))
    return result  # возвращает список с путем к оригинальному файлу


def copy_files(files: list):
    today_date = f'{datetime.now().strftime("%Y%m%d")}'
    os.makedirs(f"{'/Users/evgeniy/Pictures'}/{today_date}", exist_ok=True)
    for file in files:
        distination = f"{'/Users/evgeniy/Pictures'}/{today_date}"
        shutil.copy(file, distination)
        print(f"file {file.split('/')[-1]} was coped to {today_date} folder ")


if __name__ == '__main__':
    tagged_files = find_image_files(select_folder())
    print(f'found {len(tagged_files)} protected images')
    copy_files(tagged_files)
