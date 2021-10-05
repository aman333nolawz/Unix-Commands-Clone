#!/usr/bin/env python3
import argparse
from pathlib import Path
from typing import Union

from PIL import Image, UnidentifiedImageError

from exiftags import GPSTAGS, TAGS
from image_tags import (
    color_spaces,
    components_configurations,
    directions,
    flash_values,
    gps_processing_mehods,
    light_source_values,
    metering_modes,
    orientations,
    resolution_units,
    sensing_methods,
    y_cb_cr_positionings,
)
import filetype

parser = argparse.ArgumentParser(description="Display printable strings in file.")
parser.add_argument(
    "filename", type=str, help="Filename of the file you want to get the exif data."
)
args = parser.parse_args()

file = Path(args.filename)
file_stats = file.stat()
file_kind = filetype.guess(args.filename)
file_mime, file_ext = file_kind.mime, file_kind.extension

def sizeof_fmt(num, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


def octal_to_string(octal):
    permission = ["---", "--x", "-w-", "-wx", "r--", "r-x", "rw-", "rwx"]
    result = ""
    # Iterate over each of the digits in octal
    for ___ in [int(n) for n in str(octal)]:
        result += permission[___]
    return result


print(f"{'File Name'.ljust(32)}: {file.name}")
print(f"{'Directory'.ljust(32)}: {file.parent}")
print(f"{'File Size'.ljust(32)}: {sizeof_fmt(file_stats.st_size)}")
print(
    f"{'File Permissions'.ljust(32)}: {octal_to_string(oct(file_stats.st_mode)[-3:])}"
)
print(f"{'File Type'.ljust(32)}: {file_mime.split('/')[-1].upper()}")
print(f"{'File Extension'.ljust(32)}: {file_ext}")
print(f"{'MIME Type'.ljust(32)}: {file_mime}")


def get_img_exif(filename):
    img = Image.open(filename)
    if not img._getexif():
        return
    exif = {TAGS[key]: value for key, value in img._getexif().items() if key in TAGS}
    exif = {k: v for k, v in sorted(exif.items(), key=lambda item: item[0])}

    for key, data in exif.items():
        to_print = ""
        if key.lower() == "gps info":
            # print("----------------GPS INFO----------------")
            for k, v in data.items():
                gps_key = GPSTAGS[k]
                gps_val = v
                if gps_key.lower() == "gps altitude ref":
                    gps_val = "Below Sea Level" if gps_val[0] else "Above Sea Level"
                elif gps_key.lower() == "gps time stamp":
                    gps_val = ":".join(str(int(i)) for i in gps_val)
                elif gps_key.lower() == "gps processing method":
                    gps_val = gps_val.decode()
                    for option in gps_processing_mehods:
                        if option in gps_val:
                            gps_val = option
                elif gps_key.lower() in ["gps latitude ref", "gps longitude ref"]:
                    gps_val = directions[gps_val.upper()]
                elif gps_key.lower() in ["gps latitude", "gps longitude"]:
                    gps_val = f"{int(gps_val[0])} deg {int(gps_val[1])}' {gps_val[2]}\""
                elif type(v) in (tuple, list):
                    gps_val = ",".join(str(i) for i in v)
                elif type(v) == bytes:
                    gps_val = v.decode()

                to_print += f"{gps_key.ljust(32)}: {gps_val}\n"
            to_print = to_print.strip()
            # print("-----------------------------------------")
        elif key.lower() == "color space":
            color_space = color_spaces.get(int(data), ".")
            to_print = f"{key.ljust(32)}: {color_space}"
        elif key.lower() == "components configuration":
            to_print = f"{key.ljust(32)}: {', '.join(components_configurations[i] for i in data)}"
        elif key.lower() == "orientation":
            orientation = orientations.get(int(data), ".")
            to_print = f"{key.ljust(32)}: {orientation}"
        elif key.lower() == "resolution unit":
            resolutions_unit = resolution_units.get(int(data), ".")
            to_print = f"{key.ljust(32)}: {resolutions_unit}"
        elif key.lower() == "y cb cr positioning":
            positioning = y_cb_cr_positionings.get(int(data), ".")
            to_print = f"{key.ljust(32)}: {positioning}"
        elif key.lower() == "metering mode":
            metering_mode = metering_modes.get(int(data), ".")
            to_print = f"{key.ljust(32)}: {metering_mode}"
        elif key.lower() == "sensing method":
            sensing_method = sensing_methods.get(int(data), "Unknown (0)")
            to_print = f"{key.ljust(32)}: {sensing_method}"
        elif key.lower() == "white balance":
            white_balance = "Manual" if int(data) else "Auto"
            to_print = f"{key.ljust(32)}: {white_balance}"
        elif key.lower() == "light source":
            light_source = light_source_values.get(int(data), ".")
            to_print = f"{key.ljust(32)}: {light_source}"
        elif key.lower() == "flash":
            flash = flash_values.get(int(data), ".")
            to_print = f"{key.ljust(32)}: {flash}"
        elif key.lower() == "focal length in35mm film":
            to_print = f"{key.ljust(32)}: {data} mm"
        elif type(data) == bytes:
            to_print = f"{key.ljust(32)}: {data.decode()}"
        else:
            to_print = f"{key.ljust(32)}: {data}"

        print(to_print)

def get_zip_exif(filename):
    pass

try:
    if file_mime.split('/')[0] == "image":
        get_img_exif(args.filename)
    elif file_mime.split('/')[-1] == "zip":
        get_zip_exif(args.filename)

except UnidentifiedImageError as e:
    print(f"{'Error'.ljust(32)}: Unknown file type")
