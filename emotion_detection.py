import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}

    # handle blank input
    if not text_to_analyze or not str(text_to_analyze).strip():
        return {
            'anger': None, 'disgust': None, 'fear': None,
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }

    resp = requests.post(url, headers=headers, json=payload)

    # if API rejects (e.g., blank), return Nones
    if resp.status_code == 400:
        return {
            'anger': None, 'disgust': None, 'fear': None,
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }

    data = json.loads(resp.text)

    # your lab returns flat scores here:
    emotions = data["emotionPredictions"][0]["emotion"]

    result = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
    }
    result['dominant_emotion'] = max(result, key=result.get)
    return result
