import pandas as pd
from io import BytesIO
import os
import re
import json
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from src.prompt import SYSTEM_PROMPT  # Import the prompt


load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if OPENROUTER_API_KEY is None:
    raise ValueError("❌ API_KEY is not set in the environment!")

print("🔑 Loaded API Key")

llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",                           # Replace with Base URL of the Provider
    api_key=OPENROUTER_API_KEY,
    model="mistralai/mistral-small-3.2-24b-instruct"                   #Select Model with better accuracy 
)


def parse_file(filename: str, contents: bytes) -> pd.DataFrame:
    if filename.endswith(".csv"):
        return pd.read_csv(BytesIO(contents))
    elif filename.endswith(".xls") or filename.endswith(".xlsx"):
        return pd.read_excel(BytesIO(contents))
    else:
        raise ValueError("Unsupported file format")


def extract_json_string(text: str) -> dict:
    """Extract JSON object from LLM response safely."""
    try:
        match = re.search(r'{[\s\S]+}', text.strip())
        if match:
            return json.loads(match.group())
        return {"error": "❌ LLM response did not contain valid JSON."}
    except json.JSONDecodeError:
        return {"error": "❌ Failed to parse JSON from LLM response."}




def query_financial_llm(df: pd.DataFrame, prompt: str) -> dict:
    try:
        full_data = df.to_dict(orient="records")

        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=f"Query: {prompt}\n\nData:\n{full_data}")
        ]

        response = llm.invoke(messages)
        return extract_json_string(response.content)

    except Exception as e:
        return {"error": f"❌ Error from LLM: {str(e)}"}


