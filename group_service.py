import uuid

from note_service import Note
from storage import Storage


class Group:
    """A topic category that collects note ids, saved in Storage."""

    def __init__(self, notes=None):
        self.storage = Storage()
        # Pass in an existing Note so the group can see the same notes.
        self.notes = notes if notes is not None else Note()

    def create(self, name):
        name = self._check_name(name)
        group_id = uuid.uuid4().hex
        self.storage.save({"id": group_id, "name": name, "note_ids": []})
        return group_id

    def get(self, group_id):
        group = self.storage.get(group_id)
        if group is None:
            raise KeyError("Group not found.")
        return group

    def edit(self, group_id, name):
        group = self.get(group_id)
        group["name"] = self._check_name(name, group_id)
        return group

    def add_note(self, group_id, note_id):
        group = self.get(group_id)
        self.notes.get(note_id)  # raises KeyError if the note does not exist
        if note_id in group["note_ids"]:
            raise ValueError("Note is already in this group.")
        group["note_ids"].append(note_id)
        return group

    def remove_note(self, group_id, note_id):
        group = self.get(group_id)
        if note_id not in group["note_ids"]:
            raise ValueError("Note is not in this group.")
        group["note_ids"].remove(note_id)
        return group

    def delete(self, group_id):
        self.get(group_id)
        self.storage.delete(group_id)

    def list_all(self):
        return self.storage.all()

    def _check_name(self, name, group_id=None):
        """Strip and validate a name, and make sure it is not used by another group."""
        name = name.strip()
        if not name or len(name) > 50:
            raise ValueError("Name is required and must be 1-50 characters.")
        for group in self.storage.all():
            if group["name"] == name and group["id"] != group_id:
                raise ValueError("Group name already exists.")
        return name
