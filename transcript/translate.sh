#!/bin/bash
cd "/Users/apple/Desktop/Claude/projects/Kennzeichen"
source venv/bin/activate

echo "Waiting for transcription to complete..."
while [ ! -f "Denis 8.05.26.txt" ]; do
  sleep 5
done

echo "Transcription done. Starting translation..."
whisper "/Users/apple/Desktop/Denis 8.05.26" --model medium --task translate --output_format txt --output_dir .

echo "✓ Translation complete"
echo "Files saved:"
ls -lh Denis\ 8.05.26* | awk '{print "  " $9 " (" $5 ")"}'
