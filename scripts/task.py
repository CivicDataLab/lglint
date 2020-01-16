import abc


class Task(abc.ABC):

    def __init__(self):
        self.next_task = None
        self.shared_resource = None

    @abc.abstractmethod
    def _execute(self):
        pass

    def execute(self):
        self.share_next(self.shared_resource)
        self._execute()

    def execute_chain(self):
        self.execute()
        self.execute_next()

    def share_next(self, resource):
        if self.next_task is not None:
            self.next_task._set_shared_resource(resource)
        return

    def _set_shared_resource(self, resource):
        self.shared_resource = resource

    def execute_next(self):
        if self.next_task is not None:
            self.next_task.execute_chain()
        return

    def add_next(self, task):
        self.next_task = task
