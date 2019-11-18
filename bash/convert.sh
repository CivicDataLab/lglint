#!/bin/bash
cd /home/akhilesh/cdl/lgl/processed_posco/Bihar/txts/

for filename in *.txt; do
    cat "$filename" | xargs >> /home/akhilesh/cdl/lgl/processed_posco/Bihar/new/"$filename"
    # sed 'N;N;N; s/\n/ /g' "$filename" > /home/akhilesh/cdl/lgl/processed_posco/Bihar/new/"$filename"
done
