#coding=utf-8
__author__ = 'destr'

import os
from PyQt5.QtWidgets import QFileSystemModel
from PyQt5 import QtCore
from filecmp import dircmp

class State:
    def __init__(self):
        self.checked = False
        self.path = None


class CheckableFileSystemModel(QFileSystemModel):
    def __init__(self, parent=None):
        QFileSystemModel.__init__(self, parent)
        self.states = dict()
        self.queue = dict()

        self.directoryLoaded.connect(self.__changeChildState)

    def data(self, index, role=None):

        if role == QtCore.Qt.CheckStateRole and index.column() == 0:

            filepath = self.filePath(index)
            return self.__state(filepath)

        return QFileSystemModel.data(self, index, role)

    def setExistingDirs(self, rootdir, dirs):
        for path in dirs:
            musicpath = os.path.join(self.rootPath(), path)
            flashpath = os.path.join(rootdir, path)
            if os.path.isdir(flashpath):
                dcmp = dircmp(flashpath, musicpath)
                if dcmp.right_only:
                    # всем кто выше по пути надо ставить partialcheck
                    self.states[musicpath] = QtCore.Qt.PartiallyChecked
                    subdirpath = self.rootPath()
                    for subdir in path.split("/"):
                        subdirpath = os.path.join(subdirpath, subdir)

                        self.states[subdirpath] = QtCore.Qt.PartiallyChecked
                else:
                    self.states[musicpath] = QtCore.Qt.Checked
            else:
                self.states[musicpath] = QtCore.Qt.Checked

    def setData(self, index, data, role=None):
        if role == QtCore.Qt.CheckStateRole:
            self.__setState(index, data)
            self.__childState(index, data)

            p = index.parent()
            while self.__partialCheck(p) is not None:
                p = p.parent()
            return True

        return QFileSystemModel.setData(index, data, role)

    def flags(self, index):
        return QFileSystemModel.flags(self, index) | QtCore.Qt.ItemIsUserCheckable

    def __changeChildState(self, path):
        if path not in self.queue:
            return

        parent = self.index(path)
        state = self.queue.pop(path)
        self.__setChildState(parent, state)

    def __setChildState(self, parent, state):
        for row in range(0, self.rowCount(parent)):
            childIndex = self.index(row, 0, parent)
            self.__setState(childIndex, state)
            self.dataChanged.emit(childIndex, childIndex)

            self.__childState(childIndex, state)

    def __partialCheck(self, index):
        statekey = self.filePath(index)
        if self.rootPath() == statekey:
            return None
        state = None

        for row in range(0, self.rowCount(index)):
            childIndex = self.index(row, 0, index)
            statekey = self.filePath(childIndex)
            if row == 0:
                state = self.__state(statekey)

            if state != self.__state(statekey) :
                state = QtCore.Qt.PartiallyChecked
                break

        self.__setState(index, state)
        self.dataChanged.emit(index, index)

        return state

    def __childState(self, parent, data):
        if self.canFetchMore(parent):
            self.queue[self.filePath(parent)] = data
            self.fetchMore(parent)
            return

        # уже загружено?
        if self.rowCount(parent):
            self.__setChildState(parent, data)
        return

    def __state(self, key):

        if key in self.states:
            return self.states[key]

        return QtCore.Qt.Unchecked

    def __setState(self, index, data):
        filename = self.filePath(index)
        if data == QtCore.Qt.Unchecked:
            self.states.pop(filename, None)
        else:
            self.states[filename] = data


