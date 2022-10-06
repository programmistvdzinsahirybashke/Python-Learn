def normalize_url(url):
    https = 'https://'
    if url[:8] == https:
        return url
    elif url[:7] == 'http://':
        return https + url[7:]
    else:
        return https + url


print(normalize_url('https://ya.ru') ) # 'https://ya.ru'
normalize_url('google.com')  # 'https://google.com'
normalize_url('http://ai.fi')  # 'https://ai.fi'

