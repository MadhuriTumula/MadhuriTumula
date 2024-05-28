import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and the TTS engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Loop for user to speak
def main():
    print("Say 'exit' to terminate the program.")
    while True:
        try:
            # Use the microphone as source for input
            with sr.Microphone() as source2:
                # Adjust the energy threshold based on the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)
                
                print("Listening...")
                # Listen for the user's input
                audio2 = r.listen(source2)
                
                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                print("Did you say: ", MyText)
                SpeakText(MyText)
                
                # Check if the user said 'exit' to stop the loop
                if 'exit' in MyText:
                    print("Exiting program.")
                    SpeakText("Goodbye")
                    break
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("Could not understand the audio")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")