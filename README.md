# Shoreward - Travel Planning Assistant

A simple yet powerful travel planning assistant with AI-powered chat capabilities. This application provides a user-friendly interface to get travel recommendations, itinerary suggestions, and answers to your travel-related questions.

## Features

- AI-powered travel assistant
- Interactive chat interface
- Conversation history tracking
- FastAPI backend + Streamlit frontend

## Quick Start

### Prerequisites

- Python 3.8+
- pip

### Setup

1. **Clone the repository**

```bash
git clone https://github.com/xiaohan-coplanar/shoreward.git
cd shoreward
```

2. **Setup virtual environment**

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# For Windows
venv\Scripts\activate
# For macOS/Linux
source venv/bin/activate
```

3. **Configure environment variables**

Create a `.env` file under backend directory with the following content:

```
OPENAI_API_KEY=your_openai_api_key_here
```

4. **Install dependencies**

```bash
# Install backend dependencies
pip install -r requirements.txt
```

### Running the Application

Start the application:
```bash
fastapi run backend/main.py & streamlit run frontend/app.py
```

