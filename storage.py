class Storage:
    """Keeps notes in memory, keyed by note id."""

    def __init__(self):
        self.data = {}

    def save(self, note):
        self.data[note["id"]] = note

    def get(self, note_id):
        return self.data.get(note_id)

    def all(self):
        return list(self.data.values())

    def delete(self, note_id):
        self.data.pop(note_id, None)
