# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 21:05:32 2021

@author: TOYGARTANYEL
"""
import re

pattern = '(([\-ŞÖÜÇİĞA-Z0-9]{1,12}[a-z]*?\s*[âşöığüçiŞÖÜÇĞİA-Za-z]*?\s[âşöığüçiŞÖÜĞÇİA-Za-z]*\s*(M\.).*(ÜMRANİYE))|([\-ŞÖÜÇİĞA-Z0-9]{1,12}[a-z]*?\s*[âşöığüçiŞÖÜÇĞİA-Za-z]*?\s[âşöığüçiŞÖÜĞÇİA-Za-z]*\s*(M\.|Mah\.|MAH\.|Mahallesi|MAHALLESİ).*(/\s?İSTANBUL|/\s?İstanbul))|([\-ŞÖÜÇİĞA-Z0-9]{1,12}[a-z]*?\s*[âşöığüçiŞÖÜÇĞİA-Za-z]*?\s[âşöığüçiŞÖÜĞÇİA-Za-z]*\s*((Cad\.|CAD\.|C\.).*(/\s?İSTANBUL|/\s?İstanbul)))|(([\-ŞÖÜÇİĞA-Z0-9]{1,12}[a-z]*?\s*[âşöığüçiŞÖÜÇĞİA-Za-z]*?\s[âşöığüçiŞÖÜĞÇİA-Za-z]*\s*(YER ALTI GEÇİDİ|SONDURAK|SON DURAK|METRO|DURAĞI|İskelesi).*(/\s?İSTANBUL|/\s?İstanbul))))'
line_num = 0
with open('Adresler-rev.txt', encoding='utf8') as f:
    for line in f:
        line_num += 1
        catched = re.findall(pattern, line)
        cleaned = [item[0] for item in catched]
        
        print("Line num {}: Catched pattern: {}".format(line_num, cleaned))