#!/usr/bin/env python3
"""Entry untuk bounty make.fun "One Word, One Username, One Reward".

Menulis username make.fun milik sendiri, satu kata, ke /output/entry.txt.
Ditulis sebagai byte mentah agar hasilnya persis 9 byte "tedinasia",
tanpa newline tambahan dan tanpa translasi newline apa pun.

Hanya memakai modul standar Python (os); tanpa dependensi luar.
"""

import os

# Username make.fun milik sendiri, satu kata, 9 karakter.
ENTRY = b"tedinasia"

OUTPUT_PATH = "/output/entry.txt"


def main():
    """Tulis ENTRY ke OUTPUT_PATH, buat direktori /output bila belum ada."""
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # Mode "wb": byte ditulis apa adanya, tanpa newline translation.
    with open(OUTPUT_PATH, "wb") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
