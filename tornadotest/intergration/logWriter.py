from nb_log import LogManager
import os


class NbLog:
    def __init__(self, task_name="running", file_name="tornadoServer"):
        self.logger = LogManager(task_name).get_logger_and_add_handlers \
            (log_path=os.path.join(os.path.abspath("."), "logs"), log_filename=file_name)

    def error(self, msg):
        return self.logger.error(msg)

    def debug(self, msg):
        return self.logger.debug(msg)

    def info(self, msg):
        return self.logger.info(msg)

    def warning(self, msg):
        return self.logger.warning(msg)

    def critical(self, msg):
        return self.logger.critical(msg)

    def exception(self, msg, exc_info=True):
        return self.logger.exception(msg, exc_info)
