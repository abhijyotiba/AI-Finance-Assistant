# 💰 AI Finance Assistant

An interactive financial analysis tool powered by LangChain and LLM(OpenAI). Upload CSV or Excel sheets and ask natural language questions to receive structured, AI-generated financial insights.

---

## ✨ Features

- 📊 Upload financial files (CSV, XLS, XLSX)
- 💬 Ask questions like “What are my top expenses?”
- 🧠 Uses LLMs for context-aware financial reasoning
- 🗃️ Returns structured JSON responses
- ⚠️ Handles invalid queries with intelligent error messages
- 🎨 Clean, responsive user interface (HTML/CSS)

---
### Workflow Diagram
<p align="center">
  <img src="https://i.postimg.cc/RhF42cft/Mermaid-Chart-Create-complex-visual-diagrams-with-text-A-smarter-way-of-creating-diagrams-2025.png" width="700" height="400"/>
</p>


## 🧠 How It Works

1. You upload a `.csv` or `.xlsx` financial document.
2. The backend parses your file into a DataFrame.
3. You submit a natural language question.
4. A structured prompt is sent to a large language model (via API).
5. The LLM returns a JSON object containing your financial insights.
6. The JSON is displayed clearly in your browser.

---

## 📥 Input Examples

- CSV of personal transactions
- Excel sheet with budget categories
- Queries like:
  - "What are the total expenses this month?"
  - "Top 5 spending categories?"
  - "what is the highest expense in dataset?"

---

## 📤 Output Format

Returns structured, clean JSON like:

```json
{
  "top_categories": ["Food", "Travel", "Shopping"],
  "total_spent": 1520.25,
  "insights": "Food was your top expense this month."
}
```
<p align="center">
  <img src="https://i.postimg.cc/KYkLhMPd/Screenshot-2025-07-03-144819.png" width="400" height="600"/>
</p>
<p align="center">
  <img src="https://i.postimg.cc/Px1wPnFy/Screenshot-2025-07-03-144744.png" width="400" height="600"/>
</p>
