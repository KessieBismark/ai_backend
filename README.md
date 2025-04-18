# German Language Learning AI API

Welcome to the **German Language Learning AI API**! This API is designed to assist users in learning German through interactive and personalized features powered by **FastAPI** and **Groq AI**. It offers tools for verb conjugation, interview preparation, model exploration, and general knowledge exploration, all tailored to enhance your German language skills.

## Features

### 1. Verb Conjugation Assistant

The **Verb Section** allows users to input a German verb or word and receive detailed conjugation information along with usage examples.

- **Input**: A German verb (e.g., "laufen").
- **Output**:
  - Present tense
  - Past tense
  - Future tense
  - Past participle
  - Example sentences for each tense

#### Example Request:
```json
{
  "verb": "laufen"
}
```

#### Example Response:
```json
{
  "present": "ich laufe, du läufst, er/sie/es läuft, wir laufen, ihr lauft, sie laufen",
  "past": "ich lief, du liefst, er/sie/es lief, wir liefen, ihr lieft, sie liefen",
  "future": "ich werde laufen, du wirst laufen, er/sie/es wird laufen, wir werden laufen, ihr werdet laufen, sie werden laufen",
  "past_participle": "gelaufen",
  "examples": {
    "present": "Ich laufe jeden Morgen im Park.",
    "past": "Gestern lief ich fünf Kilometer.",
    "future": "Morgen werde ich im Wald laufen."
  }
}
```

### 2. Interview Assistant

The **Interview Assistant** simulates realistic German-language interview conversations to help users prepare for job interviews.

- **Input**: An interview prompt or topic (e.g., "Tell me about yourself").
- **Output**: A dialogue between an interviewer and interviewee in German.

#### Example Request:
```json
{
  "prompt": "Tell me about yourself"
}
```

#### Example Response:
```json
{
  "conversation": [
    { "interviewer": "Können Sie mir etwas über sich erzählen?" },
    { "interviewee": "Ja, natürlich. Mein Name ist Anna, und ich bin Softwareentwicklerin mit fünf Jahren Erfahrung im Bereich Webentwicklung." },
    { "interviewer": "Was sind Ihre Stärken?" },
    { "interviewee": "Ich bin sehr detailorientiert und arbeite gut im Team." }
  ]
}
```

### 3. Model Exploration

The **Model Section** allows users to explore and query the models offered by Groq. Users can retrieve model IDs and use them for further interactions in the **General Search** feature.

- **Input**: A query to list available models.
- **Output**: A list of models with their corresponding IDs.

#### Example Request:
```json
{
  "action": "list_models"
}
```

#### Example Response:
```json
{
  "models": [
    { "id": "model-123", "description": "German language model v1" },
    { "id": "model-456", "description": "Advanced German conversational model" }
  ]
}
```

### 4. General Search

The **General Search** feature provides answers to a wide range of queries, considering context from previous conversations to provide more accurate and tailored responses.

- **Input**: Any question or topic in German or English.
- **Output**: A response based on the query, with contextual understanding from prior interactions.

#### Example Request:
```json
{
  "query": "What is the capital of Germany?"
}
```

#### Example Response:
```json
{
  "answer": "Die Hauptstadt von Deutschland ist Berlin.",
  "context": "Based on your previous interest in German geography, here are some additional facts about Berlin."
}
```

## Installation

### Prerequisites

- Python 3.8+
- FastAPI
- Groq AI library

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/KessieBismark/ai_backend.git
   cd <your application folder>
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory with the following content:
   ```env
   GROQ_API_KEY=<your-groq-api-key>
   ```
5. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

### Accessing the API

The API will be available at `http://127.0.0.1:8000`. Use tools like Postman or cURL to test endpoints.

## Endpoints

### `/conjugate`

- **Method**: POST
- **Description**: Provides verb conjugations and examples.
- **Input**: `{ "verb": "<German verb>" }`
- **Output**: Detailed conjugations and usage examples.

### `/interview`

- **Method**: POST
- **Description**: Generates interview dialogues based on the provided prompt.
- **Input**: `{ "prompt": "<Interview prompt>" }`
- **Output**: A conversation in German.

### `/models`

- **Method**: POST
- **Description**: Lists available models offered by Groq.
- **Input**: `{ "action": "list_models" }`
- **Output**: A list of model IDs and descriptions.

### `/search`

- **Method**: POST
- **Description**: Responds to general queries with contextual understanding.
- **Input**: `{ "query": "<Search query>" }`
- **Output**: A contextual response.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.


## Related Application

I have built an application that communicates with this backend using Flutter. You can find it at this [GitHub link](https://github.com/KessieBismark/lernen.git).



## Acknowledgements

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- AI powered by [Groq](https://groq.com/)

