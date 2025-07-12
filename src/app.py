from flask import Flask, render_template, request

from src.config import settings
from src.message import UserMessage, send_message

app = Flask(
    import_name=settings.APP_NAME,
    template_folder=settings.TEMPLATES_DIR,
    static_folder=settings.STATIC_DIR,
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_form', methods=['POST'])
def send_form():
    if request.method == 'POST':
        msg = UserMessage(**request.form)
        send_message(msg)
        return {"message": "successful"}

if __name__ == '__main__':
  app.run(debug=True)