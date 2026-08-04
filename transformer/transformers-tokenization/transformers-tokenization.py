import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    """
    A word-level tokenizer with special tokens.
    """
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        
        # Special tokens
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None:
        """
        Build vocabulary from a list of texts.
        Add special tokens first, then unique words.
        """
        vocab = [self.pad_token, self.unk_token, self.bos_token, self.eos_token]
        words = [word.lower() for text in texts for word in text.split(" ")]
        words.sort()
        
        for word in words:
            if word not in vocab:
                vocab.append(word)

        self.vocab_size = len(vocab)
        for id, word in enumerate(vocab):
            self.word_to_id[word] = id
            self.id_to_word[id] = word        
    
    def encode(self, text: str) -> List[int]:
        """
        Convert text to list of token IDs.
        Use UNK for unknown words.
        """
        if not text:
            return []
            
        encoded = []
        for word in text.split(" "):
            word = word.lower()
            if word not in self.word_to_id:
                encoded.append(self.word_to_id["<UNK>"])
            else:
                encoded.append(self.word_to_id[word])
        return encoded
    
    def decode(self, ids: List[int]) -> str:
        """
        Convert list of token IDs back to text.
        """
        if not ids:
            return ""

        decoded = []
        for id in ids:
            if id > self.vocab_size:
                decoded.append("<UNK>")
            else:
                decoded.append(self.id_to_word[id])
        return " ".join(decoded)
