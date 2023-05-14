import openai
import argparse
import datetime

from recorder import Recorder

USER_INPUT_OUT_DIR = "./output"

def transcribe(audio_file):
    with open(audio_file, "rb") as f:
        transcript = openai.Audio.transcribe("whisper-1", f)
        print(transcript["text"])
    return transcript["text"]

def from_audio_file(audio_file):
    transcribe(audio_file)

def from_user_input():
    recorder = Recorder()
    user_input_filename = datetime.datetime.now().strftime("%Y%m%d_%H%M%S.wav")
    fullpath = f"{USER_INPUT_OUT_DIR}/{user_input_filename}"

    recorder.execute(fullpath)
    transcribe(fullpath)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--audio_file", default="")

    args = parser.parse_args()
    audio_file = args.audio_file

    if audio_file != "":
        from_audio_file(audio_file)
    else:
        from_user_input()
