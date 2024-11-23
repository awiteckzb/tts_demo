This contains some example code for using the OpenAI API for text-to-speech.

1. `git clone git@github.com:awiteckzb/tts_demo.git`
2. `cd tts_demo`
3. `pip install python-dotenv openai` 
4. `cp .env_example .env`
5. Add your OpenAI API key to the `.env` file
6. Fill in the text you want to convert to speech in `tts.py`
7. `python tts.py`
8. The output will be in `output.mp3`
