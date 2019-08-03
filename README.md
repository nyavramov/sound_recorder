### What is this?

This is a very small, barebones python sound recording package I created that may come in handy for personal projects.
For example, if there was music playing from your machine's speakers, this could record that sound.
 Nothing fancy. 
 
### What does it do?

It lets you record sound from whatever input devices you have on your machine. Just specify the recording duration and 
file name to save to. 

### How do I install it?

Just install the requirements by running the following from within the root project directory:
 `python3 -m pip install -r requirements.txt`
 
### How do I use it?

Check out the `main.py` file or do the following:
```python
from sound_recorder import SoundRecorder

sound_recorder = SoundRecorder(input_device_index=0)
sound_recorder.record(duration=3)
sound_recorder.save(file_name="test_recording.wav")
```
