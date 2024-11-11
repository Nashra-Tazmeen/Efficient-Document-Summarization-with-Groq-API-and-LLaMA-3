from groq import Groq

class TextSummarizer:
    def __init__(self, groq_api_key, model="llama3-8b-8192", temperature=0.7, max_tokens=1000, top_p=1):
        """
        Initializes the TextCleaner class with the Groq API key and default model parameters.
        
        Args:
            groq_api_key (str): The API key for accessing the Groq API.
            model (str): The Groq model to use for text cleaning.
            temperature (float): Controls the randomness in the output.
            max_tokens (int): The maximum number of tokens to generate.
            top_p (float): Controls the diversity of the output.
        """
        self.client = Groq(api_key=groq_api_key)
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p

    def clean_text(self, chunk):
        """
        Cleans and formats the text chunk to improve readability and focuses on specific investor elements.
        
        Args:
            chunk (str): The raw text to be cleaned.
            agent_context (str): Optional additional context for the cleaning agent.

        Returns:
            str: The cleaned and formatted text.
        """
        # Prepare the cleaning prompt
        context = """
                    You are an AI model trained to analyze financial documents from the perspective of an investor. Your task is to process the provided 
                    financial data or company report, ensuring that all relevant information is extracted in a way that highlights the most important factors for investors.
                    
                    You should clean and process the data by removing any irrelevant sections such as:
                    - **Table of contents**, legal disclaimers, boilerplate text, or other generic content that does not provide value to the analysis.
                    - **Historical or outdated data** that is not pertinent to forecasting the company's future.
                    - **Non-financial content**, like promotional material or unrelated charts and graphs.
                    - **Excessive formatting** that may obscure the core financial information."""
        
        prompt ="""Please analyze the following company financial data and provide an investor-focused and make sure to include all numeric values for all metrics
                    
                    **Future Growth Prospects**: Identify any signs of potential growth for the company, including new market opportunities, business expansions, or projected increases in revenue. **Ensure that all numeric values** mentioned, such as growth percentages, future revenue figures, or market share projections, are captured and included in your analysis.

                    **Key Business Changes**: Highlight significant changes in the company’s structure, operations, or strategy that might affect its future performance. **Include all numeric values** tied to these changes, such as revenue impacts, cost savings, or any figures provided that illustrate how these changes will affect the business.

                    **Key Triggers**: Identify any external or internal factors that might significantly affect the company’s financial performance, such as regulatory changes, market trends, or new competitors. **Ensure that all relevant numeric values** are included, such as projected market share shifts, investment figures, or economic impacts linked to these triggers.

                    **Impact on Coming Year Earnings and Growth**: Assess how the factors identified in""" + chunk


        # Set up the chat message format for the API call
       
        try:
            # Make the completion request to Groq API
            chat_completion = self.client.chat.completions.create(
                messages = [
                {"role": "system", "content": context},
                {"role": "user", "content": prompt}
               ],

               
                model=self.model,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                top_p=self.top_p,
                stop=None,
                stream=False
            )

            # Extract the cleaned text
            cleaned_text = chat_completion.choices[0].message.content.strip()
            
            return cleaned_text

        except Exception as e:
            print(f"Error during Groq API call: {e}")
            return chunk  # Return the original text if there's an error


