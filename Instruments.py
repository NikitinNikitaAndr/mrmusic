# This file contains the implementation of two classes - Piano and Guitar.
# Each class allows to create chords and notes using with real Piano and Guitar sound.
# Author: Nikitin Nikita <nikitin.nikitaa@outlook.com>
# Created: 15.11.2015. Last modified: 05.06.2016

from pydub import AudioSegment
import os


class Piano:

    """
    Piano class allows to create chords and notes using with real Piano sound. It use Piano samples.

    Attributes:
    ------------------
    tempo: str
        Tempo of generating sound (60, 120 e.t.c)

    path_to_directory: str
        Path to current directory of python script. Need to get path to samples folder.

    Methods:
    ------------------
    get_default_chord: allows to get default chord with Piano sound

        * c - generate Piano C chord with predetermined octave, harmony and duration;
        * c_sharp - generate Piano C sharp chord with predetermined octave, harmony and duration;
        * d - generate Piano D chord with predetermined octave, harmony and duration;
        * d_sharp - generate Piano D sharp chord with predetermined octave, harmony and duration;
        * e - generate Piano E chord with predetermined octave, harmony and duration;
        * f - generate Piano F chord with predetermined octave, harmony and duration;
        * f_sharp - generate Piano F sharp chord with predetermined octave, harmony and duration;
        * g - generate Piano G chord with predetermined octave, harmony and duration;
        * g_sharp - generate Piano G sharp chord with predetermined octave, harmony and duration;
        * a - generate Piano A chord with predetermined octave, harmony and duration;
        * a_sharp - generate Piano A sharp chord with predetermined octave, harmony and duration;
        * h - generate Piano H chord with predetermined octave, harmony and duration;

    get_note: allows to get default note with Piano sound

        * c - generate Piano C note with predetermined octave and duration;
        * c_sharp - generate Piano C sharp note with predetermined octave and duration;
        * d - generate Piano D note with predetermined octave and duration;
        * d_sharp - generate Piano D sharp note with predetermined octave and duration;
        * e - generate Piano E note with predetermined octave and duration;
        * f - generate Piano F note with predetermined octave and duration;
        * f_sharp - generate Piano F sharp note with predetermined octave and duration;
        * g - generate Piano G note with predetermined octave and duration;
        * g_sharp - generate Piano G sharp note with predetermined octave and duration;
        * a - generate Piano A note with predetermined octave and duration;
        * a_sharp - generate Piano A sharp note with predetermined octave and duration;
        * h - generate Piano H note with predetermined octave and duration;

    get_not_default_chord: allows to get not default chord with determine notes and their durations


    Static methods
    ------------------
    join_two_parts: allows to concatenate two AudioSegments parts

        * s - concatenate parts in sequence mode
        * p - concatenate parts in parallel mode

    calculate_duration: it private method, using inside class to calculate duration of AudioSegment part

    Private methods - methods, that use inside class
    ------------------
    create_c_chord: allows to get Piano C chord with predetermined octave, harmony and duration

    create_c_sharp_chord: allows to get Piano C sharp chord with predetermined octave, harmony and duration

    create_d_chord: allows to get Piano D chord with predetermined octave, harmony and duration

    create_d_sharp_chord: allows to get Piano D sharp chord with predetermined octave, harmony and duration

    create_e_chord: allows to get Piano E chord with predetermined octave, harmony and duration

    create_f_chord: allows to get Piano F chord with predetermined octave, harmony and duration

    create_f_sharp_chord: allows to get Piano F sharp chord with predetermined octave, harmony and duration

    create_g_chord: allows to get Piano G chord with predetermined octave, harmony and duration

    create_g_sharp_chord: allows to get Piano G sharp chord with predetermined octave, harmony and duration

    create_a_chord: allows to get Piano A chord with predetermined octave, harmony and duration

    create_a_sharp_chord: allows to get Piano A sharp chord with predetermined octave, harmony and duration

    create_h_chord: allows to get Piano H chord with predetermined octave, harmony and duration

    """

    tempo = 0
    path_to_directory = ""

    def __init__(self, tempo):
        self.tempo = tempo
        self.path_to_directory = os.path.dirname(os.path.abspath(__file__))

    def get_default_chord(self, chord, octave, duration, harmony):

        """
        Allows to get default chord with Piano sound

        :param chord: str

            * c - generate Piano C chord;
            * c_sharp - generate Piano C sharp chord;
            * d - generate Piano D chord;
            * d_sharp - generate Piano D sharp chord;
            * e - generate Piano E chord;
            * f - generate Piano F chord;
            * f_sharp - generate Piano F sharp;
            * g - generate Piano G chord;
            * g_sharp - generate Piano G sharp;
            * a - generate Piano A chord;
            * a_sharp - generate Piano A sharp;
            * h - generate Piano H chord;

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of chosen chord

        """

        result = None

        if chord == "c":
            result = self.create_c_chord(octave, duration, harmony)
        elif chord == "c_sharp":
            result = self.create_c_sharp_chord(octave, duration, harmony)
        elif chord == "d":
            result = self.create_d_chord(octave, duration, harmony)
        elif chord == "d_sharp":
            result = self.create_d_sharp_chord(octave, duration, harmony)
        elif chord == "e":
            result = self.create_e_chord(octave, duration, harmony)
        elif chord == "f":
            result = self.create_f_chord(octave, duration, harmony)
        elif chord == "f_sharp":
            result = self.create_f_sharp_chord(octave, duration, harmony)
        elif chord == "g":
            result = self.create_g_chord(octave, duration, harmony)
        elif chord == "g_sharp":
            result = self.create_g_sharp_chord(octave, duration, harmony)
        elif chord == "a":
            result = self.create_a_chord(octave, duration, harmony)
        elif chord == "a_sharp":
            result = self.create_a_sharp_chord(octave, duration, harmony)
        elif chord == "h":
            result = self.create_h_chord(octave, duration, harmony)

        return result

    def get_note(self, note, octave, duration):

        """
        Allows to get default note with Piano sound

        :param note: str
            Name of creating note

            * c - generate Piano C note;
            * c_sharp - generate Piano C sharp note;
            * d - generate Piano D note;
            * d_sharp - generate Piano D sharp note;
            * e - generate Piano E note;
            * f - generate Piano F note;
            * f_sharp - generate Piano F sharp;
            * g - generate Piano G note;
            * g_sharp - generate Piano G sharp note;
            * a - generate Piano A note;
            * a_sharp - generate Piano A sharp note;
            * h - generate Piano H note;

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :return: object of AudioSegment class which contain sound of chosen note

        """

        result = None

        if note == "c":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/piano/" + str(octave) + "/c.wav")
        elif note == "c_sharp":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/piano/" + str(octave) + "/c_sharp.wav")
        elif note == "d":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/piano/" + str(octave) + "/d.wav")
        elif note == "d_sharp":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/piano/" + str(octave) + "/d_sharp.wav")
        elif note == "e":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/piano/" + str(octave) + "/e.wav")
        elif note == "f":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/piano/" + str(octave) + "/f.wav")
        elif note == "f_sharp":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/piano/" + str(octave) + "/f_sharp.wav")
        elif note == "g":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/piano/" + str(octave) + "/g.wav")
        elif note == "g_sharp":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/piano/" + str(octave) + "/g_sharp.wav")
        elif note == "a":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/piano/" + str(octave) + "/a.wav")
        elif note == "a_sharp":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/piano/" + str(octave) + "/a_sharp.wav")
        elif note == "h":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/piano/" + str(octave) + "/h.wav")
        elif note == "silence":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/piano/silence.wav")

        return Piano.calculate_duration(result, duration, self.tempo)

    def create_c_chord(self, octave, duration, harmony):

        """

        Allows to get Piano C chord with predetermined octave, harmony and duration

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of C chord

        P.S.
        --------------
        C chord consist of C, G, C (next octave), E (next octave), G (next octave) notes in major musical harmony
            and
        C, G, C (next octave), D sharp (next octave), G (next octave) notes in minor musical harmony

        overlay - method of AudioSegment class, that allows to concatenate in parallel mode AudioSegment parts

        """

        result = None

        if str(harmony) == "major":
            c_note = AudioSegment.from_file(self.path_to_directory + "/samples/piano/"+str(octave)+"/c.wav")
            temp1 = c_note.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/g.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/c.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/e.wav"))
            result = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/g.wav"))
        elif str(harmony) == "minor":
            c_note = AudioSegment.from_file(self.path_to_directory + "/samples/piano/"+str(octave)+"/c.wav")
            temp1 = c_note.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/g.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/c.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/d_sharp.wav"))
            result = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/g.wav"))

        return Piano.calculate_duration(result, duration, self.tempo)

    def create_c_sharp_chord(self, octave, duration, harmony):

        """

        Allows to get Piano C sharp chord with predetermined octave, harmony and duration

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of C sharp chord

        P.S.
        --------------
        C sharp chord consist of C sharp, G sharp, C sharp (next octave), F (next octave), G sharp (next octave)
                                                                notes in major musical harmony
            and
        C sharp, G sharp, C sharp (next octave), E (next octave), G sharp (next octave)
                                                                notes in minor musical harmony

        overlay - method of AudioSegment class, that allows to concatenate in parallel mode AudioSegment parts

        """

        result = None

        if str(harmony) == "major":
            c_note = AudioSegment.from_file(self.path_to_directory + "/samples/piano/"+str(octave)+"/c_sharp.wav")
            temp1 = c_note.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/g_sharp.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/c_sharp.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/f.wav"))
            result = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/g_sharp.wav"))
        elif str(harmony) == "minor":
            c_note = AudioSegment.from_file(self.path_to_directory + "/samples/piano/"+str(octave)+"/c_sharp.wav")
            temp1 = c_note.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/g_sharp.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/piano/"+str(octave+1)+"/c_sharp.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/e.wav"))
            result = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/g_sharp.wav"))

        return Piano.calculate_duration(result, duration, self.tempo)

    def create_d_chord(self, octave, duration, harmony):

        """

        Allows to get Piano D chord with predetermined octave, harmony and duration

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of D chord

        P.S.
        --------------
        D chord consist of D, A, D (next octave), F sharp (next octave) notes in major musical harmony
            and
        D, A, D (next octave), F (next octave) notes in minor musical harmony

        overlay - method of AudioSegment class, that allows to concatenate in parallel mode AudioSegment parts

        """

        result = None

        if str(harmony) == "major":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/piano/"+str(octave)+"/d.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/piano/"+str(octave)+"/a.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/d.wav"))
            result = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/f_sharp.wav"))
        elif str(harmony) == "minor":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/piano/"+str(octave)+"/d.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/piano/"+str(octave)+"/a.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/d.wav"))
            result = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/f.wav"))

        return Piano.calculate_duration(result, duration, self.tempo)

    def create_d_sharp_chord(self, octave, duration, harmony):

        """

        Allows to get Piano D sharp chord with predetermined octave, harmony and duration

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of D sharp chord

        P.S.
        --------------
        D chord consist of D sharp, A sharp, D sharp (next octave), G (next octave) notes in major musical harmony
            and
        D sharp, A sharp, D sharp (next octave), F sharp (next octave) notes in minor musical harmony

        overlay - method of AudioSegment class, that allows to concatenate in parallel mode AudioSegment parts

        """

        result = None

        if str(harmony) == "major":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/piano/"+str(octave)+"/d_sharp.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/piano/"+str(octave)+"/a_sharp.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/d_sharp.wav"))
            result = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/g.wav"))
        elif str(harmony) == "minor":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/piano/"+str(octave)+"/d_sharp.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/piano/"+str(octave)+"/a_sharp.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/d_sharp.wav"))
            result = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/f_sharp.wav"))

        return Piano.calculate_duration(result, duration, self.tempo)

    def create_e_chord(self, octave, duration, harmony):

        """

        Allows to get Piano E chord with predetermined octave, harmony and duration

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of E chord

        P.S.
        --------------
        E chord consist of E (previous octave), H (previous octave), E, G sharp, H, E (next octave)
                                                            notes in major musical harmony
            and
        E (previous octave), H (previous octave), E, G, H, E (next octave)
                                                            notes in minor musical harmony

        overlay - method of AudioSegment class, that allows to concatenate in parallel mode AudioSegment parts

        """

        result = None

        if str(harmony) == "major":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/piano/"+str(octave - 1)+"/e.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/piano/"+str(octave - 1)+"/h.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/e.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/g_sharp.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/h.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/e.wav"))
        elif str(harmony) == "minor":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/piano/"+str(octave - 1)+"/e.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/piano/"+str(octave - 1)+"/h.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/e.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/g.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/h.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/e.wav"))

        return Piano.calculate_duration(result, duration, self.tempo)

    def create_f_chord(self, octave, duration, harmony):

        """

        Allows to get Piano F chord with predetermined octave, harmony and duration

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of F chord

        P.S.
        --------------
        F chord consist of F (previous octave), C, F, A, C(next octave), F (next octave)
                                                            notes in major musical harmony
            and
        F (previous octave), C, F, G sharp, C(next octave), F (next octave)
                                                            notes in minor musical harmony

        overlay - method of AudioSegment class, that allows to concatenate in parallel mode AudioSegment parts

        """

        result = None

        if str(harmony) == "major":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/piano/"+str(octave - 1)+"/f.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/piano/"+str(octave)+"/c.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/f.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/a.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/c.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/f.wav"))
        elif str(harmony) == "minor":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/piano/"+str(octave - 1)+"/f.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/piano/"+str(octave)+"/c.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/f.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/g_sharp.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/c.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/f.wav"))

        return Piano.calculate_duration(result, duration, self.tempo)

    def create_f_sharp_chord(self, octave, duration, harmony):

        """

        Allows to get Piano F sharp chord with predetermined octave, harmony and duration

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of F sharp chord

        P.S.
        --------------
        F sharp chord consist of F sharp (previous octave), C sharp, F sharp, A sharp, C sharp (next octave),
                                            F sharp (next octave) notes in major musical harmony
            and
        F sharp (previous octave), C sharp, F sharp, A, C sharp (next octave), F sharp (next octave)
                                                                    notes in minor musical harmony

        overlay - method of AudioSegment class, that allows to concatenate in parallel mode AudioSegment parts

        """

        result = None

        if str(harmony) == "major":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/piano/"+str(octave - 1)+"/f_sharp.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/piano/"+str(octave)+"/c_sharp.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/f_sharp.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/a_sharp.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/c_sharp.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/f_sharp.wav"))
        elif str(harmony) == "minor":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/piano/"+str(octave - 1)+"/f_sharp.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/piano/"+str(octave)+"/c_sharp.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/f_sharp.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/a.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/c_sharp.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/f_sharp.wav"))

        return Piano.calculate_duration(result, duration, self.tempo)

    def create_g_chord(self, octave, duration, harmony):

        """

        Allows to get Piano G chord with predetermined octave, harmony and duration

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of G chord

        P.S.
        --------------
        G chord consist of G (previous octave), D, G, H, D (next octave), G (next octave)
                                                                    notes in major musical harmony
            and
        G (previous octave), D, G, A sharp, D (next octave), G (next octave) notes in minor musical harmony

        overlay - method of AudioSegment class, that allows to concatenate in parallel mode AudioSegment parts

        """

        result = None

        if str(harmony) == "major":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/piano/"+str(octave - 1)+"/g.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/piano/"+str(octave)+"/d.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/g.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/h.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/d.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/g.wav"))
        elif str(harmony) == "minor":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/piano/"+str(octave - 1)+"/g.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/piano/"+str(octave)+"/d.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/g.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/a_sharp.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/d.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/g.wav"))

        return Piano.calculate_duration(result, duration, self.tempo)

    def create_g_sharp_chord(self, octave, duration, harmony):

        """

        Allows to get Piano G sharp chord with predetermined octave, harmony and duration

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of G sharp chord

        P.S.
        --------------
        G sharp chord consist of G sharp (previous octave), D sharp, G sharp, C (next octave), D sharp (next octave),
                                                            G sharp (next octave) notes in major musical harmony
            and
        G sharp (previous octave), D sharp, G sharp, H, D sharp (next octave),
                                                            G sharp (next octave) notes in minor musical harmony

        overlay - method of AudioSegment class, that allows to concatenate in parallel mode AudioSegment parts

        """

        result = None

        if str(harmony) == "major":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/piano/"+str(octave - 1)+"/g_sharp.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/piano/"+str(octave)+"/d_sharp.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/g_sharp.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/c.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/d_sharp.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/g_sharp.wav"))
        elif str(harmony) == "minor":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/piano/"+str(octave - 1)+"/g_sharp.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/piano/"+str(octave)+"/d_sharp.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/g_sharp.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/h.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/d_sharp.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/g_sharp.wav"))

        return Piano.calculate_duration(result, duration, self.tempo)

    def create_a_chord(self, octave, duration, harmony):

        """

        Allows to get Piano A chord with predetermined octave, harmony and duration

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of A chord

        P.S.
        --------------
        A chord consist of A (previous octave), E, A, C sharp (next octave), E (next octave), A (next octave)
                                                                    notes in major musical harmony
            and
        A (previous octave), E, A, C (next octave), E (next octave), A (next octave) notes in minor musical harmony

        overlay - method of AudioSegment class, that allows to concatenate in parallel mode AudioSegment parts

        """

        result = None

        if str(harmony) == "major":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/piano/"+str(octave - 1)+"/a.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/piano/"+str(octave)+"/e.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/a.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/c_sharp.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/e.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave+1)+"/a.wav"))
        elif str(harmony) == "minor":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/piano/"+str(octave - 1)+"/a.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/piano/"+str(octave)+"/e.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/a.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/c.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/e.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/a.wav"))

        return Piano.calculate_duration(result, duration, self.tempo)

    def create_a_sharp_chord(self, octave, duration, harmony):

        """

        Allows to get Piano A sharp chord with predetermined octave, harmony and duration

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of A sharp chord

        P.S.
        --------------
        A sharp chord consist of A sharp (previous octave), F, A sharp, D (next octave), F (next octave),
                                                    A sharp (next octave) notes in major musical harmony
            and
        A sharp (previous octave), F, A sharp, C sharp (next octave), F (next octave),
                                                    A sharp (next octave) notes in minor musical harmony

        overlay - method of AudioSegment class, that allows to concatenate in parallel mode AudioSegment parts

        """

        result = None

        if str(harmony) == "major":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/piano/"+str(octave - 1)+"/a_sharp.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/piano/"+str(octave)+"/f.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/a_sharp.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/d.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/f.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/a_sharp.wav"))
        elif str(harmony) == "minor":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/piano/"+str(octave - 1)+"/a_sharp.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/piano/"+str(octave)+"/f.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/a_sharp.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/c_sharp.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/f.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/a_sharp.wav"))

        return Piano.calculate_duration(result, duration, self.tempo)

    def create_h_chord(self, octave, duration, harmony):

        """

        Allows to get Piano H chord with predetermined octave, harmony and duration

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of H chord

        P.S.
        --------------
        H chord consist of H (previous octave), F sharp, H, D sharp (next octave), F sharp (next octave)
                                                                    notes in major musical harmony
            and
        H (previous octave), F sharp, H, D (next octave), F sharp (next octave) notes in minor musical harmony

        overlay - method of AudioSegment class, that allows to concatenate in parallel mode AudioSegment parts

        """

        result = None

        if str(harmony) == "major":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/piano/"+str(octave - 1)+"/h.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/piano/"+str(octave)+"/f_sharp.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/h.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/d_sharp.wav"))
            result = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/f_sharp.wav"))
        elif str(harmony) == "minor":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/piano/"+str(octave - 1)+"/h.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/piano/"+str(octave)+"/f_sharp.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave)+"/h.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/d.wav"))
            result = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/piano/"+str(octave + 1)+"/f_sharp.wav"))

        return Piano.calculate_duration(result, duration, self.tempo)

    def get_not_default_chord(self, notes_, duration):

        """

        Allows to get not default chord with determine notes and their durations

        :param notes_: array
            Array (list) of notes. Each elements of array must contain string in format <name of note>,<octave>:

            * <name of note>
            Name of note:
                ** c - piano C note;
                ** c_sharp - piano C sharp note;
                ** d - piano D note;
                ** d_sharp - piano D sharp note;
                ** e - piano E note;
                ** f - piano F note;
                ** f_sharp - piano F sharp;
                ** g - piano G note;
                ** g_sharp - piano G sharp note;
                ** a - piano A note;
                ** a_sharp - piano A sharp note;
                ** h - piano H note;

            * <octave>
            Octave of corresponding note
                ** 2 - second octave
                ** 3 - third octave
                ** 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :return: object of AudioSegment class which contain sound of chord

        """

        # Split each elements of input array by symbol ,
        # In result we get array of array of string.
        # Each elements of its array is array which contain two elements:
        # first element ([0][0]) - name of note. Second ([0][1]) - octave of corresponding note
        notes = [[]]
        for item in notes_:
            temp = item.split(",")
            notes.append(temp)

        del notes[0]  # Delete first element, because its empty
        i = 2  # i = 2, because before start loop, we concatenate first and second elements of array

        result = AudioSegment.from_file(self.path_to_directory + "/samples/piano/" + notes[0][1] + "/" +
                                        notes[0][0] + ".wav")
        result = result.overlay(AudioSegment.from_file(self.path_to_directory + "/samples/piano/" + notes[1][1] +
                                                       "/" + notes[1][0] + ".wav"))

        while i < len(notes):
            # Concatenate current and previous element of array in parallel mode
            result = result.overlay(AudioSegment.from_file(self.path_to_directory + "/samples/piano/" +
                                                           notes[i][1] + "/" + notes[i][0] + ".wav"))
            i += 1

        return Piano.calculate_duration(result, duration, self.tempo)

    @staticmethod
    def join_two_parts(first_part, second_part, mode):

        """

        Allows to concatenate two AudioSegments parts

        :param first_part: AudioSegment object
            First part of whole AudioSegment object, that we need to get

        :param second_part: AudioSegment object
            Second part of whole AudioSegment object, that we need to get

        :param mode: str
            Concatenating mode

            * s - sequence mode
            * p - parallel mode

        :return: whole AudioSegment object, that contain two segments, concatenated in sequence or parallel mode

        """

        if mode == "s":
            result = first_part + second_part
        elif mode == "p":
            result = first_part.overlay(second_part)

        return result

    @staticmethod
    def calculate_duration(audio_segment, duration, tempo):

        """

        Private method, using inside class to calculate duration of AudioSegment part

        :param audio_segment: AudioSegment object
            Full AudioSegment object, that corresponding semibreve note (1) in 60 tempo

        :param duration: str
            Duration of AudioSegment part, that we need to get in result

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param tempo:
            Tempo of AudioSegment part, that we need to get in result

        :return: Clipped AudioSegment object

        """

        new_size = float((120 / float(tempo)) * 2) / float(duration) * 1000

        result = audio_segment[:new_size]  # Getting first new_size second of AudioSegment object

        return result


class Guitar:

    """

    Guitar class allows to create chords and notes using with real Guitar sound. It use Piano samples.

    Attributes:
    ------------------
    tempo: str
        Tempo of generating sound (60, 120 e.t.c)

    path_to_directory: str
        Path to current directory of python script. Need to get path to samples folder.

    Methods:
    ------------------
    get_default_chord: allows to get default chord with Guitar sound

        * c - generate Guitar C chord with predetermined octave, harmony and duration;
        * c_sharp - generate Guitar C sharp chord with predetermined octave, harmony and duration;
        * d - generate Guitar D chord with predetermined octave, harmony and duration;
        * d_sharp - generate Guitar D sharp chord with predetermined octave, harmony and duration;
        * e - generate Guitar E chord with predetermined octave, harmony and duration;
        * f - generate Guitar F chord with predetermined octave, harmony and duration;
        * f_sharp - generate Guitar F sharp chord with predetermined octave, harmony and duration;
        * g - generate Guitar G chord with predetermined octave, harmony and duration;
        * g_sharp - generate Guitar G sharp chord with predetermined octave, harmony and duration;
        * a - generate Guitar A chord with predetermined octave, harmony and duration;
        * a_sharp - generate Guitar A sharp chord with predetermined octave, harmony and duration;
        * h - generate Guitar H chord with predetermined octave, harmony and duration;

    get_note: allows to get default note with Piano sound

        * c - generate Guitar C note with predetermined octave and duration;
        * c_sharp - generate Guitar C sharp note with predetermined octave and duration;
        * d - generate Guitar D note with predetermined octave and duration;
        * d_sharp - generate Guitar D sharp note with predetermined octave and duration;
        * e - generate Guitar E note with predetermined octave and duration;
        * f - generate Guitar F note with predetermined octave and duration;
        * f_sharp - generate Guitar F sharp note with predetermined octave and duration;
        * g - generate Guitar G note with predetermined octave and duration;
        * g_sharp - generate Guitar G sharp note with predetermined octave and duration;
        * a - generate Guitar A note with predetermined octave and duration;
        * a_sharp - generate Guitar A sharp note with predetermined octave and duration;
        * h - generate Guitar H note with predetermined octave and duration;

    get_not_default_chord: allows to get not default chord with determine notes and their durations


    Static methods
    ------------------
    join_two_parts: allows to concatenate two AudioSegments parts

        * s - concatenate parts in sequence mode
        * p - concatenate parts in parallel mode

    calculate_duration: it private method, using inside class to calculate duration of AudioSegment part

    Private methods - methods, that use inside class
    ------------------
    create_c_chord: allows to get Guitar C chord with predetermined octave, harmony and duration

    create_c_sharp_chord: allows to get Guitar C sharp chord with predetermined octave, harmony and duration

    create_d_chord: allows to get Guitar D chord with predetermined octave, harmony and duration

    create_d_sharp_chord: allows to get Guitar D sharp chord with predetermined octave, harmony and duration

    create_e_chord: allows to get Guitar E chord with predetermined octave, harmony and duration

    create_f_chord: allows to get Guitar F chord with predetermined octave, harmony and duration

    create_f_sharp_chord: allows to get Guitar F sharp chord with predetermined octave, harmony and duration

    create_g_chord: allows to get Guitar G chord with predetermined octave, harmony and duration

    create_g_sharp_chord: allows to get Guitar G sharp chord with predetermined octave, harmony and duration

    create_a_chord: allows to get Guitar A chord with predetermined octave, harmony and duration

    create_a_sharp_chord: allows to get Guitar A sharp chord with predetermined octave, harmony and duration

    create_h_chord: allows to get Guitar H chord with predetermined octave, harmony and duration

    """

    tempo = 0
    path_to_directory = ""

    def __init__(self, tempo):
        self.tempo = tempo
        self.path_to_directory = os.path.dirname(os.path.abspath(__file__))

    def get_default_chord(self, chord, octave, duration, harmony):

        """

        Allows to get default chord with Guitar sound

        :param chord: str

            * c - generate Guitar C chord;
            * c_sharp - generate Guitar C sharp chord;
            * d - generate Guitar D chord;
            * d_sharp - generate Guitar D sharp chord;
            * e - generate Guitar E chord;
            * f - generate Guitar F chord;
            * f_sharp - generate Guitar F sharp;
            * g - generate Guitar G chord;
            * g_sharp - generate Guitar G sharp;
            * a - generate Guitar A chord;
            * a_sharp - generate Guitar A sharp;
            * h - generate Guitar H chord;

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of chosen chord

        """

        result = None

        if chord == "c":
            result = self.create_c_chord(octave, duration, harmony)
        elif chord == "c_sharp":
            result = self.create_c_sharp_chord(octave, duration, harmony)
        elif chord == "d":
            result = self.create_d_chord(octave, duration, harmony)
        elif chord == "d_sharp":
            result = self.create_d_sharp_chord(octave, duration, harmony)
        elif chord == "e":
            result = self.create_e_chord(octave, duration, harmony)
        elif chord == "f":
            result = self.create_f_chord(octave, duration, harmony)
        elif chord == "f_sharp":
            result = self.create_f_sharp_chord(octave, duration, harmony)
        elif chord == "g":
            result = self.create_g_chord(octave, duration, harmony)
        elif chord == "g_sharp":
            result = self.create_g_sharp_chord(octave, duration, harmony)
        elif chord == "a":
            result = self.create_a_chord(octave, duration, harmony)
        elif chord == "a_sharp":
            result = self.create_a_sharp_chord(octave, duration, harmony)
        elif chord == "h":
            result = self.create_h_chord(octave, duration, harmony)

        return result

    def get_note(self, note, octave, duration):

        """

        Allows to get default note with Guitar sound

        :param note: str
            Name of creating note

            * c - generate Guitar C note;
            * c_sharp - generate Guitar C sharp note;
            * d - generate Guitar D note;
            * d_sharp - generate Guitar D sharp note;
            * e - generate Guitar E note;
            * f - generate Guitar F note;
            * f_sharp - generate Guitar F sharp;
            * g - generate Guitar G note;
            * g_sharp - generate Guitar G sharp note;
            * a - generate Guitar A note;
            * a_sharp - generate Guitar A sharp note;
            * h - generate Guitar H note;

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :return: object of AudioSegment class which contain sound of chosen note

        """

        result = None

        if note == "c":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/" + str(octave) + "/c.wav")
        elif note == "c_sharp":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/" + str(octave) + "/c_sharp.wav")
        elif note == "d":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/" + str(octave) + "/d.wav")
        elif note == "d_sharp":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/" + str(octave) + "/d_sharp.wav")
        elif note == "e":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/" + str(octave) + "/e.wav")
        elif note == "f":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/" + str(octave) + "/f.wav")
        elif note == "f_sharp":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/" + str(octave) + "/f_sharp.wav")
        elif note == "g":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/" + str(octave) + "/g.wav")
        elif note == "g_sharp":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/" + str(octave) + "/g_sharp.wav")
        elif note == "a":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/" + str(octave) + "/a.wav")
        elif note == "a_sharp":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/" + str(octave) + "/a_sharp.wav")
        elif note == "h":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/" + str(octave) + "/h.wav")
        elif note == "silence":
            result = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/silence.wav")

        return Piano.calculate_duration(result, duration, self.tempo)

    def create_c_chord(self, octave, duration, harmony):

        """

        Allows to get Guitar C chord with predetermined octave, harmony and duration

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of C chord

        P.S.
        --------------
        C chord consist of C, G, C (next octave), E (next octave), G (next octave) notes in major musical harmony
            and
        C, G, C (next octave), D sharp (next octave), G (next octave) notes in minor musical harmony

        overlay - method of AudioSegment class, that allows to concatenate in parallel mode AudioSegment parts

        """

        result = None

        if str(harmony) == "major":
            c_note = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/"+str(octave)+"/c.wav")
            temp1 = c_note.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/g.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/c.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/e.wav"))
            result = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/g.wav"))
        elif str(harmony) == "minor":
            c_note = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/"+str(octave)+"/c.wav")
            temp1 = c_note.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/g.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/c.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/d_sharp.wav"))
            result = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/g.wav"))

        return Piano.calculate_duration(result, duration, self.tempo)

    def create_c_sharp_chord(self, octave, duration, harmony):

        """

        Allows to get Guitar C sharp chord with predetermined octave, harmony and duration

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of C sharp chord

        P.S.
        --------------
        C sharp chord consist of C sharp, G sharp, C sharp (next octave), F (next octave), G sharp (next octave)
                                                                notes in major musical harmony
            and
        C sharp, G sharp, C sharp (next octave), E (next octave), G sharp (next octave)
                                                                notes in minor musical harmony

        overlay - method of AudioSegment class, that allows to concatenate in parallel mode AudioSegment parts

        """

        result = None

        if str(harmony) == "major":
            c_note = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/"+str(octave)+"/c_sharp.wav")
            temp1 = c_note.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/g_sharp.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/c_sharp.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/f.wav"))
            result = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/g_sharp.wav"))
        elif str(harmony) == "minor":
            c_note = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/"+str(octave)+"/c_sharp.wav")
            temp1 = c_note.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/g_sharp.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/c_sharp.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/e.wav"))
            result = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/g_sharp.wav"))

        return Piano.calculate_duration(result, duration, self.tempo)

    def create_d_chord(self, octave, duration, harmony):

        """

        Allows to get Guitar D chord with predetermined octave, harmony and duration

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of D chord

        P.S.
        --------------
        D chord consist of D, A, D (next octave), F sharp (next octave) notes in major musical harmony
            and
        D, A, D (next octave), F (next octave) notes in minor musical harmony

        overlay - method of AudioSegment class, that allows to concatenate in parallel mode AudioSegment parts

        """

        result = None

        if str(harmony) == "major":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/"+str(octave)+"/d.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/guitar/"+str(octave)+"/a.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/d.wav"))
            result = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/f_sharp.wav"))
        elif str(harmony) == "minor":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/"+str(octave)+"/d.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/guitar/"+str(octave)+"/a.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/d.wav"))
            result = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/f.wav"))

        return Piano.calculate_duration(result, duration, self.tempo)

    def create_d_sharp_chord(self, octave, duration, harmony):

        """

        Allows to get Guitar D sharp chord with predetermined octave, harmony and duration

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of D sharp chord

        P.S.
        --------------
        D chord consist of D sharp, A sharp, D sharp (next octave), G (next octave) notes in major musical harmony
            and
        D sharp, A sharp, D sharp (next octave), F sharp (next octave) notes in minor musical harmony

        overlay - method of AudioSegment class, that allows to concatenate in parallel mode AudioSegment parts

        """

        result = None

        if str(harmony) == "major":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/"+str(octave)+"/d_sharp.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/guitar/"+str(octave)+"/a_sharp.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/d_sharp.wav"))
            result = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/g.wav"))
        elif str(harmony) == "minor":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/"+str(octave)+"/d_sharp.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/guitar/"+str(octave)+"/a_sharp.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/d_sharp.wav"))
            result = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/f_sharp.wav"))

        return Piano.calculate_duration(result, duration, self.tempo)

    def create_e_chord(self, octave, duration, harmony):

        """

        Allows to get Guitar E chord with predetermined octave, harmony and duration

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of E chord

        P.S.
        --------------
        E chord consist of E (previous octave), H (previous octave), E, G sharp, H, E (next octave)
                                                            notes in major musical harmony
            and
        E (previous octave), H (previous octave), E, G, H, E (next octave)
                                                            notes in minor musical harmony

        overlay - method of AudioSegment class, that allows to concatenate in parallel mode AudioSegment parts

        """

        result = None

        if str(harmony) == "major":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/"+str(octave - 1)+"/e.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/guitar/"+str(octave - 1)+"/h.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/e.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/g_sharp.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/h.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/e.wav"))
        elif str(harmony) == "minor":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/"+str(octave - 1)+"/e.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/guitar/"+str(octave - 1)+"/h.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/e.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/g.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/h.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/e.wav"))

        return Piano.calculate_duration(result, duration, self.tempo)

    def create_f_chord(self, octave, duration, harmony):

        """

        Allows to get Guitar F chord with predetermined octave, harmony and duration

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of F chord

        P.S.
        --------------
        F chord consist of F (previous octave), C, F, A, C(next octave), F (next octave)
                                                            notes in major musical harmony
            and
        F (previous octave), C, F, G sharp, C(next octave), F (next octave)
                                                            notes in minor musical harmony

        overlay - method of AudioSegment class, that allows to concatenate in parallel mode AudioSegment parts

        """

        result = None

        if str(harmony) == "major":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/"+str(octave - 1)+"/f.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/guitar/"+str(octave)+"/c.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/f.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/a.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/c.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/f.wav"))
        elif str(harmony) == "minor":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/"+str(octave - 1)+"/f.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/guitar/"+str(octave)+"/c.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/f.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/g_sharp.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/c.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/f.wav"))

        return Piano.calculate_duration(result, duration, self.tempo)

    def create_f_sharp_chord(self, octave, duration, harmony):

        """

        Allows to get Guitar F sharp chord with predetermined octave, harmony and duration

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of F sharp chord

        P.S.
        --------------
        F sharp chord consist of F sharp (previous octave), C sharp, F sharp, A sharp, C sharp (next octave),
                                            F sharp (next octave) notes in major musical harmony
            and
        F sharp (previous octave), C sharp, F sharp, A, C sharp (next octave), F sharp (next octave)
                                                                    notes in minor musical harmony

        overlay - method of AudioSegment class, that allows to concatenate in parallel mode AudioSegment parts

        """
        result = None

        if str(harmony) == "major":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/"+str(octave - 1)+"/f_sharp.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/guitar/"+str(octave)+"/c_sharp.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/f_sharp.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/a_sharp.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/c_sharp.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/f_sharp.wav"))
        elif str(harmony) == "minor":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/"+str(octave - 1)+"/f_sharp.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/guitar/"+str(octave)+"/c_sharp.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/f_sharp.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/a.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/c_sharp.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/f_sharp.wav"))

        return Piano.calculate_duration(result, duration, self.tempo)

    def create_g_chord(self, octave, duration, harmony):

        """

        Allows to get Guitar G chord with predetermined octave, harmony and duration

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of G chord

        P.S.
        --------------
        G chord consist of G (previous octave), D, G, H, D (next octave), G (next octave)
                                                                    notes in major musical harmony
            and
        G (previous octave), D, G, A sharp, D (next octave), G (next octave) notes in minor musical harmony

        overlay - method of AudioSegment class, that allows to concatenate in parallel mode AudioSegment parts

        """

        result = None

        if str(harmony) == "major":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/"+str(octave - 1)+"/g.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/guitar/"+str(octave)+"/d.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/g.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/h.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/d.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/g.wav"))
        elif str(harmony) == "minor":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/"+str(octave - 1)+"/g.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/guitar/"+str(octave)+"/d.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/g.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/a_sharp.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/d.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/g.wav"))

        return Piano.calculate_duration(result, duration, self.tempo)

    def create_g_sharp_chord(self, octave, duration, harmony):

        """

        Allows to get Guitar G sharp chord with predetermined octave, harmony and duration

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of G sharp chord

        P.S.
        --------------
        G sharp chord consist of G sharp (previous octave), D sharp, G sharp, C (next octave), D sharp (next octave),
                                                            G sharp (next octave) notes in major musical harmony
            and
        G sharp (previous octave), D sharp, G sharp, H, D sharp (next octave),
                                                            G sharp (next octave) notes in minor musical harmony

        overlay - method of AudioSegment class, that allows to concatenate in parallel mode AudioSegment parts

        """

        result = None

        if str(harmony) == "major":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/"+str(octave - 1)+"/g_sharp.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/guitar/"+str(octave)+"/d_sharp.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/g_sharp.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/c.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/d_sharp.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/g_sharp.wav"))
        elif str(harmony) == "minor":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/"+str(octave - 1)+"/g_sharp.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/guitar/"+str(octave)+"/d_sharp.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/g_sharp.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/h.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/d_sharp.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/g_sharp.wav"))

        return Piano.calculate_duration(result, duration, self.tempo)

    def create_a_chord(self, octave, duration, harmony):

        """

        Allows to get Guitar A chord with predetermined octave, harmony and duration

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of A chord

        P.S.
        --------------
        A chord consist of A (previous octave), E, A, C sharp (next octave), E (next octave), A (next octave)
                                                                    notes in major musical harmony
            and
        A (previous octave), E, A, C (next octave), E (next octave), A (next octave) notes in minor musical harmony

        overlay - method of AudioSegment class, that allows to concatenate in parallel mode AudioSegment parts

        """

        result = None

        if str(harmony) == "major":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/"+str(octave - 1)+"/a.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/guitar/"+str(octave)+"/e.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/a.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/c_sharp.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/e.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave+1)+"/a.wav"))
        elif str(harmony) == "minor":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/"+str(octave - 1)+"/a.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/guitar/"+str(octave)+"/e.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/a.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/c.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/e.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/a.wav"))

        return Piano.calculate_duration(result, duration, self.tempo)

    def create_a_sharp_chord(self, octave, duration, harmony):

        """

        Allows to get Guitar A sharp chord with predetermined octave, harmony and duration

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of A sharp chord

        P.S.
        --------------
        A sharp chord consist of A sharp (previous octave), F, A sharp, D (next octave), F (next octave),
                                                    A sharp (next octave) notes in major musical harmony
            and
        A sharp (previous octave), F, A sharp, C sharp (next octave), F (next octave),
                                                    A sharp (next octave) notes in minor musical harmony

        overlay - method of AudioSegment class, that allows to concatenate in parallel mode AudioSegment parts

        """

        result = None

        if str(harmony) == "major":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/"+str(octave - 1)+"/a_sharp.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/guitar/"+str(octave)+"/f.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/a_sharp.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/d.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/f.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/a_sharp.wav"))
        elif str(harmony) == "minor":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/"+str(octave - 1)+"/a_sharp.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/guitar/"+str(octave)+"/f.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/a_sharp.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/c_sharp.wav"))
            temp4 = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/f.wav"))
            result = temp4.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/a_sharp.wav"))

        return Piano.calculate_duration(result, duration, self.tempo)

    def create_h_chord(self, octave, duration, harmony):

        """

        Allows to get Guitar H chord with predetermined octave, harmony and duration

        :param octave: str
            Octave of generating chord

            * 2 - second octave
            * 3 - third octave
            * 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param harmony: str
            Musical harmony of generating chord

            * major - major musical harmony
            * minor - minor musical harmony

        :return: object of AudioSegment class which contain sound of H chord

        P.S.
        --------------
        H chord consist of H (previous octave), F sharp, H, D sharp (next octave), F sharp (next octave)
                                                                    notes in major musical harmony
            and
        H (previous octave), F sharp, H, D (next octave), F sharp (next octave) notes in minor musical harmony

        overlay - method of AudioSegment class, that allows to concatenate in parallel mode AudioSegment parts

        """

        result = None

        if str(harmony) == "major":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/"+str(octave - 1)+"/h.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/guitar/"+str(octave)+"/f_sharp.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/h.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/d_sharp.wav"))
            result = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/f_sharp.wav"))
        elif str(harmony) == "minor":
            temp = AudioSegment.from_file(self.path_to_directory + "/samples/guitar/"+str(octave - 1)+"/h.wav")
            temp1 = temp.overlay(AudioSegment.from_file(
                   self.path_to_directory + "/samples/guitar/"+str(octave)+"/f_sharp.wav"))
            temp2 = temp1.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave)+"/h.wav"))
            temp3 = temp2.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/d.wav"))
            result = temp3.overlay(AudioSegment.from_file(
                    self.path_to_directory + "/samples/guitar/"+str(octave + 1)+"/f_sharp.wav"))

        return Piano.calculate_duration(result, duration, self.tempo)

    def get_not_default_chord(self, notes_, duration):

        """

        Allows to get not default chord with determine notes and their durations

        :param notes_: array
            Array (list) of notes. Each elements of array must contain string in format <name of note>,<octave>:

            * <name of note>
            Name of note:
                ** c - Guitar C note;
                ** c_sharp - Guitar C sharp note;
                ** d - Guitar D note;
                ** d_sharp - Guitar D sharp note;
                ** e - Guitar E note;
                ** f - Guitar F note;
                ** f_sharp - Guitar F sharp;
                ** g - Guitar G note;
                ** g_sharp - Guitar G sharp note;
                ** a - Guitar A note;
                ** a_sharp - Guitar A sharp note;
                ** h - Guitar H note;

            * <octave>
            Octave of corresponding note
                ** 2 - second octave
                ** 3 - third octave
                ** 4 - fourth octave

        :param duration: str
            Duration of generating chord

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :return: object of AudioSegment class which contain sound of chord

        """

        # Split each elements of input array by symbol,
        # In result we get array of array of string.
        # Each elements of its array is array which contain two elements:
        # first element ([0][0]) - name of note. Second ([0][1]) - octave of corresponding note
        notes = [[]]
        for item in notes_:
            temp = item.split(",")
            notes.append(temp)

        del notes[0]  # Delete first element, because its empty
        i = 2  # i = 2, because before start loop, we concatenate first and second elements of array

        result = AudioSegment.from_file(self.path_to_directory + "/samples/piano/" + notes[0][1] + "/" +
                                        notes[0][0] + ".wav")
        result = result.overlay(AudioSegment.from_file(self.path_to_directory + "/samples/piano/" + notes[1][1] +
                                                       "/" + notes[1][0] + ".wav"))

        while i < len(notes):
            # Concatenate current and previous element of array in parallel mode
            result = result.overlay(AudioSegment.from_file(self.path_to_directory + "/samples/piano/" +
                                                           notes[i][1] + "/" + notes[i][0] + ".wav"))
            i += 1

        return Piano.calculate_duration(result, duration, self.tempo)

    @staticmethod
    def join_two_parts(first_part, second_part, mode):

        """

        Allows to concatenate two AudioSegments parts

        :param first_part: AudioSegment object
            First part of whole AudioSegment object, that we need to get

        :param second_part: AudioSegment object
            Second part of whole AudioSegment object, that we need to get

        :param mode: str
            Concatenating mode

            * s - sequence mode
            * p - parallel mode

        :return: whole AudioSegment object, that contain two segments, concatenated in sequence or parallel mode

        """

        if mode == "s":
            result = first_part + second_part
        elif mode == "p":
            result = first_part.overlay(second_part)

        return result

    @staticmethod
    def calculate_duration(audio_segment, duration, tempo):

        """

        Private method, using inside class to calculate duration of AudioSegment part

        :param audio_segment: AudioSegment object
            Full AudioSegment object, that corresponding semibreve note (1) in 60 tempo

        :param duration: str
            Duration of AudioSegment part, that we need to get in result

            * 1 - semibreve note
            * 2 - breve note
            * 4 - semiminima note
            * 8 - croma note
            * 16 - semicroma note
            * 32 - biscroma note
            * 64 - semibiscroma note

        :param tempo:
            Tempo of AudioSegment part, that we need to get in result

        :return: Clipped AudioSegment object

        """

        new_size = float((120 / float(tempo)) * 2) / float(duration) * 1000

        result = audio_segment[:new_size]  # Getting first new_size second of AudioSegment object

        return result
