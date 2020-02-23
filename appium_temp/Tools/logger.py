import logging
import time
import os

class Logger(object):
    def __init__ ( self, name: object = None ) -> object:
        print("logger init!")
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_path = os.path.dirname(os.path.dirname(os.getcwd()))+'\\Logs\\'
        if not os.path.isdir(log_path):
            os.makedirs(log_path)
        log_name = log_path + rq + '.log'

        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        fh.close()
        ch.close()

    def getlog ( self ):
        return self.logger