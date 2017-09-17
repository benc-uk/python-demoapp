import os  
from waitress import serve  
from app import app

print("### Waitress starting on port "+str(os.environ["HTTP_PLATFORM_PORT"]))
serve(app, host="0.0.0.0", port=os.environ["HTTP_PLATFORM_PORT"])  

