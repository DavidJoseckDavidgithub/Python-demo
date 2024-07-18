from flask import Flask, request, render_template_string
import difflib

app = Flask(__name__)

def is_close_answer(user_answer, correct_answer, threshold=0.7):
    ratio = difflib.SequenceMatcher(None, user_answer.lower(), correct_answer.lower()).ratio()
    return ratio >= threshold

questions = [
        ("Define the function of the print() function?", "output a text or other data to the console"),
        ("What is console in python?", "a command line interpreter that takes input from the user, interprets it and gives the required output"),
        ("Define the function of Import statement?", "loads a module or specific components from a module into the current namespace"),
        ("Define the function of Assignment statements?", "assign values to variables"),
        ("What is the function of if statement in python programming?", "to execute both the true part and false part of a given condition"),
        ("Define the function of else statement in programming?", "to specify what to do if the condition is false"),
        ("Define the function of expression statement in programming?", "to evaluate expression"),
        ("Define the function of conditional statement in programming?", "to execute code based on condition")
        ("Define the function of Looping statement in programming?", "to repeat codes multiple times"),
        ("Define the function definition statement in programming?", "to define reusable functions"),
        ("Define the function of Pass statement in programming?", "placeholder for future codes"),
        ("Define the function of Break and Continue statement in programming?", "to control the flow of loops"),
        ("Define the function of Del statement in programming?", "to delete objects"),
        ("Define the function of Global and Nonlocal statement in programming?", "to modify variable scopes"),
        ("Define the function of Assert statement in programming?", "debugging aid"),
        ("Define the function of With statement in programming?", "to simplify exception handling")
        ]

@app.route('/', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        for i, (question, answer) in enumerate(questions):
            user_answer = request.form.get(f'question_{i}')
            if is_close_answer(user_answer, answer):
                score += 1

        percentage = (score / len(questions)) * 100
        return render_template_string(RESULT_TEMPLATE, score=score, percentage=percentage)

    return render_template_string(QUIZ_TEMPLATE, questions=questions)

QUIZ_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Quiz Game</title>
</head>
<body>
    <h1>Welcome to our quiz game 8th July 2024</h1>
    <form method="post">
        {% for i, (question, _) in enumerate(questions) %}
            <div>
                <label>{{ question }}</label><br>
                <input type="text" name="question_{{ i }}">
            </div>
        {% endfor %}
        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""

RESULT_TEMPLATE = """
<!doctype html
<html>
<head>
    <title>Quiz Results</title>
</head>
<body>
    <h1>Quiz Results</h1>
    <p>You got {{ score }} questions correct!</p>
    <p>Your score: {{ percentage }}%</p>
    {% if score == len(questions) %}
        <p>Congratulations, You won!</p>
    {% else %}
        <p>Failed. Try again. You have to attain 100% for you to win!</p>
    {% endif %}
    <a href="/">Try Again</a>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)
