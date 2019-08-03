#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
main.py
-------

Example of using sound_recorder to record some sound

"""
from sound_recorder import SoundRecorder, print_sound_input_devices


def main():
    # List the available devices we can use to record stuff
    print_sound_input_devices()

    # record a few seconds of sound and save it
    sound_recorder = SoundRecorder(input_device_index=0)
    sound_recorder.record(duration=3)
    sound_recorder.save(file_name="test_recording.wav")


if __name__ == '__main__':
    main()
