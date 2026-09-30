import json
from pathlib import Path

class MemoryStore:
    def __init__(self, filename="data/memories.json"):
        self.path = Path(filename)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.path.write_text("{}", encoding="utf-8")

    def load(self):
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except Exception:
            return {}

    def get(self, user_id, limit=5):
        return self.load().get(user_id, [])[-limit:]

    def add(self, user_id, message):
        data = self.load()
        data.setdefault(user_id, []).append(message)
        self.path.write_text(json.dumps(data, indent=2), encoding="utf-8")
