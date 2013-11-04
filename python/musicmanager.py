#!/usr/bin/env python
# coding: utf-8

import os
import re
import shutil
import imp
import sys

from argparse import ArgumentParser



class CopyMusic :

    opt = None
    def __init__(self):
        self.bad_char_re = re.compile(r'[<>:"\|?*]+')

    def __clean_path(self, path):
        return self.bad_char_re.sub('_', path)

    def copy(self):
        print(self.opt.src)

        for path in self.opt.src:
            path = os.path.abspath(path)
            if not os.path.exists(path):
                print("Path `{1}' not exits. Ignoring".format(path))
                continue

            pos = len(os.path.abspath(self.opt.base)) + 1
            subpath = path[pos:]
            if len(subpath) is 0:
                subpath = "."

            subpath = self.__clean_path(subpath)

            print(subpath)

            # создаём каталог в котором будем создавать дерево
            os.makedirs(os.path.join(self.opt.dst, subpath))

            for root, dirs, files in os.walk(path):

                subpath = root[pos:]
                print(subpath)
                dstpath = os.path.join(self.opt.dst, subpath)
                dstpath = self.__clean_path(dstpath)
                if not os.path.exists(dstpath):
                    os.makedirs(dstpath)

                for file in files:
                    srcfile = "%s/%s" % (root, file)
                    dstfile = "%s/%s" % (dstpath, self.__clean_path(file))
                    print("%s -> %s" % (srcfile, dstfile))
                    shutil.copy(srcfile, dstfile)

            sys.argv = ['--set-encoding=utf16-LE', self.opt.dst]
            eyeD3 = imp.load_source('eyed3', '/usr/bin/eyeD3')
            eyeD3.main()

        pass

    def main(self):
        parser = ArgumentParser(description="Options")
        parser.add_argument('-V', dest='various', help="Various artists")

        parser.add_argument("-a", dest='src', action='append', help='Sources dirs')
        parser.add_argument("-d", dest='dst', action='store', help='Destination dir', required=True)
        parser.add_argument("-b", dest='base', action='store', help='Base music dir', required=True)

        self.opt = parser.parse_args()

        if self.opt.src:
            self.copy()


if __name__ == "__main__":

    cm = CopyMusic()
    cm.main()
