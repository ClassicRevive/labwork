#!/usr/bin/env python3

''' regex matching variables '''

from re import findall
import sys

date = r"\d{1,2}[/-]\d{1,2}[/-]\d{2}"

phone = r"\b0\d[\s-]\d{7}\b"

email = r"[a-zA-z.]+@[a-z]+(?:.[a-z]+)+"

ldate = r"\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Nov|Dec)\s\d{1,4}"
