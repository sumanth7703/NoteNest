import unittest
from services.note_service import NoteService

class TestNoteService(unittest.TestCase):
    def setUp(self):
        self.service = NoteService()
        self.service.notes = []

    def test_create_note(self):
        note = self.service.create_note({'title': 'Test', 'content': 'Content'})
        self.assertEqual(note['title'], 'Test')

    def test_get_note_by_id(self):
        self.service.create_note({'title': 'Test', 'content': 'Content'})
        note = self.service.get_note_by_id(1)
        self.assertIsNotNone(note)

    def test_update_note(self):
        self.service.create_note({'title': 'Old', 'content': 'Old'})
        updated = self.service.update_note(1, {'title': 'New'})
        self.assertEqual(updated['title'], 'New')

    def test_delete_note(self):
        self.service.create_note({'title': 'Delete', 'content': 'Me'})
        success = self.service.delete_note(1)
        self.assertTrue(success)

if __name__ == '__main__':
    unittest.main()
