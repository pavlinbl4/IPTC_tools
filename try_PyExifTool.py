import exiftool

# jpg_file = '/Users/evgeniy/Pictures/python_test_images/shutterstock_235800871.jpg'
jpg_file = '/Users/evgeniy/Pictures/python_test_images/20230602_PAV5801.JPG'
# dng_file = '/Users/evgeniy/Pictures/python_test_images/20230602_PAV5801.DNG'
# orf_file = '/Users/evgeniy/Pictures/python_test_images/20230403EPAV9047.ORF'
# jpg_file = '/Users/evgeniy/Pictures/python_test_images/20211201PEV_2795-Edit.JPG'
# jpg_file_edit = '/Users/evgeniy/Pictures/python_test_images/20230403EPAV9047_xnView.jpg'


def read_all_metadata_by_type(file, metadata_type):
    with exiftool.ExifToolHelper() as et:
        metadata = et.get_metadata(file)[0]  # extract dict from list
    for d in metadata.keys():
        if d.startswith(metadata_type):
            print(d, '-->', metadata[d])

def read_main_xmp_data(file):
    with exiftool.ExifToolHelper() as et:
        metadata = et.get_metadata(file)[0]  # extract dict from list
    main_tags = ['XMP:Headline','XMP:Description', 'XMP:Rating', 'XMP:ColorClass', 'XMP:Tagged', 'XMP:Subject', 'XMP:Urgency']
    # main_tags = ['XMP:RawFileName','XMP:OriginalDocumentID','XMP:PreservedFileName','XMP:DerivedFromOriginalDocumentID']
    readed_tags = {}
    for tag in main_tags:
        readed_tags[tag.split(':')[1]] = metadata.get(tag, 'NO INFORMATION')
    return readed_tags

def read_keywords(file):
    with exiftool.ExifToolHelper() as et:
        metadata = et.get_metadata(file)[0]  # extract dict from list
    return metadata.get('XMP:Subject', [])




def write_data_to_photo(file):
    with exiftool.ExifToolHelper() as et:
        metadata = et.get_metadata(file)[0]
        keywords = metadata.get('XMP:Subject', [])
        print(keywords)
        print(type(keywords))
        et.set_tags(
            [file],
            tags={"XMP:Title": 'Python Title',
                  'XMP:Tagged': True,
                  'XMP:Rating': 1,
                  "IPTC:ObjectName": 'Lightroom Title',
                  'XMP:Label': "Blue",
                  'XMP:Description': "Python XMP_Description",
                  'XMP:Creator': 'Eugene Pavlenko',
                  'XMP:Subject': "Python",

                 },  #  'XMP:Subject': keywords.append("Python")
            params=["-P", "-overwrite_original"]
        )



if __name__ == '__main__':
    # write_data_to_photo()
    # read_all_metadata_by_type(jpg_file, "IPTC")
    # read_all_metadata_by_type(jpg_file, "XMP")
    # print(read_main_xmp_data(jpg_file))
    # write_data_to_photo(jpg_file_edit)
    # print(read_main_xmp_data(jpg_file_edit))
    # print(read_keywords(jpg_file))
    # print(type(read_keywords(jpg_file)))
    write_data_to_photo(jpg_file)