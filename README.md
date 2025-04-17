# Shoreward - Travel Planning Assistant

A simple yet powerful travel planning assistant with AI-powered chat capabilities. This application provides a user-friendly interface to get travel recommendations, itinerary suggestions, and answers to your travel-related questions.

## Features

- AI-powered travel assistant
- Interactive chat interface
- Conversation history tracking

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

5. **Set up OpenAI Platform Key**

 🔧 Setup Instructions

To use this project, you'll need access to the [OpenAI API](https://platform.openai.com/). Follow the steps below to get started:

5.1. Create an OpenAI Account

If you don't already have one, sign up at [https://platform.openai.com/signup](https://platform.openai.com/signup).

5.2. Generate an API Key

Once logged in:

1. Visit [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys).
2. Click on **"Create new secret key"**.
3. Copy and save the key somewhere secure — you won't be able to see it again.

5.3. Set the API Key in Your Environment

For security, store the API key as an environment variable:

```bash
export OPENAI_API_KEY=your-api-key-here
```

Alternatively, you can create a `.env` file in your backend directory (following existing `.env.example`) and add:

```bash
OPENAI_API_KEY=your-api-key-here
```

> ⚠️ **Note:** Using the OpenAI API is **not free**. You will be charged based on your usage. Please review the pricing at [https://openai.com/pricing](https://openai.com/pricing) before proceeding.

### Running the Application

Start the application in terminal:
```bash
streamlit run run_shoreward_app.py
```


