# скрипт добавляет новые ключевые слова
import pyexiv2


def add_keywords(new_keywords, file):
    changes = {}
    with open(file, 'rb+') as image_file:
        with pyexiv2.ImageData(image_file.read()) as meta_data:
            data = meta_data.read_xmp()
            changes['Xmp.dc.subject'] = list(set(data['Xmp.dc.subject'] + new_keywords))
            meta_data.modify_xmp(changes)
            image_file.seek(0)
            image_file.truncate()
            image_file.write(meta_data.get_bytes())
        image_file.seek(0)


file = "/Volumes/big4photo-4/2022/_mobile_2022/20220116_pavl_IMG_7653.JPG"

new_keywords = ['технология', 'нет человека', 'бизнес', 'данные', 'рабочий стол', 'факты', 'Деньги', 'Аннотация',
                'свет', 'интернет', 'электроника', 'наука', 'власть', 'яркий', 'темный', 'освещенный', 'связь',
                'коммуникация', 'исследование', 'количество']

add_keywords(new_keywords, file)
