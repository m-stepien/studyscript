class MediaEditor:
    def __init__(self, file_name):
        self.file_name = file_name
        self.TEMP_WAV_NAME = "temp.wav"

    def check_if_file_exist(self):
        pass

    def extract_wav_from_mp4(self):
        subprocess.run([
            "ffmpeg", "-i", self.file_name,
            "-af", "silenceremove=start_periods=1:start_duration=1:start_threshold=-35dB:detection=peak",
            "-acodec", "pcm_s16le", "-ar", "16000", "-ac", "1",
            self.TEMP_WAV_NAME
        ])
    