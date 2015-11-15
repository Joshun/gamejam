#!/bin/bash

rm tilesheet.png
montage item16_bed.png table*.png safe*.png wardrobe*.png -tile 8x8 -geometry 16x28+0+0 -background transparent tilesheet.png

