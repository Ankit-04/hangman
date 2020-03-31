def get_word():
    from bs4 import BeautifulSoup
    import requests

    url = 'https://randomword.com/'
    loop = True
    while loop == True:
        r = requests.get(url)
        soup = r.text
        soup = BeautifulSoup(soup, 'html5lib')
        word = soup.find("div", {"id":"random_word"})
        if "-" in word or " " in word:
            pass
        else:
            loop= False
            return (word.string)


        