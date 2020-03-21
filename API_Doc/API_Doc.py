from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/apidoc'
API_URL = '/static/swaggerDoc.json'
swaggerui_bp = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "BioViz"
    }
)