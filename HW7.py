class WordLengthIterator:
    def __init__(self, words):
        self._words = words
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._words):
            raise StopIteration
        word = self._words[self._index]
        self._index += 1
        return word, len(word)


words = ["яблуко", "груша", "апельсин", "ківі", "виноград"]

for word, length in WordLengthIterator(words):
    print(f"{word}: {length}")