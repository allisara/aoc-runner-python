from shared import get_dataset
from os import getenv
from manim import *


def is_digit(c):
    char_value = ord(c)
    return char_value >= 48 and char_value <= 57


class ShowShort(Scene):
    def construct(self):
        dataset = get_dataset()

        test_data = ["as4kfjhslpg", "as2m4so", "asdfg"]

        sum = 0

        # label = Text(str(sum)).to_edge(UL)

        # self.add(label)

        for row in test_data:
            found_digit = False

            line_obj = Text(row)
            line = line_obj.text

            first_c_pos = -1
            last_c_pos = -1

            for i in range(len(line)):
                char_value = ord(line[i])
                if char_value >= 48 and char_value <= 57:
                    found_digit = True
                    last_c_pos = i
                    if first_c_pos < 0:
                        first_c_pos = i

            self.add(line_obj)

            if not found_digit:
                for c in line_obj:
                    c.scale(1.1)
                    self.wait(.2)
                    c.scale(.9).set_color(GRAY)
                line_obj.set_color(RED)
                self.wait(.2)
                self.play(FadeOut(line_obj))

            else:
                for i in range(first_c_pos):
                    line_obj[i].scale(1.1)
                    self.wait(.2)
                    line_obj[i].scale(.9).set_color(GRAY)
                line_obj[first_c_pos].scale(1.1).set_color(GREEN)
                self.wait(.3)

                for i in range(len(line), last_c_pos, -1):
                    line_obj[i-1].scale(1.1)
                    self.wait(.2)
                    line_obj[i-1].scale(.9).set_color(GRAY)
                line_obj[last_c_pos].scale(1.1).set_color(GREEN)
                self.wait(.3)

                d = Text(line[first_c_pos] + line[last_c_pos]
                         ).set_color(GREEN).scale(2).shift(UP * 1.5)
                d1 = d[0]
                d2 = d[1]

                if first_c_pos == last_c_pos:
                    new_d = line_obj[first_c_pos]
                    self.play(ReplacementTransform(new_d, d))

                else:
                    new_d1 = line_obj[first_c_pos]
                    new_d2 = line_obj[last_c_pos]
                    line_obj.set_color(GRAY)
                    new_d1.set_color(GREEN)
                    new_d2.set_color(GREEN)

                    self.play(ReplacementTransform(new_d1, d1),
                              ReplacementTransform(new_d2, d2))

                self.wait(.2)

                # formula = label.text + " + "

                self.play(FadeOut(line_obj))

            # num1 = ""
            # num2 = ""

            # new_d1 = line_obj[0]
            # new_d2 = line_obj[0]

            # # self.add(d1, d2)

            # for i in range(len(line_obj)):
            #     line_obj[i].scale(1.1)
            #     self.wait(.3)

            #     if is_digit(line[i]):
            #         line_obj[i].set_color(GREEN)
            #         found_digit = True
            #         new_d1 = line_obj[i]
            #         num1 = line[i]
            #         break
            #     else:
            #         line_obj[i].scale(.9).set_color(GRAY)

            # if found_digit:
            #     for i in range(len(line)):
            #         line_obj[-i - 1].scale(1.1)
            #         self.wait(.3)

            #         if is_digit(line[-i-1]):
            #             line_obj[-i-1].set_color(GREEN)
            #             new_d2 = line_obj[-i-1]
            #             num2 = line[-i-1]
            #             found_digit = True
            #             break
            #         else:
            #             line_obj[-i-1].scale(.9).set_color(GRAY)
            #     if not found_digit:
            #         new_d2 = new_d1
            #         num2 = num1

            # else:
            #     line_obj.set_color(RED)

            # d = Text(num1 + num2).set_color(GREEN).scale(2).shift(UP * 1.5)
            # d1 = d[0]
            # d2 = d[1]

            # line_obj.set_color(GRAY)
            # new_d1.set_color(GREEN)
            # new_d2.set_color(GREEN)

            # # line_obj.set_color(BLACK)
            # self.play(ReplacementTransform(new_d1, d1),
            #           ReplacementTransform(new_d2, d2))

            # self.wait(.2)
            # # self.play(FadeOut(line_obj), FadeOut(d))
