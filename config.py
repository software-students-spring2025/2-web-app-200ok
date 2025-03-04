import os
from dotenv import load_dotenv

# Force to load the data in .env
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=dotenv_path, override=True)

DSN = os.getenv("DSN", "mongodb://localhost/new")
PORT = int(os.getenv("PORT", 3000))