#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
FreeCard Kids
vCard QR SVG Generator

Erzeugt einen QR-Code als SVG
für direkten FreeCAD Import.
"""

import segno
import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(PROJECT_DIR, "vcard_qr.svg")
MATRIX_FILE = os.path.join(PROJECT_DIR, "vcard_qr_matrix.py")

from config import (
    CHILD_NAME,
    MOM_PHONE,
    DAD_PHONE,
    QR_SIZE,
    QR_MARGIN
)

def create_qr(vcard):

    return segno.make(
        vcard,
        error="q"
    )

# ==========================
# Name zerlegen
# ==========================

NAME_PARTS = CHILD_NAME.split(" ")

if len(NAME_PARTS) >= 2:
    FIRST_NAME = NAME_PARTS[0]
    LAST_NAME = " ".join(NAME_PARTS[1:])
else:
    FIRST_NAME = CHILD_NAME
    LAST_NAME = ""


# ==========================
# vCard erstellen
# ==========================

VCARD = f"""BEGIN:VCARD
VERSION:3.0
N:{LAST_NAME};{FIRST_NAME}
FN:{CHILD_NAME}
TEL;TYPE=CELL:{MOM_PHONE}
TEL;TYPE=CELL:{DAD_PHONE}
END:VCARD
"""


# ==========================
# QR-Code erzeugen
# ==========================

QR = create_qr(VCARD)


# ==========================
# SVG speichern
# ==========================

QR.save(
    OUTPUT_FILE,
    scale=10,
    border=QR_MARGIN
)

# ------------------------------------------------------------
# Matrix für FreeCAD erzeugen
# ------------------------------------------------------------

MATRIX_FILE = os.path.join(PROJECT_DIR, "vcard_qr_matrix.py")

with open(MATRIX_FILE, "w", encoding="utf-8") as f:

    f.write('"""\n')
    f.write("AUTOMATISCH ERZEUGT\n")
    f.write("Nicht bearbeiten!\n")
    f.write('"""\n\n')

    matrix = list(QR.matrix)

    f.write(f"QR_MODULES = {len(matrix)}\n\n")

    f.write("QR_MATRIX = [\n")

    for row in matrix:

        line = ", ".join(
            "True" if cell else "False"
            for cell in row
        )

        f.write(f"    [{line}],\n")

    f.write("]\n")

# ==========================
# Ausgabe
# ==========================

print("--------------------------------")
print("FreeCard Kids QR erzeugt")
print("--------------------------------")
print("Datei :", OUTPUT_FILE)
print("Name  :", CHILD_NAME)
print("QR    :", QR_SIZE, "mm")
print("Mom   :", MOM_PHONE)
print("Dad   :", DAD_PHONE)
print("--------------------------------")
