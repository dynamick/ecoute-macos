# import custom_speech_recognition as sr
import speech_recognition as sr
# import pyaudio
# import platform

# script to fetch various speech_recognition module metadata

BLACKHOLE_MIC_NAME = "BlackHole 2ch"
MBP_MIC_NAME = "MacBook Pro Microphone"
PLANTRONICS_3220_MIC_NAME = "Plantronics Blackwire 3220 Series"

dev_index = None

## list available microphones and obtain macOS "BlackHole 2ch" microphone index
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
    if name == PLANTRONICS_3220_MIC_NAME and dev_index is None:
        dev_index = index

print("\"{}\" microphone index is: {}".format(PLANTRONICS_3220_MIC_NAME, dev_index))

working_mics = sr.Microphone.list_working_microphones()
print("Available working microphones: {}".format(working_mics))

# r = sr.Recognizer()
# with sr.Microphone(device_index=dev_index) as source:
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
