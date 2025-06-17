from flask import Flask, render_template, request, jsonify
import cv2
import base64
import numpy as np
import random
from hand_detector import HandGestureDetector

app = Flask(__name__)
detector = HandGestureDetector()

moves = ['rock', 'paper', 'scissors']

def fingers_up(landmarks):
    tips = [4, 8, 12, 16, 20]
    up = []
    if landmarks[tips[0]][0] < landmarks[tips[0] - 1][0]:
        up.append(1)
    else:
        up.append(0)
    for i in range(1, 5):
        if landmarks[tips[i]][1] < landmarks[tips[i] - 2][1]:
            up.append(1)
        else:
            up.append(0)
    return up

def get_gesture(fingers):
    if fingers == [0, 0, 0, 0, 0]:
        return "rock"
    elif fingers == [1, 1, 1, 1, 1]:
        return "paper"
    elif fingers == [0, 1, 1, 0, 0]:
        return "scissors"
    else:
        return "Invalid"

def decide_winner(player, computer):
    if player == computer or player == "Invalid":
        return "Tie"
    if (player == "rock" and computer == "scissors") or \
       (player == "paper" and computer == "rock") or \
       (player == "scissors" and computer == "paper"):
        return "Player"
    return "Computer"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    data = request.json
    img_data = base64.b64decode(data['image'].split(',')[1])
    np_arr = np.frombuffer(img_data, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    landmarks_list = detector.get_hand_landmarks(frame)
    player_gesture = "Invalid"
    if landmarks_list:
        fingers = fingers_up(landmarks_list[0])
        player_gesture = get_gesture(fingers)

    computer_gesture = random.choice(moves)
    winner = decide_winner(player_gesture, computer_gesture)

    return jsonify({
        "player": player_gesture,
        "computer": computer_gesture,
        "winner": winner
    })

if __name__ == '__main__':
    app.run(debug=True,port='8000')
