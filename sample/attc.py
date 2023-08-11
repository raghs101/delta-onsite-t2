import requests

main_server_url = "http://localhost:81"  # Replace with your main server's URL
num_requests = 100  # Number of requests to send

final_urls = []

for _ in range(num_requests):
    response = requests.get(main_server_url, allow_redirects=True)
    final_url = response.url  # This will give you the final URL after redirection
    final_urls.append(final_url)

# Print the final URLs reached after redirection
for url in final_urls:
    print(f"Final URL after redirection: {url}")
