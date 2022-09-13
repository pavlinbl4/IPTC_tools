file = "/Volumes/big4photo-4/EDITED_JPEG_ARCHIV/2022/KSP_017489_00060_1h.jpg"

import pyexiv2

img = pyexiv2.Image(file)

data = img.read_xmp()
# data = img.read_iptc()
data = img.read_exif()
for i in data:
    print(f" {i}  - {data[i]}")
# print(data['Xmp.dc.subject'])
