#!/usr/bin/env python
# coding: utf-8

import os
import re
import shutil
import imp
import sys

from argparse import ArgumentParser

class FormatException(Exception):
    def __init__(self, files):
        Exception.__init__(self)
        self.files = files

    def __str__(self):
        return "File with format errors: \n" + '\n'.join(self.files)

class CopyMusic:

    def __init__(self):
        self.opt = None
        self.image_cache = dict()
        self.img_ext = ['.jpg', '.jpeg', '.png']
        self.bad_char_re = re.compile(r'[<>:"\|?*]+')
        self.check_format_re = re.compile(r".*/.+/\d{4} .+/\d{2,3} - (\S|\S.*\S)\.mp3$")
        self.temp = '/tmp/car_music'
        self.eyeD3 = imp.load_source('eyed3', '/usr/bin/eyeD3')


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
            if os.path.exists(self.temp):
                shutil.rmtree(self.temp)

            os.makedirs(os.path.join(self.temp, subpath))

            for root, dirs, files in os.walk(path):

                subpath = root[pos:]
                print(subpath)
                dstpath = os.path.join(self.temp, subpath)
                dstpath = self.__clean_path(dstpath)
                if not os.path.exists(dstpath):
                    os.makedirs(dstpath)

                for file in files:
                    if not file.endswith('.mp3'):
                        continue
                    srcfile = "%s/%s" % (root, file)
                    dstfile = "%s/%s" % (dstpath, self.__clean_path(file))
                    print("%s -> %s" % (srcfile, dstfile))
                    shutil.copy(srcfile, dstfile)
                    sys.argv = ['/usr/bin/eyeD3', '--set-encoding=utf16-LE', '--force-update', dstfile]
                    if self.eyeD3.main():
                        raise StandardError("Write tag error: %s" % dstfile)

            for item in os.listdir(self.temp):
                s = os.path.join(self.temp, item)
                d = os.path.join(self.opt.dst, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d)
                else:
                    shutil.copy2(s, d)

    def write_tags(self):
        for path in self.opt.src:
            path = os.path.abspath(path)
            if not os.path.exists(path):
                print ("Path %s not exists. Ignore" % path)

            tracks = []
            error_tracks = []
            # формируем список треков
            for root, dirs, files in os.walk(path):
                for file in files:
                    track_path = "%s/%s" % (root, file)
                    #print (track_path)
                    if self.check_format_re.match(track_path):
                        tracks.append(track_path)
                    else:
                        # если это картинка, то всё нормально
                        ext = os.path.splitext(track_path)
                        if ext[-1] not in self.img_ext:
                            error_tracks.append(track_path)

                if error_tracks:
                    raise FormatException(error_tracks)

        for track in tracks:
            eyed3_opt = ['/usr/bin/eyeD3', '--remove-all', '--set-encoding=utf8']

            # разбиваем на куски
            path_tokens = track.rsplit('/', 3)

            img = self.__find_album_img(path_tokens)
            eyed3_opt.append('--add-image=%s:FRONT_COVER' % img)

            if not self.opt.various:
                eyed3_opt.append('--artist=%s' % path_tokens[1])

            year, album_name = path_tokens[2].split(' ', 1)
            eyed3_opt.append('--year=%s' % year)
            eyed3_opt.append('--set-text-frame=TRDC:%s' % year)
            eyed3_opt.append('--set-text-frame=TYER:%s' % year)
            eyed3_opt.append('--album=%s' % album_name)

            track_id, ignore, track_name = path_tokens[3].split(' ', 2)
            if self.opt.various:
                artist, track_name = track_name.split(' - ', 1)
                eyed3_opt.append('--artist=%s' % artist)

            eyed3_opt.append('--track=%s' % track_id)
            eyed3_opt.append('--title=%s' % track_name.rsplit('.', 1)[0])
            eyed3_opt.append(track)

            sys.argv = eyed3_opt
            self.eyeD3.main()

    def __find_album_img(self, path_tokens):
        cache_key = (path_tokens[1], path_tokens[2])
        if cache_key in self.image_cache:
            return self.image_cache[cache_key]
        basedir = "/".join(path_tokens[:-1])
        for ext in self.img_ext:
            img_path = os.path.join(basedir, "%s%s" % (path_tokens[2], ext))
            if os.path.exists(img_path):
                # кешируем с ключом исполнитель, альбом
                self.image_cache[cache_key] = img_path
                return img_path

        while True:
            str = "Не найдено изображение для %s/%s. Продолжить?" % cache_key
            print(str)
            answer = raw_input().decode(sys.stdin.encoding).lower()
            if answer == "y":
                self.image_cache[cache_key] = ""
                return ""
            elif answer == "n":
                raise "Not fount image for %s/%s" % cache_key
            else:
                continue

    def main(self):
        parser = ArgumentParser(description="Options")
        parser.add_argument('-V', dest='various', action='store_true', help="Various artists")

        group = parser.add_mutually_exclusive_group()
        group.add_argument('-w', dest='write', action='store_true', help=u"Записать ID3 теги")
        group.add_argument('-c', dest='copy', action='store_true', help=u"Скопировать car music")

        parser.add_argument("-a", dest='src', action='append', help='Sources dirs', required=True)
        parser.add_argument("-d", dest='dst', action='store', help='Destination dir')
        parser.add_argument("-b", dest='base', action='store', help='Base music dir')

        self.opt = parser.parse_args()

        if self.opt.write:
            self.write_tags()
            return

        if self.opt.copy:
            if self.opt.dst is None or self.opt.base is None:
                raise "option -b and -d required for option c"
            self.copy()

            return


if __name__ == "__main__":
    try:
        cm = CopyMusic()
        cm.main()
    except FormatException as e:
        print e
