from flask import Flask

from PairAlign import pair_align_bp
from Game import game_bp
from MSA import msa_bp
from API_Doc import swaggerui_bp, SWAGGER_URL

app = Flask(__name__)
app.register_blueprint(pair_align_bp, url_prefix='/pair')
app.register_blueprint(game_bp, url_prefix='/game')
app.register_blueprint(msa_bp, url_prefix='/msa')
app.register_blueprint(swaggerui_bp, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    app.run(port=4000, debug=True)
