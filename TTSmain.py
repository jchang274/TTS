from azure.cognitiveservices.speech import AudioDataStream
from azure.cognitiveservices.speech import SpeechConfig
from azure.cognitiveservices.speech import SpeechSynthesizer
from azure.cognitiveservices.speech import SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig
import os
import time
time_now = time.strftime("%Y%m%d-%H%M-%S", time.localtime())
KEY = 'dece00af114f42a8b6c7324dca4d4125'
REGION = "southeastasia"
speech_config = SpeechConfig(subscription=KEY, region=REGION)
mp3_format='Audio16Khz32KBitRateMonoMp3'
speech_config.set_speech_synthesis_output_format(SpeechSynthesisOutputFormat[mp3_format])
audio_config = AudioOutputConfig(filename=r'Cache\ConvertCache.mp3')
synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
ssml_string = open("InputText.xml", "r").read()
synthesizer.speak_ssml_async(ssml_string)

filename1 = r'Cache\ConvertCache.mp3'
filename2 = r'AudioOutput\Audio'+time_now+'.mp3'
os.system('copy %s %s' % (filename1, filename2)) 
os.startfile(r'AudioOutput\Audio'+time_now+'.mp3')
start_directory = r'AudioOutput'
os.startfile(start_directory)