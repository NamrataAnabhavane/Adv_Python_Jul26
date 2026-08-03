from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

REPORT_DIR = BASE_DIR / "reports"

REPORT_DIR = BASE_DIR / "exports"

REPORT_DIR = BASE_DIR / "logs"

REPORT_DIR.mkdir(exist_ok=True)
EXPORT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)