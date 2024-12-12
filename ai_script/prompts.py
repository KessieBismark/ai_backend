from langchain_core.prompts import PromptTemplate


def verb_prompt(data:str):
    prompt = PromptTemplate(
        input_variables=["data"],
        template = """
        Provide a comprehensive, structured JSON response for the verb "{data}":
        {{
            "german_data": "German translation of '{data}'",
            "data_forms": {{
                "present": {{
                    "ich": "form",
                    "du": "form",
                    "er/sie/es": "form",
                    "wir": "form",
                    "ihr": "form",
                    "sie/Sie": "form"
                }},
                "present_continuous": {{
                    "ich": "form",
                    "du": "form",
                    "er/sie/es": "form",
                    "wir": "form",
                    "ihr": "form",
                    "sie/Sie": "form"
                }},
                "past": {{
                    "ich": "form",
                    "du": "form",
                    "er/sie/es": "form",
                    "wir": "form",
                    "ihr": "form",
                    "sie/Sie": "form"
                }},
                "past_participle": "Past participle form"
            }},
            "example_sentences": {{
                "present": "Example sentence in present tense",
                "present_continuous": "Example sentence in present continuous",
                "past": "Example sentence in past tense",
                "past_participle": "Example sentence using past participle"
            }}
        }}

        Ensure the response is valid, well-structured JSON and provides all verb forms and examples with pronouns."""

    )
    return prompt


def conversation_prompt(data:str):
    prompt = PromptTemplate(
    input_variables=["data"],
    template = """
         Provide a bilingual conversation based on the input provided. The response should include both the German and English translations for each line of dialogue. Structure the response as a JSON object.

    Input: "{data}"

    Output:
    {{
        "conversation": [
            {{
                "speaker": "Speaker 1",
                "german": "German translation of the first line of '{data}'",
                "english": "English translation of the first line of '{data}'"
            }},
            {{
                "speaker": "Speaker 2",
                "german": "German translation of the second line of '{data}'",
                "english": "English translation of the second line of '{data}'"
            }}
            // Add more speakers and lines if necessary
        ]
    }}

    Ensure the output is valid, well-structured JSON and matches the conversation input provided.
    """
    )
    return prompt

def general_search_prompt(query: str):
    prompt = PromptTemplate(
        input_variables=["query"],
        template = """
        You are tasked with performing a general search based on the input provided. The response should include the key topics, categories, and a summarized overview relevant to the search query. Structure the response as a JSON object.

        Input: "{query}"

        Output:
        {{
            "search_summary": {{
                "query": "{query}",
                "key_topics": [
                    "Key topic 1 relevant to '{query}'",
                    "Key topic 2 relevant to '{query}'",
                    // Add more key topics if necessary
                ],
                // Add categories if any
                "categories": [
                    "Category 1",
                    "Category 2",
                    // Add more categories if necessary
                ],
                "overview": "A concise summary of the search result for '{query}'"
            }}
        }}

        Ensure the output is valid JSON, contains all fields, and accurately reflects the input query.
        """
    )
    return prompt
