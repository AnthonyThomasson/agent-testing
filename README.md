# OpenAI Agent SDK Example

This is a simple example project demonstrating how to use OpenAI's Agent SDK to create an AI agent that can perform tasks.

## Setup

### Option 1: Using DevContainer (Recommended)

1. Install [Docker](https://www.docker.com/products/docker-desktop/) and [VS Code](https://code.visualstudio.com/)
2. Install the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension in VS Code
3. Clone this repository
4. Open the project in VS Code
5. When prompted, click "Reopen in Container" or use the command palette (F1) and select "Remote-Containers: Reopen in Container"
6. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

### Option 2: Local Setup

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the example agent:
```bash
python main.py
```

The example agent demonstrates:
- Creating a simple agent with tools
- Using the agent to perform tasks
- Handling agent responses and errors

## Project Structure

- `main.py`: Contains the main agent implementation
- `requirements.txt`: Project dependencies
- `.env`: Environment variables (create this file with your API key)
- `.devcontainer/`: Development container configuration
  - `devcontainer.json`: VS Code devcontainer settings
  - `Dockerfile`: Container image definition 