#!/usr/bin/env python3

# Script to rename pdf files to the paper title

import os, sys
import textract 

# get text 
text = textract.process(sys.argv[1])
lines = text.splitlines()

title = lines[0]
title_words = str(title).split("'")[1].split()
title_str = "_".join(title_words)

authors = lines[1].decode()
for ii, author in enumerate(authors.split(',')):
    if ii % 2 == 1 or ii == 0:
        if ii == 0:
            author_title = f'{author.split()[0][0]}.{author.split()[1]}'

# get date
for line in lines:
    if 'Published' in str(line):
        try:
            yearDate = str(line).split()[-1]
        except:
            print("No year found!")

if yearDate:
    print(f'{author_title}_{title}_{yearDate}.pdf')
else:
    print(f'{author_title}_{title}.pdf')