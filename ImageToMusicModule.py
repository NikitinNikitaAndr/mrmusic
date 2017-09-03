# This file contains the implementations of ImageToMusic class, five classes of color and notes schemes,
# ChromaticColors class, Gamma class, Note and Chord classes.

# ImageToMusic class allows to get sound (Object of AudioSegment class) by path to loaded image.
#
# NewtonScheme, CastelScheme, RimingtonScheme, AepliScheme, BelmontScheme classes is the classes that
# allows to get the note by color according to scheme of corresponding authors.
#
# ChromaticColors class allows to compare the chromatic scale and the color wheel.
#
# Gamma class allows to determine does the note contains in an appropriate gamma.
#
# Note class is the representation of real note. Attributes of this class is note_name, duration and octave.
#
# Chord class is the representation of real chord. Attributes of this class is chord_name, duration, type and mode
#
# Author: Nikitin Nikita <nikitin.nikitaa@outlook.com>
# Created: 20.12.2015. Last modified: 11.06.2016

from AnalysisImageModule import AnalysisImage
from CreateMusic import CreateMusicByXml


class ImageToMusic:

    """

    This class allows to get sound (Object of AudioSegment class) by path to loaded image.

    Attributes:
    ------------------
    path_to_image: str
        Is the path to loaded image.

    tempo: str
        Tempo of result sound

    tonality: str
        Tonality of result sound

    domination_color: str
        Domination color of loaded image

    mass_of_colors: array (list)
        Array of objects of PrimaryColor class (from AnalysisImageModule)

    Methods:
    ------------------
    image_to_music_characteristics: allows to get sound (Object of AudioSegment class) by path to loaded image.

    get_tonality: allows to get tonality of result sound.

    get_melody_sequence: allows to get melody sequence (array of objects of Note class)

    get_harmony_sequence: allows to get harmony sequence (array of objects of Chord class)

    create_xml_text: allows to create xml-text by array of notes (melody sequence), array of chords (harmony sequence),
                     tempo and tonality of result composition (sound).

    get_duration_by_saturation: allows to get duration of note by saturation of corresponding color.

    get_octave_by_brightness: allows to get octave of note by brightness of corresponding color.

    get_number_of_cycles: allows to get number of cycles by array of notes (melody sequence).

    """

    path_to_image = None
    tempo = None
    tonality = None
    domination_color = None
    mass_of_colors = None

    def __init__(self, _path_to_image):
        self.path_to_image = _path_to_image

    def image_to_music_characteristics(self, instrument, scheme):

        """

        This method allows to get sound (Object of AudioSegment class) by path to loaded image.

        :param instrument: str
            String that contains name of selected instrument (piano or guitar)

        :param scheme: str
            String that contains name of selected scheme (newton, castel, rimington, aepli or belmont)

        :return: generated sound (object of AudioSegment class), tonality of generated sound (string),
                 tempo of generated sound (string) and domination color of loaded image (string).

        """

        # Initialize object of AnalysisImage class, passing as the param path to loaded image
        analysis_image = AnalysisImage(self.path_to_image)

        # Get array of objects of PrimaryColor class using get_mass_of_colors method of AnalysisImage class
        prime_colors = analysis_image.get_mass_of_colors()

        # Get array of objects of PrimaryColor class with combining the same color sequence
        # It using static method combine_same_prime_pixels of AnalysisImage class
        # passing as the param array of objects of PrimaryColor class
        colors_with_params = AnalysisImage.combine_same_prime_pixels(prime_colors)

        # If the image is almost the same color
        if len(colors_with_params) < 10:

            # Get domination color of loaded image. Set return value to domination_color param of ImageToMusic class.
            # It using static method find_domination_color of AnalysisImage class
            # passing as the param array of objects of PrimaryColor class
            self.domination_color = AnalysisImage.find_domination_color(prime_colors)

            self.mass_of_colors = [self.domination_color]

            # Get tonality of result composition (sound). Set return value to tonality param of ImageToMusic class.
            # It using get_tonality method of ImageToMusic class
            # passing as the param string that contains name of selected scheme
            self.tonality = self.get_tonality(scheme)

            # If tonality is major
            if "major" in self.tonality:

                # Then tempo of result sound is 120 - The most typical tempo of major compositions
                self.tempo = "120"
            else:

                # Else tempo of result sound is 85 - The most typical tempo of minor compositions
                self.tempo = "85"

            # Get tonic
            note = self.tonality.split('_')

            # Create the array of notes that contains five tonic notes
            mass_of_notes = [Note(note[0], "4", "5"), Note(note[0], "4", "5"), Note(note[0], "4", "5"),
                             Note(note[0], "4", "5"), Note(note[0], "1", "5")]

            # Create the array of notes that contains five tonality chords
            mass_of_chords = [Chord(note[0], "4", "standard", note[1]), Chord(note[0], "4", "standard", note[1]),
                              Chord(note[0], "4", "standard", note[1]), Chord(note[0], "4", "standard", note[1]),
                              Chord(note[0], "1", "standard", note[1])]

        else:

            # Get domination color of loaded image. Set return value to domination_color param of ImageToMusic class.
            # It using static method find_domination_color of AnalysisImage class
            # passing as the param array of objects of PrimaryColor class
            self.domination_color = AnalysisImage.find_domination_color(colors_with_params)

            self.mass_of_colors = colors_with_params

            # Get tonality of result composition (sound). Set return value to tonality param of ImageToMusic class.
            # It using get_tonality method of ImageToMusic class
            # passing as the param string that contains name of selected scheme
            self.tonality = self.get_tonality(scheme)

            # If tonality is major
            if "major" in self.tonality:

                # Then tempo of result sound is 120 - The most typical tempo of major compositions
                self.tempo = "120"
            else:

                # Else tempo of result sound is 85 - The most typical tempo of minor compositions
                self.tempo = "85"

            # Get array of notes (Array of objects of Note class) using get_melody_sequence method of ImageToMusic class
            # Passing as the param string that contains name of selected scheme
            mass_of_notes = self.get_melody_sequence(scheme)

            # Get number of cycles using get_number_of_cycles static method of ImageToMusic class.
            # Passing as the param array of notes (Array of objects of Note class)
            number_of_cycles = int(ImageToMusic.get_number_of_cycles(mass_of_notes))

            # Get array of chord (of objects of Chord class) using get_harmony_sequence method of ImageToMusic class
            # Passing as the param number (int) - the number of cycles
            mass_of_chords = self.get_harmony_sequence(number_of_cycles)

        # Create xml text by mass_of_notes and mass_of_chords using create_xml_text method of ImageToMusic class.
        xml_text = self.create_xml_text(mass_of_notes, mass_of_chords)

        # Initialize object of CreateMusicByXml class passing as the params:
        #
        # The first param is boolean value is_from_file.
        # The value is False, because we have string that contains xml text
        #
        # The second param is path to file that contains xml text.
        # The value is None, because we dont need to load xml text from file
        #
        # The third param is string that contains xml text
        #
        # The fourth param is the string that contains name of selected instrument
        music = CreateMusicByXml(False, None, xml_text, instrument)

        # Get harmony (Object of AudioSegment class) using get_harmony method of CreateMusicByXml class
        harmony = music.get_harmony()

        # Get melody (Object of AudioSegment class) using get_melody method of CreateMusicByXml class
        melody = music.get_melody()

        # Concatenate melody and harmony components of musical composition
        # using static join_harmony_and_melody method of CreateMusicByXml class
        # Passing as the param creating melody and harmony components of musical composition
        sound = CreateMusicByXml.join_harmony_and_melody(harmony, melody)

        # Return generated sound (object of AudioSegment class), tonality of generated sound (string),
        # tempo of generated sound (string) and domination color of loaded image (string).
        return sound, self.tonality, self.tempo, self.domination_color

    def get_tonality(self, scheme):

        """

        This method allows to get tonality of result sound.
        It use NewtonScheme, CastelScheme, RimingtonScheme, AepliScheme and BelmontScheme classes

        :param scheme: str
            Name of selected scheme

        :return: str
            Name of tonality of result composition

        """

        # If domination color of image is white
        if self.domination_color is "white":

            # Then tonality is the most typical tonality - C Major
            tonality = "c_major"

        else:

            # Initialize objects of corresponding class by name of selected scheme
            scheme_local = None
            if scheme == "newton":
                scheme_local = NewtonScheme()
            elif scheme == "castel":
                scheme_local = CastelScheme()
            elif scheme == "rimington":
                scheme_local = RimingtonScheme()
            elif scheme == "aepli":
                scheme_local = AepliScheme()
            elif scheme == "belmont":
                scheme_local = BelmontScheme()

            # Get the name of tonality of result music composition
            # Using get_note_by_color method of class of selected scheme
            # Passing as the param the domination color
            tonality = scheme_local.get_note_by_color(self.domination_color)

            # If the domination color refers to the warm color group
            if ((self.domination_color is "yellow") or (self.domination_color is "yelloworange") or
                (self.domination_color is "orange") or (self.domination_color is "redorange") or
                    (self.domination_color is "red") or (self.domination_color is "purple")):

                # Then tonality is major
                tonality += "_major"

            elif ((self.domination_color is "blue") or (self.domination_color is "greenblue") or
                    (self.domination_color is "green") or (self.domination_color is "yellowgreen") or
                    (self.domination_color is "violet") or (self.domination_color is "blueviolet")):

                # Else tonality is minor
                tonality += "_minor"

        self.tonality = tonality

        return tonality

    def get_melody_sequence(self, scheme):

        """

        This method allows to get melody sequence (array of objects of Note class) by selected scheme

        :param scheme: str
            Name of selected scheme

        :return: array
            Array of objects of Note class

        """

        mass_of_notes = []  # result array

        # Initialize object of ChromaticColors class, passing as the param domination_color of loaded image
        # and the name of selected scheme
        chromatic_scale_vs_colors = ChromaticColors(self.domination_color, scheme)

        # for each color in array of primary colors
        for color in self.mass_of_colors:

            # If the name of current color is white - pause
            if color.clear_color is "white":

                # Then append to the result array of notes the object of Note class
                # Passing as the params:
                #
                # As the first param (name of note) - silence (keyword for pause note)
                #
                # As the second param duration of added note
                # it use get_duration_by_saturation method of ImageToMusic class
                #
                # As the third param (octave) - None, because pause has no octave
                mass_of_notes.append(Note("silence", ImageToMusic.get_duration_by_saturation(color.saturation), None))

            else:

                # If current color is not white then we need to append in the result array note
                # with name, octave and duration

                # Get note by name of current color using get_note_by_color method of ChromaticColors class
                # Passing as the param name of current color
                note_name = chromatic_scale_vs_colors.get_note_by_color(color.clear_color)

                # Check if gamma defines tonality param contains note define note_name param
                if Gamma.check_gamma(str(self.tonality), str(note_name)):

                    # If gamma contains note then we need to append note to the result array of notes
                    # Added element is the object of Note class
                    # Passing as the params:
                    #
                    # As the first param (name of note) - note_name
                    #
                    # As the second param duration of added note
                    # it use get_duration_by_saturation method of ImageToMusic class
                    #
                    # As the third param octave of added note, because pause has no octave
                    # it use get_octave_by_brightness method of ImageToMusic class
                    mass_of_notes.append(Note(note_name, ImageToMusic.get_duration_by_saturation(color.saturation),
                                              ImageToMusic.get_octave_by_brightness(color.brightness)))

        # Now we need to combine long sequence of silences (pauses) to one pause
        # And if the last note before pause is the same to the note after pause
        # We need to delete this (after pause) note from melody sequence

        notes = []  # the result array of notes
        last_note = None  # the last added note before pause
        is_added = True  # if note or pause was added

        # for each element in mass of notes
        for i in range(0, len(mass_of_notes)):

            # if current note is pause
            if mass_of_notes[i].get_note_name() == "silence":

                # if previous note is not pause then last note before pause if note by i-1 index
                if not (mass_of_notes[i - 1].get_note_name() == "silence"):
                    last_note = mass_of_notes[i - 1]

                # if is_added is True - it means that we need to append current pause
                if is_added:

                    # Then append current pause to the result array
                    notes.append(mass_of_notes[i])

            # if we dont have the last note before pause - it means that we dont found a long sequence of pauses yet
            # or it means that we have already processed a long sequence of pauses
            elif last_note == None:

                # Then we need to append current note to the result array of notes
                notes.append(mass_of_notes[i])

            # If we have the last note before pause we need to determine does the current note
            # (the first note after pause) is the same to the last note (the last note before pause)
            elif not (last_note.get_note_name() == mass_of_notes[i].get_note_name() and
                              last_note.get_octave() == mass_of_notes[i].get_octave()):

                # If the first note after pause is not equal to the last note before pause
                # We need to append current note to the result mass
                notes.append(mass_of_notes[i])

                # And we need to reset the variables, it shows that we have already processed a long sequence of pauses
                last_note = None
                is_added = True

            # If current and previous notes are the pause we dont need to add current pause to the result array of notes
            else:
                is_added = False

        result = []  # result mass

        # Now we need to combine long sequence of equal notes

        for i in range(0, len(notes)):

            # if there is a next element
            if i < len(notes) - 1:

                # if name of current note is not equal to name of next note
                if notes[i].note_name != notes[i+1].note_name:

                    # append element to the result mass
                    result.append(notes[i])

                # if duration of current note is not equal to duration of next note
                elif notes[i].duration != notes[i+1].duration:

                    # append element to the result mass
                    result.append(notes[i])

                # if octave of current note is not equal to octave of next note
                elif notes[i].octave != notes[i+1].octave:

                    # append element to the result mass
                    result.append(notes[i])

        return result

    def get_harmony_sequence(self, number_of_cycles):

        """

        This method allows to get harmony sequence (array of objects of Chord class).

        :param number_of_cycles: int
            The number of cycles of the result musical composition. It calculates by array of notes.

        :return: array
            Array of objects of Chord class

        """

        harmony_sequence = []  # the result array

        # Initialize object of Gamma class passing as the param tonality of result musical composition
        # So we get the gamma of tonality of result musical composition
        gamma = Gamma.get_gamma(self.tonality)

        # Mode of tonality - major or minor
        mode = None
        if "major" in self.tonality:
            mode = "major"
        else:
            mode = "minor"

        temp = 0  # Temporary variable that stores count of added chords

        stage = 0  # Stage of gamma - index of note in gamma

        # We need to append chords in the tact (cycle) according to the following rule:
        # First square (sequence of four tacts(cycles)) we need to fill of Tonality chords
        # Second square we need to fill of Dominant chords
        # Third and fourth squares we need to fill of Subdominant chords
        # After this we need to start over

        for i in range(0, number_of_cycles):

            # If we work with first square we need to append Tonality chord
            if temp < 4:

                # So the stage is 0 - 0 is the stage of Tonality chord
                stage = 0

            # If we work with second square we need to append Dominant chord
            elif temp >= 4 and temp < 8:

                # So the stage is 3 - 3 is the stage of Dominant chord
                stage = 3

            # If we work with third and fourth square we need to append Subdominant chord
            elif temp >= 8 and temp < 16:

                # So the stage is 4 - 4 is the stage of Subdominant chord
                stage = 4

            # Else we need to start over
            else:

                # So we need to reset variables to the initial state
                stage = 0
                temp = 0

            # Append the object of Chord class to the result mass of chords
            # Passing as the params:
            #
            # The first param - name of tonic of the chord.
            # We take note of the gamma according to the previously calculated stage
            #
            # The second param - duration of chord. For harmony is the semiminima
            #
            # The third param - type of chord (own or standard). We work to the standard chord
            #
            # The fourth param - mode of chord (major or minor). We passing mode variable
            harmony_sequence.append(Chord(gamma[stage], "4", "standard", mode))

            # Increase the count of added chords
            temp += 1

        return harmony_sequence

    def create_xml_text(self, mass_of_notes, mass_of_chords):

        """

        This method allows to create xml-text by array of notes (melody sequence), array of chords (harmony sequence),
        tempo and tonality of result composition (sound).

        :param mass_of_notes: array
            Array of objects of Note class - melody component of musical composition

        :param mass_of_chords: array
            Array of objects of Chord class - harmony component of musical composition

        :return: str
            Xml-text - is a formalized description of a musical composition

        """

        # First we need to append to the result xml-text tonality and tempo of musical composition
        xmltext = "<doc><tonality>" + self.tonality + "</tonality><tempo value=\"" + self.tempo + "\"></tempo><harmony>"

        # For each chord in array of chords
        for chord in mass_of_chords:

            # Append to the result xml-text duration, type, name and mode of current chord
            xmltext += ("<chord duration=\"" + chord.get_duration() + "\"><type value=\"" + chord.get_type() +
                       "\"/><chord_name value=\"" + chord.get_chord_name() + "\"/><mode value=\"" +
                       chord.get_mode() + "\"/></chord>")

        # Close hamony tag and open melody tag
        xmltext += "</harmony><melody>"

        # For each note in array of notes
        for note in mass_of_notes:

            # If current note is the pause
            if note.get_note_name() == "silence":

                # Append current pause to the result xml-text. Keyword for pause is the word silence
                xmltext += ("<note duration=\"" + note.get_duration() + "\"><note_name value=\"silence\"/></note>")

            # If current note is not pause
            else:

                # Append duration, name and octave of current note to the result xml-text
                xmltext += ("<note duration=\"" + note.get_duration() + "\"><note_name value=\"" +
                           note.get_note_name() + "\"/><octave value=\"" +
                           note.get_octave() + "\"/></note>")

        # Close melody tag and close tag doc which indicates that xml-text is finished
        xmltext += "</melody></doc>"

        return xmltext

    @staticmethod
    def get_duration_by_saturation(saturation):

        """

        This method allows to get duration of note by saturation of corresponding color.
        Duration is calculated according to the following rules:
        ------- if saturation is 0 or 1 - the duration is breve
        ------- if saturation is 2 - the duration is semiminima
        ------- if saturation is 3 - the duration is croma
        ------- if saturation is 4 - the duration is semicroma

        :param saturation: int
            Saturation of color

        :return: str
            Duration of note

        """

        duration = -1  # the result duration

        # if saturation is 0 or 1
        if (saturation == 0) or (saturation == 1):

            # the duration is breve
            duration = 2

        # if saturation is 2
        elif saturation is 2:

            # the duration is semiminima
            duration = 4

        # if saturation is 3
        elif saturation is 3:

            # the duration is croma
            duration = 8

        # if saturation is 4
        elif saturation is 4:

            # the duration is semicroma
            duration = 16

        return str(duration)

    @staticmethod
    def get_octave_by_brightness(brightness):

        """

        This method allows to get octave of note by brightness of corresponding color.
        Octave is calculated according to the following rules:

        :param brightness: int
            Brightness of corresponding color

        :return: str
            Octave of note

        """

        octave = - 1  # the result duration

        if brightness == 0:

            octave = 5

        else:

            octave = 4

        return str(octave)

    @staticmethod
    def get_number_of_cycles(notes):

        """

        This method allows to get number of cycles by array of notes (melody sequence).

        :param notes: array
            Array of notes (melody sequence).

        :return: float
            Number of cycles

        """

        number_of_cycles = float(0)  # the result number of cycles

        # For each note in array of notes
        for note in notes:

            # Addition current value of number_of_cycles and 1/duration of current note
            number_of_cycles = float(number_of_cycles + float(1 / float(note.duration)))

        # Round the result value of cycles
        return round(number_of_cycles + 0.5)


class NewtonScheme:

    """

    This class allows to get the note by color according to scheme of Isaac Newton

    Attributes:
    ------------------
    comparison_table: array
        Is the two-dimensional array first table of which contains colors and second table contains corresponding note

    Methods:
    ------------------
    get_note_by_color: allows to get note by color according to the comparison table of Isaac Newton

    """

    comparison_table = [["red", "c"], ["redorange", "c_sharp"], ["orange", "d"], ["yelloworange", "d_sharp"],
                        ["yellow", "e"], ["green", "f"], ["greenblue", "f_sharp"], ["blue", "g"],
                        ["blueviolet", "g_sharp"], ["violet", "a"], ["yellowgreen", "a_sharp"], ["purple", "h"]]

    def __init__(self):
        pass

    def get_note_by_color(self, color):

        """

        This method allows to get note by color according to the comparison table of Isaac Newton

        :param color: str
            Name of color

        :return: str
            Name of corresponding note

        """

        # Find the obtained color in comparison_table
        for couple in self.comparison_table:

            # If current color from comparison_table is equal to obtained color
            if couple[0] is color:

                # Then return corresponding note
                return couple[1]


class CastelScheme:

    """

    This class allows to get the note by color according to scheme of Louis-Bertrand Castel

    Attributes:
    ------------------
    comparison_table: array
        Is the two-dimensional array first table of which contains colors and second table contains corresponding note

    Methods:
    ------------------
    get_note_by_color: allows to get note by color according to the comparison table of Louis-Bertrand Castel

    """

    comparison_table = [["blue", "c"], ["greenblue", "c_sharp"], ["green", "d"], ["yellowgreen", "d_sharp"],
                        ["yellow", "e"], ["yelloworange", "f"], ["orange", "f_sharp"], ["red", "g"],
                        ["redorange", "g_sharp"], ["purple", "a"], ["blueviolet", "a_sharp"], ["violet", "h"]]

    def __init__(self):
        pass

    def get_note_by_color(self, color):

        """

        This method allows to get note by color according to the comparison table of Louis-Bertrand Castel

        :param color: str
            Name of color

        :return: str
            Name of corresponding note

        """

        # Find the obtained color in comparison_table
        for couple in self.comparison_table:

            # If current color from comparison_table is equal to obtained color
            if couple[0] is color:

                # Then return corresponding note
                return couple[1]


class RimingtonScheme:

    """

    This class allows to get the note by color according to scheme of A. Wallace Rimington

    Attributes:
    ------------------
    comparison_table: array
        Is the two-dimensional array first table of which contains colors and second table contains corresponding note

    Methods:
    ------------------
    get_note_by_color: allows to get note by color according to the comparison table of A. Wallace Rimington

    """

    comparison_table = [["red", "c"], ["yelloworange", "c_sharp"], ["redorange", "d"], ["orange", "d_sharp"],
                        ["yellow", "e"], ["yellowgreen", "f"], ["green", "f_sharp"], ["greenblue", "g"],
                        ["blueviolet", "g_sharp"], ["violet", "a"], ["blue", "a_sharp"], ["purple", "h"]]

    def __init__(self):
        pass

    def get_note_by_color(self, color):

        """

        This method allows to get note by color according to the comparison table of A. Wallace Rimington

        :param color: str
            Name of color

        :return: str
            Name of corresponding note

        """

        # Find the obtained color in comparison_table
        for couple in self.comparison_table:

            # If current color from comparison_table is equal to obtained color
            if couple[0] is color:

                # Then return corresponding note
                return couple[1]


class AepliScheme:

    """

    This class allows to get the note by color according to scheme of A. Aepli

    Attributes:
    ------------------
    comparison_table: array
        Is the two-dimensional array first table of which contains colors and second table contains corresponding note

    Methods:
    ------------------
    get_note_by_color: allows to get note by color according to the comparison table of A. Aepli

    """

    comparison_table = [["red", "c"], ["redorange", "c_sharp"], ["orange", "d"], ["yelloworange", "d_sharp"],
                        ["yellow", "e"], ["yellowgreen", "f"], ["green", "f_sharp"], ["greenblue", "g"],
                        ["purple", "g_sharp"], ["blue", "a"], ["blueviolet", "a_sharp"], ["violet", "h"]]

    def __init__(self):
        pass

    def get_note_by_color(self, color):

        """

        This method allows to get note by color according to the comparison table of A. Aepli

        :param color: str
            Name of color

        :return: str
            Name of corresponding note

        """

        # Find the obtained color in comparison_table
        for couple in self.comparison_table:

            # If current color from comparison_table is equal to obtained color
            if couple[0] is color:

                # Then return corresponding note
                return couple[1]


class BelmontScheme:

    """

    This class allows to get the note by color according to scheme of L. J. Belmont

    Attributes:
    ------------------
    comparison_table: array
        Is the two-dimensional array first table of which contains colors and second table contains corresponding note

    Methods:
    ------------------
    get_note_by_color: allows to get note by color according to the comparison table of L. J. Belmont

    """

    comparison_table = [["red", "c"], ["redorange", "c_sharp"], ["orange", "d"], ["yelloworange", "d_sharp"],
                        ["yellow", "e"], ["yellowgreen", "f"], ["green", "f_sharp"], ["greenblue", "g"],
                        ["blue", "g_sharp"], ["violet", "a"], ["purple", "a_sharp"], ["blueviolet", "h"]]

    def __init__(self):
        pass

    def get_note_by_color(self, color):

        """

        This method allows to get note by color according to the comparison table of L. J. Belmont

        :param color: str
            Name of color

        :return: str
            Name of corresponding note

        """

        # Find the obtained color in comparison_table
        for couple in self.comparison_table:

            # If current color from comparison_table is equal to obtained color
            if couple[0] is color:

                # Then return corresponding note
                return couple[1]


class ChromaticColors:

    """

    This class allows to compare the chromatic scale and the color wheel.

    Attributes:
    ------------------
    domination_color: str
        Is the domination color of loaded image

    comparison_mass: array
        Is the two-dimensional array first table of which contains colors and second table contains corresponding notes

    scheme: str
        Is the selected scheme

    Methods:
    ------------------
    initialization method realize comparing the chromatic scale and the color wheel.

    get_note_by_color: allows to get note by color according to the comparison mass

    """

    domination_color = None
    comparison_mass = []
    scheme = None

    def __init__(self, _domination_color, scheme):
        self.domination_color = _domination_color

        # Array of notes that contains twelve notes from C to H
        mass_of_notes = ["c", "c_sharp", "d", "d_sharp", "e", "f", "f_sharp", "g", "g_sharp", "a", "a_sharp", "h"]

        # Array of colors that contains twelve colors from blue to blueviolet
        mass_of_colors = ["blue", "greenblue", "green", "yellowgreen", "yellow", "yelloworange", "orange", "redorange",
                          "red", "purple", "violet", "blueviolet"]

        scheme_local = None  # the name of selected scheme
        if scheme == "newton":

            # Initialize object of NewtonScheme class if the selected scheme is newton
            scheme_local = NewtonScheme()
        elif scheme == "castel":

            # Initialize object of CastelScheme class if the selected scheme is castel
            scheme_local = CastelScheme()
        elif scheme == "rimington":

            # Initialize object of RimingtonScheme class if the selected scheme is rimington
            scheme_local = RimingtonScheme()
        elif scheme == "aepli":

            # Initialize object of AepliScheme class if the selected scheme is aepli
            scheme_local = AepliScheme()
        elif scheme == "belmont":

            # Initialize object of BelmontScheme class if the selected scheme is belmont
            scheme_local = BelmontScheme()

        # Get corresponding note to domination color - is the tonality
        tonality = scheme_local.get_note_by_color(self.domination_color)

        temp_mass = []  # Temporary array

        index_of_domination_color = -1  # Index of domination color in array of colors
        index_of_tonic = -1  # Index of tonic in array of notes

        # Find index of domination color in array of colors
        # And index of tonic in array of notes
        for i in range(0, len(mass_of_colors)):

            # If current color from array of colors is equal to domination color
            if mass_of_colors[i] is self.domination_color:

                # Then we found index of domination color
                index_of_domination_color = i

            # If current note from array of notes is equal to tonality
            if mass_of_notes[i] is tonality:

                # Then we found index of tonic
                index_of_tonic = i

        offset_colors = 0  # Offset of colors
        offset_notes = 0  # Offset of colors

        for i in range(0, len(mass_of_colors)):

            # If current color is located at the left of the domination color
            if ((i + index_of_domination_color) >= len(mass_of_colors)) and (offset_colors == 0):

                # Then we need to calculate offset of colors
                offset_colors = i + index_of_domination_color

            # If current note is located at the left of the tonic
            if ((i + index_of_tonic) >= len(mass_of_notes)) and (offset_notes == 0):

                # Then we need to calculate offset of notes
                offset_notes = i + index_of_tonic

            # Append color from array of colors by index = i + index_of_domination_color - offset_colors
            # And note from array of notes by index = i + index_of_tonic - offset_notes
            # to the result array
            #
            # If color or note are located at the right of domination color or tonic
            # then offset of colors or notes is equal to zero
            #
            # But if they are located at the left - then offset is not zero and we need to append all colors
            # at the left of domination color or tonic
            temp_mass.append([mass_of_colors[i + index_of_domination_color - offset_colors],
                              mass_of_notes[i + index_of_tonic - offset_notes]])

        self.comparison_mass = temp_mass

    def get_note_by_color(self, color):

        """

        This method allows to get note by color according to the comparison mass

        :param color: str
            Name of color

        :return: str
            Name of corresponding note

        """

        # Find the obtained color in comparison_table
        for couple in self.comparison_mass:

            # If current color from comparison_table is equal to obtained color
            if couple[0] is color:

                # Then return corresponding note
                return couple[1]


class Gamma:

    """

    This class allows to determine does the note contain in an appropriate gamma.

    Methods:
    ------------------
    check_gamma: allows to determine does the note contain in an appropriate gamma

    get_gamma: allows to get gamma (array of notes) by name of tonic

    """

    def __init__(self):
        pass

    @staticmethod
    def check_gamma(tonality, note):

        """

        This method allows to determine does the note contain in an appropriate gamma.

        :param tonality: str
            Name of tonic of gamma

        :param note: str
            Name of note

        :return: boolean
            True if note contains in gamma or False if note doesnt contain in gamma

        """

        # Get gamma by tonality
        gamma = Gamma.get_gamma(tonality)

        if note in gamma:
            return True
        else:
            return False

    @staticmethod
    def get_gamma(gamma):

        """

        This method allows to get gamma (array of notes) by name of tonic

        :param gamma: str
            Name of tonic of gamma

        :return: array
            Array of notes in gamma

        """

        result = None

        if gamma == str("c_major"):
            result = ["c", "d", "e", "f", "g", "a", "h"]
        elif gamma == str("c_sharp_major"):
            result = ["c_sharp", "d_sharp", "f", "f_sharp", "g_sharp", "a_sharp", "c"]
        elif gamma == str("d_major"):
            result = ["d", "e", "f_sharp", "g", "a", "h", "c_sharp"]
        elif gamma == str("d_sharp_major"):
            result = ["d_sharp", "f", "g", "g_sharp", "a_sharp", "c", "d"]
        elif gamma == str("e_major"):
            result = ["e", "f_sharp", "g_sharp", "a", "h", "c_sharp", "d_sharp"]
        elif gamma == str("f_major"):
            result = ["f", "g", "a", "a_sharp", "c", "d", "e"]
        elif gamma == str("f_sharp_major"):
            result = ["f_sharp", "g_sharp", "a_sharp", "h", "c_sharp", "d_sharp", "f"]
        elif gamma == str("g_major"):
            result = ["g", "a", "h", "c", "d", "e", "f_sharp"]
        elif gamma == str("g_sharp_major"):
            result = ["g_sharp", "a_sharp", "c", "c_sharp", "d_sharp", "f", "g"]
        elif gamma == str("a_major"):
            result = ["a", "h", "c_sharp", "d", "e", "f_sharp", "g_sharp"]
        elif gamma == str("a_sharp_major"):
            result = ["a_sharp", "c", "d", "d_sharp", "f", "g", "a"]
        elif gamma == str("h_major"):
            result = ["h", "c_sharp", "d_sharp", "e", "f_sharp", "g_sharp", "a_sharp"]
        elif gamma == str("c_minor"):
            result = ["c", "d", "d_sharp", "f", "g", "g_sharp", "a_sharp"]
        elif gamma == str("c_sharp_minor"):
            result = ["c_sharp", "d_sharp", "e", "f_sharp", "g_sharp", "a", "h"]
        elif gamma == str("d_minor"):
            result = ["d", "e", "f", "g", "a", "a_sharp", "c"]
        elif gamma == str("d_sharp_minor"):
            result = ["d_sharp", "f", "f_sharp", "g_sharp", "a_sharp", "h", "c_sharp"]
        elif gamma == str("e_minor"):
            result = ["e", "f_sharp", "g", "a", "h", "c", "d"]
        elif gamma == str("f_minor"):
            result = ["f", "g", "g_sharp", "a_sharp", "c", "c_sharp", "d_sharp"]
        elif gamma == str("f_sharp_minor"):
            result = ["f_sharp", "g_sharp", "a", "h", "c_sharp", "d", "e"]
        elif gamma == str("g_minor"):
            result = ["g", "a", "a_sharp", "c", "d", "d_sharp", "f"]
        elif gamma == str("g_sharp_minor"):
            result = ["g_sharp", "a_sharp", "h", "c_sharp", "d_sharp", "e", "f_sharp"]
        elif gamma == str("a_minor"):
            result = ["a", "h", "c", "d", "e", "f", "g"]
        elif gamma == str("a_sharp_minor"):
            result = ["a_sharp", "c", "c_sharp", "d_sharp", "f", "f_sharp", "g_sharp"]
        elif gamma == str("h_minor"):
            result = ["h", "c_sharp", "d", "e", "f_sharp", "g", "a"]

        return result


class Note:

    """

    This class is the representation of real note

    Attributes:
    ------------------
    note_name: str
        Is the name of note

    duration: str
        Is the duration of note

    octave: str
        Is the octave of note

    Methods:
    ------------------
    set_note_name: allows to set the value of note_name

    set_duration: allows to set the value of duration

    set_octave: allows to set the value of octave

    get_note_name: allows to get the value of note_name

    get_duration: allows to get the value of duration

    get_octave: allows to get the value of octave

    """

    note_name = None
    duration = None
    octave = None

    def __init__(self, _note_name, _duration, _octave):
        self.set_note_name(_note_name)
        self.set_duration(_duration)
        self.set_octave(_octave)

    def set_note_name(self, _note_name):
        self.note_name = _note_name

    def set_duration(self, _duration):
        self.duration = _duration

    def set_octave(self, _octave):
        self.octave = _octave

    def get_note_name(self):
        return self.note_name

    def get_duration(self):
        return self.duration

    def get_octave(self):
        return self.octave


class Chord:

    """

    This class is the representation of real note

    Attributes:
    ------------------
    chord_name: str
        Is the name of tonic of the chord

    duration: str
        Is the duration of chord

    type: str
        Is the type of chord (own or standard)

    mode: str
        Is the mode of chord (major or minor)

    Methods:
    ------------------
    set_chord_name: allows to set the value of chord_name

    set_duration: allows to set the value of duration

    set_type: allows to set the value of type

    set_mode: allows to set the value of mode

    get_chord_name: allows to get the value of chord_name

    get_duration: allows to get the value of duration

    get_type: allows to get the value of type

    get_mode: allows to get the value of mode

    """

    chord_name = None
    duration = None
    type = None
    mode = None

    def __init__(self, _chord_name, _duration, _type, _mode):
        self.set_chord_name(_chord_name)
        self.set_duration(_duration)
        self.set_type(_type)
        self.set_mode(_mode)

    def set_chord_name(self, _chord_name):
        self.chord_name = _chord_name

    def set_duration(self, _duration):
        self.duration = _duration

    def set_type(self, _type):
        self.type = _type

    def set_mode(self, _mode):
        self.mode = _mode

    def get_chord_name(self):
        return self.chord_name

    def get_duration(self):
        return self.duration

    def get_type(self):
        return self.type

    def get_mode(self):
        return self.mode

