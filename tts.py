from pathlib import Path
from openai import OpenAI
import logging
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def text_to_speech(text: str) -> bytes:
    try:
        response = client.audio.speech.create(
            model="tts-1",
            voice="onyx",
            input=text,
        )
        # Return bytes
        return response.content
    except Exception as e:
        logging.error(f"Error in text_to_speech: {e}")
        raise e


if __name__ == "__main__":
    text = "This is some example text."
    audio_bytes = text_to_speech(text)
    with open("output.mp3", "wb") as f:
        f.write(audio_bytes)
