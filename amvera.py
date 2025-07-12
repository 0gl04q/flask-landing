from gunicorn.app.base import BaseApplication
from src.app import app

class StandaloneApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.application = app
        self.options = options or {}
        super().__init__()

    def load_config(self):
        for key, value in self.options.items():
            self.cfg.set(key, value)

    def load(self):
        return self.application

if __name__ == '__main__':
    options = {
        "bind": "0.0.0.0:8000",
        "workers": 4,
        "reload": True
    }
    StandaloneApplication(app, options).run()