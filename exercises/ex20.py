#!/usr/bin/python


def translate(translation_list):

    trans_dict = {"merry":"god", "christmas":"jul", "and":"och",
                  "happy":"gott", "new":"nytt", "year":"år"}

    final_translation_list = []

    for word in translation_list:
        if word in trans_dict:
            final_translation_list.append(trans_dict[word])
    
    return(final_translation_list)

