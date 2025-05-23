from flask import Flask
from flask import render_template, request, redirect, url_for


app = Flask(__name__)

counter_id = 1

users = []

@app.route("/")
def index():
    return render_template("home.html", users=users)

# add a product
@app.route('/submit', methods=['POST'])
def submit():
    global counter_id
    prod_name = request.form['name']
    prod_quantity = request.form['age']

    data = {
        "id": counter_id,
        "prodName": prod_name,
        "prodQuantity": prod_quantity,
    }

    counter_id += 1
    users.append(data)
    return render_template("home.html", users=users)

# delete a product
@app.route("/delete/<int:id>", methods=['GET'])
def delete(id):
    global users
    global counter_id

    test = [x for x in users if x['id'] != id]

    users = test

    if len(users) == 0:
        counter_id = 1
        print("All users deleted, resetting or redirecting...")

    return redirect(url_for('index'))


@app.route("/edit/<int:id>")
def edit(id):
    for user in users:
        if user['id'] == id:
            return render_template("edit.html", user=user)
    return "User not found", 404

@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    name = request.form['name']
    quantity = request.form['age']

    for user in users:
        if user['id'] == id:
            user['prodName'] = name
            user['prodQuantity'] = quantity
            break

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)