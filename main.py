# -*- coding: utf-8 -*-

# This file is main file that contains all UI interactions
#
# This file contains the implementation of ChooseSchemeDialog class
# This class allows users to select one of five scheme
#
# This file also contains MrMusicApp class. This class represents interaction with users
#
# Author: Nikitin Nikita <nikitin.nikitaa@outlook.com>
# Created: 10.01.2016. Last modified: 12.06.2016

import os
import sys
from PyQt4 import QtGui, QtCore, Qt
import cv2

import vlc
import design

from ImageToMusicModule import ImageToMusic

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class ChooseSchemeDialog(QtGui.QDialog):

    """

    This class allows users to select one of five scheme

    Methods:
    ------------------
    init method contains creating of ui elements such as radio buttons and other

    get_scheme: allows to get selected scheme by the user

    """

    def __init__(self, scheme, parent=None):
        super(ChooseSchemeDialog, self).__init__(parent)

        # Create vertical box layout
        layout = QtGui.QVBoxLayout(self)

        # Set title of dialog window
        self.setWindowTitle(_translate("", "Выбор схемы соотнесения цветов и нот", None))

        # Create radio button Newton Scheme
        self.rb_newton = QtGui.QRadioButton(_translate("", "Схема Ньютона", None), self)

        # Add created button on the vertical box layout
        layout.addWidget(self.rb_newton)

        # Create radio button Castel Scheme
        self.rb_castel = QtGui.QRadioButton(_translate("", "Схема Кастеля", None), self)

        # Add created button on the vertical box layout
        layout.addWidget(self.rb_castel)

        # Create radio button Rimington Scheme
        self.rb_rimington = QtGui.QRadioButton(_translate("", "Схема Римингтона", None), self)

        # Add created button on the vertical box layout
        layout.addWidget(self.rb_rimington)

        # Create radio button Aepli Scheme
        self.rb_aepli = QtGui.QRadioButton(_translate("", "Схема Эппли", None), self)

        # Add created button on the vertical box layout
        layout.addWidget(self.rb_aepli)

        # Create radio button Belmont Scheme
        self.rb_belmont = QtGui.QRadioButton(_translate("", "Схема Бельмонта", None), self)

        # Add created button on the vertical box layout
        layout.addWidget(self.rb_belmont)

        # Set previously selected scheme
        if scheme == "castel":
            self.rb_castel.setChecked(True)
        elif scheme == "rimington":
            self.rb_rimington.setChecked(True)
        elif scheme == "aepli":
            self.rb_aepli.setChecked(True)
        elif scheme == "belmont":
            self.rb_belmont.setChecked(True)
        else:
            self.rb_newton.setChecked(True)

        # Create OK and Cancel buttons to dialog window
        self.buttons = QtGui.QDialogButtonBox(
            QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal, self)
        layout.addWidget(self.buttons)

        # Connect clicked on the OK button to the accept method
        self.buttons.accepted.connect(self.accept)

        # Connect clicked on the Cancel button to the reject method
        self.buttons.rejected.connect(self.reject)

    def get_scheme(self):

        """

        This method allows to get selected scheme by the user

        :return: str
            Selected scheme

        """

        if self.rb_newton.isChecked():
            return "newton"
        elif self.rb_castel.isChecked():
            return "castel"
        elif self.rb_rimington.isChecked():
            return "rimington"
        elif self.rb_aepli.isChecked():
            return "aepli"
        elif self.rb_belmont.isChecked():
            return "belmont"


class MrMusicApp(QtGui.QMainWindow, design.Ui_MainWindow):

    """

    This class represents interaction with users

    Attributes:
    ------------------
    path_to_image: boolean
        Path to loaded image by the user

    selected_scheme: str
        Selected scheme

    instrument: str
        Selected musical instrument (piano or guitar)

    music: AudioSegment
        Is the representation of result musical composition as the object of AudioSegment class

    sound: MediaPlayer
        Is the representation of result musical composition as the object of MediaPlayer class from vlc lib

    Methods:
    ------------------
    on_browse_image: is the method that calls when user select 'Load image' action in Menu 'File'

    on_select_scheme_dialog: is the method that calls when user select 'Select scheme' action in Menu 'Schemes'

    on_generate: is the method that calls when user clicked on 'Generate' button

    on_play: is the method that calls when user clicked on 'Play' button

    on_pause: is the method that calls when user clicked on 'Pause' button

    on_stop: is the method that calls when user clicked on 'Stop' button

    on_save: is the method that calls when user select 'Save' action in Menu 'File'

    on_set_piano: is the method that calls when user select 'Piano' action in Menu 'Instruments'

    on_set_guitar: is the method that calls when user select 'Guitar' action in Menu 'Instruments'

    get_russian_tonality: this method allows to translate english name of tonality to russian

    get_russian_color: this method allows to translate english name of color to russian

    """

    path_to_image = None
    selected_scheme = "newton"
    instrument = "piano"
    music = None
    sound = None

    def __init__(self):

        super(self.__class__, self).__init__()
        self.setupUi(self)

        # Get current working directory
        curr_dir = os.path.dirname(os.path.abspath(__file__))

        # Set style of graphicsView - is the area where shows loaded image
        self.graphicsView_LoadedImage.setStyleSheet("border-image: url(" + curr_dir +
                                                    "/images/image_default.png) 0 0 0 0 stretch stretch;")

        # Set default name of current scheme - newton scheme is the default scheme
        self.label_RScheme.setText(_translate("", "Ньютона", None))

        # Connect event of Generate button clicked with on_generate method
        self.pushButton_Generate.clicked.connect(self.on_generate, QtCore.Qt.QueuedConnection)

        # Connect event of Play button clicked with on_play method
        self.pushButton_Play.clicked.connect(self.on_play)

        # Connect event of Pause button clicked with on_pause method
        self.pushButton_Pause.clicked.connect(self.on_pause)

        # Connect event of Stop button clicked with on_stop method
        self.pushButton_Stop.clicked.connect(self.on_stop)

        # Connect event of selected 'Load image' action in Menu 'File' with the method on_browse_image
        self.action_loadImage.triggered.connect(self.on_browse_image)

        # Connect event of selected 'Select scheme' action in Menu 'Schemes' with the method on_select_scheme_dialog
        self.action_SelectScheme.triggered.connect(self.on_select_scheme_dialog)

        # Connect event of selected 'Piano' action in Menu 'Instruments' with the method on_set_piano
        self.action_Piano.triggered.connect(self.on_set_piano)

        # Connect event of selected 'Guitar' action in Menu 'Instruments' with the method on_set_guitar
        self.action_Guitar.triggered.connect(self.on_set_guitar)

        # Connect event of selected 'Save' action in Menu 'File' with the method on_save
        self.action_SaveSong.triggered.connect(self.on_save)

    def on_browse_image(self):

        """

        This is the method that calls when user select 'Load image' action in Menu 'File'

        """

        # Open select file name dialog and get path to selected image
        self.path_to_image = QtGui.QFileDialog.getOpenFileName(self, "Pick a folder", "",
                                                               "Image Files (*.png *.jpg *jpeg *jpe *.bmp)")

        # Is user select image
        if self.path_to_image:

            # Read selected image
            input_img = cv2.imread(str(self.path_to_image))

            # Get size of loaded image
            height, width = input_img.shape[:2]

            if height > 500 or width > 500:

                msg_box = QtGui.QMessageBox()
                msg_box.setIcon(QtGui.QMessageBox.Warning)
                msg_box.setWindowTitle(_translate("", "Загрузка изображения", None))
                msg_box.setText(_translate("", "Изображение не должно быть более 500x500", None))
                msg_box.exec_()

            else:

                # Show selected image to the user
                self.graphicsView_LoadedImage.setStyleSheet("border-image: url(" + self.path_to_image +
                                                        ") 0 0 0 0 stretch stretch;")

    def on_select_scheme_dialog(self):

        """

        This is the method that calls when user select 'Select scheme' action in Menu 'Schemes'

        """

        # Create the object of ChooseSchemeDialog class passing as the param current selected scheme
        choose_scheme_dialog = ChooseSchemeDialog(self.selected_scheme)

        # Execute the dialog window
        if choose_scheme_dialog.exec_():

            # Get selected scheme from ChooseSchemeDialog
            self.selected_scheme = choose_scheme_dialog.get_scheme()

            # Shows the user the selected scheme
            if self.selected_scheme == "castel":
                self.label_RScheme.setText(_translate("", "Кастеля", None))
            elif self.selected_scheme == "rimington":
                self.label_RScheme.setText(_translate("", "Римингтона", None))
            elif self.selected_scheme == "aepli":
                self.label_RScheme.setText(_translate("", "Эппли", None))
            elif self.selected_scheme == "belmont":
                self.label_RScheme.setText(_translate("", "Бельмонта", None))
            else:
                self.label_RScheme.setText(_translate("", "Ньютона", None))

    def on_generate(self):

        """

        This is the method that calls when user select 'Select scheme' action in Menu 'Schemes'

        """

        try:

            # Create the object of ImageToMusic class passing as the param path to loaded image
            image_to_music = ImageToMusic(str(self.path_to_image))

            # Generate composition by loaded image using image_to_music_characteristics method of ImageToMusic class
            # Passing as the param selected instrument and selected scheme
            #
            # Beside getting generated sound as the object of AudioSegment class
            # We get tonality and tempo of composition, and domination color of loaded image
            sound, tonality, tempo, domination_color = image_to_music.image_to_music_characteristics(
                str(self.instrument), str(self.selected_scheme))

            # Shows the domination color to the user
            self.label_RColor.setText(_translate("", self.get_russian_color(domination_color), None))

            # Shows the tempo of generated sound to the user
            self.label_RTempo.setText(_translate("", tempo, None))

            # Shows the tonality of generated sound to the user
            self.label_RTonality.setText(_translate("", self.get_russian_tonality(tonality), None))

            # Calculate duration of musical composition
            duration = round((len(sound) * 0.001) / 60, 1)

            # Shows the duration of generated sound to the user
            self.label_RDuration.setText(_translate("", str(duration) + " минуты", None))

            # Save composition to the default directory
            sound.export("sound.mp3", format='mp3')

            # Create the object of vlc.MediaPlayer class passing as the param name of sound to be played
            self.music = vlc.MediaPlayer("sound.mp3")

            self.sound = sound

            # Show message that sound has been generated
            msg_box = QtGui.QMessageBox()
            msg_box.setIcon(QtGui.QMessageBox.Information)
            msg_box.setWindowTitle(_translate("", "Генерация композиции", None))
            msg_box.setText(_translate("", "Композиция была сгенерирована", None))
            msg_box.exec_()

        except:

            # If something went wrong
            # Show error message to the user
            text = "Ошибка при генерации композиции."

            if (self.path_to_image == "") or (self.path_to_image is None):
                text += "\nНе загружено изображение."

            msg_box = QtGui.QMessageBox()
            msg_box.setIcon(QtGui.QMessageBox.Warning)
            msg_box.setWindowTitle(_translate("", "Генерация композиции", None))
            msg_box.setText(_translate("", text, None))
            msg_box.exec_()

    def on_play(self):

        """

        This is the method that calls when user clicked on 'Play' button

        """

        # If the sound has been generated
        if self.music is not None:

            # Play musical composition using play method of vlc.MediaPlayer class
            self.music.play()

        # If the sound hasnt been generated
        else:

            # Show error message to the user
            msg_box = QtGui.QMessageBox()
            msg_box.setIcon(QtGui.QMessageBox.Warning)
            msg_box.setWindowTitle(_translate("", " Проигрывание композиции", None))
            msg_box.setText(_translate("", "Нечего проигрывать. Композиция не была сгенерирована.", None))
            msg_box.exec_()

    def on_pause(self):

        """

        This is the method that calls when user clicked on 'Pause' button

        """

        # If the sound has been generated
        if self.music is not None:

            # Pause playing of musical composition using pause method of vlc.MediaPlayer class
            self.music.pause()

        # If the sound hasnt been generated
        else:

            # Show error message to the user
            msg_box = QtGui.QMessageBox()
            msg_box.setIcon(QtGui.QMessageBox.Warning)
            msg_box.setWindowTitle(_translate("", " Приостановка воспроизведения композиции", None))
            msg_box.setText(_translate("", "Нечего приостанавливать. Композиция не была сгенерирована.", None))
            msg_box.exec_()

    def on_stop(self):

        """

        This is the method that calls when user clicked on 'Stop' button

        """

        # If the sound has been generated
        if self.music is not None:

            # Stop playing of musical composition using stop method of vlc.MediaPlayer class
            self.music.stop()

        # If the sound hasnt been generated
        else:

            # Show error message to the user
            msg_box = QtGui.QMessageBox()
            msg_box.setIcon(QtGui.QMessageBox.Warning)
            msg_box.setWindowTitle(_translate("", " Остановка воспроизведения композиции", None))
            msg_box.setText(_translate("", "Нечего останавливать. Композиция не была сгенерирована.", None))
            msg_box.exec_()

    def on_save(self):

        """

        This is the method that calls when user select 'Save' action in Menu 'File'

        """

        # If the sound has been generated
        if self.sound is not None:

            # Open save file dialog and get selected path
            path_to_save_sound = QtGui.QFileDialog.getSaveFileName(self, "Pick a folder")

            # If user select the path
            if path_to_save_sound:

                # Save sound to the selected path in mp3 format
                self.sound.export(str(path_to_save_sound), format='mp3')

                # Shows message to the user
                msg_box = QtGui.QMessageBox()
                msg_box.setIcon(QtGui.QMessageBox.Information)
                msg_box.setWindowTitle(_translate("", "Сохранение композиции", None))
                msg_box.setText(_translate("", "Композиция была сохранена в " + path_to_save_sound, None))
                msg_box.exec_()

        # If the sound hasnt been generated
        else:

                # Shows error message to the user
                msg_box = QtGui.QMessageBox()
                msg_box.setIcon(QtGui.QMessageBox.Warning)
                msg_box.setWindowTitle(_translate("", "Сохранение композиции", None))
                msg_box.setText(_translate("", "Нечего сохранять. Для начал нужно сгененировать композицию.", None))
                msg_box.exec_()

    def on_set_piano(self):

        """

        This is the method that calls when user select 'Piano' action in Menu 'Instruments'

        """

        # Set that current instrument is the piano
        self.instrument = "piano"

        # Shows user current instrument
        self.label_RInstrument.setText(_translate("", "Фортепьяно", None))

    def on_set_guitar(self):

        """

        This is the method that calls when user select 'Guitar' action in Menu 'Instruments'

        """

        # Set that current instrument is the guitar
        self.instrument = "guitar"

        # Shows user current instrument
        self.label_RInstrument.setText(_translate("", "Гитара", None))

    @staticmethod
    def get_russian_tonality(tonality):

        """

        This method allows to translate english name of tonality to russian

        :param tonality: str
            English name of tonality

        :return: str
            Russian name of tonality

        """

        russian_tonality = ""
        if tonality == "c_major":
            russian_tonality = "До Мажор"
        elif tonality == "c_sharp_major":
            russian_tonality = "До Диез Мажор"
        elif tonality == "c_minor":
            russian_tonality = "До Минор"
        elif tonality == "c_sharp_minor":
            russian_tonality = "До Диез Минор"
        elif tonality == "d_major":
            russian_tonality = "Ре Мажор"
        elif tonality == "d_sharp_major":
            russian_tonality = "Ре Диез Мажор"
        elif tonality == "d_minor":
            russian_tonality = "Ре Минор"
        elif tonality == "d_sharp_minor":
            russian_tonality = "Ре Диез Минор"
        elif tonality == "e_major":
            russian_tonality = "Ми Мажор"
        elif tonality == "e_minor":
            russian_tonality = "Ми Минор"
        elif tonality == "f_major":
            russian_tonality = "Фа Мажор"
        elif tonality == "f_sharp_major":
            russian_tonality = "Фа Диез Мажор"
        elif tonality == "f_minor":
            russian_tonality = "Фа Минор"
        elif tonality == "f_sharp_minor":
            russian_tonality = "Фа Диез Минор"
        elif tonality == "g_major":
            russian_tonality = "Соль Мажор"
        elif tonality == "g_sharp_major":
            russian_tonality = "Соль Диез Мажор"
        elif tonality == "g_minor":
            russian_tonality = "Соль Минор"
        elif tonality == "g_sharp_minor":
            russian_tonality = "Соль Диез Минор"
        elif tonality == "a_major":
            russian_tonality = "Ля Мажор"
        elif tonality == "a_sharp_major":
            russian_tonality = "Ля Диез Мажор"
        elif tonality == "a_minor":
            russian_tonality = "Ля Минор"
        elif tonality == "a_sharp_minor":
            russian_tonality = "Ля Диез Минор"
        elif tonality == "h_major":
            russian_tonality = "Си Мажор"
        elif tonality == "h_minor":
            russian_tonality = "Си Минор"

        return russian_tonality

    @staticmethod
    def get_russian_color(en_color):

        """

        This method allows to translate english name of color to russian

        :param en_color: str
            English name of color

        :return: str
            Russian name of color

        """

        russian_color = ""
        if en_color == "blue":
            russian_color = "Синий"
        elif en_color == "greenblue":
            russian_color = "Сине-зелёный"
        elif en_color == "green":
            russian_color = "Зелёный"
        elif en_color == "yellowgreen":
            russian_color = "Жёлто-зелёный"
        elif en_color == "yellow":
            russian_color = "Жёлтый"
        elif en_color == "yelloworange":
            russian_color = "Жёлто-оранжевый"
        elif en_color == "orange":
            russian_color = "Оранжевый"
        elif en_color == "redorange":
            russian_color = "Красно-оранжевый"
        elif en_color == "red":
            russian_color = "Красный"
        elif en_color == "purple":
            russian_color = "Розовый(пурпурный)"
        elif en_color == "violet":
            russian_color = "Фиолетовый"
        elif en_color == "blueviolet":
            russian_color = "Фиолетово-синий"

        return russian_color


def main():

    # Create a new instance of QApplication
    app = QtGui.QApplication(sys.argv)

    # Create object of MrMusicApp class
    mr_music_app = MrMusicApp()

    # Show the form
    mr_music_app.show()

    # and execute the app
    app.exec_()

# if we're running file directly and not importing it
if __name__ == '__main__':

    # run the main function
    main()



