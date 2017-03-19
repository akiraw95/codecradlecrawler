import unicodedata

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_urls = [
        'https://stackoverflow.com/questions/tagged/python?sort=frequent&pageSize=50',
        'http://stackoverflow.com/questions/tagged/python?sort=newest&pagesize=50'
        ]



# opening up connection, grabbing raw html
for my_url in my_urls:
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    # html parsing
    page_soup = soup(page_html, "html.parser")

     # now we need to traverse the html
     # grabs each question
    questions = page_soup.findAll("div", {"class":"question-summary"})
    counter = 0

    for question in questions:
        # Initialize Post Fields
        t_questionName = 'EMPTY'
        t_questionLink = 'EMPTY'
        t_questionText = 'EMPTY'
        t_answerText   = 'EMPTY'

        counter += 1

        # Obtain Question Name
        t_QuestionName = question.findAll("div", {"class":"summary"})
        if len(t_QuestionName) > 0:
            t_questionName = t_QuestionName[0].a.text.strip()
        # Obtain Question Link & Text
        t_QuestionLink = question.findAll("div", {"class":"summary"})
        if len(t_QuestionLink) > 0:
            t_questionLink = 'https://stackoverflow.com' + t_QuestionLink[0].a.get('href')
            # Crawl the Link into the Question
            t_Client = uReq(t_questionLink)
            t_page_html = t_Client.read()
            t_Client.close()
            t_link_soup = soup(t_page_html, "html.parser")
            t_postTexts = t_link_soup.findAll("div", {"class":"post-text"})
            if len(t_postTexts) > 1:
                t_questionText = t_postTexts[0].get_text()
                t_answerText   = t_postTexts[1].get_text()

        # print to file
        #print("Entry " + str(counter) + ":")
        #print("\tQuestion Name: " + str(t_questionName.encode('utf8')) )
        #print("\tQuestion Link: " + t_questionLink)
        #print("\tQuestion Text: " + t_questionText)
        #print("\tAnswer Text: " + t_answerText)
        if t_answerText != 'EMPTY':
            t_filename = "questions/" + t_questionLink.split("/")[-1] + ".txt"
            f = open(t_filename, "w")
            f.write( t_questionName.encode('ascii','ignore').decode('ascii') )
            f.write( "\nLink: " + t_questionLink )
            f.write("\n\n" + t_questionText.encode('ascii','ignore').decode('ascii') )
            f.write("\n\nAnswer Text: " + t_answerText.encode('ascii','ignore').decode('ascii') + "\n")
            f.close()

