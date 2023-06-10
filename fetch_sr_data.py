# import custom_speech_recognition as sr
import speech_recognition as sr
# import pyaudio
# import platform

# script to fetch various speech_recognition module metadata

BLACKHOLE_MIC_NAME = "BlackHole 2ch"

## list available microphones and obtain macOS "BlackHole 2ch" microphone index
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
    if name == BLACKHOLE_MIC_NAME:
        blackhole_mic_index = index

print("\"{}\" microphone index is: {}".format(BLACKHOLE_MIC_NAME, blackhole_mic_index))

# r = sr.Recognizer()
# with sr.Microphone(device_index=blackhole_mic_index) as source:
#     print("Say something!")
#     audio = r.listen(source)

# # write audio to a RAW file
# with open("microphone-results.raw", "wb") as f:
#     f.write(audio.get_raw_data())

# # write audio to a WAV file
# with open("microphone-results.wav", "wb") as f:
#     f.write(audio.get_wav_data())

# # write audio to an AIFF file
# with open("microphone-results.aiff", "wb") as f:
#     f.write(audio.get_aiff_data())

# # write audio to a FLAC file
# with open("microphone-results.flac", "wb") as f:
#     f.write(audio.get_flac_data())
