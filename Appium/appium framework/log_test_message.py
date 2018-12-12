import datetime

import os

from log_config import LogConfig


def delete(source):
    config = LogConfig()
    if (config.deleteLog):
        try:
            fullFileName = source.replace('.py', '_log.txt')
            os.remove(fullFileName)
        except Exception as ex:
            print(ex)


def log(source, function, description):
    try:
        fullFileName = source.replace('.py', '_log.txt')
        logFile = open(fullFileName, 'a')

        time = datetime.datetime.now().strftime("%H_%M_%S_%B_%d_%Y")
        message = time + ' - ' + function + ' - ' + description
        print(message)
        message += '\n'
        logFile.write(message)

        logFile.close()
    except Exception as ex:
        print(ex)


def logFnEntryExit(source, function, description):
    config = LogConfig()
    if (config.logLevel < 10):
        return

    log(source, function, description)


def logProgress(source, function, description):
    config = LogConfig()
    if (config.logLevel < 5):
        return

    log(source, function, description)


def logError(source, function, description):
    config = LogConfig()
    if (config.logLevel == 0):
        return

    log(source, function, description)


def logException(source, function, exception):
    config = LogConfig()
    if (config.logLevel == 0):
        return

    log(source, function, str(exception))

