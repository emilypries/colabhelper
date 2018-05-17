import requests

# via turdus-merula's answer on https://stackoverflow.com/questions/25010369/wget-curl-large-file-from-google-drive/39225039#39225039
def download_file_from_google_drive(id, destination):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)

def download(file_id="0B9jhaT37ydSyb0NuYmk2ZEpOR0E", destination='./model.ckpt'):
    import sys
    # DESTINATION FILE ON YOUR DISK
    download_file_from_google_drive(file_id, destination)

# Google Drive ids for style transfer models via Logan Engstrom
# https://drive.google.com/drive/folders/0B9jhaT37ydSyRk9UX0wwX3BpMzQ?usp=sharing
# https://github.com/lengstrom/fast-style-transfer
MODEL_IDS = {
    "udnie": "0B9jhaT37ydSyb0NuYmk2ZEpOR0E",
    "wreck": "0B9jhaT37ydSySjNrM3J5N2gweVk",
    "wave": "0B9jhaT37ydSyVGk0TC10bDF1S28",
    "scream": "0B9jhaT37ydSyZ0RyTGU0Q2xiU28",
    "rain": "0B9jhaT37ydSyaEJlSFlIeUxweGs",
    "lamuse": "0B9jhaT37ydSyQU1sYW02Sm9kV3c"   
}

def get_model_id(name):
  out = MODEL_IDS.get(name)
  if out is None:
    out = name
  return out