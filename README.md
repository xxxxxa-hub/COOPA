## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/cyrilli/COOPA.git
cd COOPA
```

### 2. Install Dependencies
Please refer to the installation instructions in readme file of the app you want to use.

### 3. Configure Environment Variables

Create a `.env` file in the root of `COOPA` and add your API keys:

```
OPENAI_API_KEY=your_openai_api_key
# Optionally, add other keys as needed for the app you want to use
```
### 4. Run Operations Research Experiments
```bash
python -m apps.operations_research.run_exp_with_kb --dataset nlp4lp --model_id gpt-4.1 --start_index 1 --is_curation
```

**Parameters:**
- `--dataset`: Choose from `nlp4lp`, `nlp4opt`, `industryor`, `complexlp`, `BWOR`
- `--model_id`: Choose from `gpt-4.1`, `o4-mini`
- `--start_index`: Starting index of question in the dataset (integer)
- `--is_curation`: Add this flag for curation mode, omit for retrieval mode

---