import webrtcvad
import pyaudio
import wave


class Recorder:
    # 録音のパラメータ設定
    CHUNK = 480
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    WAVE_OUTPUT_FILENAME = "output.wav"

    def __init__(self) -> None:
        pass

    def init(self):
        self.vad = webrtcvad.Vad(3)
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            frames_per_buffer=self.CHUNK
        )

    def execute(self, export_name=WAVE_OUTPUT_FILENAME):
        self.init()
        frames = []
        silent_frames = 0
        has_voice = False

        while True:
            data = self.stream.read(self.CHUNK)
            if self.vad.is_speech(data, self.RATE):
                print("Speech detected.")
                frames.append(data)
                silent_frames = 0
                has_voice = True
            else:
                print("Silence detected.")
                silent_frames += 1
                if has_voice and silent_frames > 20:
                    break

        print("* done recording")

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

        wf = wave.open(export_name, "wb")
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
