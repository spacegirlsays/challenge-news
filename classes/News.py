from bs4 import BeautifulSoup

class News():
    # def __init__(self):
    #     self.title = title
    #     self.description = description
    #     self.category = category
    
    def get_news(var_strResponse):
        soup = BeautifulSoup(var_strResponse, 'html.parser')

        var_objTitle = soup.find_all('div', class_='PagePromo-title')
        
