from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def home():

    return render_template('register.html')

@app.route('/register', methods=['POST'])

def register():

    username = request.form['username']

    password = request.form['password']

    email = request.form['email']

    with open('database.txt', 'a') as file:

        file.write(f'{username},{password},{email}\n')

    return 'Registrasi berhasil!'

if __name__ == '__main__':

    app.run()
    
