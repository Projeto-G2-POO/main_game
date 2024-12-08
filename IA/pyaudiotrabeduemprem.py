import pyaudio
import speech_recognition as sr # type: ignore


r = sr.Recognizer()


mic = sr.Microphone()


p = pyaudio.PyAudio()


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024


stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

try:
    while True:
        
        audio = r.listen(stream)

        try:
           
            text = r.recognize_google(audio)
            print(text)
        except sr.UnknownValueError:
            print("Não entendi")
        except sr.RequestError as e:
            print("Serviço de reconhecimento de fala indisponível; {0}".format(e))

except KeyboardInterrupt:
    pass


stream.stop_stream()
stream.close()
p.terminate()