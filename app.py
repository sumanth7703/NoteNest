from flask import Flask, request, jsonify
from services.note_service import NoteService

app = Flask(__name__)
note_service = NoteService()

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(note_service.get_all_notes())

@app.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    note = note_service.get_note_by_id(note_id)
    if note:
        return jsonify(note)
    return jsonify({'error': 'Note not found'}), 404

@app.route('/notes', methods=['POST'])
def create_note():
    data = request.get_json()
    new_note = note_service.create_note(data)
    return jsonify(new_note), 201

@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    data = request.get_json()
    updated_note = note_service.update_note(note_id, data)
    if updated_note:
        return jsonify(updated_note)
    return jsonify({'error': 'Note not found'}), 404

@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    success = note_service.delete_note(note_id)
    if success:
        return jsonify({'message': 'Note deleted'})
    return jsonify({'error': 'Note not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
