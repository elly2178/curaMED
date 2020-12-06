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

    def get_request(self, path, timeout=2, retries=1):
        url = self.get_url_for_path(path)
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
        if not response:
            raise ValueError(f"Failed to retrieve resource for GET request to {url}")
        else:
            return response.json(), response.status_code
        



with open("/home/schumi/Bachelor/secrets/orthanc-secret.json","r") as secretstore:
    data = json.load(secretstore)
    http_credentials = data.get("c0100-orthanc.curapacs.ch",None)
    http_hostname = "https://c0100-orthanc.curapacs.ch"
    http_username = http_credentials.get("user")
    http_password = http_credentials.get("password")

orthanc = Orthanc(http_hostname, http_username, http_password)