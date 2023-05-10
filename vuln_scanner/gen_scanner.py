import requests
from bs4 import BeautifulSoup

def request(url):
    try:
        return requests.get("http://" + url)
    except Exception:
        pass

target_url = "testphp.vulnweb.com/login.php"
response = request(target_url)

parsed_html = BeautifulSoup(response.content)
form_list = parsed_html.find_all("form")

for form in form_list:
    action = form.get("action")
    print(action)
    method = form.get("method")
    print(method)
    
    input_list = form.find_all("input")
    for inpt in input_list:
        input_name = inpt.get("name")
        print(input_name)