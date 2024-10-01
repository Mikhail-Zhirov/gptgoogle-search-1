import logging
try:
    from tavily import Client as TavilyClient
except ImportError:
    print("Error: Tavily package not found. Please make sure it's installed correctly.")
    print("Try running: pip install tavily-python==0.3.1")
    raise

from requests.exceptions import RequestException

class SearchService:
    def __init__(self, api_key):
        self.client = TavilyClient(api_key=api_key)
        self.logger = logging.getLogger(__name__)

    def search(self, query, max_results=50):
        try:
            response = self.client.search(query, max_results=max_results)
            return response.get('results', [])
        except RequestException as e:
            self.logger.error(f"Error searching Tavily API: {str(e)}")
            if hasattr(e.response, 'text'):
                self.logger.error(f"Response content: {e.response.text}")
            return []