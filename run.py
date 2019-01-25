from app.server import run_app
from app.db import db_up


if __name__ == '__main__':
    db_up()
    run_app(debug=True)
