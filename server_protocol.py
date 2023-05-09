import random, string, hashlib, json
class server_protocol: 
    def createKey(self):
        auth_key = "".join(random.choices(string.ascii_uppercase + string.digits, k = 26))
        keys = json.loads(open("auth_keys/keys.txt", 'r+').readlines()[0])
        keys.append(hashlib.sha256(auth_key.encode('UTF-8')).hexdigest())
        
        open("auth_keys/keys.txt", 'r+').truncate(); open("auth_keys/keys.txt", 'r+').write(json.dumps(keys))
        return auth_key

    def defineKey(self, KEY):
        keys = json.loads(open("auth_keys/keys.txt", 'r+').readlines()[0])
        if hashlib.sha256(KEY.encode('UTF-8')).hexdigest() in keys:
            return True
        else: return False

    def destroyKey(self, KEY):
        keys = json.loads(open("auth_keys/keys.txt", 'r+').readlines()[0])
        try:
            del keys[keys.find(hashlib.sha256(KEY.encode('UTF-8')).hexdigest())]
            open("auth_keys/keys.txt", 'r+').truncate(); open("auth_keys/keys.txt", 'r+').write(json.dumps(keys))
            return True
        except: return False