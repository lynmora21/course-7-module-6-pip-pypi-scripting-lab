from datetime import datetime
import requests


def fetch_data():
    """Fetch a sample post from a public API."""
    url = "https://jsonplaceholder.typicode.com/posts/1"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as error:
        print(f"Error fetching API data: {error}")
        return {}


def generate_log():
    """Generate a log file containing local and API information."""
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    post = fetch_data()

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("Automation Tool Log\n")
        file.write("===================\n")

        for entry in log_data:
            file.write(f"{entry}\n")

        file.write("\nAPI Data\n")
        file.write("========\n")
        file.write(f"Post Title: {post.get('title', 'No title found')}\n")
        file.write(f"Post Body: {post.get('body', 'No body found')}\n")

    print(f"Log written to {filename}")


if __name__ == "__main__":
    generate_log()
