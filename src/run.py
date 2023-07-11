from app import app
from views.auth.views import auth_bp
from views.main.views import main_bp

app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)

if __name__ == "__main__":
    app.run()
