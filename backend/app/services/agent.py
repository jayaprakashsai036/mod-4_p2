from .memory import MemoryStore

class Agent:
    def __init__(self):
        self.memory = MemoryStore()

    def run(self, user_id: str, message: str):
        context = self.memory.get(user_id)
        if context:
            reply = f"Previous context: {context[-1]}\nCurrent message: {message}"
        else:
            reply = f"Received: {message}"
        self.memory.add(user_id, message)
        return reply, context
