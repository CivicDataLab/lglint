import abc


class Task(object):

    @abc.abstractmethod
    def execute(self):
        pass
