import os
import urllib.request

class Episode():
    def __init__(self, program_name, date, name, url):
        self.program_name = program_name
        self.date = date
        self.name = name
        self.url = url
        self.file_name = self.date.strftime("%y%m%d ") + self.name + ".mp3"
        self.is_downloaded = False

    def __str__(self):
        string = ""
        string += "Date: " + str(self.date) + '\n'
        string += "Name: " + self.name + '\n'
        string += "URL: " + self.url + '\n\n'
        return string

    def download(self):
        print("Downloading...")

        cur_path = os.path.dirname(os.path.abspath(__file__))
        download_dir = os.path.join(cur_path, "downloads")
        if not os.path.exists(download_dir):
            os.mkdir(download_dir)

        download_path = os.path.join(download_dir, self.program_name)
        if not os.path.exists(download_path):
            os.mkdir(download_path)

        file_path = os.path.join(download_path, self.file_name)
        urllib.request.urlretrieve(self.url, file_path)
        print("Download finish")