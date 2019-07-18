#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, bs4, glob, uuid

from dateutil.parser import parse
from datetime import datetime

inter_note = "\n\n>S>C>A>R>L>E>T>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>N>O>T>E>S>\n\n"

files = glob.glob("Keep/*.html")

# Prep TXT file
now = datetime.now()
txtfile = "notes_%s.txt" % now.strftime("%d-%m-%Y_%H%M")
txtout = open(txtfile,"w")

txtout.write(inter_note)

for i,file in enumerate(files):
    print(file)
    page = open(file)
    soup = bs4.BeautifulSoup(page.read(), "html.parser")

    # Get title
    if len(soup.select('.title')) == 0:
        title = ''
    else:
        title = soup.select('.title')[0].getText()

    # Parse Content
    html = soup.select(".content")[0]
    # Convert linebreaks
    for br in soup.find_all("br"):
        br.replace_with("\n")

    # Convert check boxes
    content = html.getText().replace(u"\u2610"+'\n','[ ] ')
    content = content.replace(' [ ]','[ ]')
    
    # We could include Web description thanks to Google
    #if desc = soup.select(".chips")[0]:
    #    website_description = desc

    note = {
        "title": title,
        "content": content
    }

    # Make big title in Markdown
    txtout.write("# ")
    if title:
        txtout.write(note['title'].encode('utf-8')+"\n")
    # If we have a list but not title, we do not put any title
    elif '\n' in content:
        txtout.seek(-2, os.SEEK_END)
        txtout.truncate()

    txtout.write(
        note['content'].encode('utf-8') + 
        inter_note
    )
    
print('\n'+'-'*50 + '\nDone! %s notes saved to %s\n' % (len(files), txtfile))