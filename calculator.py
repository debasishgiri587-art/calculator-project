from flask import Flask, render_template_string, request

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple Calculator</title>
    <style>
        body {
            background-color: black;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: Arial;
        }
        .calculator {
            background: #1e1e1e;
            padding: 20px;
            border-radius: 10px;
            width: 300px;
        }
        input {
            width: 100%;
            height: 50px;
            font-size: 22px;
            margin-bottom: 15px;
            text-align: right;
            background: black;
            color: white;
            border: none;
            padding-right: 10px;
        }
        button {
            width: 60px;
            height: 60px;
            font-size: 18px;
            margin: 5px;
            border: none;
            cursor: pointer;
            background: #2c2c2c;
            color: white;
        }
        .equal {
            background: #ff7f50;
        }
    </style>
</head>
<body>

<div class="calculator">
    <form method="POST">
        <input type="text" name="expression" value="{{ expression }}" readonly>
        <div>
            {% for btn in buttons %}
                <button name="btn" value="{{ btn }}" 
                    {% if btn == '=' %} class="equal" {% endif %}>
                    {{ btn }}
                </button>
                {% if loop.index % 4 == 0 %}<br>{% endif %}
            {% endfor %}
        </div>
    </form>
</div>

</body>
</html>
"""

buttons = [
    "C", "%", "⌫", "/",
    "7", "8", "9", "*",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "00", "0", ".", "="
]

@app.route("/", methods=["GET", "POST"])
def home():
    expression = ""

    if request.method == "POST":
        expression = request.form.get("expression", "")
        btn = request.form.get("btn")

        if btn == "C":
            expression = ""
        elif btn == "⌫":
            expression = expression[:-1]
        elif btn == "=":
            try:
                expression = str(eval(expression))
            except:
                expression = "Error"
        else:
            expression += btn

    return render_template_string(html, expression=expression, buttons=buttons)

if __name__ == "__main__":
    app.run(debug=True)
