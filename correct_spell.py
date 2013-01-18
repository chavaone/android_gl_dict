#!/usr/bin/python
# -*- coding: utf8 -*-

import re
import enchant

language = "gl_ES"
fin = "words.txt"
fout = "words2.txt"

d = enchant.Dict(language)

f = open(fin,"r")
words = f.read()
lines = words.split("\n")

f2 = open(fout,"w")

for l in lines:
	w = re.split("\d+ (.+)",l)[1]
	if d.check(w):
		f2.write(l+"\n")

