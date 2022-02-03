import logging
from urllib.error import URLError
from urllib.request import urlopen

import sites


def do():
    url = "https://www.cpubenchmark.net/cpu_value_available.html"
    try:
        html = get_page(url)
    except URLError as e:
        logging.warning(f'URL failed to open: {e}, {url}')
        return
    # TODO don't use strings ewww
    sites.parse_cpu_benchmark(html, start_string='class="chartlist">',
                              end_string="/span></a></li>\n    </ul>")

    # TODO ADD A NEW SITE!!! :D
    return


def get_page(page_url: str) -> str:
    # TODO errors in here
    page = urlopen(page_url)
    html_bytes = page.read()
    return html_bytes.decode("utf-8")
