# pip install googletrans
from googletrans import Translator
import win32com.client as wincl
translator = Translator()

a=translator.translate('Harry Brother is very brilliant really',src='en',dest='hi')
print (a.text)
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak(a.text)