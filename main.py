from flask import Flask, render_template, request

app = Flask(__name__)

# Initial data for the tables
table1_data = [
    {"name": "John Doe", "age": 30},
    {"name": "Jane Smith", "age": 25}
]

table2_data = [
    {"product": "Laptop", "price": 999},
    {"product": "Smartphone", "price": 599}
]

@app.route('/')
def index():
    return render_template('index.html', table1_data=table1_data, table2_data=table2_data)

@app.route('/update', methods=['POST'])
def update():
    global table1_data, table2_data
    table1_data = [
        {"name": request.form['name1'], "age": int(request.form['age1'])},
        {"name": request.form['name2'], "age": int(request.form['age2'])}
    ]
    table2_data = [
        {"product": request.form['product1'], "price": int(request.form['price1'])},
        {"product": request.form['product2'], "price": int(request.form['price2'])}
    ]
    return render_template('index.html', table1_data=table1_data, table2_data=table2_data)

if __name__ == '__main__':
    app.run(debug=True)
