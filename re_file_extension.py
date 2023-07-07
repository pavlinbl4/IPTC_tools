import re


def find_extension(file):
    rg_pattern = r'NEF|nef|ORF|orf|JPG|jpg|CRW|crw'
    print(re.search(rg_pattern, file))


if __name__ == '__main__':
    orf_file = '/Users/evgeniy/Pictures/Pyton_tes_images/20230620EPAV8084.ORF'
    find_extension(orf_file)
