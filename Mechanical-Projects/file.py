filename = input("Enter filename: ")
with open(filename, 'r') as file:
    text = file.read()
    word_count = len(text.split())
print(f"Word count: {word_count}")