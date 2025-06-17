import cv2
import mediapipe as mp

class HandGestureDetector:
    def __init__(self, max_num_hands=1):
        self.hands_module = mp.solutions.hands
        self.hands = self.hands_module.Hands(static_image_mode=False,
                                             max_num_hands=max_num_hands,
                                             min_detection_confidence=0.7)
        self.draw = mp.solutions.drawing_utils


#MediaPipe expects RGB images, but OpenCV gives BGR - convert the webcam frame from BGR -> RGB
    def get_hand_landmarks(self, image):
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result = self.hands.process(img_rgb)
        landmarks_list = []
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                self.draw.draw_landmarks(image, hand_landmarks, self.hands_module.HAND_CONNECTIONS)
                landmarks = []
                for lm in hand_landmarks.landmark:
                    landmarks.append((int(lm.x * image.shape[1]), int(lm.y * image.shape[0])))
                landmarks_list.append(landmarks)
        return landmarks_list #Returns a list of all landmark points for each detected hand




