import uuid

from storage import Storage


class Note:
    """A note with view and like counters, saved in Storage."""

    def __init__(self):
        self.storage = Storage()

    def create(self, title, content=""):
        title = title.strip()
        if not title or len(title) > 100:
            raise ValueError("Title is required and must be 1-100 characters.")
        note_id = uuid.uuid4().hex
        self.storage.save({"id": note_id, "title": title, "content": content, "views": 0, "likes": 0})
        return note_id

    def get(self, note_id):
        note = self.storage.get(note_id)
        if note is None:
            raise KeyError("Note not found.")
        return note

    def open(self, note_id):
        note = self.get(note_id)
        note["views"] += 1
        return note

    def edit(self, note_id, title, content):
        note = self.get(note_id)
        note["title"] = title.strip() or note["title"]
        note["content"] = content
        return note

    def like(self, note_id):
        note = self.get(note_id)
        note["likes"] += 1
        return note

    def delete(self, note_id):
        self.get(note_id)
        self.storage.delete(note_id)

    def list_all(self):
        return self.storage.all()

math=Note.creat("riazi","x+y=10")