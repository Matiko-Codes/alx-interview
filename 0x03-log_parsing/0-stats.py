#!/usr/bin/env python3
"""
module contains a script that reads stdin line by line and computes metrics
"""

import sys

# Initialize variables
total_size = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}
line_count = 0

# Loop through stdin line by line
for line in sys.stdin:
    # Parse line and extract file size and status code
    fields = line.strip().split(' ')
    if len(fields) != 7:
        continue
    try:
        file_size = int(fields[6])
        status_code = int(fields[5])
    except ValueError:
        continue
    
    # Update variables
    total_size += file_size
    status_codes[status_code] += 1
    line_count += 1
    
    # Print metrics every 10 lines
    if line_count % 10 == 0:
        print(f'Total file size: {total_size}')
        for code in sorted(status_codes.keys()):
            if status_codes[code] > 0:
                print(f'{code}: {status_codes[code]}')
        print()
    
    # Handle keyboard interrupt (CTRL+C)
    try:
        pass
    except KeyboardInterrupt:
        print(f'Total file size: {total_size}')
        for code in sorted(status_codes.keys()):
            if status_codes[code] > 0:
                print(f'{code}: {status_codes[code]}')
        sys.exit(0)

# Print final metrics
print(f'Total file size: {total_size}')
for code in sorted(status_codes.keys()):
    if status_codes[code] > 0:
        print(f'{code}: {status_codes[code]}')
