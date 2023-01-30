from googletrans import Translator

# made an instance of the Translator
translator = Translator()

# simple detection
test1 = "hello world"
dtest1 = translator.detect(test1)
print(dtest1)

# simple translation
test2 = "namaste duniya"
ttest2 = translator.translate(test2)
# .text is important, because it prints the raw version of the translation, raw meaning, it prints the translation along with the source, detected language, translated language and many other.
print(ttest2.text)

# now using the source and destination parameters for the translation
test3 = "i am a programmer"
ttest3 = translator.translate(test3, src="en", dest="hi")
print(ttest3.text)

# translating a list of texts
test4 = ["hello world", "my name is albert", "i am a programmer"]
for test in test4 :
    ttest4 = translator.translate(test, src="en", dest="hi")
    print(ttest4.text)
    
