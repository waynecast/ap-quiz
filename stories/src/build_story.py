"""Build a Story mode episode: narrate each line with Kokoro, join into one
audio track, and write a JSON cue sheet (scene/line start and end times).

usage: python3 build_story.py <script_module> <out_dir> [voice]
"""
import importlib.util, json, re, subprocess, sys, os
import numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pron import to_phonemes

mod_path, out_dir = sys.argv[1], sys.argv[2]
voice = sys.argv[3] if len(sys.argv) > 3 else "af_heart"
spec = importlib.util.spec_from_file_location("s", mod_path)
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
story = m.STORY

TTS = os.environ.get("KOKORO_DIR", "kokoro")  # folder with model.onnx + voices.bin
k = Kokoro(f"{TTS}/model.onnx", f"{TTS}/voices.bin")
SR = 24000
GAP_LINE, GAP_SCENE, LEAD = 0.45, 1.1, 0.4

def strip(s):
    return re.sub(r"\*\*(.+?)\*\*", r"\1", s)

chunks, t = [np.zeros(int(LEAD * SR), np.float32)], LEAD
out = {k2: v for k2, v in story.items() if k2 != "scenes"}
out["voice"] = voice
out["scenes"] = []
for si, sc in enumerate(story["scenes"]):
    scene = {k2: sc[k2] for k2 in ("lec", "title", "img", "terms")}
    if scene["img"]:
        scene["img"] = os.path.splitext(scene["img"])[0] + ".jpg"
    scene["start"] = round(t, 2)
    scene["lines"] = []
    for li, line in enumerate(sc["lines"]):
        show, say = (line, strip(line)) if isinstance(line, str) else line
        say = strip(say)
        ph = to_phonemes(say, lambda x: k.tokenizer.phonemize(x, "en-us"))
        if ph:
            audio, sr = k.create(ph, voice=voice, speed=0.95, is_phonemes=True)
        else:
            audio, sr = k.create(say, voice=voice, speed=0.95, lang="en-us")
        assert sr == SR
        # trim leading/trailing near-silence so gaps are consistent
        nz = np.where(np.abs(audio) > 0.01)[0]
        if len(nz):
            audio = audio[max(0, nz[0] - 600): nz[-1] + 1200]
        start = t
        chunks.append(audio.astype(np.float32)); t += len(audio) / SR
        scene["lines"].append({"text": show, "start": round(start, 2), "end": round(t, 2)})
        gap = GAP_LINE if li < len(sc["lines"]) - 1 else GAP_SCENE
        chunks.append(np.zeros(int(gap * SR), np.float32)); t += gap
        print(f"{si:2d}.{li} {t:6.1f}s  {say}", flush=True)
    scene["end"] = round(t, 2)
    out["scenes"].append(scene)
out["duration"] = round(t, 2)

os.makedirs(out_dir, exist_ok=True)
wav = f"{out_dir}/{story['id']}.wav"
sf.write(wav, np.concatenate(chunks), SR)
mp3 = f"{out_dir}/{story['id']}.mp3"
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-ac", "1", "-b:a", "64k", mp3], check=True)
out["audio"] = f"stories/{story['id']}.mp3"
json.dump(out, open(f"{out_dir}/{story['id']}.json", "w"), ensure_ascii=False, indent=1)
os.remove(wav)
print("duration", round(t), "->", mp3)
