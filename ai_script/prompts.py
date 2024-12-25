from langchain_core.prompts import PromptTemplate


def verb_prompt(data:str):
    prompt = PromptTemplate(
        input_variables=["data"],
        template = """
        Provide a comprehensive, structured json response for the verb "{data}":
        {{
            "german_data": "German translation of '{data}' as well as the english if the verb is not in english",
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
                "future": {{
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
                "future": "Example sentence in future tense",
                "past": "Example sentence in past tense",
                "past_participle": "Example sentence using past participle",
                "Dative": "Example sentence using dative",
                "Accusative": "Example sentence using accusative"


            }}
        }}

        Ensure the response is valid, well-structured JSON and provides all verb forms and examples with pronouns."""

    )
    return prompt


def conversation_prompt(data:str):
    prompt = PromptTemplate(
    input_variables=["data"],
    template = """
         Provide a bilingual conversation based on the input provided. The response should include both the German and English translations for each line of dialogue and most have at least 30 conversations. Structure the response as a JSON object.

    Input: "{data}"

    Output:
    {{
        "conversation": [
            {{
                "speaker": "Interviewer",
                "german": "German translation of the first line of '{data}'",
                "english": "English translation of the first line of '{data}'"
            }},
            {{
                "speaker": "Interviewee",
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

def conversation_continuation_prompt(data:str):
    prompt = PromptTemplate(
    input_variables=["data", "chat_history"],
    template = """
    Previous conversation:
    {chat_history}

    continue with this bilingual conversation based on the chat history input provided. The response should include both the German and English translations for each line of dialogue and most have at least 30 conversations. Structure the response as a JSON object.

    Input: "{data}"

    Output:
    {{
        "conversation": [
            {{
                "speaker": "Interviewer",
                "german": "German translation of the first line of '{data}'",
                "english": "English translation of the first line of '{data}'"
            }},
            {{
                "speaker": "Interviewee",
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

def get_title_prompt(query: str):

    prompt = PromptTemplate(
        input_variables=["query"],
        template="""
      "give me a short name for this {query} not more than 2 words"

    Input: "{query}"
    Output:
    {{
       "chat_title":  
    }}
    
    
    output result in a json format
        """
    )
    return prompt


def general_search_prompt(query: str):
    prompt = PromptTemplate(
        input_variables=["query", "chat_history"],
        template="""
Previous conversation:
{chat_history}

You are a highly intelligent and knowledgeable assistant. Your goal is to provide accurate, concise, and relevant information in response to the user's query. Always maintain a professional and friendly tone. When applicable, include structured and detailed explanations, examples, or steps to help the user.

You are tasked with performing a general search based on the input provided. The response should be structured as an HTML document with the following sections:

Current query: {query}


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generate concise title for - {query}</title>

</head>
<body>
    <section>
        <p>A concise, well-structured summary of the query, with examples or steps if needed.</p>
    </section>
    <!-- Include this section only if the query asks for a process or instructions -->
    <section>
        <h2>Step-by-Step Solution</h2>
        <ol>
            <li>Step 1: Provide a clear description of the first step.</li>
            <li>Step 2: Explain the next step in detail.</li>
            <li>Step 3: Continue adding steps as necessary.</li>
        </ol>
    </section>
    <!-- Include the following only if relevant -->
    <section>
        <h2>List</h2>
        <ul>
            <li>Item 1: Provide details here</li>
            <li>Item 2: Add more information</li>
            <li>Item 3: Continue the list as necessary</li>
        </ul>
    </section>
    <section>
        <h2>Code</h2>
        <pre><code>
// Provide a code snippet related to the query, with comments explaining its functionality.
        </code></pre>
    </section>
    <section>
        <h2>Table</h2>
        <table>
            <thead>
                <tr>
                    <th>Column 1</th>
                    <th>Column 2</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Row 1 Column 1</td>
                    <td>Row 1 Column 2</td>
                </tr>
                <tr>
                    <td>Row 2 Column 1</td>
                    <td>Row 2 Column 2</td>
                </tr>
            </tbody>
        </table>
    </section>
    <!-- End optional sections -->
</body>
</html>
    """
    )
    return prompt
