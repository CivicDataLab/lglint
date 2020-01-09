from scripts.task import Task


class Pipeline(object):
    def __init__(self):
        self._commands = list()

    def add(self, command: Task):
        self._commands.append(command)
        return self

    def execute(self):
        for command in self._commands:
            command.execute()
