class StateManager:
    def __init__(self):
        self.current_goal = None
        self.context = []

    def update_context(self, new_data: dict):
        self.context.append(new_data)
    