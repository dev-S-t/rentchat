# Backend Developer Guide: Rental Agreement Assistant Integration

This guide provides documentation for backend developers who want to integrate the Rental Agreement Assistant chatbot into their applications.

## Overview

The `GeminiWrapper` class provides a simple interface to Google's Gemini AI model specifically configured for rental agreement assistance. The wrapper handles:

- API key configuration
- Conversation history management
- System prompt initialization
- Response generation

## Integration Options

### 1. Direct Class Import

```python
from gemini_wrapper import GeminiWrapper

# Create an instance
chatbot = GeminiWrapper()

# Generate a response
response = chatbot.chat("What are tenant rights in California?")
print(response)
```

### 2. API Wrapper (REST API Example)

For a web application, you might wrap the GeminiWrapper in a Flask/FastAPI endpoint:

```python
from flask import Flask, request, jsonify
from gemini_wrapper import GeminiWrapper

app = Flask(__name__)
chatbot = GeminiWrapper()

@app.route('/api/chat', methods=['POST'])
def chat_endpoint():
    data = request.json
    user_message = data.get('message', '')
    user_id = data.get('user_id', 'default')
    
    # In a production app, you'd retrieve/store conversations per user
    # This is a simplified example
    response = chatbot.chat(user_message)
    
    return jsonify({
        'response': response
    })

if __name__ == '__main__':
    app.run(debug=True)
```

## Customization

### Modifying the System Prompt

You can modify the system prompt to change the behavior of the chatbot:

```python
chatbot = GeminiWrapper()
chatbot.system_prompt = (
    "You are a rental agreement assistant specializing in California law. "
    "Provide detailed information about California tenant rights, "
    "obligations, and relevant laws."
)
# Reset history to apply the new prompt on next interaction
chatbot.reset_chat()
```

### Using Different Gemini Models

You can change the model used (if you have access to other Gemini models):

```python
class CustomGeminiWrapper(GeminiWrapper):
    def __init__(self, model_name='gemini-pro'):
        super().__init__()
        self.model = genai.GenerativeModel(model_name)
```

## Session Management

For multi-user applications, maintain separate instances:

```python
class ChatSessionManager:
    def __init__(self):
        self.sessions = {}
        
    def get_session(self, user_id):
        if user_id not in self.sessions:
            self.sessions[user_id] = GeminiWrapper()
        return self.sessions[user_id]
        
    def chat(self, user_id, message):
        session = self.get_session(user_id)
        return session.chat(message)
        
    def reset_session(self, user_id):
        if user_id in self.sessions:
            self.sessions[user_id].reset_chat()
```

## Error Handling

The wrapper handles basic API errors, but you may want to extend this:

```python
try:
    response = chatbot.chat(user_input)
except Exception as e:
    # Log the error
    logging.error(f"Error generating response: {e}")
    # Provide a fallback response
    response = "I'm having trouble processing your request. Please try again later."
```

## Environment Configuration

Ensure your application loads the environment variables properly:

```python
# In your application's initialization
from dotenv import load_dotenv
load_dotenv()  # Load from .env file

# Or set programmatically
import os
os.environ["GEMINI_API_KEY"] = "your-api-key"
```

## Extending Functionality

### Adding Search Capabilities

To enhance the chatbot with real search capabilities:

```python
class EnhancedGeminiWrapper(GeminiWrapper):
    def __init__(self):
        super().__init__()
        
    def search_regional_info(self, query, region):
        # Implement a search API call (e.g., Google Search API)
        # Return relevant information for the region
        pass
        
    def chat_with_search(self, user_input, region=None):
        # Extract region from input or use provided region
        extracted_region = self._extract_region(user_input) or region
        
        if extracted_region:
            search_results = self.search_regional_info(user_input, extracted_region)
            enhanced_input = f"{user_input}\n\nRelevant information for {extracted_region}: {search_results}"
            return self.chat(enhanced_input)
        else:
            # Ask for region if not provided
            return self.chat(user_input)
            
    def _extract_region(self, text):
        # Implement region extraction logic
        # Could use NER or pattern matching
        pass
```

## Performance Considerations

- The API calls to Gemini may have latency. Consider implementing asynchronous handling for web applications.
- For high-traffic applications, implement rate limiting and queuing to avoid exceeding API rate limits.
- Consider caching common responses to reduce API usage.

## Security Best Practices

- Never expose your API key in client-side code
- Validate and sanitize all user inputs before passing to the model
- Implement appropriate rate limiting for your API endpoints
- Consider implementing content filtering for responses when serving sensitive information 