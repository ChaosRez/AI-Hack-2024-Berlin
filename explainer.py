import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting

def explain_photo(prompt, image_base64):
    image_part = Part.from_data(data=base64.b64decode(image_base64), mime_type="image/jpeg")

    generation_config = {
        "max_output_tokens": 8192,
        "temperature": 1,
        "top_p": 0.95,
    }

    safety_settings = [
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
    ]

    vertexai.init(project="aihack24ber-8516", location="europe-west3")
    model = GenerativeModel("gemini-1.5-flash-002")
    responses = model.generate_content(
        [image_part, prompt],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=False,
    )

    return responses.text


# prompt = "explain this photo briefly as you do for a blind person (answer without extra information)"
# image_path = "_archive/IMG_5528.jpeg"
# response_text = explain_photo(prompt, image_path)
# print(response_text)
