#!/usr/bin/python
# -*- coding: utf8 -*-

import lxml.html
import os
import sys
from bs4 import BeautifulSoup
import codecs
import enchant	


html_folder = "__tmp_html_folder"

#Set valid letters in our language
valid_letters = [unicode(chr(i)) for i in range(97,122)]
valid_letters.append(u'á')
valid_letters.append(u'é')
valid_letters.append(u'í')
valid_letters.append(u'ó')
valid_letters.append(u'ú')
valid_letters.append(u'ñ')

#Set Enchant dict for our language
enchant_dict = enchant.Dict("gl_ES")

#Auxiliar functions...
def get_words_text (s):
	if s == "":
		return u""
	soup = BeautifulSoup(s)
	for st in soup("script"):
		st.extract()
	
	text = lxml.html.fromstring(soup.renderContents()).text_content()
	
	text = "".join(["\n" if a not in valid_letters else a for a in text.lower()])
	return [a for a in text.split("\n") if a != ""]

def word_distribution(freqs):
	dic_freq = {}
	for f in freqs:
		if f in dic_freq.keys():
			dic_freq[f] = dic_freq[f] + 1
		else:
			dic_freq[f] = 1

	initial_value = 0
	i = 0
	wei = 254
	counter = 0
	x = 0

	dic_freq2 = {}
	for f in sorted(dic_freq.keys(),reverse=True):
		i = i + 1
		if dic_freq[f] < 5 and initial_value < 100:
			dic_freq2[f] = 255
			initial_value = initial_value + dic_freq[f]
			continue
		elif x == 0:
			x = (len(dic_freq) - 10 - i + 1) / 245 + ((len(dic_freq) - 10 - i + 1) % 245 == 0)

		elif i > len(dic_freq) - 10:
			x = 1

		if(counter == x):
			counter = 0
			wei = wei -1
		dic_freq2[f] = wei
		counter = counter +1

	return dic_freq2

if len(sys.argv) == 1:
	print("Usage ./create_dict <web> <web> <...>")
	sys.exit()

os.mkdir("./" + html_folder)

#Download webs
for web in sys.argv[1:]:
	print("Descargando webs de " +  web)

	os.system("wget -r -nd -Q1G -A *.php,*.html -P " + html_folder + " "  + web + " | grep saved")

#Get list of words
list_of_words = []
for fname in os.listdir(html_folder):
	ffile = open(html_folder + "/"  + fname,"r")
	list_of_words = list_of_words + get_words_text(ffile.read())
	ffile.close()

os.removedirs("./" + html_folder)

#Get frequency (using a Python dictionary)
dic_words = {}
for word in list_of_words:
	if word in dic_words.keys():
		dic_words[word] = dic_words[word] + 1
	else:
		dic_words[word] = 1

#Check spell and unfold dictionary.
words_freq = [(word,dic_words[word]) for word in dic_words.keys() if enchant_dict.check(word)]

#Sort words.
words = sorted(words_freq, key=lambda line: line[1], reverse=True)

#Calculate frequencies
wd =  word_distribution([b for (a,b) in words])

#Print result
fout = codecs.open("dict.xml","w","utf8")
fout.write("<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n<wordlist>")
fout.write("\n".join([u"\t<w f=\"" + unicode(wd[freq]) + u"\">" + word + u"</w>" for (word,freq) in words]))
fout.write("\n</wordlist>")
fout.close()
