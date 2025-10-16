# Rock Paper Scissors (Webcam-Based Game)
A real-time Rock Paper Scissors game where the computer picks randomly and the user's move is detected via webcam hand gesture recognition.

# Table of Contents
- Overview
- Features
- Screenshots & Demo
- Tech Stack
- Setup Instructions
- Usage
- Contributing
- License

# Overview
This interactive game lets users play Rock Paper Scissors against the computer. The computer selects its move randomly, while the user's move is captured in real-time using their webcam, thanks to computer vision gesture recognition.

# Features
- Real-time Hand Gesture Detection: Plays based on your webcam feed.
- Random Computer Choices: The computer picks rock, paper, or scissors at random every round.
- Score Tracking: See how many rounds you've won, lost, and drawn.
- Responsive Web Interface: Seamless gameplay experience in your browser.
- Cross-Platform: Works on most computers with a webcam.

# Screenshots & Demo
<img width="2932" height="1606" alt="image" src="https://github.com/user-attachments/assets/1fcc7a0b-089f-4659-9a33-d771f6e225ab" />

<img width="2932" height="1578" alt="image" src="https://github.com/user-attachments/assets/e47a1d57-88f3-42bd-83ac-22fb73d3c120" />

<img width="2758" height="1596" alt="image" src="https://github.com/user-attachments/assets/83a3ecfb-7686-4717-9766-2031b9185185" />


# Tech Stack
- Computer Vision/Backend: Python (OpenCV, Mediapipe or similar for hand gesture recognition)
- Frontend: HTML, CSS, JavaScript
- Integration: Communication between Python backend and frontend (e.g., Flask, WebSockets)

# Setup Instructions
- Clone the Repository: <br>
bash <br>
git clone https://github.com/aishwarya-41/rock_paper_scissor.git <br>
cd rock_paper_scissor

- Install Python Dependencies: <br>
bash <br>
pip install library_names <br>
(Ensure you have OpenCV, Mediapipe, Flask, or other required libraries.)

- Run the Application: <br>
bash <br>
python app.py

- Open the Game: <br>
Open your browser and navigate to http://localhost:5000 (or as directed).

- Allow Webcam Access: <br>
Grant permission when prompted to use your webcam for gesture recognition.

# Usage
- Position your hand (left hand) in front of the webcam and make the rock, paper, or scissors gesture.
- Click the “Play” button to let the system capture your move.
- The computer will pick its move, and the result will be displayed.
- Play multiple rounds and track your score.

# Contributing
Improvements and bug fixes are welcome! Please open an issue or pull request to contribute.

# License
Distributed under the MIT License.
