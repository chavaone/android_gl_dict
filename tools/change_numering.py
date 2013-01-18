#!/usr/bin/python
# -*- coding: utf8 -*-



import re


f = open("words2.txt")
f2 = open("words.xml","w")

f2.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n<wordlist>\n")

text = f.read()

rec_wei = "-1"
peso = 255
change = 0
camb = 3

for line in text.split("\n")[:-1] : 
	(_,wei,pal) = re.split("(\d)+",line)
	if rec_wei != wei:
		rec_wei = wei
		change = (change + 1) % camb 
		if change == (camb - 1):
			peso = peso - 1
		if peso == 15 :
			camb = 2
		if peso == 11:
			camb = 1

	f2.write("\t<w  f=\"" + str(peso) + "\">" + pal[1:] + "</w>\n")

f2.write("</wordlist>")
