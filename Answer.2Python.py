#Q2
def highest_frequency_word_length(s):
    words = s.split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    max_frequency = max(word_count.values())
    max_length = 0

    for word, frequency in word_count.items():
        if frequency == max_frequency:
            max_length = max(max_length, len(word))

    return max_length

# Test cases
if __name__ == "__main__":
    # Test case 1
    string1 = "write write write all the number from from from 1 to 100"
    print(highest_frequency_word_length(string1)) 

    # Test case 2
    string2 = "apple orange banana apple banana orange apple orange"
    print(highest_frequency_word_length(string2))  

    # Test case 3
    string3 = "hello world hello world world world"
    print(highest_frequency_word_length(string3)) 
