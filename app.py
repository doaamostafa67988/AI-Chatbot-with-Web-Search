import streamlit as st
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from datetime import datetime
from dotenv import load_dotenv
import os
# loads .env into environment variables
load_dotenv()  
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# Page configuration
st.set_page_config(
    page_title="AI Chatbot with Web Search",
    page_icon="🤖",
    
)

# Title and description
st.title("🤖 AI Chatbot with Web Search")
st.markdown("Ask me anything! I can search the web for real-time information.")

if not GROQ_API_KEY:
    st.error("GROQ_API_KEY is missing")
    st.stop()
# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize session state for agent
if "agent" not in st.session_state:
    st.session_state.agent = None

# Create agent automatically
if st.session_state.agent is None:
    try:
        # Initialize tools
        tools = [DuckDuckGoSearchRun()]
        
        # Initialize LLM
        llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=GROQ_API_KEY,
            temperature=0.7
        )
        
        # Create agent
        st.session_state.agent = create_react_agent(
            model=llm,
            tools=tools,
            name="search_agent",
            prompt="You are a helpful AI assistant with access to web search. Use the search tool when you need current information or when you're not sure about something. Always provide accurate, well-researched answers."
        )
        
    except Exception as e:
        st.markdown("error")
        st.error(f"❌ Error initializing agent: {e}")
        st.stop()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        # Display tool calls if available
        if "tool_calls" in message and message["tool_calls"]:
            with st.expander("🔍 View Agent Thinking Process"):
                for call in message["tool_calls"]:
                    st.code(f"Tool: {call['name']}\nArguments: {call['args']}", language="python")

# Chat input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Invoke agent
                result = st.session_state.agent.invoke({
                    "messages": [{"role": "user", "content": prompt}]
                })
                
                # Extract tool calls
                tool_calls = []
                for msg in result["messages"]:
                    if hasattr(msg, "tool_calls") and msg.tool_calls:
                        for call in msg.tool_calls:
                            tool_calls.append({
                                "name": call["name"],
                                "args": call["args"]
                            })
                
                # Get final answer
                response = result["messages"][-1].content
                
                # Display response
                st.markdown(response)
                
                # Display tool calls if any
                if tool_calls:
                    with st.expander("🔍 View Agent Thinking Process"):
                        for call in tool_calls:
                            st.code(f"Tool: {call['name']}\nArguments: {call['args']}", language="python")
                
                # Add assistant message to chat history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response,
                    "tool_calls": tool_calls
                })
                
            except Exception as e:
                error_msg = f"❌ Error: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_msg,
                    "tool_calls": []
                })
