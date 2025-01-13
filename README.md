# Browser Use: AI-Powered Browser Automation

This Python script demonstrates how to harness the power of Browser Use, a powerful yet simple tool that connects AI agents to the browser. Browser Use allows AI agents to interact with websites seamlessly, making web-based automation tasks straightforward and efficient.

## Overview

Browser Use simplifies browser automation by providing an easy-to-use interface for AI agents. This tool enables AI-powered agents to:

- Access and navigate websites programmatically.
- Perform complex interactions like clicking buttons, filling forms, or playing videos.
- Retrieve content from web pages and process it intelligently.
In this script, Browser Use is used alongside LangChain's ChatOpenAI for robust task execution and asynchronous Python for efficient processing.

# Demo 1

[Prompt]: Go to British Airways website, search for a return flight from London to New York, Depart 20/01/2025 return 30/01/2025 and return the cheapest flight.
![Letter to Papa](https://github.com/Haryohmi/browse_use_agent_for_browser/blob/main/agent_history1.gif)

<br/><br/>

# Demo 2

[Prompt]: Go to https://www.youtube.com/@HarvestersTV/videos, click on the first video and play it.
![Letter to Papa](https://github.com/Haryohmi/browse_use_agent_for_browser/blob/main/agent_historyHtv.gif)

---

Features
Effortless Browser Automation: Connect AI agents to browsers with minimal setup.
AI-Driven Interaction: Utilize OpenAI's GPT models to drive intelligent web interactions.
Customizable Tasks: Easily adapt the script for different websites and tasks.
Asynchronous Execution: Efficiently handle tasks without blocking resources.

---

## Prerequisites

Prerequisites
To use this script, you need:
1. Python 3.8+.
2. Required Libraries:
- Browser Use
- langchain
- asyncio
- openai
3. OpenAI API Key:
- Obtain an API key from OpenAI.
- Set it as an environment variable:
     ```bash
     export OPENAI_API_KEY='your_openai_api_key'
     ```

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
2. Install dependencies:
```bash
   pip install -r requirements.txt
```

# Usage
1. Open the main.py file.

2. Specify the task for the agent in the Agent object:
```bash
agent = Agent(
    task="Go to https://www.youtube.com/@HarvestersTV, click on the first video and play it",
    llm=ChatOpenAI(model="gpt-4o"),
)
```
3. Run the script:
```bash
python main.py
```

# Customization
You can easily modify the task parameter to suit your needs. Examples:

- Search and Fetch:
```bash
task="Search Google for 'top Python frameworks' and return the first result link."
```
- Extract Content:
```bash
task="Go to a news website and retrieve the latest headlines."
```

# feel free to fork the repository and submit a pull request.


Acknowledgments
- Browser Use: The backbone of the browser automation.
- LangChain: Framework for AI agent integration.
- penAI: For powering the intelligent interactions.
- Python Community: For the tools and libraries that make automation accessible.

With Browser Use, you can empower your AI agents to navigate and interact with the web like never before. 🚀
