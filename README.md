AI Chat Bot with Multiple Personalities

An AI-powered chatbot that can interact with users using multiple personalities. The project uses modern Generative AI tools and LangChain to create flexible and engaging conversations.

🚀 Features
🤖 AI-powered conversational chatbot
🎭 Multiple AI personalities
💬 Natural and interactive conversations
🧠 Embedding-based functionality
🔗 LangChain integration
⚡ FastAPI backend
🔐 API keys managed securely using .env
📦 Modular project structure
🔄 Easy to add new personalities and models
🛠️ Tech Stack
Python
LangChain
LangChain Core
LangChain Community
LangChain OpenAI
LangChain Groq
LangChain Google GenAI
LangChain Mistral AI
FAISS
FastAPI
Uvicorn
Python-dotenv
Tiktoken
📁 Project Structure
AI-CHATBOT-WITH-MULTIPLE-PERSONALITIES/
│
├── CHATMODELS/
│   └── chat.py
│
├── EMBEDDINGSMODELS/
│   └── embedding.py
│
├── .gitignore
├── requirements.txt
├── README.md
└── .env

.env is intentionally excluded from GitHub because it contains API credentials.

⚙️ Installation
1. Clone the repository
git clone https://github.com/Tushar-Raghav01/AI-CHATBOT-WITH-MULTIPLE-PERSONALITIES.git
2. Navigate to the project
cd AI-CHATBOT-WITH-MULTIPLE-PERSONALITIES
3. Create a virtual environment
python -m venv .venv
4. Activate the virtual environment

Windows PowerShell:

.venv\Scripts\activate
5. Install dependencies
python -m pip install -r requirements.txt
🔑 Environment Variables

Create a .env file in the root directory:

OPENAI_API_KEY=your_api_key
GROQ_API_KEY=your_api_key
GOOGLE_API_KEY=your_api_key
MISTRAL_API_KEY=your_api_key

Add only the API keys required by the models you are using.

Never upload your .env file or API keys to GitHub.

▶️ Running the Project

For the chatbot:

python CHATMODELS/chat.py

If using FastAPI:

uvicorn main:app --reload

Then open:

http://127.0.0.1:8000
🧠 Embeddings

The project also contains embedding-related functionality inside:

EMBEDDINGSMODELS/

Large downloaded model files are excluded from Git using .gitignore.

🔮 Future Improvements
Add a web-based chat interface
Add more personalities
Add conversation memory
Add authentication
Store chat history
Add streaming responses
Deploy the application
Add RAG-based document chatting
👨‍💻 Author

Tushar Raghav

GitHub: Tushar-Raghav01

⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub.
