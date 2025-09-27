from models.note import Note
from utils.file_handler import read_notes, write_notes

class NoteService:
    def __init__(self):
        self.notes = read_notes()

    def get_all_notes(self):
        return self.notes

    def get_note_by_id(self, note_id):
        return next((note for note in self.notes if note['id'] == note_id), None)

    def create_note(self, data):
        new_id = max([note['id'] for note in self.notes], default=0) + 1
        note = Note(new_id, data['title'], data['content'])
        self.notes.append(note.to_dict())
        write_notes(self.notes)
        return note.to_dict()

    def update_note(self, note_id, data):
        for note in self.notes:
            if note['id'] == note_id:
                note['title'] = data.get('title', note['title'])
                note['content'] = data.get('content', note['content'])
                write_notes(self.notes)
                return note
        return None

    def delete_note(self, note_id):
        original_len = len(self.notes)
        self.notes = [note for note in self.notes if note['id'] != note_id]
        if len(self.notes) < original_len:
            write_notes(self.notes)
            return True
        return False
