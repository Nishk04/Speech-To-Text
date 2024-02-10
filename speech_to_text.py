import speech_recognition as sr
import pyttsx3

#Initializes the voice recognizer
r = sr.Recognizer()

def record_text():
    # To check for errors when speaking
    while(1):
        try:
            # Our source of input
            with sr.Microphone() as source:
                # Prepare recognizer to receive input
                r.adjust_for_ambient_noise(source, duration=0.2)
                
                # Listens for user's input
                audio = r.listen(source)
                
                # Uses google to recognize audio
                MyText = r.recognize_google(audio)

                return MyText

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        
        except sr.UnknownValueError:
            print("Unknown error occurred.")
    return

def output_text(text):
    # Creates a text file that appends 
    # the text to the end of the file
    f = open("output.txt", "a")
    f.write(text) # Adds text
    f.write("\n") # Line break
    f.close() # Closes file
    return
listen = 1
while(listen):
    text = record_text()
    if(text == "stop listening"):
        listen = 0 
    else: listen = 1
    output_text(text)
    print("Wrote text and listen is: ")
    print(listen)