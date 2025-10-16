from EmotionDetection import emotion_detector

test_cases = {
    "I am glad this happened": "joy",
    "I am really mad about this": "anger",
    "I feel disgusted just hearing about this": "disgust",
    "I am so sad about this": "sadness",
    "I am really afraid that this will happen": "fear"
}

for statement, expected_emotion in test_cases.items():
    result = emotion_detector(statement)
    dominant = result['dominant_emotion']
    print(f"Statement: {statement}")
    print(f"Expected: {expected_emotion}, Got: {dominant}")
    print("PASS" if dominant == expected_emotion else "FAIL")
    print()
