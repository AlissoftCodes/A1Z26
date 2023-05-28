# -*- coding: utf-8 -*-
from unidecode import unidecode


def text_to_a1z26(text: str) -> str:
	"""
	Converts plaintext into A1Z26 code.
	Example: a1z26_to_text('hello, world!')
	Output: 8-5-12-12-15, 23-15-18-12-4!
	"""

	text = text.strip()
	if text:
		new_text = ''

		for i in unidecode(text).upper().strip():

			if i.isalpha():
				new_text += str(ord(i) - 64) + '-'
			else:
				new_text = new_text[:-1] + i + '-'

		new_text = new_text[:-1] if new_text[-1] == '-' else new_text

		return new_text.replace(' -', ' ').strip()

	return ''


def a1z26_to_text(text):
	"""
	Converts A1Z26 code into plaintext.
	Example: text_to_a1z26('8-5-12-12-15, 23-15-18-12-4!')
	Output: HELLO, WORLD!
	"""

	text = text.strip()
	if text:
		transformed = []
		
		for word in text.split():
			for char in word.split('-'):
				cache = []
				if char.isnumeric() and 0 < int(char) < 27:
					transformed.append(chr(int(char)+64))
				else:
					for c in char:
						if c.isnumeric() and len(cache) > 0 and cache[-1].isnumeric():
							cache[-1] += c
						elif c.isnumeric():
							cache += [c]
						else:
							cache += c

					for i in cache:
						if i.isnumeric() and 0 < int(i) < 27:
							transformed.append(chr(int(i) + 64))
						else:
							transformed.append(i)

			transformed.append(' ')

		return ''.join(transformed).strip()

	return ''
