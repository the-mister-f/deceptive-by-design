import json

def read_creds(filename):
    with open(filename, "r") as f:
        return json.load(f)

def get_db_uri():
    json_creds_path = "credentials/creds.json"
    creds = read_creds(json_creds_path)
    user = creds.get("db.username")
    pwd = creds.get("db.pwd")
    server = creds.get("db.server")
    port = creds.get("db.port")
    db_name = creds.get("db.name")
    return f"postgresql://{user}:{pwd}@{server}:{port}/{db_name}"
