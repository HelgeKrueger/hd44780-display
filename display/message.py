import os
import time

class Message:
    def __init__(self, config):
        self.path = config['messageFolder']
        self.lastupdate = time.time()
        self.message = 'Starting up'
        self.displaytime = config['displayTime']

        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def get_message(self):

        if time.time() - self.lastupdate > self.displaytime:
            self.message = self.get_current_message_from_file()
            if self.message:
                self.lastupdate = time.time()

        return self.message


    def get_current_message_from_file(self):
        oldest_file = self._get_oldest_file()
        if not oldest_file:
            return ''
        f = open(self._get_path_for_file(oldest_file))
        line = f.readline()
        f.close()
        os.remove(self._get_path_for_file(oldest_file))
        return line.rstrip()

    def _get_path_for_file(self, fileName):
        return self.path + '/' + fileName;

    def _get_oldest_file(self):
        ls = self.sorted_ls(self.path)
        if len(ls) == 0:
            return
        return ls[0]

    def sorted_ls(self, path):
        mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
        return list(sorted(os.listdir(path), key=mtime))
