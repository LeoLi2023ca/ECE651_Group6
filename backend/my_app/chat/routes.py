from flask import request, jsonify, render_template
import re
import uuid
from ..models import db, Student, Tutor, Subject, Student_Post, ChatMessage
from flask import Blueprint
from datetime import date, datetime
import json

chat = Blueprint("chat", __name__)

@chat.route('/get_message', methods=['GET'])
def get_messages():
    sender_username = request.args.get('sender')
    receiver_username = request.args.get('receiver')
    messages = ChatMessage.query.filter(
        ((ChatMessage.sender_username == sender_username) & (ChatMessage.receiver_username == receiver_username)) | ((ChatMessage.sender_username == receiver_username) & (ChatMessage.receiver_username == sender_username))
    ).order_by(ChatMessage.timestamp.asc()).all()
    return jsonify([message.to_dict() for message in messages])

@chat.route('/send_message', methods=['POST'])
def send_message():
    sender_username = request.form['sender']
    receiver_username = request.form['receiver']
    text = request.form['text']
    parent_message_id = request.form['parent_message_id']

    Student_sender = Student.query.filter_by(username=sender_username).first()
    Tutor_sender = Tutor.query.filter_by(username=sender_username).first()
    Student_receiver = Student.query.filter_by(username=receiver_username).first()
    Tutor_receiver = Tutor.query.filter_by(username=receiver_username).first()
    if not Student_sender and not Tutor_sender:
        return jsonify({'error': 'Sender not found'}), 400
    if not Student_receiver and not Tutor_receiver:
        return jsonify({'error': 'Receiver not found'}), 400
    # print('sender:', sender_username, 'receiver:', receiver_username, 'text:', text, 'parent_message_id:', parent_message_id)
    message = ChatMessage(sender_username=sender_username, receiver_username=receiver_username, text=text, parent_message_id=parent_message_id)
    db.session.add(message)
    db.session.commit()
    return jsonify({'message': 'Message sent successfully'}), 200