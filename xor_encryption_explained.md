# XOR File Encryption/Decryption Script — Detailed Syntax & Function Explanation

This Markdown file explains the **syntax** and **function** of each line in your Python script.

---

```python
import os
```
- **`import`** → Keyword to include a Python module.
- **`os`** → Module for interacting with the operating system (e.g., file checking, path handling).

---

```python
def xor_encrypt_decrypt(input_path, output_path, key):
```
- **`def`** → Defines a function.
- **`xor_encrypt_decrypt`** → Function name.
- **`input_path`** → String: Path of file to process.
- **`output_path`** → String: Where to save processed file.
- **`key`** → Integer (0–255) used for XOR encryption.

---

```python
    try:
```
- **`try:`** → Starts a block of code to monitor for errors.

---

```python
        with open(input_path, 'rb') as f_in, open(output_path, 'wb') as f_out:
```
- **`with`** → Context manager; ensures files are automatically closed after use.
- **`open(input_path, 'rb')`** → Opens the input file in **binary read mode** (`rb`).
- **`open(output_path, 'wb')`** → Opens the output file in **binary write mode** (`wb`).
- **`as f_in / as f_out`** → Assigns these file objects to variables `f_in` and `f_out`.

---

```python
            data = f_in.read()
```
- **`.read()`** → Reads entire file contents as bytes.

---

```python
            encrypted_data = bytearray([byte ^ key for byte in data])
```
- **List comprehension** → `[byte ^ key for byte in data]` loops over each byte.
- **`^`** → XOR operator; compares bits and returns 1 where bits differ.
- **`key`** → Integer key for encryption/decryption.
- **`bytearray(...)`** → Mutable sequence of bytes, allows binary data manipulation.

---

```python
            f_out.write(encrypted_data)
```
- **`.write()`** → Writes binary data to file.

---

```python
        print(f"✔ Operation successful! Output saved to '{output_path}'")
```
- **`print()`** → Outputs text to console.
- **`f"..."`** → f-string; allows variable insertion inside `{}`.

---

```python
    except FileNotFoundError:
        print("❌ Error: File not found.")
```
- **`except FileNotFoundError:`** → Catches missing file error.

---

```python
    except Exception as e:
        print(f"❌ An error occurred: {e}")
```
- **`Exception`** → Catches all other errors.
- **`as e`** → Stores the error object in variable `e`.

---

```python
def main():
```
- Defines the **main program** function.

---

```python
    while True:
```
- Infinite loop until `break` is encountered.

---

```python
        print("\n==== Simple File Encryption Tool ====")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")
```
- Displays a user menu.
- **`\n`** → Inserts a blank line.

---

```python
        choice = input("Enter your choice (1/2/3): ")
```
- **`input()`** → Gets text from user.
- Stores choice as a string in `choice`.

---

```python
        if choice not in ['1', '2', '3']:
            print("⚠ Invalid choice. Try again.")
            continue
```
- **`not in`** → Checks if value is absent in the list.
- **`continue`** → Skips to the next loop iteration.

---

```python
        if choice == '3':
            print("Goodbye!")
            break
```
- **`break`** → Exits loop.

---

```python
        file_path = input("Enter file path: ").strip()
```
- **`.strip()`** → Removes leading/trailing spaces.

---

```python
        if not os.path.exists(file_path):
            print("❌ File does not exist.")
            continue
```
- **`os.path.exists()`** → Returns `True` if file or directory exists.

---

```python
        try:
            key = int(input("Enter numeric key (0-255): "))
            if not (0 <= key <= 255):
                raise ValueError
```
- **`int()`** → Converts string to integer.
- **`0 <= key <= 255`** → Validates key range.
- **`raise ValueError`** → Forces an error if range is invalid.

---

```python
        except ValueError:
            print("❌ Invalid key. Must be an integer between 0 and 255.")
            continue
```
- Handles invalid integer inputs.

---

```python
        if choice == '1':
            output_file = input("Enter output filename for encrypted file: ").strip()
            xor_encrypt_decrypt(file_path, output_file, key)

        elif choice == '2':
            output_file = input("Enter output filename for decrypted file: ").strip()
            xor_encrypt_decrypt(file_path, output_file, key)
```
- Calls `xor_encrypt_decrypt()` with given parameters.

---

```python
if __name__ == "__main__":
    main()
```
- **`__name__`** → Special variable; equals `"__main__"` if script is run directly.
- **`main()`** → Starts the program.
