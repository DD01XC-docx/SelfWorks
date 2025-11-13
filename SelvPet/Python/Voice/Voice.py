import speech_recognition as sr
import subprocess
import webbrowser
import os

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
    
        self.commands = {
            'open browser': self.open_browser,
            'start calculator': self.open_calculator,
            'open notepad': self.open_notepad,
            'play music': self.open_music,
            'open email': self.open_email,
            'open github': self.open_github,
            'shut down computer': self.shutdown_pc,
            'work mode': self.work_mode,
            'game mode': self.game_mode
        }
    
    def open_browser(self):
        """Open browser"""
        webbrowser.open("https://google.com")
        return "Opening browser"
    
    def open_calculator(self):
        """Open calculator"""
        if os.name == 'nt':
            subprocess.Popen("calc.exe")
        else:
            subprocess.Popen(["gnome-calculator"])
        return "Starting calculator"
    
    def open_notepad(self):
        """Open notepad"""
        if os.name == 'nt':
            subprocess.Popen("notepad.exe")
        else:
            subprocess.Popen(["gedit"])
        return "Opening notepad"
    
    def open_music(self):
        """Open music"""
        webbrowser.open("https://music.youtube.com")
        return "Playing music"
    
    def open_email(self):
        """Open email"""
        webbrowser.open("https://gmail.com")
        return "Opening email"
    
    def open_github(self):
        """Open GitHub"""
        webbrowser.open("https://github.com")
        return "Opening GitHub"
    
    def shutdown_pc(self):
        """Shut down the computer"""
        confirm = input("Are you sure you want to shut down the computer? (yes/no): ")
        if confirm.lower() == 'yes':
            if os.name == 'nt':
                os.system("shutdown /s /t 30")
            else:
                os.system("shutdown -h now")
            return "Shutting down the computer in 30 seconds"
        return "Shutdown canceled"
    
    def work_mode(self):
        """Work mode"""
        programs = ["notepad.exe", "calc.exe", "chrome.exe"]
        for program in programs:
            try:
                subprocess.Popen(program)
            except:
                pass
        return "Starting work mode"
    
    def game_mode(self):
        """Game mode"""
        webbrowser.open("https://steam.com")
        return "Starting game mode"
    
    def listen(self):
        """Listen for voice commands"""
        try:
            with self.microphone as source:
                print("Say a command...")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source, timeout=5)
            
            command = self.recognizer.recognize_google(audio, language='en-US').lower()
            print(f"Recognized: {command}")
            return command
            
        except sr.WaitTimeoutError:
            print("Listening timeout")
            return None
        except sr.UnknownValueError:
            print("Could not understand speech")
            return None
    
    def process_command(self, command):
        """Process the given command"""
        if not command:
            return
        
        for cmd, action in self.commands.items():
            if cmd in command:
                result = action()
                print(result)
                return
        
        print(f"Unknown command: {command}")
        print("Available commands:", list(self.commands.keys()))
    
    def run(self):
        """Main loop"""
        print("Voice assistant started!")
        print("Available commands:", list(self.commands.keys()))
        
        while True:
            command = self.listen()
            if command == 'stop':
                print("Assistant shutting down")
                break
            self.process_command(command)


if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()
