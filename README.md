### HOW TO Google Cloud Text-To-Speech API https://cloud.google.com/text-to-speech

#### Download Google Cloud SDK
https://cloud.google.com/sdk/docs/install

#### Install Google Cloud SDK
./google-cloud-sdk/install.sh

"Modify profile to update your $PATH and enable bash completion?"
Yes

Enter this path to modify:
/Users/YOUR_USERNAME/.bashrc

#### Initialize Google Cloud SDK
./google-cloud-sdk/bin/gcloud init

#### Update PATH for Google Cloud SDK
source /Users/YOUR_USERNAME/google-cloud-sdk/path.zsh.inc

#### Enable zsh completion for gcloud
source /Users/YOUR_USERNAME/google-cloud-sdk/completion.zsh.inc

#### Activate NLP API on GCP and create key
https://console.developers.google.com/apis/api/texttospeech.googleapis.com/overview?project=YOUR_PROJECT_ID

#### Download .json key and adjust reference for glcoud
export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/key.json"

#### Request API to synthesize your given text
curl -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) -H "Content-Type: application/json; charset=utf-8" --data "{
  'input':{
    'text':'Google Cloud Text-to-Speech enables developers to synthesize natural-sounding speech with 100+ voices, available in multiple languages and variants. It applies DeepMind’s groundbreaking research in WaveNet and Google’s powerful neural networks to deliver the highest fidelity possible. As an easy-to-use API, you can create lifelike interactions with your users, across many applications and devices.'
  },
  'voice':{
    'languageCode':'en-gb',
    'name':'en-GB-Standard-A',
    'ssmlGender':'FEMALE'
  },
  'audioConfig':{
    'audioEncoding':'MP3'
  }
}" "https://texttospeech.googleapis.com/v1/text:synthesize"

#### Decode Base64 audioContent to given audioEncoding MP3
base64 --decode source_base64_text_file > dest_audio_file

#### Let python do the magic
script_without_translation (swiss german audio file - german transcription - speech synthesis) 
script_with_translation (swiss german audio file - german transcription - translation - speech synthesis)

#### SOURCES
https://stackoverflow.com/questions/31037279/gcloud-command-not-found-while-installing-google-cloud-sdk
https://gist.github.com/dwchiang/10849350

#### HINTS
https://colab.research.google.com/notebooks/io.ipynb (colab file upload snippets)
