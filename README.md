![AI Chatbot Preview](https://drive.google.com/uc?export=view&id=1_JCZ5Oku_tnQnxI_aXBOqxgywylgROYN)

# AI-Chatbot-with-Web-Search
A Streamlit-based AI chatbot that can answer questions in real-time using both an advanced LLM and live web search. This project integrates LangChain, LangGraph, and ChatGroq to create a responsive assistant capable of retrieving up-to-date information from the web using DuckDuckGo Search
## Features
- **Real-time web search**: Provides accurate answers by querying the web when needed.  
- **Advanced language model**: Powered by `llama-3.3-70b-versatile` via ChatGroq.  
- **Interactive chat interface**: Built with Streamlit, allowing a smooth conversational experience.  
- **Tool usage transparency**: View the AI’s reasoning and tool calls via expandable sections.  
- **Session-based chat history**: Keeps track of previous messages in the session for context-aware conversations.  

## Requirements
- Python 3.11+
- Streamlit
- LangChain, LangGraph, LangChain-Groq
- DuckDuckGoSearchRun
- `.env` file with `GROQ_API_KEY`  

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/doaamostafa67988/AI-Chatbot-with-Web-Search
   ```
3. Install dependencies:
   ```bash
    pip install -r requirements.txt
   ```
3. Create a .env file and add your GROQ API key:
   ```bash
    GROQ_API_KEY=your_api_key_here
   ```
4. Run the app:
   ```bash
    streamlit run app.py
   ```

## License

This project is open-source and available under the MIT License
