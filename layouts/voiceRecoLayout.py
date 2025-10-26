from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QGroupBox, QRadioButton, QPushButton, QStackedLayout, QComboBox, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import QSize, Qt
import os 
from pathlib import Path
import sys

class voiceRecognitionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Translation App")
        self.winIcon = QIcon()
        self.winIcon.addFile(os.path.join(Path(__file__).parents[1], "Icons", 'languagetranslation.webp'), QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(self.winIcon)
        self.setFixedSize(1300, 715)

        self.font = QFont("Arial")
        self.font.setPointSize(10)

        self.mainVerticalLayout = QVBoxLayout()
        self.mainVerticalLayout.setSpacing(50)
        

        self.languageSelectionGrpBox = QGroupBox()
        self.languageSelectionGrpBox.setFont(self.font)
        self.languageSelectionGrpBox.setStyleSheet("""
                QGroupBox {
                    border: 0.5px solid gray;
                    border-radius: 5px;
                    margin-top: 20px;
                }
                QGroupBox::title {
                    subcontrol-origin: margin;
                    padding: 0 3px;
                    background-color: transparent;
                }
                QGroupBox:hover {
                    border: 1px solid #F86A38;
                    background-color: #FFF5F0;
            }
        """)
        
        self.languageSelectionHLayout = QHBoxLayout()


        self.selectVoiceLanguageGrpBox = QGroupBox()
        self.selectVoiceLanguageGrpBox.setTitle("Voice Language")
        self.selectVoiceLanguageHLayout = QHBoxLayout()
        self.selectVoiceLanguageModel = QComboBox()
        
        self.languageSelectionDirectionLabel = QLabel()
        self.languageSelectionDirectionLabel.setAlignment(Qt.AlignCenter)
        self.arrowImg = os.path.join(Path(__file__).parents[1], "Icons", "arrow.png")
        self.languageSelectionDirImg = QPixmap(self.arrowImg).scaled(QSize(22, 22))
        self.languageSelectionDirectionLabel.setPixmap(self.languageSelectionDirImg)



        self.selectTranslationLangGrpBox = QGroupBox()
        self.selectTranslationLangGrpBox.setTitle("Translation Language")
        self.selectTranslationLangHLayout = QHBoxLayout()
        self.selectTranslationLanguageModel = QComboBox()
        
        self.voiceLanguageModel = [["English (India)", "en-IN"], ["English (United Kingdom)","en-GB"], ["Hindi (India)", "hi-IN"], ["Punjabi (Gurmukhi India)", "pa-Guru-IN"], ["Tamil (India)", "ta-IN"], ["Telugu (India)", "te-IN"], ["Marathi (India)", "mr-IN"], ["Kannada (India)", "kn-IN"], ["Chinese (Simplified, China)", "cmn-Hans-CN"], ["Italian (Italy)", "it-IT"], ["Japanese (Japan)", "ja-JP"], ["Nepali (Nepal)", "ne-NP"], ["Portuguese (Portugal)","pt-PT"]]
        for language in self.voiceLanguageModel:
            self.selectVoiceLanguageModel.addItem(language[0], language[1])
            self.selectTranslationLanguageModel.addItem(language[0], language[1])
        self.selectVoiceLanguageModel.setCurrentIndex(0)
        self.selectTranslationLanguageModel.setCurrentIndex(0)

        self.selectVoiceLanguageHLayout.addWidget(self.selectVoiceLanguageModel)
        self.selectTranslationLangHLayout.addWidget(self.selectTranslationLanguageModel)

        self.selectVoiceLanguageGrpBox.setLayout(self.selectVoiceLanguageHLayout)
        self.selectTranslationLangGrpBox.setLayout(self.selectTranslationLangHLayout)

        self.languageSelectionHLayout.addWidget(self.selectVoiceLanguageGrpBox)
        self.languageSelectionHLayout.addWidget(self.languageSelectionDirectionLabel)
        self.languageSelectionHLayout.addWidget(self.selectTranslationLangGrpBox)

        self.languageSelectionGrpBox.setLayout(self.languageSelectionHLayout)

        self.horizontalTextEditBtnLayout = QHBoxLayout()
        self.horizontalTextEditBtnLayout.setSpacing(20)

        self.speechToTextVerticalLayout = QVBoxLayout()

        self.voiceToTextEditBox = QTextEdit()
        self.voiceToTextEditBox.setObjectName("voiceToTextEditBox")
        self.voiceToTextEditBox.setFixedSize(630, 500)
        self.voiceToTextEditBox.setFont(self.font)
        self.voiceToTextEditBox.setPlaceholderText("Voice to text display here!")
        self.speechToTextVerticalLayout.addWidget(self.voiceToTextEditBox)


        self.horizontalPushBtnLayout = QHBoxLayout()
        
        self.stackedPushBtnLayout = QStackedLayout()

        self.startVoiceRecognitionBtn = QPushButton("Start")
        self.startIcon = QIcon()
        self.startIcon.addFile(os.path.join(Path(__file__).parents[1], "Icons", "startRecording.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.startVoiceRecognitionBtn.setIcon(self.startIcon)

        self.stopVoiceRecognitionBtn = QPushButton("Stop")
        self.stopIcon = QIcon()
        self.stopIcon.addFile(os.path.join(Path(__file__).parents[1], "Icons", "stopRecording.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.stopVoiceRecognitionBtn.setIcon(self.stopIcon)

        self.stackedPushBtnLayout.addWidget(self.startVoiceRecognitionBtn)
        self.stackedPushBtnLayout.addWidget(self.stopVoiceRecognitionBtn)

        self.clearVoiceRecognizedTextBtn = QPushButton("Clear")
        self.clearVoiceRecognizedTextBtn.setAccessibleName("clearVoiceRecognizedTextBtn")

        self.translateRecognizedTextBtn = QPushButton("Translate")
        self.translateRecognizedTextBtn.setAccessibleName("translateRecognizedTextBtn")

        self.horizontalPushBtnLayout.addLayout(self.stackedPushBtnLayout)
        self.horizontalPushBtnLayout.addWidget(self.clearVoiceRecognizedTextBtn)
        self.horizontalPushBtnLayout.addWidget(self.translateRecognizedTextBtn)

        self.speechToTextVerticalLayout.addLayout(self.horizontalPushBtnLayout)

        self.translateTextBoxVerticalLayout = QVBoxLayout()

        self.translateSpeechTextEditBox = QTextEdit()
        self.translateSpeechTextEditBox.setObjectName("translateSpeechTextEditBox")
        self.translateSpeechTextEditBox.setFixedSize(630, 500)
        self.translateSpeechTextEditBox.setFont(self.font)
        self.translateSpeechTextEditBox.setPlaceholderText("Translated Text Display here!")
        self.translateTextBoxVerticalLayout.addWidget(self.translateSpeechTextEditBox)

        self.translatePushBtnHLayout = QHBoxLayout()

        self.clearTranslateTextBtn = QPushButton("Clear")
        self.clearTranslateTextBtn.setAccessibleName("clearTranslateTextBtn")

        self.translatePushBtnHLayout.addWidget(self.clearTranslateTextBtn)

        self.copyTranslatedTextBtn = QPushButton("Copy Text")
        self.copyTranslatedTextBtn.setAccessibleName("copyTranslatedTextBtn")

        self.translatePushBtnHLayout.addWidget(self.copyTranslatedTextBtn)

        self.translateTextBoxVerticalLayout.addLayout(self.translatePushBtnHLayout)

        self.horizontalTextEditBtnLayout.addLayout(self.speechToTextVerticalLayout)
        self.horizontalTextEditBtnLayout.addLayout(self.translateTextBoxVerticalLayout)

        self.radioBtnStyle = """
            QRadioButton {
                spacing: 8px;
                font-size: 14px;
                color: #000;
                outline: none;
                border: none;
            }

            QRadioButton:focus {
                outline: none;
                border: none;
            }

            QRadioButton::indicator {
                width: 18px;
                height: 18px;
                border-radius: 9px;
                border: 2px solid #ccc;
                background-color: #fff;
            }

            QRadioButton::indicator:checked {
                border: 2px solid #ccc;
                background-color: qradialgradient(
                    cx:0.5, cy:0.5, radius:0.6,
                    fx:0.5, fy:0.5,
                    stop:0 #007BFF, stop:0.4 #007BFF, stop:0.41 #ffffff
                );
            }

            QRadioButton::indicator:focus {
                outline: none;
            }

            QRadioButton::indicator:unchecked:hover {
                border: 2px solid #007BFF;
            }
        """

        self.pushBtnStyle = """
                QPushButton {
                    color: white;
                    background-color: #F86A38;
                    width: 100px;
                    height: 25px;
                    border-radius: 5px;
                }
                """
        self.startStopBtnStyle = """
                QPushButton {
                    color: white;
                    background-color: #F86A38;
                    max-width: 100px;
                    height: 5px;
                    border-radius: 5px;
                }
                """

        self.setPushBtnStyleSheet = [self.startVoiceRecognitionBtn, self.stopVoiceRecognitionBtn, self.clearVoiceRecognizedTextBtn, self.translateRecognizedTextBtn, self.clearTranslateTextBtn, self.copyTranslatedTextBtn]
        
        for widget in self.setPushBtnStyleSheet:
            if widget in [self.startVoiceRecognitionBtn, self.stopVoiceRecognitionBtn]:
                widget.setStyleSheet(self.startStopBtnStyle)
            else:
                widget.setStyleSheet(self.pushBtnStyle)


        self.mainVerticalLayout.addWidget(self.languageSelectionGrpBox)
        self.mainVerticalLayout.addLayout(self.horizontalTextEditBtnLayout)

        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.mainVerticalLayout)
        self.setCentralWidget(self.centralWidget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = voiceRecognitionWindow()
    window.show()
    app.exec_()



