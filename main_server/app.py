from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/select_mess', methods=['POST'])
def select_mess():
    roll_number = request.form.get('roll_number')
    mess = request.form.get('mess')
    if mess == 'first_mess':
        return redirect(f'http://first_mess:81')
    elif mess == 'second_mess':
        return redirect(f'http://second_mess:82')
    elif mess == 'third_mess':
        return redirect(f'http://third_mess:83')
    else:
        return "Invalid mess selection"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
