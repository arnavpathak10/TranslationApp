from PyQt5.QtWidgets import QApplication, QGraphicsOpacityEffect, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
import speech_recognition as sr
from layouts.voiceRecoLayout import voiceRecognitionWindow
import sys
from deep_translator import GoogleTranslator


class SpeechRecognizerThread(QThread):
    reconizer = pyqtSignal(str)
    recordingStarted = pyqtSignal()
    recordingStopped = pyqtSignal(str)

    def __init__(self, win, language):
        super().__init__()
        self.win = win
        self.voicelanguage = language
        self.speechToText = ""


    def run(self):
        self.running = True
        self.recognizer = sr.Recognizer()

        self.recognizer.energy_threshold = 300
        self.recognizer.pause_threshold = 0.8

        self.recordingStarted.emit()

        self.microphone = sr.Microphone()
        with self.microphone as source:
            print("Adjusting for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)

        self.stopListening = self.recognizer.listen_in_background(self.microphone, self.recordAudioToText)
        print("Background listening started")

        while self.running:
            self.msleep(100)  

        print("Stopped listening")

    def recordAudioToText(self, recognizer, audio):
        try:
            text = recognizer.recognize_google(audio, language=self.voicelanguage)
            self.speechToText += text + " "
            print("Recognized (recordAudioToText):", text)
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Recognition error: {e}")
        
    
    def stopRecording(self):
        self.running = False
        if hasattr(self, 'stopListening'):
            self.stopListening(wait_for_stop=False)
        self.recordingStopped.emit(self.speechToText)
        self.quit()
        self.wait()
        self.win.voiceToTextEditBox.insertPlainText(self.speechToText)
        self.speechToText = ""


class SpeechToTextRecognition:
    def __init__(self, app, win):
        self.win = win
        self.win.show()

        self.voiceLanguage = "en-IN"
        self.translationLanguage = "en-IN"

        self.win.selectVoiceLanguageModel.currentTextChanged.connect(self.getVoiceLanguageModel)
        self.win.selectTranslationLanguageModel.currentTextChanged.connect(self.getTranslationLanguageModel)
        
        self.recognizerSpeechThread = SpeechRecognizerThread(self.win, self.voiceLanguage)
        self.win.startVoiceRecognitionBtn.clicked.connect(self.recognizerSpeechThread.start)
        self.win.stopVoiceRecognitionBtn.clicked.connect(self.recognizerSpeechThread.stopRecording)
        self.recognizerSpeechThread.recordingStarted.connect(self.onRecordingStarted)
        self.recognizerSpeechThread.recordingStopped.connect(self.onRecordingStop)

        self.win.clearVoiceRecognizedTextBtn.clicked.connect(self.clearRecognizedPlainText)

        self.win.translateRecognizedTextBtn.clicked.connect(self.translateRecognizedSpeech)
        self.win.clearTranslateTextBtn.clicked.connect(self.clearTranslatedText)
        self.win.copyTranslatedTextBtn.clicked.connect(self.copyTranslatedTextToClipBoard)


    def getVoiceLanguageModel(self):
        self.voiceLanguage = self.win.selectVoiceLanguageModel.currentData()
        print(self.voiceLanguage)
    
    def getTranslationLanguageModel(self):
        self.translationLanguage = self.win.selectTranslationLanguageModel.currentData()
        print(self.translationLanguage)

    def clearRecognizedPlainText(self):
        if self.win.voiceToTextEditBox.toPlainText()=="":
            QMessageBox.about(self.win, "Empty Field", "Text not found to clear")
            return
        self.win.voiceToTextEditBox.setPlainText("")

    def onRecordingStarted(self):
        self.win.stackedPushBtnLayout.setCurrentIndex(1)
        self.setPushBtnList = [self.win.clearVoiceRecognizedTextBtn, self.win.translateRecognizedTextBtn, self.win.clearTranslateTextBtn, self.win.copyTranslatedTextBtn]
        for btnWidget in self.setPushBtnList:
            btnWidget.setEnabled(False)
            self.setOpacity(btnWidget, 0.5)


    def onRecordingStop(self):
        self.win.stackedPushBtnLayout.setCurrentIndex(0)
        self.setPushBtnList = [self.win.clearVoiceRecognizedTextBtn, self.win.translateRecognizedTextBtn, self.win.clearTranslateTextBtn, self.win.copyTranslatedTextBtn]
        for btnWidget in self.setPushBtnList:
            btnWidget.setEnabled(True)
            self.setOpacity(btnWidget, 1)

    def setOpacity(self, widget, opacity):
        effect = QGraphicsOpacityEffect()
        effect.setOpacity(opacity)
        widget.setGraphicsEffect(effect)

    def translateRecognizedSpeech(self):
        self.win.translateSpeechTextEditBox.setPlainText("")
        self.speech = self.win.voiceToTextEditBox.toPlainText()
        if self.speech == "":
            QMessageBox.about(self.win, "Input Required", "Please provide text to translate")
            return
        self.transText =  GoogleTranslator(source='auto', target=self.translationLanguage[0:2]).translate(self.speech)
        self.win.translateSpeechTextEditBox.insertPlainText(self.transText)

    def clearTranslatedText(self):
        if self.win.translateSpeechTextEditBox.toPlainText()=="":
            QMessageBox.about(self.win, "Empty Field", "Text not found to clear")
            return
        self.win.translateSpeechTextEditBox.setPlainText("")
        
    def copyTranslatedTextToClipBoard(self):
        if self.win.translateSpeechTextEditBox.toPlainText()=="":
            QMessageBox.about(self.win, "Empty Field", "Nothing to Copy")
            return
        clipboard = QApplication.clipboard()
        copyText = self.win.translateSpeechTextEditBox.toPlainText()
        clipboard.setText(copyText)
        if clipboard:
            QMessageBox.about(self.win, "Copied", "Text Copied Successfully")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = voiceRecognitionWindow()
    speechReco = SpeechToTextRecognition(app=app, win=win)
    app.exec_()


