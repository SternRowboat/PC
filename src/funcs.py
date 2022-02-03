import logging


def find_start(html, start_string) -> int:
    quick_start = html.find(start_string)
    if quick_start == -1:
        raise IndexError(" -1")
    try:
        start_index = quick_start + len(start_string)
        return start_index
    except IndexError:
        raise IndexError("-5")


def find_end(html, start_index, end_string) -> int:
    quick_end = html[start_index:].find(end_string)
    if quick_end == -1:
        raise IndexError("-1")
    try:
        end_index = quick_end + start_index
        if end_index < start_index:
            logging.warning(f'End index {end_index}, before start index: {start_index}.')
            raise IndexError("-3")
        return end_index
    except IndexError:
        raise IndexError("-5")


def bullet_loop(text) -> dict:
    delimiter = "/li>"
    if delimiter not in text:
        logging.warning(f'Delimiter: {delimiter}, not in Text: "{text}"')
    return text.split(delimiter)


# Unused?
def print_list(input_list):
    for i in range(len(input_list)):
        print("#" + str(i+1) + str(input_list[i]))
