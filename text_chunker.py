
import re

class TextChunker:
    def __init__(self, max_words=300):
        """Initializes the TextChunker with a maximum number of words per chunk."""
        self.max_words = max_words

    def split_text_into_chunks(self, text):
        """
        Splits the given text into chunks with a maximum number of words per chunk.

        Parameters:
            text (str): The text to split.

        Returns:
            list: A list of text chunks.
        """
        sentences = re.split(r'(?<=[.!?]) +', text)
        chunks = []
        current_chunk = []
        current_word_count = 0

        for sentence in sentences:
            sentence_word_count = len(sentence.split())
            if current_word_count + sentence_word_count > self.max_words:
                chunks.append(" ".join(current_chunk))
                current_chunk = []
                current_word_count = 0

            current_chunk.append(sentence)
            current_word_count += sentence_word_count

        if current_chunk:
            chunks.append(" ".join(current_chunk))

        return chunks
# text_chunker = TextChunker()
# chunked_text = text_chunker.split_text_into_chunks(pdf_text)

# print(chunked_text)
# # print(type(chunked_text))
# # print(len(chunked_text))


