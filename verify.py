from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization

with open("public_key.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

with open("documents.txt", "rb") as f:
    document = f.read()

document_hash = hashes.Hash(hashes.SHA256())
document_hash.update(document)
digest = document_hash.finalize()

with open("signature.sig", "rb") as f:
    signature = f.read()

try:
    public_key.verify(
        signature,
        digest,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature is valid.")
except:
    print("Signature is invalid.")

