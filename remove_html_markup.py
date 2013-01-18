#!/usr/bin/python
# -*- coding: utf8 -*-


import lxml.html
import os
from bs4 import BeautifulSoup
import codecs

html_folder = "html_files"
txt_folder = "txt_files"

def convertir_a_texto (s):
	if s == "":
		return ""
	soup = BeautifulSoup(s)
	for st in soup("script"):
		st.extract()
	text = lxml.html.fromstring(soup.renderContents()).text_content()
	text = text.lower()
	text = text.replace("."," ")
	text = text.replace(","," ")
	text = text.replace(";"," ")
	text = text.replace(":"," ")
	text = text.replace('"'," ")
	text = text.replace('?'," ")
	text = text.replace("!"," ")
	text = text.replace("-"," ")
	text = text.replace("'"," ")
	return text

for fname in os.listdir(html_folder):
	print("->" + fname + "\n")
	ffile = open(html_files + fname,"r")
	fhtml = ffile.read()
	ffile.close()
	ftext = convertir_a_texto(fhtml)
	fout = codecs.open(txt_folder + "/" + fname + ".txt","w","utf8")
	fout.write(ftext)
	fout.close()
