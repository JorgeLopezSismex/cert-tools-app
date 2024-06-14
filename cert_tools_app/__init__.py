from flask import Flask

def create_app():
    app = Flask(__name__)
    
    #Import and register Blueprints
    from .routes.template_routes import template_bp
    from .routes.unsigned_certificate_routes import unsigned_certificate_bp
    
    app.register_blueprint(template_bp, url_prefix='/templates')
    app.register_blueprint(unsigned_certificate_bp, url_prefix='/unsigned-certificates')
    
    return app