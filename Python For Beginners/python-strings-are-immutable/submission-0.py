def remove_fourth_character(word: str) -> str:
    word1 = word[:3]
    word2 = word[4:]

    return word1 + word2


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
