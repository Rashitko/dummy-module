from up.base_started_module import BaseStartedModule


class DummyModule2(BaseStartedModule):
    def _execute_start(self):
        super()._execute_start()
        self.logger.debug("Dummy2 Starting")
        return True

    def _execute_initialization(self):
        super()._execute_initialization()
        self.logger.debug("Dummy2 Initializing")

    def _execute_stop(self):
        super()._execute_stop()
        self.logger.debug("Dummy2 Stopping")

    def load(self):
        return True
