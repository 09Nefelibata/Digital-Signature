## Digital Signature Verification Tool

This is a simple command-line tool written in Python that verifies the validity of a digital signature. It uses RSA public-key cryptography to ensure the authenticity and integrity of a document. This tool can be used to verify that a document has not been altered and was indeed signed by the owner of the public key.

# How It Works

1. **Public Key**: Provided directly in PEM format as an input.
2. **Document**: The exact content of the document to be verified is passed as a string.
3. **Signature**: The digital signature of the document, encoded in base64, is passed as an input.
4. **Verification**: The tool verifies the signature using the provided public key and indicates whether the signature is valid or not.

### Usage
1. you need to generate private and public key by using keygen.py
2. you need to signed a document with the help of default.py
3. you can now verify that your signature is valid or not.

### Security Considerations

- Ensure the public key provided is from a trusted source to prevent unauthorized verification.
- The document provided must match exactly what was originally signed.
- Use secure channels to transmit public keys and signatures.

#this is my first project
--Aayushi


