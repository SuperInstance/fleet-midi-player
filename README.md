# 🔊 fleet-midi-player

> *MIDI → Audio rendering server*

Renders any Standard MIDI Format 1 file to WAV audio using FluidSynth with professional soundfonts.

```bash
pip install fluidsynth
python lib/player.py path/to/file.mid
# → produces path/to/file.wav
```

## Architecture
```
MIDI → FluidSynth → SoundFont → WAV audio file
```

## Ennsign: **Resonance** — Fleet Audio Officer
**Summon:** `/ensign resonance play path/to/file.mid`
