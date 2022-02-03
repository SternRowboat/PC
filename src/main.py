import logging

import app
from dynaconf import Dynaconf


if __name__ == '__main__':
    conf = Dynaconf(settings_file="settings.toml", lowercase_read=True)
    logging.basicConfig(filename=conf.filename,
                        level=conf.level,
                        format=conf.format,
                        filemode=conf.filemode)
    logging.info(f'Hello, log level is {str(conf.level)}')
    app.do()
    print("Congrats, it ran till the end!")
