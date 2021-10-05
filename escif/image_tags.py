gps_processing_mehods = ("GPS", "CELLID", "WLAN", "MANUAL")
directions = {"N": "North", "S": "South", "E": "East", "W": "West"}

color_spaces = {
    0x1: "sRGB",
    0x2: "Adobe RGB",
    0xFFFD: "Wide Gamut RGB",
    0xFFFE: "ICC Profile",
    0xFFFF: "Uncalibrated",
}
components_configurations = {
    0: "-",
    1: "Y",
    2: "Cb",
    3: "Cr",
    4: "R",
    5: "G",
    6: "B",
}
orientations = {
    1: "Horizontal (normal)",
    2: "Mirror horizontal",
    3: "Rotate 180",
    4: "Mirror vertical",
    5: "Mirror horizontal and rotate 270 CW",
    6: "Rotate 90 CW",
    7: "Mirror horizontal and rotate 90 CW",
    8: "Rotate 270 CW",
}
resolution_units = {1: None, 2: "inches", 3: "cm"}
y_cb_cr_positionings = {1: "Centered", 2: "Co-sited"}
metering_modes = {
    0: "Unknown",
    1: "Average",
    2: "Center-weighted average",
    3: "Spot",
    4: "Multi-spot",
    5: "Multi-segment",
    6: "Partial",
    255: "Other",
}
sensing_methods = {
    1: "Monochrome area",
    2: "One-chip color area",
    3: "Two-chip color area",
    4: "Three-chip color area",
    5: "Color sequential area",
    6: "Monochrome linear",
    7: "Trilinear",
    8: "Color sequential linear",
}
light_source_values = {
    0: "Unknown",
    1: "Daylight",
    2: "Fluorescent",
    3: "Tungsten (Incandescent)",
    4: "Flash",
    9: "Fine Weather",
    10: "Cloudy",
    11: "Shade",
    12: "Daylight Fluorescent",
    13: "Day White Fluorescent",
    14: "Cool White Fluorescent",
    15: "White Fluorescent",
    16: "Warm White Fluorescent",
    17: "Standard Light A",
    18: "Standard Light B       ",
    19: "Standard Light C       ",
    20: "D55",
    21: "D65",
    22: "D75",
    23: "D50",
    24: "ISO Studio Tungsten",
    255: "Other",
}
flash_values = {
    0x0: "No Flash",
    0x1: "Fired",
    0x5: "Fired, Return not detected",
    0x7: "Fired, Return detected",
    0x8: "On, Did not fire",
    0x9: "On, Fired",
    0xD: "On, Return not detected",
    0xF: "On, Return detected",
    0x10: "Off, Did not fire",
    0x14: "Off, Did not fire, Return not detected",
    0x18: "Auto, Did not fire",
    0x19: "Auto, Fired",
    0x1D: "Auto, Fired, Return not detected",
    0x1F: "Auto, Fired, Return detected",
    0x20: "No flash function",
    0x30: "Off, No flash function",
    0x41: "Fired, Red-eye reduction",
    0x45: "Fired, Red-eye reduction, Return not detected",
    0x47: "Fired, Red-eye reduction, Return detected",
    0x49: "On, Red-eye reduction",
    0x4D: "On, Red-eye reduction, Return not detected",
    0x4F: "On, Red-eye reduction, Return detected",
    0x50: "Off, Red-eye reduction",
    0x58: "Auto, Did not fire, Red-eye reduction",
    0x59: "Auto, Fired, Red-eye reduction",
    0x5D: "Auto, Fired, Red-eye reduction, Return not detected",
    0x5F: "Auto, Fired, Red-eye reduction, Return detected",
}
