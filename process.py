from openpyxl import load_workbook
from konlpy.tag import Kkma
from konlpy.tag import Twitter
from collections import Counter
import pandas as pd
import numpy as np
twitter = Twitter()
from konlpy.utils import pprint

wb = load_workbook('test.xlsx')
sheet = wb['Sheet1']

row = 2

sentences = list()

while True:
    text = sheet.cell(row=row, column=2).value

    if not text:
        break

    sentences.append(text)

    row += 1

print(row)
kkma = Kkma()

poslist = list()

sentences_tag = []
for sentence2 in sentences:
    morph = twitter.pos(sentence2)
    sentences_tag.append(morph)
print(len(sentences_tag))


noun_adj_list = []
for sentence3 in sentences_tag:
    for word, tag in sentence3:
        if tag in ['Noun','Adjective']:
            noun_adj_list.append(word)

counts = Counter(noun_adj_list)
print(counts.most_common(5))
test_val = [counts.most_common(5)]
data = pd.DataFrame.from_records(test_val)
data.to_excel('result.xlsx')
