#!/bin/bash

rm furnituresheet.png
echo "If this makes more than one tilesheet, then change the -tile 8x8 part of the script to have bigger dimensions."
montage item*.png -tile 8x8 -geometry 16x16+0+0 -background transparent itemsheet.png
