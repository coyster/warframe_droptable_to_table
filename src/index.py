import requests
import bs4

droptable_url = 'https://www.warframe.com/droptables'

def get_droptable_list():
    r = requests.get(droptable_url)
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    tables = soup.find_all('table', class_='droptable')
    return tables

def main():
    '''Table Patter:
    Location / Mission
    
    
    '''