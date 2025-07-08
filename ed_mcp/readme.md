# MCP learning and practice

## Scenario

Build a knowledge assistant for curious minds—students, journalists, or professionals—who frequently use Wikipedia for background research. Instead of opening tabs and scanning walls of text, users should be able to ask “Tell me about Alan Turing,” or “Summarize the topic of carbon cycles,” and receive structured results: a clean summary, the article title, and a link to the full page.

## Setting up the environment

The code is written in Python.

Install libs:

```python
# Python wrapper for the wikipedia API
pip install wikipedia

# Extends the default functionality of the `wikipedia` package and
# enable getting section-level content of a given wikipedia page
pip install wikipedia_sections

# Official Python SDK for MCP
pip install mcp

pip install langchain

# Help us construct the agent capable of tool invocation 
pip install langgraph

# Adapter package that integrates OpenAI models with LangChain
pip install langchain-openai

# Bridges LangChain's agent interface with the MCP client tools
pip install langchain-mcp-adapters
```
