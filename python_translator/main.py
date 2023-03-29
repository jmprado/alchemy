# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os
import google

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    end_translator = False

    while not end_translator:
        print("\033[H\033[J", end="")
        print("\n"
              "|---------------------------------------------------------------------------|\n"
              "|                       Google Text Translator 1.0                          |\n"
              "| Use language codes from https://cloud.google.com/translate/docs/languages |\n"
              "|---------------------------------------------------------------------------|\n"
              "")
        text_to_translate = input("1. Type the text to translate [Enter]: ")
        source = input("2. Type language code 'from' [Enter]: ")
        target = input("3. Type language code 'to' [Enter]: ")

        translator = google.Translator(text_to_translate, source, target)
        translator.do_translation()
        end_translator = input('Do another translation (Y, n): ') == 'n'

