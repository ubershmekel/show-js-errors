#!/usr/local/bin/python
"""
I usually develop and test on `index.html` then use this script to copy
frome there to `snippet.html`.

Note to caculate the min gzip size use:
    html-minifier --minify-js 1 --minify-css 1 --collapse-whitespace snippet.html | gzip | wc
"""
import subprocess

html = open("index.html").read()

start_tag = '<!-- start the snippet -->'
end_tag = '<!-- end the snippet -->'

start_index = html.find(start_tag)
end_index = html.find(end_tag)


snippet = html[start_index + len(start_tag):end_index].strip('\r\n')
# pretty print https://stackoverflow.com/questions/6150108/python-how-to-pretty-print-html-into-a-file/16505750#16505750
#document_root = html.fromstring(snippet)
#snippet = etree.tostring(document_root, encoding='unicode', pretty_print=True)

OUT_FILE = 'snippet.html'
OUT_MIN_FILE = 'snippet.min.html'
open(OUT_FILE, 'w').write(snippet)
print("Saved snippet length: %d" % len(snippet))

subprocess.check_call(
    'html-minifier --minify-js 1 --minify-css 1 --collapse-whitespace ' +
    OUT_FILE + ' > ' + OUT_MIN_FILE, shell=True)
