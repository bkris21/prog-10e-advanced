def different_characters_in_word(word):
    return {item for item in word}


def different_characters_in_word_dict(word):
    result = {}
    for char in word:
        if char not in result.keys():
            result[char] = 0
        result[char] += 1
    return result


def max_char_in_word(word):
    my_dict = different_characters_in_word_dict(word)
    print(my_dict)
    max_char_value = 0
    max_char = list(my_dict.keys())[0]
    for k, v in my_dict.items():
        if max_char_value < v:
            max_char = k
            max_char_value = v
    return max_char, max_char_value


if __name__ == '__main__':
    word_in = input("Kérek egy szót:")
    print(f'Különböző karakterek száma: {len(different_characters_in_word(word_in))}')
    result_dict = different_characters_in_word_dict(word_in)
    print(f'Karakterek és azok száma: {result_dict}, tehát a különböző karakterek száma {len(result_dict)}')
    my_tuple = max_char_in_word(word_in)
    print(f'A legtöbbször előforduló karakter: {my_tuple[0]} db: {my_tuple[1]}')
