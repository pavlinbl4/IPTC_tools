import exiftool

# file = "/Users/evgeniy/Pictures/2022/20220630_Юридический форум/20220630EPAV0184.ORF"
# file = '/Users/evgeniy/Pictures/2022/20220914_Северная звезда/20220914PEV_6785.NEF'
file = '/Volumes/big4photo-4/2022/01_January/20220108_музей Бродского/20220108PEV_6568.DNG'

def read_xmp():
    with exiftool.ExifToolHelper() as et:
        metadata = et.get_metadata(file)

    # for d in metadata[0].keys():
        # print(d, metadata[0][d])
        # if d.startswith("XMP"):
        #     print(d, metadata[0][d])
        # if d.startswith("IPTC"):
        #     print(d, metadata[0][d])
    return metadata[0]["XMP:Title"], metadata[0]['XMP:Label'], metadata[0]['XMP:Creator']


def write_data_to_photo():
    with exiftool.ExifToolHelper() as et:
        title = "exiftool NEF"
        et.set_tags(
            [file],
            tags={"XMP:Title": title,
                  "IPTC:ObjectName": title,
                  'XMP:Label': "Yellow",
                  'XMP:Creator': 'Eugene Pavlenko'},
            params=["-P", "-overwrite_original"]
        )


write_data_to_photo()
print(read_xmp())
