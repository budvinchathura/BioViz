from flask import Flask

from PairAlign import pair_align_bp

app = Flask(__name__)
app.register_blueprint(pair_align_bp, url_prefix='/pair')


if __name__ == "__main__":
    app.run(port=4000, debug=True)
