#54.What is memoization? How is it different from caching?
cache = {}

def get_data(url):
    if url in cache:
        return cache[url]  # return cached result
    print("Fetching from API...")
    result = f"Data from {url}"  # pretend API call
    cache[url] = result
    return result

print(get_data("https://example.com"))
print(get_data("https://example.com"))  # returns from cache
