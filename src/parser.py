import logging
import urllib.parse

from src import funcs


def parse_cpu(cpu_list) -> dict:
    cpu_data = {'err': []}
    for line in cpu_list:
        name = get_cpu_name(line)
        cpu_data[name] = {}
        # TODO refactor ugly
        try:
            cpu_data[name]['price'] = get_cpu_price(line)
        except IndexError:
            cpu_data[name]['price'] = ""
            cpu_data[name]['err'] = True
            cpu_data['err'].append(name)
        try:
            cpu_data[name]['passmark'] = get_cpu_mark(line)
        except IndexError:
            cpu_data[name]['passmark'] = ""
            cpu_data[name]['err'] = True
            cpu_data['err'].append(name)
    return cpu_data


def parse_line(line, start_string: str, end_string: str) -> str:
    try:
        start_index = funcs.find_start(line, start_string)
    except IndexError:
        # TODO refactor error stack
        logging.error(f'Start string could not be found, {IndexError}')
        logging.debug(f'Looking for {start_string} in {line}')
        raise IndexError
    try:
        end_index = funcs.find_end(line, start_index, end_string)
    except IndexError:
        # TODO refactor error stack
        logging.error(f'End string could not be found, {IndexError}')
        logging.debug(f'Looking for {end_string} in {line}')
        raise IndexError
    cpu_property = line[start_index:end_index]
    cpu_property = urllib.parse.unquote_plus(cpu_property)
    return cpu_property


def get_cpu_name(line) -> str:
    try:
        return parse_line(line, "cpu=", "&amp")
    except IndexError:
        return IndexError


def get_cpu_price(line) -> str:
    try:
        return parse_line(line, 'class="price-neww">', "<")
    except IndexError:
        raise IndexError


def get_cpu_mark(line) -> str:
    try:
        return parse_line(line, 'class="mark-neww">', "<")
    except IndexError:
        raise IndexError
