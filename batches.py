class TokenBatcher:
    def __init__(self, token_limit=4000, model="llama3-8b-8192"):
        self.token_limit = token_limit
        self.model = model

    def num_tokens_from_string(self, string):
        """
        Calculates the number of tokens in a string.
        """
        return len(string.split())

    def create_batches(self, text_chunks):
        """
        Creates batches of text chunks, each within the token limit.
        """
        batches = []
        current_batch = []
        current_token_count = 0

        for chunk in text_chunks:
            chunk_tokens = self.num_tokens_from_string(chunk)

            if current_token_count + chunk_tokens > self.token_limit:
                # If adding this chunk exceeds the token limit, start a new batch
                batches.append(current_batch)
                current_batch = [chunk]
                current_token_count = chunk_tokens
            else:
                # Add the chunk to the current batch
                current_batch.append(chunk)
                current_token_count += chunk_tokens

        # Add the final batch if there are any remaining chunks
        if current_batch:
            batches.append(current_batch)

        return batches

