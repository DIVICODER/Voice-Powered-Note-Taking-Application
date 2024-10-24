
import speech_recognition as sr
import pyttsx3
from datetime import datetime

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts = pyttsx3.init()

# Function to provide spoken feedback
def speak_text(command):
    tts.say(command)
    tts.runAndWait()

# Function to listen for voice commands and convert them to text
def listen_and_note():
    notes = []
    stop = False
    
    # Greet the user
    speak_text("I am ready to take notes. Say 'next line' to move to the next line, and 'stop' to finish.")

    while not stop:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)  # Adjust to ambient noise levels
            audio = recognizer.listen(source)
        
        try:
            # Use Google Speech Recognition to convert speech to text
            text = recognizer.recognize_google(audio).lower()
            print(f"You said: {text}")
            
            if "next line" in text:
                notes.append("")  # Add a new line to notes
                # speak_text("Moved to the next line.")
            elif "stop" in text:
                stop = True
                speak_text("Noting stopped. Saving your notes.")
            else:
                notes.append(text)  # Add the spoken text to the current line

        except sr.UnknownValueError:
            speak_text("Sorry, I did not understand that.")
        except sr.RequestError as e:
            speak_text(f"Could not request results from Google Speech Recognition service; {e}")
    
    # Save notes to file
    save_notes(notes)

# Function to save notes to a file
def save_notes(notes):
    filename = f"notes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    
    with open(filename, "w") as file:
        for note in notes:
            file.write(note + "\n")
    
    print(f"Notes saved to {filename}")
    speak_text("Your notes have been saved successfully.")

# Run the note-taking system
if __name__ == "__main__":
    listen_and_note()
