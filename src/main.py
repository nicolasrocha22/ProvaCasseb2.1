from flask import Flask, request
from flask.templating import render_template
import database_class as db

app = Flask(__name__)
main = db.Database()
main.connect_db()


@app.route("/")
def loadHome():
    main.create_table_db()
    return render_template("home.html", viewData=main.show_table_db())


@app.route("/view", methods=["POST"])
def loadView():
    if request.method == "POST" and "insert" in request.form:
        movie_title = request.form["movie_title"]
        movie_code = int(request.form["movie_code"])
        client_name = request.form["client_name"]
        client_id = int(request.form["client_id"])

        main.add_values_db(movie_title, movie_code, client_name, client_id)
        if not main.show_table_db():
            return render_template("view.html", viewWarning="[ERROR]: Unable to fetch data!")
        else:
            return render_template("view.html", viewData=main.show_table_db())
    elif request.method == "POST" and "delete" in request.form:
        client_id = int(request.form["client_id"])

        main.delete_values_db(client_id)
        return render_template("view.html", viewData=main.show_table_db())
    elif request.method == "POST" and "modify" in request.form:
        client_id = int(request.form["client_id"])
        movie_title = request.form["movie_title"]
        movie_code = int(request.form["movie_code"])

        main.modify_values_db(movie_title, movie_code, client_id)
        if not main.show_table_db():
            return render_template("view.html", viewWarning="[ERROR]: Unable to fetch data!")
        else:
            return render_template("view.html", viewData=main.show_table_db())


@app.route("/insert")
def loadInsert():
    return render_template("insert.html", viewData=main.show_table_db())


@app.route("/delete")
def loadDelete():
    return render_template("delete.html", viewData=main.show_table_db())


@app.route("/modify")
def loadModify():
    return render_template("modify.html", viewData=main.show_table_db())


app.run()
