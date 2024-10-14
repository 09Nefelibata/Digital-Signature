from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend  

try:
    with open("private_key.pem", "rb") as f:
        private_key = serialization.load_pem_private_key(
            f.read(),
            password=None, 
            backend=default_backend()  
        )
except FileNotFoundError:
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    with open("private_key.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))
with open("documents.txt", "rb") as f:
    document = f.read()

document_hash = hashes.Hash(hashes.SHA256())
document_hash.update(document)
digest = document_hash.finalize()

signature = private_key.sign(
    digest,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

with open("signature.sig", "wb") as f:
    f.write(signature)
