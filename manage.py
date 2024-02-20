#from flask.cli import FlaskGroup

#from src import app

#cli = FlaskGroup(app)


#if __name__ == "__main__":
#   cli()

#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=8000, debug=True)
from flask.cli import FlaskGroup
from src import app

cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()

