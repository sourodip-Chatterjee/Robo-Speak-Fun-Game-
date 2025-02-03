import os

if __name__ == '__main__':
    print("Welcome to robo Speak..")
    
    while True:
        speak = input('What you want it to speak out? ')
        if speak.lower() == 'exit':
            break 
        
        command = f'powershell -Command "Add-Type –AssemblyName System.Speech; ' \
                f'$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; ' \
                f'$synth.Speak(\'{speak}\')"'
        os.system(command)


