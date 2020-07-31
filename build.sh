#!/bin/bash
#Generates the _site folder and moves its contents to the lieuzhenghong.github.io folder 

rm -rf ./_site/
npx @11ty/eleventy
DESTDIR=../lieuzhenghong.github.io/
rm -rf ../lieuzhenghong.github.io/*
mv -v ./_site/* $DESTDIR 
rm -rf ./_site/
rm -f $DESTDIR/build.sh
echo lieuzhenghong.com > $DESTDIR/CNAME
