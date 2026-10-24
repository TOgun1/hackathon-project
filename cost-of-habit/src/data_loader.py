import json
from pathlib import Path

def load_presets():
    path = Path("data/presets.json")
    if not path.exists():
        return []
    
    with open(path, "r") as f:
        return json.load(f)
