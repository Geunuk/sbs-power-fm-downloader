class Episode():
    def __init__(self, date, name, url):
        self.date = date
        self.name = name
        self.url = url
        self.file_name = self.date.strftime("%y%m%d ") + self.name
        self.is_downloaded = False

    def __str__(self):
        string = ""
        string += "Date: " + str(self.date) + '\n'
        string += "Name: " + self.name + '\n'
        string += "URL: " + self.url + '\n\n'
        return string

    def download(self):
        print("Download...")