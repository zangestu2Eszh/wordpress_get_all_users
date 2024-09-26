import requests



#https://www.zuj.edu.jo

url=input("Enter URL:")

while True:
    choose=input("1) Wp-json:\n2) Author:\n0) Exit:\nChoose: ")
    if choose=="1":
        response = requests.get(f'{url}/wp-json/wp/v2/users', headers={"accept":"*/*"})
        for i in response.json():
            print(f'id: {i["id"]} , name: {i["name"]}')
    elif choose=="2":
        for i in range(1,101):
            res = requests.get(f'{url}/?author={i}', headers={"accept" : "*/*"})
            if res.status_code == 200:
                print(f'{i} : {res.text.split("/author/")[1].split("/feed/")[0]}')
    elif choose=="0":
        break


