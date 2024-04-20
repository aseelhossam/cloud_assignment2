import re
from collections import Counter
from nltk.corpus import stopwords

# Function to read the contents of a file
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Function to remove stop words from text
def remove_stop_words(text):
    stop_words = set(stopwords.words('english'))
    # Split text into words
    words = re.findall(r'\b\w+\b', text.lower())
    # Remove stop words
    filtered_words = [word for word in words if word not in stop_words]
    return filtered_words

# Function to count word frequency
def count_word_frequency(words):
    return Counter(words)

# Main function
def main():
    # Read contents of the file
    file_content = read_file("paragraphs.txt")
    
    # Remove stop words
    filtered_words = remove_stop_words(file_content)
    
    # Count word frequency
    word_frequency = count_word_frequency(filtered_words)
    
    # Display word frequency count
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    main()