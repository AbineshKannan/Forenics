from PIL import Image
from PIL.ExifTags import TAGS
import sys
import colorama
colorama.init()
REd = colorama.Fore.RED
RESET = colorama.Fore.RESET

imagename = sys.argv[1]

# read the image data using PIL
image = Image.open(imagename)

# extract EXIF data
exifdata = image.getexif()
# iterating over all EXIF data fields
for tag_id in exifdata:
    # get the tag name
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes 
    if isinstance(data, bytes):
        data = data.decode('utf-8').strip()
    print(f"{REd}{tag:30}: {RESET} {data}")
    