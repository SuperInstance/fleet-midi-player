"""MIDI to audio rendering via FluidSynth."""
import subprocess, os, json, tempfile

def midi_to_wav(midi_path: str, soundfont: str = "/usr/share/sounds/sf2/FluidR3_GM.sf2", 
                output: str = None) -> str:
    """Render MIDI file to WAV audio using FluidSynth."""
    if not os.path.exists(midi_path):
        raise FileNotFoundError(f"MIDI not found: {midi_path}")
    
    if output is None:
        output = midi_path.replace('.mid', '.wav')
    
    if not os.path.exists(soundfont):
        # Try common locations
        for sf in ["/usr/share/sounds/sf2/FluidR3_GM.sf2",
                    "/usr/share/soundfonts/FluidR3_GM.sf2",
                    "FluidR3_GM.sf2"]:
            if os.path.exists(sf):
                soundfont = sf
                break
    
    cmd = ['fluidsynth', '-ni', soundfont, midi_path, '-F', output, '-r', '44100']
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    
    if result.returncode != 0:
        # Try with alsa
        cmd = ['fluidsynth', '-a', 'alsa', '-ni', soundfont, midi_path, '-F', output, '-r', '44100']
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    
    return output if os.path.exists(output) else None

if __name__ == "__main__":
    import sys
    path = sys.argv[1]
    result = midi_to_wav(path)
    print(json.dumps({"input": path, "output": result, "status": "ok" if result else "failed"}))
