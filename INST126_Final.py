import requests

def fetch_recipes(api_key, app_id, userinput, limit=5): 
    """" This fetches recipes from the Edemam API based on the users input. It makes a request using get
    based on the parameters below."""

    api_url = 'https://api.edamam.com/search'
    params = {'q': userinput, 'app_id': app_id, 'app_key': api_key, 'from': 0, 'to': limit} # Dictionary for each parameter 
    response = requests.get(api_url, params=params) # Requests to get information based on the parameters listed 

    """The status code 200 means the request was successful through JSON."""
    if response.status_code == 200:
        recipes_data = response.json()
        return recipes_data.get('hits', [])
    else:
        print(f"Failed to fetch recipes.")
        return None


print("⋆ ˚｡⋆୨୧⋆ ˚｡⋆ WELCOME TO THE ULTIMATE RECIPE-FETCHER⋆ ˚｡⋆୨୧⋆ ˚｡⋆")
print("\n")


def RecipeFetcher():
    """The main function that uses a while loop and it allows user input until user 
     exits. """
    edamam_api_key = '2ad693b877e92a5dbad204d943124456'  
    edamam_app_id = 'f87e6802'  
    
    while True:
        userinput = input("\nEnter a recipe you'd like to learn ⸜(｡˃ ᵕ ˂ )⸝ (type 'exit' to quit): ")
        if userinput.lower() == 'exit':
            print("Exiting the Recipe Fetcher. Goodbye!")
            break

        recipes = fetch_recipes(api_key=edamam_api_key, app_id=edamam_app_id, userinput=userinput)

        if recipes is not None:
            print(f"\nThese were the recipes found for '{userinput}':")
            for hit in recipes:
                print(f"- {hit['recipe']['label']} ({hit['recipe']['url']})")  
                """It will print the recipes label and url from Edemam. """
        else:
            print("Unfortunately, we were unable to fetch recipes ˙◠˙.")
        

RecipeFetcher()