#### Tools of Trade for Misc Challenge

* [`pdf2txt.py`](https://github.com/euske/pdfminer/blob/master/tools/pdf2txt.py) from [pdfminer project](https://github.com/euske/pdfminer)
	* or `pdftotext` command (yum, apt, brew...)
* 

		$ pdf2txt.py challenge.pdf
		...
		Thanks for buying our super special awesome product, the Foobarnizer 9000!
		Your credentials to the web interface are:

		● Username:​...........................
		● Password: ​CTF{ICanReadDis}

		Note​: For security reasons we cannot change your password. Please store them safely.

* [`tesseract`](https://github.com/tesseract-ocr/tesseract) for OCR
* 
		$ tesseract OCR_is_cool.png OCR_is_cool && cat OCR_is_cool.txt
		Tesseract Open Source OCR Engine v4.0.0 with Leptonica
		Warning: Invalid resolution 0 dpi. Using 70 instead.
		Estimating resolution as 122
		...
		Ynk xgtfiex, axkx' t ebim hy ybex! matm rhn’kx vnkkxgmer Imhkbgz pbma ni:
		hyyanu_ybkfptkx.ubg ‘ChagMK
		BHIM_vkxwxgmbtel.iwy\ \(wxexmsxw\) Pagmxkinmxw
		Yhhutgbsxk9000_Fignte.iwy — Phgmxkinmxw
		yhh.bvh Mnkuh
		...


* [cracker-ng](https://github.com/BoboTiG/cracker-ng) project for zip password cracking
	* [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) wordlist 
* 
		$ cat ~/naive-hashcat/dicts/rockyou.txt | ./zipcracker-ng -f ../../target -

		 ~ ZIP Cracker-ng v2015.02-03 ~
 		 - File......: target
		 * Chosen one: password.txt (32 bytes)
		 - Encryption: standard (traditional PKWARE)
 		 - Method....: stored
 		 - Generator.: STDIN
 		 . Worked at ~ 4782K pwd/sec for ~ 14M tries.
 		 + Password found: asdf
   			HEXA[ 61 73 64 66 ]
		 ^ Ex(c)iting.
