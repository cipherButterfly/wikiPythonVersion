import wikipediaapi

wiki = wikipediaapi.Wikipedia('en')

keyword = ''
while keyword != '-1':
    print("What do you want to know about?            Type -1 to exit the program")
    keyword = input()
    try:
        page = wiki.page(keyword)
        print(page.title)
        print(page.summary)
    except:
        print("We are sorry, we also don't know about that ")



