from googletrans import Translator
translator = Translator()
text1 = "hello world"
dt1 = translator.detect(text1)
print(dt1)