# The 'requests' and 'json' libraries are imported.
# 'requests' is used to send HTTP requests, while 'json' is used for parsing the JSON data that we receive from the API.
from elevenlabs import play
from elevenlabs.client import ElevenLabs
import yaml

# Load the YAML file
with open("_archive/key.yaml", "r") as file:
    config = yaml.safe_load(file)

# Access specific values
API_KEY = config["elevenlabs"]["api_key"]

# input: array of strings
def text_to_speech(texts):
    client = ElevenLabs(
        api_key=API_KEY, # Defaults to ELEVEN_API_KEY
    )
    for txt in texts:
        audio = client.generate(
            text= txt,
            voice="Brian",
            model="eleven_multilingual_v2"
        )
        play(audio)


