from up.base_started_module import BaseStartedModule


class DummyModule(BaseStartedModule):
    def _execute_start(self):
        super()._execute_start()
        self.logger.debug("Dummy Starting")
        return True

    def _execute_initialization(self):
        super()._execute_initialization()
        self.logger.debug("Dummy Initializing")

    def _execute_stop(self):
        super()._execute_stop()
        self.logger.debug("Dummy Stopping")
