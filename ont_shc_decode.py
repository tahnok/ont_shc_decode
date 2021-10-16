"""
Decode Ontario (or any other place using the SHC format) Vaccine Passports

Usage:
    pass a file (or list of files) containing the contents of the QR code

    OR

    pass contents of QR code in stdin

Outputs: JSON encoded data
"""
import fileinput
import json

import jwt


def decode_shc(raw):
    if not raw.startswith("shc:/"):
        raise Exception("malformed SHC, should start with shc:/")
    raw = raw.strip()[5:]  # clean up input, remove shc:/
    pairs = [
        chr(int(raw[i : i + 2]) + 45)  # add 45 to each 2 digits and turn into char
        for i in range(0, len(raw), 2)
    ]
    raw_jwt = "".join(pairs)

    decoded_jwt = jwt.decode(
        raw_jwt,
        options={
            "verify_signature": False
        },  # could verify if we download the right key
    )
    return decoded_jwt


if __name__ == "__main__":
    for raw in fileinput.input():
        print(json.dumps(decode_shc(raw), indent=2))
