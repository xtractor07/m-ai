# M-AI

A customizable AI assistant built with Llama 2, featuring conversational abilities and extensible architecture.

## Project Structure

```
m-ai/
├── src/               # Source code
│   ├── core/         # Core AI functionality
│   ├── conversation/ # Conversation handling
│   ├── plugins/      # Extensible plugins
│   ├── api/          # API interface
│   └── utils/        # Utility functions
├── tests/            # Test files
├── configs/          # Configuration files
├── docs/             # Documentation
└── scripts/          # Utility scripts
```

## Features

- Llama 2 integration for powerful language processing
- Modular plugin architecture for extensibility
- Conversation management with context awareness
- API interface for easy integration
- Configurable system parameters

## Setup

1. Clone the repository
2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure the environment variables
5. Run the application

## Configuration

Create a `.env` file based on `.env.example` and set your configuration values.

## Development

- Follow PEP 8 style guide
- Write tests for new features
- Document your code
- Create feature branches for development

## License

[MIT License](LICENSE)