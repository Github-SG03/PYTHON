from ast import main
import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    print(response)
    data=response.json()
    if data["success"] and "data" in data:
            userdata= data["data"]
            username=userdata["login"]["username"]
            country=userdata["location"]["country"]
            return username,country
    else:
            raise Exception("Failed to fetch data")
        
    
    def main():
        try:
            username,country=fetch_random_user_freeapi()
            print(f"Username: {username}")
            print(f"Country: {country}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()

        