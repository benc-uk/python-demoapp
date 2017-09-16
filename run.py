import os
from app import app

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 80))
	app.jinja_env.auto_reload = True
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(host='127.0.0.1', port=port)