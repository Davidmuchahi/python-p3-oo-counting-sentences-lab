class MyString:
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value
  
    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith(".")
  
    def is_question(self):
        return self._value.endswith("?")
  
    def is_exclamation(self):
        return self._value.endswith("!")
    
    def count_sentences(self):
        if not self._value:
            return 0
            
        # Replace all sentence-ending punctuation with a single marker
        replaced = self._value.replace('!', '.').replace('?', '.')
        # Split on periods and filter out empty strings
        sentences = [s for s in replaced.split('.') if s.strip()]
        return len(sentences)