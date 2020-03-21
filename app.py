from flask import Flask

from PairAlign import pair_align_bp
from UserGame import game_bp

app = Flask(__name__)
app.register_blueprint(pair_align_bp, url_prefix='/pair')
app.register_blueprint(game_bp, url_prefix='/game')


if __name__ == "__main__":
    app.run(port=4000, debug=True)
