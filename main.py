
import requests
from bs4 import BeautifulSoup



def get_html(url):
    response = requests.get(url)
    return response.text


def get_all_links(html):
    links = []
    soup = BeautifulSoup(html, "html.parser")
    divs = soup.find("div", class_ = "grid-deputs").find_all("div", class_ = "dep-item")
    for deputi in divs:
        part_link = deputi.find("a").get("href")
        name = deputi.find("a", class_ = "name").text
        full_link = "http://kenesh.kg" + part_link
        links.append(full_link)
    return links


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    div = soup.find("div", class_ = "universal-section__column__center")
    name = div.find('div', class_="deput-name").text
    fraction = div.find_all('a', class_ = "deput-text")[0].text
    phone_number = div.find('div', class_ = "item")
    if phone_number:
        phone_number = phone_number.text.strip()
    else:
        phone_number = ""
    
    biography = div.find('div', class_ = "ck-editor").text
    data = {
        "name": name,
        "fraction": fraction,
        "phone_number": phone_number,
        "biography": biography
    }
    return data


def main():
    html=get_html("http://kenesh.kg/ru/deputy/list/35")
    deputi_links = get_all_links(html)
    for link in deputi_links:
        deputi_html = get_html(link)
        data = get_data(deputi_html)



if __name__ == '__main__':
    main()




























