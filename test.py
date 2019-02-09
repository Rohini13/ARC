import requests 
 
y={
    "text":"happy"
}

x=requests.post("http://127.0.0.1:5000",y)

print(x.text)
