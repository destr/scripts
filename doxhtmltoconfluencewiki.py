#!/usr/bin/env python
# coding: utf-8
#
import lxml.html
import sys
import os
import re
from optparse import OptionParser

def convertcontent(filename):

    doc = lxml.html.parse(filename)
    divs = doc.xpath('/html/body/div[@class="contents"]/div[@class="memitem"]');

    for div in divs:
        tds = div.xpath('div[@class="memproto"]/table/tr/td');
        func = ""
        for td in tds:
            if td.text: 
                func += td.text;

            a = td.xpath("*");
            for el in a :
                if not el.tag == "code":
                    func += " " + el.text
                if el.tag == "em":
                    func += ", "

        ps = div.xpath('div[@class="memdoc"]/p');
        desc = "";
        for p in ps:
            desc += p.text.encode('utf-8');

        args = div.xpath('div[@class="memdoc"]/dl/dd/table/tr');
        argtable = ""
        for arg in args:
            tds = arg.xpath('*')
            argtable += "|"
            for td in tds:
                argtable += td.text + "|"
            argtable += "\n"

#    desc = desc.replace("Замещается в", "");
        desc = desc.replace("Замещает", "");
        func = func.replace(", )", ')');
        print "{{code:language=cpp}}{0}{{code}} {1} \n\n\t\t*Аргументы* \n\n\t\t{2}".format(func.encode('utf-8'), desc, argtable.encode('utf-8'));

def findhtml(htmldir, classname) :
    cre = re.compile('<title>.+?' + classname + '</title>')
    for (root, dirs, files) in os.walk(htmldir):
        for name in files:
            filename = os.path.join(root, name)
            f = open(filename, 'r')
            data = f.read()
            string = str(data)
            f.close()

            if cre.search(string):
                return filename

    raise StandardError("File not found")

if __name__ == "__main__":
    try:
        usage = "Usage %prog [options]"

        parser = OptionParser(usage=usage)
        parser.add_option("-n", "--name", dest="name", help="Doxygen class name",
                metavar="Doxygen class");
        parser.add_option("-H", "--html",  dest="html", help="Html doxygen dir output",
                metavar="Doxygen html");

        (options, args) = parser.parse_args();

        filename = findhtml(options.html, options.name);

        convertcontent(filename)

    except StandardError, e:
        print e
        exit(1)

    exit(0)
