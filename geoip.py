import requests

def get_location(ip):

    try:
        r = requests.get(f"http://ip-api.com/json/{ip}").json()
        return f"{r['country']} - {r['city']}"
    except:
        return "Unknown"
