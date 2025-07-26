import hashlib


class Hasher:
    
    hashes = {
        'sha1' : hashlib.sha1,
        'sha224' : hashlib.sha224,
        'sha256' : hashlib.sha256,  
        'sha384' : hashlib.sha384,
        'sha512' : hashlib.sha512,
        'sha3_224' : hashlib.sha3_224,
        'sha3_256' : hashlib.sha3_256,
        'sha3_384': hashlib.sha3_384,
        'sha3_512': hashlib.sha3_512,
        'shake_128' : hashlib.shake_128,
        'shake_256' : hashlib.shake_256,
        'blake2b' : hashlib.blake2b,
        'blake2s' : hashlib.blake2s,
        'md5' : hashlib.md5
    }

    @staticmethod
    def get_hash(hash_alg,file_path):
        hash = Hasher.hashes[hash_alg]()
        
        with open(file_path, 'rb') as file:
            while chunk := file.read(4096):
                hash.update(chunk)
        
        if hash_alg in ('shake_128','shake_256'):
            return hash.hexdigest(32)

        return hash.hexdigest()
    
    @staticmethod
    def save_file(hash_alg,file_path,hash):
        new_file_path = f"{file_path}.{hash_alg}"
        
        with open(new_file_path,"w") as file:
            print(hash)
            file.write(hash)
            