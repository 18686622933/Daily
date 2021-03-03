# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

import os

file_name = "E:\\迅雷下载\\Git-2.30.1-64-bit.exe"

file_stats = os.stat(file_name)

# print(file_stats)
size = file_stats.st_size/1024/1024
size =round(size,2)
print(f'File Size in Bytes is {size}')

oldname = file_name
newname = oldname + '_'
os.rename(oldname, newname)

# os.rename(oldname,newname)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
