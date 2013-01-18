#!/bin/bash

if [ "$1" == "" ]
then
	echo "Usage: ./retrieve_html.sh <webpage>"
	exit
fi

html_folder="html_folder"

wget -r -Q1G -A *.php,*.html $1

files=`find $1/ -exec ls -ld \{\} \; | awk '{print $9}' | grep html` 
co=1
IFS="
"

for file in $files 
do
	name="$html_folder/$co.html"
	cp $file $name 
	co=$((co+1))
done

rm -rf $1
