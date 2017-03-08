from flask import Flask, render_template, request, session, redirect, g, url_for, Blueprint
from db_controller import DB
from controllers.attendances_ctrl import attendances_ctrl



DATABASE = 'data/ccms.db'

app = Flask(__name__)
app.register_blueprint(attendances_ctrl)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = DB.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    pass


if __name__ == "__main__":
    # DB.create_database()
    app.run(debug=True)