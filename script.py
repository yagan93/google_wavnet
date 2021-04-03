# Install and import according modules
!pip3 install transformers
!pip3 install datasets

import requests
import json
import base64
import soundfile as sf
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
from datasets import load_dataset
import IPython.display as display
import librosa
import numpy as np

# Display swiss-german audio file
display.Audio("own_sample.wav", autoplay=True, rate=16000)

# Load swiss-german audio file
audio, rate = librosa.load("own_sample.wav", sr = 16000)

# Download pretrained tokenizer and model from HF
processor = Wav2Vec2Processor.from_pretrained("Yves/wav2vec2-large-xlsr-53-swiss-german")
model = Wav2Vec2ForCTC.from_pretrained("Yves/wav2vec2-large-xlsr-53-swiss-german")

# Passing the audio array to the tokenizer (expect pytorch format tensors)
input_values = processor(audio, return_tensors = "pt").input_values

# Storing non-normalized prediction values as logits
logits = model(input_values).logits

# Storing argmax of logits as prediction
prediction = torch.argmax(logits, dim = -1)

# Let tokenizer decode predictions
transcription = processor.batch_decode(prediction)[0]

# Preparation of GCP API call
url = 'https://texttospeech.googleapis.com/v1/text:synthesize'
json_data = {
  "input": {
    "text": transcription
    },
  "voice": {
    "languageCode": "de-DE",
    "name": "de-DE-Wavenet-A",
    "ssmlGender": "FEMALE"
  },
  "audioConfig": {
    "audioEncoding": "MP3" }
}
# Get your own token with gcloud auth application-default print-access-token
headers = {'content-type': 'application/json; charset=utf-8', "Authorization": "Bearer YOUR_OWN_TOKEN"}

# Execute request
r = requests.post(url, data=json.dumps(json_data).encode("UTF-8"), headers=headers)

# Parse audiContent and save as base64_string
base64_string = r.json()["audioContent"]

# Decode base64_string to .mp3 audio file
with open("audio.mp3", 'wb') as f:
    f.write(base64.b64decode(base64_string))

# Display german audio file
display.Audio("audio.mp3", autoplay=True, rate=16000)
