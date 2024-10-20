from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    user_id = request.form.get('user_id')
    password = request.form.get('password')

    if not user_id or not password:
        flash('User ID and Password are required!', 'error')
        return redirect(url_for('index'))

    # Registration logic here (e.g., save user credentials)
    flash('Registration successful!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
