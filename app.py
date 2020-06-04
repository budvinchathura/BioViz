from flask import Flask
from flask_cors import CORS
from PairAlign import PAIR_ALIGN_BP
from Game import GAME_BP
from MSA import MSA_BP
from API_Doc import swaggerui_bp, SWAGGER_URL

APP = Flask(__name__)
CORS(APP)

APP.register_blueprint(PAIR_ALIGN_BP, url_prefix='/pair')
APP.register_blueprint(GAME_BP, url_prefix='/game')
APP.register_blueprint(MSA_BP, url_prefix='/msa')
APP.register_blueprint(swaggerui_bp, url_prefix=SWAGGER_URL)


if __name__ == "__main__":
    APP.run(port=4000, debug=True)
