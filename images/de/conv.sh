#!/bin/bash

if [[ -f "./$1.eps" ]]
then
    epstopdf.exe $1.eps $1.pdf
    convert -density 300 -quality 100 $1.pdf $1.png
    echo "Done."
fi


