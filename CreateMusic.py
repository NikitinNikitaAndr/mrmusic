# This file contains the implementation of CreateMusicByXml class.
# This class allows to create the music (melody and harmony) by xml text, which can be obtained after image analysis.
#
# Author: Nikitin Nikita <nikitin.nikitaa@outlook.com>
# Created: 30.11.2015. Last modified: 05.06.2016

from bs4 import BeautifulSoup
from Instruments import Piano, Guitar


class CreateMusicByXml:

    """

    CreateMusicByXml class allows to create melody and harmony components of music.
    It also allows concatenate melody and harmony components into single musical composition.

    Attributes:
    ------------------
    is_from_file: boolean
        A flag that shows whether to load the text from a file (True) or from string (False)

    path_to_file: str
        Path to xml file that contains xml text of musical composition.

    xml_text: str
        String that contains xml text of musical composition.

    instrument: str
        String that contains selected musical instrument (piano or guitar)

    Methods:
    ------------------
    get_harmony: allows to get harmony part of musical composition by xml text.

    get_melody: allows to get melody part of musical composition by xml text.

    join_harmony_and_melody: allows concatenate melody and harmony components into single musical composition.

    """
    is_from_file = False
    path_to_file = None
    xml_text = None
    instrument = None

    def __init__(self, is_from_file_, path_to_file_, xml_text_, instrument_):
        self.is_from_file = is_from_file_
        self.instrument = instrument_

        if is_from_file_:
            self.path_to_file = path_to_file_
        else:
            self.xml_text = xml_text_

    def get_harmony(self):
        """

        Allows to get harmony part of musical composition by xml text.

        :return: object of AudioSegment class that contains harmony part of musical composition.

        """

        chords_audio_segment = []  # result mass of AudioSegment representation of chords

        # if xml text must be loaded from a file
        if self.is_from_file:
            txt = open(self.path_to_file)
            xml_music_notation = BeautifulSoup(txt, "xml")
        else:
            xml_music_notation = BeautifulSoup(self.xml_text, "xml")

        # Find in xml text into harmony tag all chord tags
        chords = xml_music_notation.doc.harmony.findAll("chord")

        # Get value of tempo tag, that represents tempo of generated sound
        tempo = xml_music_notation.doc.tempo["value"]

        # Selected required musical instrument
        instrument_local = None
        if self.instrument == "piano":

            # Create object of Piano class (from Instruments module)
            # passing as the param tempo of composition
            instrument_local = Piano(int(float(tempo)))
        elif self.instrument == "guitar":

            # Create object of Guitar class (from Instruments module)
            # passing as the param tempo of composition
            instrument_local = Guitar(int(float(tempo)))

        # For each chord tag in xml text
        for chord in chords:

            # Get type of chord (standard or own)
            chord_type = chord.type["value"]

            # Get duration of chord
            duration = chord["duration"]

            if chord_type == "standard":

                # Get name of current chord
                chord_name = chord.chord_name["value"]

                # Get the musical mode of current chord (major or minor)
                mode = chord.mode["value"]

                # Using method get_default_chord of Piano or Guitar class
                # getting default chord, passing as the params name of chord, octave
                # duration, and musical mode of chord
                temp = instrument_local.get_default_chord(chord_name, 3, duration, mode)

                # Then we need to append received chord into result mass of chord
                chords_audio_segment.append(temp)

            elif chord_type == "own":

                # Get notes of chord
                notes = chord.notes["value"].split(";")

                # Using method get_not_default_chord of Piano or Guitar class
                # getting not default chord, passing as the params notes and duration of chord
                temp = instrument_local.get_not_default_chord(notes, duration)

                # Then we need to append received chord into result mass of chord
                chords_audio_segment.append(temp)

        # Now we need to concatenate mass of chords into single musical composition

        i = 2  # Because we concatenate first and second chord before started the loop

        # Concatenate first and second chord before started the loop
        # symbol s indicates that we need to concatenate musical parts in sequence mod
        result = Piano.join_two_parts(chords_audio_segment[0], chords_audio_segment[1], "s")

        # Concatenate all chords from mass of chords
        while i < len(chords_audio_segment):
            result = Piano.join_two_parts(result, chords_audio_segment[i], "s")
            i += 1

        # Decrease volume of chords
        res = result - 6
        return res

    def get_melody(self):
        """

        Allows to get melody part of musical composition by xml text.

        :return: object of AudioSegment class that contains melody part of musical composition.

        """

        melody_audio_segment = []  # result mass of AudioSegment representation of chords

        # if xml text must be loaded from a file
        if self.is_from_file:
            txt = open(self.path_to_file)
            xml_music_notation = BeautifulSoup(txt, "xml")
        else:
            xml_music_notation = BeautifulSoup(self.xml_text, "xml")

        # Find in xml text into melody tag all note tags
        notes = xml_music_notation.doc.melody.findAll("note")

        # Get value of tempo tag, that represents tempo of generated sound
        tempo = xml_music_notation.doc.tempo["value"]

        # Selected required musical instrument
        instrument_local = None
        if self.instrument == "piano":

            # Create object of Piano class (from Instruments module)
            # passing as the param tempo of composition
            instrument_local = Piano(int(float(tempo)))
        elif self.instrument == "guitar":

            # Create object of Guitar class (from Instruments module)
            # passing as the param tempo of composition
            instrument_local = Guitar(int(float(tempo)))

        # For each note tag in xml text
        for note in notes:

            # Get name of current note
            note_name = note.note_name["value"]

            # Get duration of current note
            duration = note["duration"]

            # If current note is pause
            if note_name == "silence":

                # Using method get_note of Piano or Guitar class
                # getting note, passing as the params name of note (silence),
                # octave is None for pause and duration of pause
                temp = instrument_local.get_note(note_name, None, duration)

                # Then we need to append received note into result mass of notes
                melody_audio_segment.append(temp)
            else:

                # Get octave of note
                octave = note.octave["value"]

                # Using method get_note of Piano or Guitar class
                # getting note, passing as the params name of note,
                # octave and duration of current note
                temp = instrument_local.get_note(note_name, octave, duration)

                # Then we need to append received note into result mass of notes
                melody_audio_segment.append(temp)

        # Now we need to concatenate mass of chords into single musical composition

        i = 2  # Because we concatenate first and second chord before started the loop

        # Concatenate first and second note before started the loop
        # symbol s indicates that we need to concatenate musical parts in sequence mod
        result = Piano.join_two_parts(melody_audio_segment[0], melody_audio_segment[1], "s")

        # Concatenate all notes from mass of notes
        while i < len(melody_audio_segment):
            result = Piano.join_two_parts(result, melody_audio_segment[i], "s")
            i += 1

        return result

    @staticmethod
    def join_harmony_and_melody(harmony_, melody_):
        """

        Allows concatenate melody and harmony components into single musical composition.

        :param harmony_: Object of AudioSegment class
            Harmony component of musical composition

        :param melody_: Object of AudioSegment class
            Melody component of musical composition

        :return: object of AudioSegment class that contains melody part of musical composition.

        """

        # Increase of volume of melody component
        melody = melody_ + 6

        return Piano.join_two_parts(harmony_, melody, "p")
