import os
def xor_encrypt_decrypt(input_path, output_path, key):
    try:
        with open(input_path, 'rb') as f_in, open(output_path, 'wb') as f_out:
            data = f_in.read()
            encrypted_data = bytearray([byte ^ key for byte in data])
            f_out.write(encrypted_data)
        print(f"✔ Operation successful! Output saved to '{output_path}'")
    except FileNotFoundError:
        print("❌ Error: File not found.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

def main():
    while True:
        print("\n==== Simple File Encryption Tool ====")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice not in ['1', '2', '3']:
            print("⚠ Invalid choice. Try again.")
            continue

        if choice == '3':
            print("Goodbye!")
            break

        file_path = input("Enter file path: ").strip()
        if not os.path.exists(file_path):
            print("❌ File does not exist.")
            continue

        try:
            key = int(input("Enter numeric key (0-255): "))
            if not (0 <= key <= 255):
                raise ValueError
        except ValueError:
            print("❌ Invalid key. Must be an integer between 0 and 255.")
            continue

        if choice == '1':
            output_file = input("Enter output filename for encrypted file: ").strip()
            xor_encrypt_decrypt(file_path, output_file, key)

        elif choice == '2':
            output_file = input("Enter output filename for decrypted file: ").strip()
            xor_encrypt_decrypt(file_path, output_file, key)

if __name__ == "__main__":
    main()

