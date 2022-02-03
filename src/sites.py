import json
import logging

import funcs
from src import parser


def parse_cpu_benchmark(html: str, start_string: str, end_string: str) -> None:
    start_len = len(start_string)
    html_len = len(html)
    try:
        start_index = funcs.find_start(html, start_string)
        if start_index in range(html_len - start_len + 5, html_len + start_len + 5):
            logging.warning(f'Start string "{start_string}" not found, '
                            f'index set to: {start_index}, '
                            f'html len: {len(html)}')
            raise IndexError("-3")
    except IndexError as e:
        logging.error(f'Start string could not be found, {e}')
        return
    try:
        end_index = funcs.find_end(html, start_index, end_string)
    except IndexError as e:
        logging.error(f'End string could not be found, {e}')
        return

    text_i_want = html[start_index:end_index]
    cpu_list = funcs.bullet_loop(text_i_want)
    cpu_data = parser.parse_cpu(cpu_list)
    threshold = 1
    # TODO refactor into log_results(data=cpu_data, threshold): -> None
    if len(cpu_list) < threshold:
        logging.warning(f"CPU's FOUND: {len(cpu_list)}")
    elif len(cpu_data) < threshold:
        logging.warning(f'CPU DATA EMPTY: {json.dumps(cpu_data)}')
    else:
        logging.info(f"CPU's FOUND: {len(cpu_list)}")
        logging.info(f"CPU's PARSED: {len(cpu_data) - 1}")
    if not len(cpu_data['err']) == 0:
        logging.warning(f"CPU's had errors: {cpu_data['err']}")
        for name in cpu_data['err']:
            for key, item in cpu_data[name].items():
                if item == "":
                    logging.debug(f'{name} has no {key}')

def parse_some_other_site():
    pass