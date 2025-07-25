"""
Run the app with the built-in server for local development only.
"""
from app import create_app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5050, debug=True)

