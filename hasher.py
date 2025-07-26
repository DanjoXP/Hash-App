import hashlib
import os
from typing import Optional


class Hasher:
    hashes = {
        "sha1": hashlib.sha1,
        "sha224": hashlib.sha224,
        "sha256": hashlib.sha256,
        "sha384": hashlib.sha384,
        "sha512": hashlib.sha512,
        "sha3_224": hashlib.sha3_224,
        "sha3_256": hashlib.sha3_256,
        "sha3_384": hashlib.sha3_384,
        "sha3_512": hashlib.sha3_512,
        "shake_128": hashlib.shake_128,
        "shake_256": hashlib.shake_256,
        "blake2b": hashlib.blake2b,
        "blake2s": hashlib.blake2s,
        "md5": hashlib.md5,
    }

    @staticmethod
    def create_hash(hash_alg: str, file_path: str) -> Optional[str]:
        if hash_alg not in Hasher.hashes:
            raise ValueError(f"Unsupported hash algorithm: {hash_alg}")

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        if not os.access(file_path, os.R_OK):
            raise PermissionError(f"Cannot read file: {file_path}")

        try:
            hash_obj = Hasher.hashes[hash_alg]()
            with open(file_path, "rb") as file:
                while chunk := file.read(4096):
                    hash_obj.update(chunk)
            if hash_alg in ("shake_128", "shake_256"):
                return hash_obj.hexdigest(32)
            return hash_obj.hexdigest()
        except Exception as e:
            raise RuntimeError(f"Error creating hash: {e}")

    @staticmethod
    def save_file(hash_alg: str, file_path: str, hash_value: str) -> None:
        if hash_alg not in Hasher.hashes:
            raise ValueError(f"Unsupported hash algorithm: {hash_alg}")

        new_file_path = f"{file_path}.{hash_alg}"

        try:
            with open(new_file_path, "w") as file:
                file.write(hash_value)
        except PermissionError:
            raise PermissionError(f"Cannot write to file: {new_file_path}")
        except Exception as e:
            raise RuntimeError(f"Error saving hash file: {e}")
