#!/usr/bin/python3

"""
module contains a script that reads stdin line by line and computes metrics
"""

import sys

status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
status_dict = {code: 0 for code in status_codes}
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        split_line = line.split()
        if len(split_line) < 7:
            continue
        if not split_line[6].isdigit():
            continue
        if split_line[5][1:] != "/projects/260":
            continue
        status_code = split_line[8]
        if status_code in status_codes:
            status_dict[status_code] += 1
        total_size += int(split_line[6])
        if line_count % 10 == 0:
            print("File size: {}".format(total_size))
            for code in sorted(status_dict.keys()):
                if status_dict[code] > 0:
                    print("{}: {}".format(code, status_dict[code]))
            print("")

except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for code in sorted(status_dict.keys()):
        if status_dict[code] > 0:
            print("{}: {}".format(code, status_dict[code]))
    print("")