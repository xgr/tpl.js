'''
 * tpl.py
 * python script to convert tpl.js template to bottle.py style.
 *
 * TEMPLATE IS PROTOTYPE
 *
 * Author: Panda Xiong
 * License: MIT
'''

import re
import sys
import codecs


def xlate(s):
    s = re.sub(r"<%=(.+?)%>", r"{{\1}}", s)
    s = re.sub(r"\{\{\W*tpl\.(\w+?)\s*\((.+?)\)\W*\}\}", r"%include \1 **\2", s)
    s = re.sub(r"<%\W*if\s*\((.+?)\)\W*%>", r"%if \1:", s)
    s = re.sub(r"<%\W*else\W*%>", r"%else:", s)
    s = re.sub(r"<%\s*}\s*%>", r"%end", s)
    s = re.sub(r"<%\W*for\s*\(\s*(\w+?)\s+in\s+(\w+?)\s*\)\W*%>", r"%for \1, _ in enumerate(\2):", s)
    s = re.sub(r'<%', r'%', s)
    s = re.sub(r'%>', r'', s)
    print s
    return s


def mktpl(infile, outpath):
    inf = codecs.open(infile+'.html', 'r', 'utf-8')
    tpls = re.findall(r'<script.+?id="tpl\.(\w+?)">(.+?)</script>', inf.read(), re.S)
    inf.close

    for tpl in tpls:
        outname = outpath + '/' + tpl[0] + '.tpl'
        print outname
        outf = codecs.open(outname, 'w', 'utf-8')
        outf.write(xlate(tpl[1]))
        outf.close


if __name__ == '__main__':
    mktpl(sys.argv[1], sys.argv[2])