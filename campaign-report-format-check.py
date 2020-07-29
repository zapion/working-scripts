import re
from argparse import ArgumentParser

HEADER = "H {7}\\d{8}3 {9}"
DATA = "D\\d{7}.{10}.{60}\\w{12} {8}\\d{14}[01][0-9 ]{20}[0-9 ]{20}[0-9 ]{20}[0-9 ]{20}[0-9 ]{20}[0-9 ]{20}[0-9 ]{20}[0-9 ]{20}[0-9 ]{20}[0-9 ]{20}[0-9 ]{20}[0-9 ]{20}[0-9 ]{20}[0-9 ]{20}[0-9 ]{20}[0-9 ]{20}[0-9 ]{20}[0-9 ]{20}[0-9 ]{20}[0-9 ]{20}\\d{2}\\d{8}"
TAIL = "T {7}\\d{9}"


parser = ArgumentParser()
parser.add_argument("-f", "--file", help="input file of campaign report", dest="cp_file")

opt = parser.parse_args()
if not opt.cp_file:
    raise Exception("No input file")

lines = []
error = []
with open(opt.cp_file) as fh:
    lines = fh.readlines()

if not re.match(HEADER, lines[0]):
    error.append("header line error")

for index, data_line in enumerate(lines[1:-1]):
    if not re.match(DATA, data_line):
        error.append("data line error, line no.{}".format(index + 1))

if not re.match(TAIL, lines[-1]):
    error.append("tail line error")

if error:
    print("\n".join(error))
else:
    print("Parsed successfully. No format error found.")
