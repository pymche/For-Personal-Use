#!/bin/bash

cd /Users/Documents/pandoc-test

created_time=$(date +"%Y%m%d_%H%M%p")
mkdir $created_time

for x in *.docx
do
        x2=${x%%.docx}.md
        Pandoc --extract-media=. $x
        Pandoc -f docx -t markdown $x -o $x2
done

mv *.md $created_time
mv media $created_time
