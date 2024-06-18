import requests

def number_of_subscribers(subreddit):
  """
  This function queries the Reddit API and returns the number of subscribers 
  for a given subreddit.

  Args:
      subreddit: The name of the subreddit to query.

  Returns:
      The number of subscribers (integer) or 0 if the subreddit is invalid.
  """

  # Set a custom User-Agent header to avoid throttling
  headers = {'User-Agent': 'My Reddit Script v1.0 (by your_username)'}

  # Construct the API endpoint URL
  url = f"https://www.reddit.com/r/{subreddit}/about.json?limit=0"

  try:
    # Send a GET request without following redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check for successful response (status code 200)
    if response.status_code == 200:
      data = response.json()
      return data.get('data', {}).get('subscribers', 0)  # Handle nested data structure
    else:
      return 0  # Handle non-200 status codes

  except requests.exceptions.RequestException as e:
    print(f"Error querying Reddit API: {e}")
    return 0
