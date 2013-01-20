Android Galician Keyboard Dictionary
====================================

## Dicionario de galego para teclado de Android (Galego)

Empregando a información [deste post](http://forum.xda-developers.com/showthread.php?t=1027207) en XDA-Developers e uns cuantos scripts que escribín en Python e Bash costruín un dicionario de galego para os nosos teclados en Android.

Para obter as frecuencias das palabras en galego empreguei a paxina de novas [praza.com](http://praza.com).


### Pasos para facer o diccionario

  * Descargar os documentos web. Isto podese facer co script **retrieve_html.sh**. Este script recibe como parametro a paxina web da que queremos sacar as palabras e descarga de forma recursiva (visitando os enlaces que aparecen en cada documento) todas as web ata completar o nivel 5 de forma recursiva ou descargar un xigabyte de información. O script creará unha carpeta de nome html_folder que contera todos os arquivos html descargados.

  * Quitarlle os documentos descargados as etiquetas de html. Para isto podemos empregar o script **remove_html_markup.py** que crea unha carpeta txt_folder na que garda os documentos html da carpeta html_folder quitandolles as etiquetas de html e substituindo guións, puntos, comas e puntos e comas entre outros por espacios.

  * Agora temos que copiar todos os textos que temos a un so arquivo.
  ```bash
  cat `ls` > all.txt
  ```

  * Temos que quitar os elementos dos textos que non sexan palabras.

  ```bash
  cat forum.txt | tr "[:punct:][:blank:][:digit:]" "\n" | grep "^." > unsortedallwordslist.txt
  ```
	 
 * Temos que ordear as palabras por orde de frecuancia de aparición como por orde alfabético. 

  ```bash
  cat allwordslist.txt | tr "A-Z" "a-z" | sort | uniq -c | sort -nr  > words.txt
  ```

  * Antes de meter estas palabras no dicionario debemos asegurarnos de que son correctas. Para isto empregaremos o modulo PyEnchant que ten un dicionario do idioma galego. O script **correct_spell.py** permitenos facer isto.

  * Por ultimo temos que adaptar a lista de palabras a sintaxe do dicionario. Acompañando a cada palabra temos que indicar a frecuencia desta nos textos. A frecuencia midese de 0 a 255, sendo 255 os elementos máis frecuentes. O script **change_numering.py** fai isto. Máis este script esta feito adhoc para esa lista de palabras polo que para empregalo con outra lista hai que cambialo.
