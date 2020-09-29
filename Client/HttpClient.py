import requests

hostName = "localhost"
serverPort = 8080

if __name__ == "__main__":
    r = requests.get("http://" + hostName + ":" + str(serverPort) + "/help")

    print(r.json())