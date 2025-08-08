from pyannote.audio import Pipeline
import whisper
from pydub import AudioSegment
import io

# Load once (slow)
print("Loading diarization & STT models...")
diarization_pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization")
stt_model = whisper.load_model("base")  # 'small', 'medium', etc.

def process_audio(filepath: str, max_speakers: int = 2):
    diarization = diarization_pipeline(filepath, min_speakers=1, max_speakers=max_speakers)

    segments = []
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        segments.append({
            "start": turn.start,
            "end": turn.end,
            "speaker": speaker
        })
    segments.sort(key=lambda s: s["start"])

    audio = AudioSegment.from_file(filepath)
    results = []
    for seg in segments:
        start_ms = int(seg["start"] * 1000)
        end_ms = int(seg["end"] * 1000)
        chunk = audio[start_ms:end_ms]

        buf = io.BytesIO()
        chunk.export(buf, format="wav")
        buf.seek(0)

        transcription = stt_model.transcribe(buf, language="en")
        results.append({
            "speaker": seg["speaker"],
            "start": seg["start"],
            "end": seg["end"],
            "text": transcription["text"].strip()
        })

    return results

