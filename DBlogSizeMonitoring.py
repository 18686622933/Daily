import os

log_paths = ["E:\\app\\Administrator\\diag\\tnslsnr\\DATABASE\\listener\\trace\\listener.log",
             "E:\\app\\Administrator\\diag\\rdbms\\ucit\\ucit\\trace\\alert_ucit.log"]

# log_paths = ["C:\\Users\\duomeiti\\Downloads\\python-3.9.2-amd64.exe", "C:\\Users\\duomeiti\\Downloads\\my-new-years-aspirations.pptx"]


size = 3800


class DBlogSizeMonitoring:
    def __init__(self, log_paths, size):
        self.log_paths = log_paths
        self.size = size

    def getSize(self, log_path):
        try:
            file_stats = os.stat(log_path)

            # print(file_stats)
            size = file_stats.st_size / 1024 / 1024
            size = round(size, 2)
            print("《%s》 文件大小为：%s m" % (log_path, size))
            return size

        except FileNotFoundError:
            print("《%s》 文件未找到" % log_path)
            return False

    def reName(self, log_path):
        newName = log_path + '_'
        os.rename(log_path, newName)

    def main(self):
        for i in self.log_paths:
            fileSize = self.getSize(i)
            if fileSize:
                if fileSize >= self.size:
                    self.reName(i)
                    print("File is full and rename completed.")
                else:
                    print("File is not full yet.")


if __name__ == '__main__':
    DBL = DBlogSizeMonitoring(log_paths, size)
    DBL.main()
