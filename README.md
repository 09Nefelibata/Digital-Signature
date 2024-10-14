Digital Signature Verification Tool

This is a simple command-line tool written in Python that verifies the validity of a digital signature. It uses RSA public-key cryptography to ensure the authenticity and integrity of a document. This tool can be used to verify that a document has not been altered and was indeed signed by the owner of the public key.
How It Works

    Public Key: Provided directly in PEM format as an input.
    Document: The exact content of the document to be verified is passed as a string.
    Signature: The digital signature of the document, encoded in base64, is passed as an input.
    Verification: The tool verifies the signature using the provided public key and indicates whether the signature is valid or not.

Usage

    you need to generate private and public key by using keygen.py
    you need to signed a document (replace documents.txt with your document) with the help of default.py
    you can now verify that your signature is valid or not.(Replace documents.txt with your original document)

Security Considerations

    Ensure the public key provided is from a trusted source to prevent unauthorized verification.
    The document provided must match exactly what was originally signed.
    Use secure channels to transmit public keys and signatures.
