import requests
from requests import Request

class APIRequest(): 
    def _parse_url(self, url: str, dictionary_parameters: dict) -> str:
        url += "?"
        
        for parameter in dictionary_parameters.keys():
            
            url += parameter + "=" + str(dictionary_parameters[parameter])
            
            if parameter != list(dictionary_parameters.keys())[-1]:
                # If the parameter is not the last key, add an & symbol
                url += "&"
                
        return url

    def http_get(self, url: str, parameters: dict = None) -> dict:
        url = self._parse_url(url, parameters) if parameters else url
        
        request: Request = requests.get(url)
        json_data: dict = request.json()
        api_response: APIResponse = APIResponse(json_data)
        
        return api_response
    
class APIResponse():
    def __init__(self, json_array: dict) -> None:
        self.json_array: dict = json_array
    
    def get_data(self) -> dict:
        return self.json_array["data"]
    
    def get_status(self) -> str:
        return self.json_array["status"]
