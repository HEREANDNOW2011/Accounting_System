import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Read CSV data and store it in a list
def read_csv_data():
    data = []
    with open('accounting_system.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

# Route for displaying the accounting data
@app.route('/')
def index():
    csv_data = read_csv_data()
    return render_template('index.html', csv_data=csv_data)

# Route for adding a new entry
@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    if request.method == 'POST':
        date = request.form['date']
        reason = request.form['reason']
        amount = request.form['amount']
        remarks = request.form['remarks']
        new_entry = [date, reason, amount, remarks]
        data = read_csv_data()
        data.append(new_entry)
        with open('accounting_system.csv', mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(data)
        return redirect('/')
    return render_template('add.html')

# Route for editing an entry
@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_entry(index):
    data = read_csv_data()
    entry = data[index]
    if request.method == 'POST':
        entry[0] = request.form['date']
        entry[1] = request.form['reason']
        entry[2] = request.form['amount']
        entry[3] = request.form['remarks']
        with open('accounting_system.csv', mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(data)
        return redirect('/')
    return render_template('edit.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)
