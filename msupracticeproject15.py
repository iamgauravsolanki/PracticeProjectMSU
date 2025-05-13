# CSE 231 Fall 2007, Project 02  
# Section: [Your Section]  
# Date: [Submission Date]  
# Description: Converts musical notes (octave-pitch) to frequencies in Hz.  

from math import pow  

def calculate_frequency(octave, pitch_class):  
    """Calculate frequency using the tempered scale formula."""  
    # Reference: A4 (4.9) = 440 Hz  
    octave_diff = octave - 4  
    semitone_diff = pitch_class - 9  
    return 440 * pow(2, octave_diff + semitone_diff / 12)  

def main():  
    print("Musical Note Frequency Calculator")  
    print("--------------------------------")  
    print("Enter three musical notes as octave and pitch class pairs.")  
    print("Pitch classes: 0=C, 1=C#, ..., 11=B\n")  

    notes = []  
    for i in range(3):  
        octave = int(input(f"Note {i+1} - Enter octave (e.g., 4 for A4): "))  
        pitch_class = int(input(f"Note {i+1} - Enter pitch class (0-11): "))  
        frequency = calculate_frequency(octave, pitch_class)  
        notes.append((octave, pitch_class, frequency))  

    # Output results  
    print("\nNote Frequencies:")  
    for octave, pitch_class, frequency in notes:  
        print(f"Octave {octave}.{pitch_class}: {frequency:.2f} Hz")  

    # Optional: Play notes (Windows-only)  
    try:  
        from winsound import Beep  
        print("\nPlaying notes (500ms each)...")  
        for _, _, frequency in notes:  
            if 37 <= frequency <= 32767:  
                Beep(int(frequency), 500)  
    except ImportError:  
        print("\n(Beep feature skipped: Requires Windows.)")  

if __name__ == "__main__":  
    main()  