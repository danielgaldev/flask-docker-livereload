from flask import Flask
from livereload import Server

def main():
    app = Flask(__name__)

    @app.route("/")
    def root():
        return "Change"

    server = Server(app.wsgi_app)
    server.serve(port=5000, host='0.0.0.0')

if __name__ == "__main__":
    main()
