from flask import Flask

from endpoints.SerieA import SerieA_bp
from endpoints.SerieB import SerieB_bp
from endpoints.SerieC import SerieC_bp
from endpoints.SerieD import SerieD_bp

app = Flask(__name__)

# Registro dos Blueprints
app.register_blueprint(SerieA_bp)
app.register_blueprint(SerieB_bp)
app.register_blueprint(SerieC_bp)
app.register_blueprint(SerieD_bp)

if __name__ == "__main__":
    app.run(debug=True)