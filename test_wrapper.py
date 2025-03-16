import unittest
from unittest.mock import patch, MagicMock
from gemini_wrapper import GeminiWrapper

class TestGeminiWrapper(unittest.TestCase):
    
    @patch('gemini_wrapper.genai.GenerativeModel')
    def test_chat_first_message(self, mock_generative_model):
        # Setup mock
        mock_model_instance = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "I'm a helpful assistant. What region are you inquiring about?"
        mock_model_instance.generate_content.return_value = mock_response
        mock_generative_model.return_value = mock_model_instance
        
        # Create an instance of GeminiWrapper
        wrapper = GeminiWrapper()
        
        # Test chat method with first message
        response = wrapper.chat("Hello, I need help with my rental agreement.")
        
        # Assert history has system prompt, user message, and assistant response
        self.assertEqual(len(wrapper.history), 3)
        self.assertEqual(wrapper.history[0]["role"], "system")
        self.assertEqual(wrapper.history[1]["role"], "user")
        self.assertEqual(wrapper.history[1]["parts"][0], "Hello, I need help with my rental agreement.")
        self.assertEqual(wrapper.history[2]["role"], "assistant")
        self.assertEqual(wrapper.history[2]["parts"][0], "I'm a helpful assistant. What region are you inquiring about?")
        
        # Assert mock was called with correct history
        mock_model_instance.generate_content.assert_called_once()
        
    @patch('gemini_wrapper.genai.GenerativeModel')
    def test_reset_chat(self, mock_generative_model):
        # Setup mock
        mock_model_instance = MagicMock()
        mock_generative_model.return_value = mock_model_instance
        
        # Create an instance of GeminiWrapper
        wrapper = GeminiWrapper()
        
        # Add some items to history
        wrapper.history = [{"role": "user", "parts": ["test"]}]
        
        # Reset the chat
        wrapper.reset_chat()
        
        # Assert history is empty
        self.assertEqual(len(wrapper.history), 0)
        
if __name__ == "__main__":
    unittest.main() 