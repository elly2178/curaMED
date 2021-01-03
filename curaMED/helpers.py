import os
import json
import hashlib
import requests

class Orthanc:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def get_orthanc_id(self, patient_id: str, study_id="", series_id="", instance_id=""):
        patient_id, study_id, series_id, instance_id = str(patient_id), str(study_id), str(series_id), str(instance_id)
        if not study_id:
            orthanc_id = hashlib.sha1(str.encode(patient_id)).hexdigest()
        elif not series_id:
            orthanc_id = hashlib.sha1(str.encode(patient_id + study_id)).hexdigest()
        elif not instance_id:
            orthanc_id = hashlib.sha1(str.encode(patient_id + study_id + series_id)).hexdigest()
        else:
            orthanc_id = hashlib.sha1(str.encode(patient_id + study_id + series_id + instance_id)).hexdigest() 
        #adding dashes every 8 characters    
        return '-'.join(orthanc_id[i:i+8] for i in range(0, len(orthanc_id),8))      
    
    def get_url_for_path(self, path: str):
        if not path.startswith("/"):
            path = "/" + path
        return self.host + path

    def get_request(self, path, timeout=3, retries=1):
        url = self.get_url_for_path(path)
        response = None
        for _ in range(retries + 1):
            try:
                response = requests.get(url,
                                        auth=(self.username, self.password),
                                        timeout=timeout)
                if response.status_code == 404:
                    return {}, response.status_code
                break
            except requests.Timeout:
                continue
        if response is None:
            raise ValueError(f"Failed to retrieve resource for GET request to {url}")
        else:
            if response.status_code != 200:
                return {"error": f"Request to {url} failed.", "status": f"{response.status_code}", "response": f"{response}"}, response.status_code
            else:
                return response.json(), response.status_code    

    def post_request(self, path: str, body: dict, timeout=2, retries=1):
        """
        Do a post request to this orthanc instance

        Args:
            path (str): path of the resource to send the request to
            body (dict): json serializable dict
            timeout (int, optional): [Time in seconds until request is considered as timed out]. Defaults to 2.
            retries (int, optional): [Nr of times to retry the post request, 0 retries means exactly one try]. Defaults to 1.

        Raises:
            ValueError: [Gets thrown if the User tries to access a false url, port, unexisting location ]

        Returns:
            [Tuple]: [Item0: Response content as a dictionary or a list, Item1: HTTP status code as int]
        """
        url = self.get_url_for_path(path)
        response = None
        for _ in range(retries + 1):
            try:
                response = requests.post(url,
                                        json=body,
                                        auth=(self.username, self.password),
                                        timeout=timeout)
                if response.status_code == 404:
                    return {}, response.status_code
                break
            except requests.Timeout:
                continue
        if response is None:
            raise ValueError(f"Failed to POST request to {url}")
        else:
            return response.json(), response.status_code

    def delete_request(self, path, timeout=3, retries=1):
        url = self.get_url_for_path(path)
        response = None
        for _ in range(retries + 1):
            try:
                response = requests.delete(url,
                                        auth=(self.username, self.password),
                                        timeout=timeout)
                if response.status_code == 404:
                    return {}, response.status_code
                break
            except requests.Timeout:
                continue
        if response is None:
            raise ValueError(f"Failed to retrieve resource for DELETE request to {url}")
        else:
            if response.status_code != 200:
                return {"error": f"Request to {url} failed.", "status": f"{response.status_code}", "response": f"{response}"}, response.status_code
            else:
                return response.json(), response.status_code
         
          
secrets_files = [os.environ.get("CURAMED_ORTHANC_SECRET"),
                 "/home/schumi/Bachelor/secrets/orthanc-secret.json",
                 "C:/Users/taadrar1/Documents/secrets.txt"]

for secrets_file in secrets_files:
    if secrets_file is not None:
        try:
            with open(secrets_file,"r") as secretstore:
                secrets_data = json.load(secretstore)
        except FileNotFoundError:
            pass

try:
    http_credentials = secrets_data.get("c0100-orthanc.curapacs.ch", None)
except NameError:
    raise ValueError(f"Failed to find orthanc secrets data in any of {', '.join(secrets_files)}")
else:
    http_hostname = "https://c0100-orthanc.curapacs.ch"
    http_username = http_credentials.get("user")
    http_password = http_credentials.get("password")

orthanc = Orthanc(http_hostname, http_username, http_password)
