import requests
import wikipedia
import datetime
import time

def get_news(apikey, country='in'):
    apikey = '9f408a43ce764868b97f19c0745fbb35'
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={apikey}"
    response = requests.get(url)
    news_data = response.json()
    if news_data['status'] == 'ok':
        articles = news_data['articles']
        headlines = [article['title'] for article in articles]
        return headlines
    else:
        return None
    
while True:
    userinput = str(input("\t\t\t\t I am a chatbot designed to help you ... say something - \n"))
    if  userinput in ["hello" , "hii"  ] :
        print("\t\t\t\tHello !! how can i assist you today ?? \n")

    elif userinput.startswith(("search about", "describe about")):
        keyword = userinput.split(" ", 2)[1:]
        print("\t\t\t\t")
        result = wikipedia.summary(keyword , sentences=3)
        print("\n")
        print(result)

    elif userinput in ["time"]:
        now = datetime.datetime.now()
        print(now.strftime("\t\t\t\t %H:%M:%S \n"))

    elif userinput in ["tell me some jokes" , "make me laugh" , "joke"] :
        url = "https://api.chucknorris.io/jokes/random"
        response = requests.get(url)
        joke_data = response.json()
        print("\t\t\t\t\n")
        print(joke_data['value'])

    elif userinput in ["update me about latest headlines" , "headlines"] :
        news_headlines = get_news('9f408a43ce764868b97f19c0745fbb35')
        for i, headline in enumerate(news_headlines, start=1):
            print(f"{i}.\t {headline}\n")

    elif userinput in ["quit" , "bye"] : 
        print("\t\t\t\t bye !! have a nice day ahead !! see you soon \n")
        break
    
    else:
        print("\t\t\t\t Try again \n")
