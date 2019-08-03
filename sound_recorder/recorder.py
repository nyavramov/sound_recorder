#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
sound_recorder.recorder
-----------------------

This module creates the SoundRecorder object that allows a user to record sound for some duration of time
"""
import pyaudio
import wave


class SoundRecorder:
    """A user-created class SoundRecorder object.

    Used to allow a user to easily record sound and save it as a .wav file

    :param input_device_index: which physical or virtual sound input device you'd like to record from

    Usage::

        >>> from sound_recorder import SoundRecorder
        >>> sound_recorder = SoundRecorder(input_device_index=0)
        >>> sound_recorder.record(duration=3)
        >>> sound_recorder.save(file_name="test_recording.wav")
    """
    def __init__(self, input_device_index):
        self.input_device_index = input_device_index
        self.bits_per_sample = pyaudio.paInt16
        self.channels = 2
        self.rate = 44100
        self.chunk = 1024
        self.frames = []
        self.pyaudio = pyaudio.PyAudio()
        self.recorder = self.pyaudio.open(format=self.bits_per_sample,
                                          input_device_index=self.input_device_index,
                                          channels=self.channels,
                                          rate=self.rate,
                                          input=True,
                                          frames_per_buffer=self.chunk)

    def record(self, duration):
        """Records sound from a given input device for some duration

        :param duration: the duration to record for in seconds
        :return None:
        """
        for i in range(0, int(self.rate / self.chunk * duration)):
            data = self.recorder.read(self.chunk)
            self.frames.append(data)

        self.recorder.stop_stream()
        self.recorder.close()
        self.pyaudio.terminate()

    def save(self, file_name):
        """Saves a sound recording

        :param file_name: the intended name of the sound recording file
        :return: None
        """
        if not file_name.endswith(".wav"):
            raise Exception("Recordings must be saved as .wav")

        wav_file = wave.open(file_name, 'wb')
        wav_file.setnchannels(self.channels)
        wav_file.setsampwidth(self.pyaudio.get_sample_size(self.bits_per_sample))
        wav_file.setframerate(self.rate)
        wav_file.writeframes(b''.join(self.frames))
        wav_file.close()

