def count_words(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read().lower()
            for ch in ['.', ',', '!', '?', ';', ':', '"', "'", '(', ')', '[', ']', '{', '}', '-', '_', '/']:
                text = text.replace(ch, ' ')
            
            words = text.split()
            counts = {}
            for word in words:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1
            for word, count in counts.items():
                print(f"{word}: {count}")
    except FileNotFoundError:
        print(f"File '{file}' not found.")

if __name__ == "__main__":
    filename = 'Sample.txt'
    count_words(filename)