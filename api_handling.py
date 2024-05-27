import requests
def fetch_random_user_freeapi():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)
    data=response.json()
    if data["success"] and "data" in data:
        user_data=data["data"]
        first_name=user_data["name"]["first"]
        last_name=user_data["name"]["last"]
        title=user_data["name"]["title"]
        coordinates=user_data["location"]["coordinates"]["latitude"]
        country=user_data["location"]["country"]
        return first_name,last_name,title,coordinates,country
    else:
        raise Exception("faied to fetch user data")
def main():
    try:
        first_name,last_name,title,coordinates,country=fetch_random_user_freeapi()
        print(f"{title} {first_name} {last_name} \n coordinates:{coordinates} \n country:{country}")
    except Exception as e:
        print(str(e))
if __name__=="__main__":
    main()

