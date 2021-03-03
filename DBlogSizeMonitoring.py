#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

log_path = "E:\\app\\Administrator\\diag\\tnslsnr\\DATABASE\\listener\\trace\\listener.log"
size = 3800


class DBlogSizeMonitoring:
    def __init__(self, log_path, size):
        self.log_path = log_path
        self.size = size

    def getSize(self):
        try:
            file_stats = os.stat(self.log_path)

            # print(file_stats)
            size = file_stats.st_size / 1024 / 1024
            size = round(size, 2)
            print("%s文件大小为：%s m" % (self.log_path, size))
            return size

        except FileNotFoundError:
            print("no files found")
            return False

    def reName(self):
        newName = self.log_path + '_'
        os.rename(self.log_path, newName)

    def main(self):
        fileSize = self.getSize()
        if fileSize:
            if fileSize >= self.size:
                self.reName()
                print("Oracle log file is full and rename completed.")
            else:
                print("Oracle log file is not full yet.")


if __name__ == '__main__':
    DBL = DBlogSizeMonitoring(log_path, size)
    DBL.main()

