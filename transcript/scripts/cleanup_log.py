#!/usr/bin/env python3
"""
Clean up Whisper transcription log by removing progress bars and keeping only
timestamped transcript lines. Automatically detects where the transcript starts.

Usage: python cleanup_log.py <input_file> <output_file>
"""

import sys
import re

def cleanup_log(input_file, output_file):
    """
    Find the first line matching the timestamp pattern and keep all matching lines.
    This handles variable-length audio files (different progress bar lengths).
    """
    timestamp_pattern = re.compile(r'^\[\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}\.\d{3}\]')

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find the first line with a timestamp
    start_idx = None
    for i, line in enumerate(lines):
        if timestamp_pattern.match(line.strip()):
            start_idx = i
            break

    if start_idx is None:
        print("✗ No timestamped lines found in input file")
        sys.exit(1)

    # Keep all lines from first timestamp onwards that match the pattern
    cleaned_lines = [
        line for line in lines[start_idx:]
        if timestamp_pattern.match(line.strip())
    ]

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_lines)

    print(f"✓ Cleaned log: removed first {start_idx} lines (progress bars)")
    print(f"✓ Kept {len(cleaned_lines)} timestamped transcript lines")
    print(f"✓ Saved to: {output_file}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python cleanup_log.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        cleanup_log(input_file, output_file)
    except Exception as e:
        print(f"✗ Error: {e}")
        sys.exit(1)
