# ! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
sound_record.utils
------------------

Utility that can be used to get more system sound input information
"""
import pyaudio


def print_sound_input_devices():
    """Prints out the available recording devices and their respective system indices

    Original source was modified from: https://stackoverflow.com/a/39677871
    """
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    for i in range(numdevices):
        if p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels') > 0:
            device_name = p.get_device_info_by_host_api_device_index(0, i).get('name')
            print(f"Input device \"{device_name}\" at index {i}.")
