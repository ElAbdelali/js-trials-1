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
    chars = []
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    str = ""
    for letter in word:
        if letter in vowel_list:
            chars.append('*')
        else:
            chars.append(letter)
    return str.join(chars)
            


def snake_to_camel(string):
    camel = []
    
    for word in string.split('_'):
        camel.append(f'{word[0].upper()}{word.split(1)}')
        
    return ''.join(camel)
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
