#!/bin/bash

rm tilesheet.png
montage wardrobe*.png item16_bed.png table*.png safe*.png bath*.png toilet*.png -tile 8x8 -geometry 16x28+0+0 -background transparent tilesheet.png

