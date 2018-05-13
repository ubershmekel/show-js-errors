#!/usr/local/bin/python
"""
I usually develop and test on `index.html` then use this script to copy
frome there to `snippet.html`.
"""
# #from lxml import etree, html


html = open("index.html").read()

start_tag = '<!-- start the snippet -->'
end_tag = '<!-- end the snippet -->'

start_index = html.find(start_tag)
end_index = html.find(end_tag)


snippet = html[start_index + len(start_tag):end_index].strip('\r\n')
# pretty print https://stackoverflow.com/questions/6150108/python-how-to-pretty-print-html-into-a-file/16505750#16505750
#document_root = html.fromstring(snippet)
#snippet = etree.tostring(document_root, encoding='unicode', pretty_print=True)

open('snippet.html', 'w').write(snippet)
print("Saved snippet length: %d" % len(snippet))