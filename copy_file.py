import shutil


def copy_file(file_path, distination):
    shutil.copy(file_path, distination)


if __name__ == '__main__':
    copy_file('/Users/evgeniy/Pictures/Pyton_tes_images/20230620EPAV8163.jpg',
              '/Users/evgeniy/Desktop/Fast_jpeg')
