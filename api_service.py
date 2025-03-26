import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code ==200:
        return response.json()
    else:
        return None
    
if __name__ == '__main__':
    print(fetch_data("https://jsonplaceholder.typicode.com/todos/1"))