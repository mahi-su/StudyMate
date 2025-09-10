# StudyMate Application

StudyMate is an AI-powered academic assistant designed to help students interact with their study materials in a conversational format. This application allows users to upload PDF documents and ask questions related to the content, receiving AI-generated responses based on the material.

## Features

- **AI-Powered Q&A**: Leverage the power of AI to ask questions about your study materials and receive accurate answers.
- **PDF Upload**: Easily upload PDF documents for analysis and interaction.
- **Conversation History**: Keep track of your questions and the AI's responses for future reference.

## Installation

To get started with the StudyMate application, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd studymate
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

This will start the Streamlit interface, allowing you to upload PDFs and interact with the AI assistant.

## Project Structure

```
studymate
├── src
│   ├── main.py          # Entry point for the application
│   ├── ai
│   │   └── assistant.py # AI interaction management
│   ├── pdf
│   │   └── parser.py    # PDF text extraction
│   ├── conversation
│   │   └── chat.py      # Conversation history management
│   └── utils
│       └── helpers.py    # Utility functions
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
└── setup.py              # Packaging information
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.