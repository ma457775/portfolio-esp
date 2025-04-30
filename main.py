# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_pressed = None

    if 'button_python' in request.form:
        button_pressed = 'python'
    elif 'button_discord' in request.form:
        button_pressed = 'discord'
    elif 'button_html' in request.form:
        button_pressed = 'html'
    elif 'button_db' in request.form:
        button_pressed = 'db'
    elif 'button_roblox' in request.form:
        button_pressed = 'roblox'

    return render_template('index.html', button_pressed=button_pressed)




if __name__ == "__main__":
    app.run(debug=True)
