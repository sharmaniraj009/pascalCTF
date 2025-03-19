# import os, random, string

# alphabet = string.ascii_letters + string.digits + "{}_-.,/%?$!@#"
# FLAG : str = os.getenv("FLAG")
# assert FLAG.startswith("pascalCTF{")
# assert FLAG.endswith("}")

# def romanize(input_string):
#     key = random.randint(1, len(alphabet) - 1)
#     result = [""] * len(input_string)
#     for i, c in enumerate(input_string):
#         result[i] = alphabet[(alphabet.index(c) + key) % len(alphabet)]
#     return "".join(result)

# if __name__ == "__main__":
#     result = romanize(FLAG)
#     assert result != FLAG
#     with open("output.txt", "w") as f:
#         f.write(result)

# # output: TEWGEP6a9rlPkltilGXlukWXxAAxkRGViTXihRuikkos



import string

def deromanize(encrypted_flag):
    alphabet = string.ascii_letters + string.digits + "{}_-.,/%?$!@#"
    
    for key in range(len(alphabet)):
        result = "".join(
            alphabet[(alphabet.index(c) - key) % len(alphabet)] if c in alphabet else c
            for c in encrypted_flag
        )
        if result.startswith("pascalCTF{") and result.endswith("}"):
            return result
    return None

def main():
    with open("output.txt", "r") as f:
        encrypted_flag = f.read().strip()
    
    flag = deromanize(encrypted_flag)
    if flag:
        print("[+] Flag found:", flag)
    else:
        print("[-] Could not retrieve flag.")

if __name__ == "__main__":
    main()