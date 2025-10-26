# Import dependencies
from flask import Flask
from app.routes.address_routes import address_bp
from app.routes.health_routes import health_bp

def create_app():
    # Initialize app
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False  # keep UTF-8 in JSON

    # Register routes
    app.register_blueprint(health_bp)
    app.register_blueprint(address_bp)

    return app

if __name__ == '__main__':
    # Run in debug mode for local dev
    app = create_app()
    app.run(debug=True)
