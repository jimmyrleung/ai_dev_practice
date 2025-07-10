# MCP learning and practice

<!-- TOC start (generated with https://github.com/derlin/bitdowntoc) -->

- [MCP learning and practice](#mcp-learning-and-practice)
   * [Scenario](#scenario)
   * [Setting up the environment](#setting-up-the-environment)
   * [Running with Docker](#running-with-docker)
      + [Pre-requisites](#pre-requisites)

<!-- TOC end -->

<!-- TOC --><a name="scenario"></a>
## Scenario

Build a knowledge assistant for curious minds—students, journalists, or professionals—who frequently use Wikipedia for background research. Instead of opening tabs and scanning walls of text, users should be able to ask “Tell me about Alan Turing,” or “Summarize the topic of carbon cycles,” and receive structured results: a clean summary, the article title, and a link to the full page.

<!-- TOC --><a name="setting-up-the-environment"></a>
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

<!-- TOC --><a name="running-with-docker"></a>
## Running with Docker

You can customize this source code and build your own Docker image, or if you just want to test how it works, you can use the `jimmyrl19/mcp_wikipedia` docker image.

<!-- TOC --><a name="pre-requisites"></a>
### Pre-requisites

- An OpenAI API key

Once you have an OpenAI API KEY, you should be able to execute the following command to test it:

```sh
docker run -it -e OPENAI_API_KEY={your-open-ai-api-key} --rm jimmyrl19/mcp_wikipedia
```

- `-it` is needed since the interaction is done via CLI
- `--rm` will remove the container after it is deleted
- `-e OPENAI_API_KEY={your-open-ai-api-key}` will setup the OpenAI API Key
