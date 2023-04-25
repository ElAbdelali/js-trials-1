"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    even_nums = []
    
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums


def get_odd_indices(items):
    odd_indices = []
    
    for item in items:
        if item % 2 != 0:
            odd_indices.append(items[item])
    return odd_indices


def print_as_numbered_list(items):
    i = 1
    
    for item in items:
        print(f"{i}. {item}")
        i += 1


def get_range(start, stop):
    
    nums = []
    
    for i in range(start, stop):
        nums.append(i)
    return nums    


def censor_vowels(word):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    chars = ['*' if letter in vowel_list else letter for letter in word]
    return ''.join(chars)
    

def snake_to_camel(string):
    camel_case = ""
    false = False
    
    for char in string:
        if char == '_':
            false = True
        elif false:
            camel_case += char.upper()
            false = False
        else:
            camel_case +=  char
    
    return camel_case


def longest_word_length(words):
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return len(longest_word)



def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
