# Import all these libraries
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
from scipy.io.wavfile import write

# Function to generate sine wave sound using numpy
def generate_sine_wave(frequency, duration_ms, sample_rate=44100, amplitude=0.5):
    t = np.linspace(0, duration_ms / 1000, int(sample_rate * (duration_ms / 1000)), False)
    wave = np.sin(frequency * t * 2 * np.pi)
    
    # Ensure that the wave is within the range of int16
    audio_data = np.int16(wave * amplitude * 32767)
    
    # Create a temporary .wav file
    write("temp.wav", sample_rate, audio_data)
    
    # Load the .wav file into an AudioSegment object
    return AudioSegment.from_wav("temp.wav")

# Create short and long beeps (dot and dash)
dot_sound = generate_sine_wave(frequency=1000, duration_ms=100)  # Dot = short beep
dash_sound = generate_sine_wave(frequency=1000, duration_ms=300)  # Dash = long beep
space_sound = AudioSegment.silent(duration=300)  # Silent pause between letters

# Morse Code Dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': '/'
}

# Function to convert text to Morse code and generate sound
def text_to_morse_audio(text):
    morse_code = ''
    combined_audio = AudioSegment.silent(duration=0)  # Empty audio segment
    
    for char in text.upper():
        if char in morse_code_dict:
            code = morse_code_dict[char]
            morse_code += code + ' '
            
            for symbol in code:
                if symbol == '.':
                    combined_audio += dot_sound
                elif symbol == '-':
                    combined_audio += dash_sound
                combined_audio += space_sound
        else:
            combined_audio += AudioSegment.silent(duration=700)  # Space between words
    return combined_audio, morse_code

# Main program loop
def main():
    while True:
        choice = input("Enter '1' for Text to Morse (Audio), 'q' to quit: ")

        if choice == '1':
            text = input("Enter text to convert to Morse code: ")
            combined_audio, morse_code = text_to_morse_audio(text)
            print(f"Morse Code: {morse_code}")

            # Export audio file for Morse code
            combined_audio.export("morse_code_output.wav", format="wav")
            print("Morse code audio saved as 'morse_code_output.wav'.")

        elif choice == 'q':
            break

        else:
            print("Invalid option, please try again.")

if __name__ == '__main__':
    main()
