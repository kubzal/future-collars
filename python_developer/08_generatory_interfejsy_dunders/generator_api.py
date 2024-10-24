import requests


def fetch_random_users(results_per_page, total_pages):
    print("Results per page:", results_per_page)
    print("Total pages:", total_pages)
    print("-" * 100)

    base_url = "https://randomuser.me/api/"
    for page in range(1, total_pages + 1):
        params = {"page": page, "results": results_per_page}
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            yield data["results"]  # Yielding only the 'results' section
        else:
            print(f"Failed to fetch page {page}: {response.status_code}")


# Using the generator
total_pages = 5
results_per_page = 3

for users in fetch_random_users(results_per_page, total_pages):
    for user in users:
        # Extracting title, first name, last name, city, and country
        title = user["name"]["title"]
        first_name = user["name"]["first"]
        last_name = user["name"]["last"]
        city = user["location"]["city"]
        country = user["location"]["country"]

        # Print the extracted information
        print(
            f"Title: {title}, Name: {first_name} {last_name}, City: {city}, Country: {country}"
        )
    print("-" * 100)
