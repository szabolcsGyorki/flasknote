from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

@app.route('/')  # Register the 'http://localhost:5000/' route to this function.
def route_index():  # Just a normal function, I named it this way for cleaner code
    note_text = None
    if 'note' in session:
        note_text = session['note']
    return render_template('index.html', note=note_text)


@app.route('/edit-note')  # Registering GET requests sent to 'http://localhost:5000/edit-note' to this function
def route_edit():
    note_text = None
    if 'note' in session:
        note_text = session['note']
    return render_template('edit.html', note=note_text)


@app.route('/edit-note', methods=['POST'])
def route_save():
     print('POST request received!')
     session['note'] = request.form['note']
     return redirect('/')


if __name__ == "__main__":
    app.secret_key = 'test'  # Change the content of this string
    app.run(
        debug=True, # Allow verbose error reports
        port=5000 # Set custom port
    )