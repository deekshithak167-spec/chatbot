from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load scholarship data
scholarships = pd.read_csv('scholarships.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    name = request.form['name']
    percentage = float(request.form['percentage'])
    income = float(request.form['income'])
    category = request.form['category']

    eligible = []

    for index, row in scholarships.iterrows():
        if (
            percentage >= row['Min_Percentage']
            and income <= row['Max_Income']
            and (
                category == row['Category']
                or row['Category'] == 'General'
            )
        ):
            eligible.append(row['Scholarship'])

    return render_template(
        'result.html',
        name=name,
        eligible=eligible
    )

if __name__ == '__main__':
    app.run(debug=True)