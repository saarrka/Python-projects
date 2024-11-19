from flask import Flask, render_template, session, request # type: ignore
import random
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


@app.route('/', methods=['GET', 'POST'])
def home():
    if 'target' not in session:
        session['target'] = random.randint(1, 10)
        session['attempted_numbers'] = []

    feedback = None

    if request.method == 'POST':
        if 'new_game' in request.form:
            session.clear()  
            session['target'] = random.randint(1, 20)  
            session['attempted_numbers'] = [] 
            feedback = "New game started!"
        elif 'guess' in request.form:
            try:
                guessed_num = int(request.form['guess'])
            except ValueError:
                feedback = "Please select a valid number!"
                return render_template(
                    'index.html',
                    feedback=feedback,
                    attempted_numbers=session.get('attempted_numbers', []),
                )

            
            if guessed_num in session['attempted_numbers']:
                feedback = f"You already tried {guessed_num}!"
            else:
                session['attempted_numbers'].append(guessed_num)
                session.modified = True

                if guessed_num == session['target']:
                    feedback = "Congratulations, you guessed my number! Click New Game to play again."
                elif guessed_num > session['target']:
                    feedback = f"My number is smaller than {guessed_num}. Try again!"
                else:
                    feedback = f"My number is greater than {guessed_num}. Try again!"

    return render_template(
        'index.html',
        feedback=feedback,
        attempted_numbers=session.get('attempted_numbers', []),
    )


if __name__ == '__main__':
    app.run(debug=True)
