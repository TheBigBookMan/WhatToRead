import requests

API_KEY = 'AIzaSyAm6aX3MADdPugpsrgoRe99RcoSd7v9pcM'


def call_google_books(values):
    url = f"https://www.googleapis.com/books/v1/volumes?q={values}&maxResults=40&key={API_KEY}"
    response = requests.get(url)
    content = response.json()['items']
    # print(content)
    return content


# if __name__ == '__main__':
#     call_google_books("heroes + stephen")