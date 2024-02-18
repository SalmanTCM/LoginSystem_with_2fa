from flask.cli import FlaskGroup

from src import app

cli = FlaskGroup(app)


# if __name__ == "__main__":
#     cli()

if __name__ == '__main__':
    app.run(host='192.168.200.98', port=5000, debug=True)