from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)


def save_screenshot(url, filename, debug=False):
    driver.get(url)
    # To get real width and height, you have to compare some measures of width and height.
    # See https://stackoverflow.com/questions/15932650/body-scrollheight-doesnt-work-in-firefox
    page_width = max(
        max(
            driver.execute_script('return document.body.scrollWidth'),
            driver.execute_script('return document.documentElement.scrollWidth')
        ),
        max(
            driver.execute_script('return document.body.offsetWidth'),
            driver.execute_script('return document.documentElement.offsetWidth')
        ),
        max(
            driver.execute_script('return document.body.clientWidth'),
            driver.execute_script('return document.documentElement.clientWidth')
        )
    );
    page_height = max(
        max(
            driver.execute_script('return document.body.scrollHeight'),
            driver.execute_script('return document.documentElement.scrollHeight')
        ),
        max(
            driver.execute_script('return document.body.offsetHeight'),
            driver.execute_script('return document.documentElement.offsetHeight')
        ),
        max(
            driver.execute_script('return document.body.clientHeight'),
            driver.execute_script('return document.documentElement.clientHeight')
        )
    );
    if debug:
        print( '\t'.join([
            'url: {}'.format(url),
            'width: {}'.format(page_width),
            'height: {}'.format(page_height)
        ]))
    driver.set_window_size(page_width, page_height)
    driver.save_screenshot(filename)
    if debug:
        print('Saved successfully.' if debug else '')
