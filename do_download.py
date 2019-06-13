from screenshot_getter import save_screenshot
lines = open('url_list.txt').read().splitlines()
indices = [ line.split('\t')[0] for line in lines ]
urls = [ line.split('\t')[2] for line in lines ]

for idx, url in zip(indices, urls):
    filename = 'image/ss_{}_dev.png'.format(idx)
    save_screenshot(url, filename)
