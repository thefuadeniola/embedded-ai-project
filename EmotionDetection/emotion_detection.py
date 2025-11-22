import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 400:
        return { 
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)
    
    emotion_dict = formatted_response["emotionPredictions"][0]["emotion"]

    dominant_emotion = ""
    emotion_score = 0

    for key, value in emotion_dict.items():
        if value > emotion_score:
            emotion_score = value
            dominant_emotion = key
    
    emotion_dict['dominant_emotion'] = dominant_emotion
    return emotion_dict


