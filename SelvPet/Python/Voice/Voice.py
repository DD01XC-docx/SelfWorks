import speech_recognition as sr
import subprocess
import webbrowser
import os

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
    
        self.commands = {
            'открой браузер': self.open_browser,
            'запусти калькулятор': self.open_calculator,
            'открой блокнот': self.open_notepad,
            'включи музыку': self.open_music,
            'открой почту': self.open_email,
            'открой гитхаб': self.open_github,  
            'открой github': self.open_github,   
            'выключи компьютер': self.shutdown_pc,
            'рабочий режим': self.work_mode,
            'игровой режим': self.game_mode
        }
    
    def open_browser(self):
        """Открыть браузер"""
        webbrowser.open("https://google.com")
        return "Открываю браузер"
    
    def open_calculator(self):
        """Открыть калькулятор"""
        if os.name == 'nt':
            subprocess.Popen("calc.exe")
        else:
            subprocess.Popen(["gnome-calculator"])
        return "Запускаю калькулятор"
    
    def open_notepad(self):
        """Открыть блокнот"""
        if os.name == 'nt':
            subprocess.Popen("notepad.exe")
        else:
            subprocess.Popen(["gedit"])
        return "Открываю блокнот"
    
    def open_music(self):
        """Открыть музыку"""
        webbrowser.open("https://music.youtube.com")
        return "Включаю музыку"
    
    def open_email(self):
        """Открыть почту"""
        webbrowser.open("https://gmail.com")
        return "Открываю почту"
    
    # ДОБАВЛЯЕМ НОВЫЙ МЕТОД ДЛЯ GITHUB
    def open_github(self):
        """Открыть GitHub"""
        webbrowser.open("https://github.com")
        return "Открываю GitHub"
    
    def shutdown_pc(self):
        """Выключение компьютера"""
        confirm = input("Вы уверены, что хотите выключить компьютер? (да/нет): ")
        if confirm.lower() == 'да':
            if os.name == 'nt':
                os.system("shutdown /s /t 30")
            else:
                os.system("shutdown -h now")
            return "Выключаю компьютер через 30 секунд"
        return "Отмена выключения"
    
    def work_mode(self):
        """Режим работы"""
        programs = ["notepad.exe", "calc.exe", "chrome.exe"]
        for program in programs:
            try:
                subprocess.Popen(program)
            except:
                pass
        return "Запускаю рабочий режим"
    
    def game_mode(self):
        """Игровой режим"""
        webbrowser.open("https://steam.com")
        return "Запускаю игровой режим"
    
    def listen(self):
        """Прослушивание голосовых команд"""
        try:
            with self.microphone as source:
                print("Скажите команду...")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source, timeout=5)
            
            command = self.recognizer.recognize_google(audio, language='ru-RU').lower()
            print(f"Распознано: {command}")
            return command
            
        except sr.WaitTimeoutError:
            print("Время ожидания истекло")
            return None
        except sr.UnknownValueError:
            print("Не удалось распознать речь")
            return None
    
    def process_command(self, command):
        """Обработка команды"""
        if not command:
            return
        
        for cmd, action in self.commands.items():
            if cmd in command:
                result = action()
                print(result)
                return
        
        print(f"Неизвестная команда: {command}")
        print("Доступные команды:", list(self.commands.keys()))
    
    def run(self):
        """Основной цикл работы"""
        print("Голосовой ассистент запущен!")
        print("Доступные команды:", list(self.commands.keys()))
        
        while True:
            command = self.listen()
            if command == 'стоп':
                print("Ассистент завершает работу")
                break
            self.process_command(command)


if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()