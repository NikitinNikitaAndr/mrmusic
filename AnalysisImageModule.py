# -*- coding: utf-8 -*-

# This file contains the implementation of AnalysisImage class and helper class PrimaryColor.
# AnalysisImage class allows to get the mass of primary colors
# each element of this mass is the object of PrimaryColor class.
# AnalysisImage class also allows to get the domination color of image and combine the same color sequence.
#
# PrimaryColor class is the helper class, which is needed for more convenient storage of simple colors.
#
# Author: Nikitin Nikita <nikitin.nikitaa@outlook.com>
# Created: 10.12.2015. Last modified: 07.06.2016

import cv2


class AnalysisImage:

    """

    AnalysisImage class allows to get the mass of primary colors
    each element of this mass is the object of PrimaryColor class.

    It also allows to get the domination color of image and combine the same color sequence.

    Attributes:
    ------------------
    path_to_image: str
        Path to loaded image.

    Methods:
    ------------------
    get_color_by_hue: allows to get the name of color by hue value of hsv image

    calculate_saturation: allows to calculate the saturation value of hsv image to saturation in range [0; 4]

    calculate_brightness: allows to calculate the brightness value of hsv image to brightness in range [0; 2]

    get_mass_of_colors: allows to get mass of primary colors by image.
                        Each element of mass is the object of PrimaryColor class.

    combine_same_prime_pixels: allows to combine the same color sequence of mass of primary colors, that can be
                                obtained from get_mass_of_colors method

    find_domination_color: allows to get the domination color of image. Return name of color.

    """

    path_to_image = None

    def __init__(self, _path_to_image):
        self.path_to_image = _path_to_image

    @staticmethod
    def get_color_by_hue(color):
        """

        This method allows to get the name of color by hue value of hsv image.

        The work of this method is based on the fact that each color has a range of hue value.
        Ranges of each colors was found in OpenCV documentation:
            red - [0; 5] or [175; 180]
            red orange - [6; 10]
            orange - [11; 20]
            yellow orange - [21; 25]
            yellow - [26; 30]
            yellow green - [31; 40]
            green - [41; 75]
            green blue - [76; 100]
            blue - [101; 120]
            blue violet - [121; 140]
            violet - [141; 160]
            purple (pink) - [161; 175]

        :param color: int
            Hue value of hsv image. According to OpenCV documentation is the value in range [0; 180]

        :return: str
            name of color according to hue value

        """

        result = ""

        # According to ranges of each color get name of color by hue
        if (0 <= color <= 5) or (175 <= color <= 180):
            result = "red"
        elif 6 <= color <= 10:
            result = "redorange"
        elif 11 <= color <= 20:
            result = "orange"
        elif 21 <= color <= 25:
            result = "yelloworange"
        elif 26 <= color <= 30:
            result = "yellow"
        elif 31 <= color <= 40:
            result = "yellowgreen"
        elif 41 <= color <= 75:
            result = "green"
        elif 76 <= color <= 100:
            result = "greenblue"
        elif 101 <= color <= 120:
            result = "blue"
        elif 121 <= color <= 140:
            result = "blueviolet"
        elif 141 <= color <= 160:
            result = "violet"
        elif 161 <= color <= 175:
            result = "purple"

        return result

    @staticmethod
    def calculate_saturation(saturation_hsv):
        """

        This method allows to calculate the saturation value of hsv image to saturation in range [0; 4].

        The work of this method is based on the fact that saturation value of hsv image has range [0; 255].
        The saturation value of hsv image is increase from 0 to 255. I.e. 255 - very saturation color.

        :param saturation_hsv: int
             Saturation value of hsv image. According to OpenCV documentation it the value in range [0; 255].

        :return: int
            Calculated value of saturation - the value in range [0; 4], where 0 - very saturation color.

        """
        result = 0

        # Saturation value of hsv image was divided to 5 ranges.
        # 0 is very saturation color.
        if 0 <= saturation_hsv <= 50:
            result = 4
        elif 51 <= saturation_hsv <= 101:
            result = 3
        elif 102 <= saturation_hsv <= 152:
            result = 2
        elif 153 <= saturation_hsv <= 203:
            result = 1
        elif 204 <= saturation_hsv <= 255:
            result = 0

        return result

    @staticmethod
    def calculate_brightness(brightness_hsv):

        """

        This method allows to calculate the brightness value of hsv image to brightness in range [0; 2].

        The work of this method is based on the fact that the brightness value of hsv image has range [0; 255].
        The brightness value of hsv image is increase from 0 to 255.
        255 - very brightness color, 0 - very dark color.

        :param brightness_hsv: int
            Brightness value of hsv image. According to OpenCV documentation it the value in range [0; 255].

        :return: int
            Calculated value of brightness - the value in range [0; 2], where 0 - very brightness color.

        """

        result = 0

        # Brightness value of hsv image was divided to 3 ranges.
        # 0 - very brightness color
        # 1 - average brightness color
        # 2 - dark color.
        if 0 <= brightness_hsv <= 84:
            result = 2
        elif 85 <= brightness_hsv <= 170:
            result = 1
        elif 171 <= brightness_hsv <= 255:
            result = 0

        return result

    def get_mass_of_colors(self):

        """

        This method allows to get mass of primary colors by image.
        Each element of mass is the object of PrimaryColor class.

        This method does not require any explicit parameter passing, but it use path_to_image parameter passing
        at initialization of object of AnalysisImage class.

        :return: massive (list) of object of PrimaryColor class.

        """

        result = []  # result mass
        input_img_rgb = cv2.imread(self.path_to_image)  # read image from path that contain path_to_image variable
        input_img_hsv = cv2.cvtColor(input_img_rgb, cv2.COLOR_BGR2HSV)  # convert source RGB image to HSV image

        img = input_img_hsv[0::20]  # get each 20 pixels from image

        # for each pixel in image
        for item in img:
            for pixel in item:

                    # Initialize object of PrimaryColor class, passing as the params calculated hue, saturation
                    # and brightness values
                    prime_color = PrimaryColor(self.get_color_by_hue(pixel[0]), self.calculate_saturation(pixel[1]),
                                               self.calculate_brightness(pixel[2]))

                    # Append object of PrimaryColor class to the result mass
                    result.append(prime_color)

        return result

    @staticmethod
    def combine_same_prime_pixels(mass_of_colors):

        """

        This method allows to combine the same color sequence of mass of primary colors, that can be
        obtained from get_mass_of_colors method.

        The same color sequence is the colors that have the same hue, saturation and brightness values.

        :param mass_of_colors: massive (list)
            mass of primary colors, that can be obtained from get_mass_of_colors method.

        :return: massive (list) of primary colors.

        """

        result = []  # result mass

        i = 0
        for i in range(0, len(mass_of_colors)):

            # if there is a next element
            if i < len(mass_of_colors) - 1:

                # if hue value of current element is not equal to hue value of next element
                if mass_of_colors[i].clear_color != mass_of_colors[i+1].clear_color:

                    # append element to the result mass
                    result.append(mass_of_colors[i])

                # if saturation value of current element is not equal to saturation value of next element
                elif mass_of_colors[i].saturation != mass_of_colors[i+1].saturation:

                    # append element to the result mass
                    result.append(mass_of_colors[i])

                # if brightness value of current element is not equal to brightness value of next element
                elif mass_of_colors[i].brightness != mass_of_colors[i+1].brightness:

                    # append element to the result mass
                    result.append(mass_of_colors[i])

        return result

    @staticmethod
    def find_domination_color(color_with_params):

        """

        This method allows to get the domination color of image.

        :param color_with_params: massive (list)
            massive of objects of PrimaryColors class

        :return: str
            name of domination color

        """

        # Initialize two-dimensional array, each element of which is array of two elements:
        # first element - is the name of color
        # second element - is the number of occurrences of the corresponding color on the image
        counts = [["blue", 0], ["greenblue", 0], ["green", 0], ["yellowgreen", 0], ["yellow", 0],
                  ["yelloworange", 0], ["orange", 0], ["redorange", 0], ["red", 0], ["purple", 0],
                  ["violet", 0], ["blueviolet", 0], ["white", 0]]

        # for each element in mass of primary colors
        for color in color_with_params:

            # for each element from counts array
            for item in counts:

                # if the names of current color from mass of primary colors and from counts array are equal
                if color.clear_color == item[0]:

                    # then increase the number of occurrences of the corresponding color on the image
                    item[1] += 1

        # Then we need to find max element in the resulting array
        max_index = 0
        max = 0
        for i in range(0, len(counts)):
            if counts[i][1] > max:
                max = counts[i][1]
                max_index = i

        # return name of color, that have max number of occurrences
        return counts[max_index][0]


class PrimaryColor:

    clear_color = None
    saturation = None
    brightness = None

    def __init__(self, _clear_color, _saturation, _brightness):
        self.clear_color = _clear_color
        self.saturation = _saturation
        self.brightness = _brightness
