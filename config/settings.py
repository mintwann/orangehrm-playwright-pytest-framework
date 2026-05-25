import os
from pathlib import Path
from configparser import ConfigParser
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).parent.parent
ENV_PATH = ROOT_DIR / ".env"
INI_PATH = ROOT_DIR / "config" / "config.ini"

# Load environment variables from .env file
load_dotenv(dotenv_path=ENV_PATH)

# Load configuration from config.ini
config = ConfigParser()
config.read(INI_PATH)

class Settings:
    # Environment variables
    BASE_URL = os.getenv("BASE_URL", "")
    ADMIN_USER = os.getenv("ADMIN_USER", "")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")

    # Configuration from config.ini
    DEFAULT_TIMEOUT = config.getint("framework", "default_timeout", fallback=10000)
    HEADLESS = config.getboolean("framework", "headless", fallback=True)
    BROWSER = config.get("framework", "browser", fallback="chromium")
    
    # Target API Endpoints
    LOGIN_API = f"{BASE_URL}/web/index.php/auth/validateCredentials"
    API_EMPLOYEE_URL = f"{BASE_URL}/web/index.php/api/v2/pim/employees"
    