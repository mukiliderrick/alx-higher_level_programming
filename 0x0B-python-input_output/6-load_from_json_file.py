import json

def load_from_json_file(filename):
    try:
        with open(filename,'r') as f:
            return json.load(f)
    except json.decoder.JSONDecoderError as e:
        print(f"Error: {e}")