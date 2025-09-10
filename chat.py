class Chat:
    def __init__(self):
        self.history = []

    def add_user_message(self, message):
        self.history.append({"role": "user", "content": message})

    def add_ai_response(self, response):
        self.history.append({"role": "ai", "content": response})

    def get_conversation_history(self):
        return self.history

    def export_history(self):
        return "\n".join([f"{entry['role']}: {entry['content']}" for entry in self.history])