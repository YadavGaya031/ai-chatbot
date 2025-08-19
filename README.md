# AI Chatbot with Context Memory

## Description
A sophisticated chatbot application built using Streamlit and the Groq API, featuring persistent context memory that maintains conversation history throughout the session. The chatbot leverages the LangChain library for robust message handling and provides seamless integration with DeepSeek's distilled Llama-70B model via Groq's high-performance API.

## Key Features

### 🧠 Context-Aware Conversations
- **Persistent Memory**: Maintains complete conversation history throughout the session
- **Context Window**: Uses previous messages to provide relevant, contextual responses
- **Message Threading**: Organizes conversations in a clear, chronological flow

### 🎯 Advanced AI Integration
- **DeepSeek R1 Distilled Llama-70B**: Powered by Groq's ultra-fast inference
- **Temperature Control**: Configurable creativity level (currently set to 1.0 for balanced responses)
- **Clean Output**: Automatically removes `<think>` tags from model responses for cleaner presentation

### 📁 Export & Data Management
- **JSON Export**: Download complete chat history with role-based message structure
- **Markdown Export**: Human-readable format with user/assistant labeling
- **Session Persistence**: Chat history maintained until browser session ends

## Installation

### Prerequisites
- Python 3.8 or higher
- Groq API key (obtain from [console.groq.com](https://console.groq.com))

### Setup Instructions

1. **Clone or download the project files**
   ```bash
   git clone <repository-url>
   cd ai-chatbot
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```
   GROQ_API_KEY=your_actual_api_key_here
   ```

4. **Verify installation**
   ```bash
   python -c "import streamlit; print('Streamlit installed successfully')"
   ```

## Usage

### Running the Application
```bash
streamlit run chatbot.py
```

### Accessing the Chatbot
1. Open your web browser to `http://localhost:8501`
2. Start typing in the chat input at the bottom
3. Press Enter or click the send button to submit your message
4. The AI will respond using the full conversation context

### Conversation Flow
- **System Context**: Each conversation starts with a system message defining the AI as a helpful assistant
- **User Messages**: Your inputs are added to the conversation history
- **AI Responses**: Generated based on the entire conversation context
- **Visual Indicators**: User messages and AI messages will get diifer by the emojis

## Technical Architecture

### Message Handling
The application uses LangChain's message classes for robust conversation management:
- **SystemMessage**: Defines AI behavior and constraints
- **HumanMessage**: Stores user inputs with full context
- **AIMessage**: Preserves AI responses for context continuity

### Context Management
- **Session State**: Utilizes Streamlit's session state to persist messages
- **Memory Efficiency**: Messages are stored in-memory during the session
- **Context Window**: No hard limit on conversation length (subject to model constraints)

### Export Formats

#### JSON Export Structure
```json
[
  {
    "role": "system",
    "content": "You are a helpful assistant."
  },
  {
    "role": "user",
    "content": "What's the weather like?"
  },
  {
    "role": "assistant",
    "content": "I don't have access to real-time weather data..."
  }
]
```

#### Markdown Export Format
```
**You:** What's the weather like?

**AI:** I don't have access to real-time weather data...
```

## Configuration Options

### Model Parameters
- **Model**: deepseek-r1-distill-llama-70b
- **Temperature**: 1.0 (adjustable for creativity vs. consistency)
- **Max Tokens**: Model default (can be customized)

### UI Customization
- **Page Title**: "AI Chatbot (Groq + Streamlit)"
- **Page Icon**: Robot emoji (🤖)

## Troubleshooting

### Common Issues

**API Key Problems**
- Ensure `.env` file exists in project root
- Verify API key is valid and has sufficient credits
- Check for typos in the environment variable name

**Import Errors**
- Verify all packages in requirements.txt are installed
- Check Python version compatibility (3.8+)
- Ensure virtual environment is activated (if using one)

**Display Issues**
- Clear browser cache and refresh the page
- Check browser console for JavaScript errors
- Verify Streamlit is updated to latest version

### Performance Optimization
- **Response Time**: Typically 1-3 seconds per query
- **Memory Usage**: Scales with conversation length
- **Browser Compatibility**: Works on all modern browsers

## Development & Extension

### Adding New Features
The modular structure supports easy extension:
- **New Export Formats**: Add functions to export_chat_json and export_chat_markdown
- **Model Switching**: Modify the ChatGroq initialization parameters
- **UI Enhancements**: Customize Streamlit components and styling

### Environment Variables
Additional configuration options can be added to `.env`:
```
GROQ_API_KEY=your_key_here
MODEL_NAME=deepseek-r1-distill-llama-70b
TEMPERATURE=1.0
MAX_TOKENS=4000
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Support & Contributing
For issues, feature requests, or contributions, please refer to the project repository's issue tracker.
