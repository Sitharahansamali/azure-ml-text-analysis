# ML Text Analysis

A Python application that uses Azure AI Language services to analyze customer reviews for sentiment and language detection.

## Overview

This project analyzes text reviews using Azure Cognitive Services Text Analytics API. It processes multiple review files, detects the language of each review, and performs sentiment analysis to determine whether reviews are positive, neutral, or negative.

## Features

- **Language Detection**: Automatically detects the language of each review
- **Sentiment Analysis**: Analyzes the sentiment (positive, neutral, negative) with confidence scores
- **Batch Processing**: Efficiently processes reviews in batches to optimize API usage
- **Multiple Review Files**: Supports loading and analyzing reviews from multiple text files

## Project Structure

```
ml-text-analysis/
├── src/
│   └── analyse-text/
│       ├── text-anlysis.py      # Main application script
│       └── reviews/              # Sample review text files
│           ├── reviews1.txt
│           ├── reviews2.txt
│           ├── reviews3.txt
│           ├── reviews4.txt
│           └── reviews5.txt
├── pyproject.toml               # Project dependencies
└── README.md                    # This file
```

## Prerequisites

- Python 3.11 or higher
- Azure subscription with Azure AI Language service
- Azure AI Language service endpoint and key

## Setup

### 1. Clone or download this repository

### 2. Install dependencies

```bash
uv pip install -e .
```

Or install dependencies directly:

```bash
uv pip install azure-ai-textanalytics python-dotenv
```

### 3. Configure Azure credentials

Create a `.env` file in the root directory with your Azure AI Language service credentials:

```env
AI_SERVICE_ENDPOINT=your-azure-endpoint-here
AI_SERVICE_KEY=your-azure-key-here
```

**How to get Azure credentials:**
1. Go to [Azure Portal](https://portal.azure.com)
2. Create or navigate to your Azure AI Language service
3. In the "Keys and Endpoint" section, copy your endpoint and one of the keys
4. Paste them into the `.env` file

## Usage

Navigate to the script directory and run:

```bash
cd src/analyse-text
python text-anlysis.py
```

The application will:
1. Load all reviews from the `reviews/` folder
2. Process them in batches of 10
3. Display detected language and sentiment analysis for each review

### Sample Output

```
Review: The hotel room was clean and the staff were very friendly.
Detected Language: English
Language Code: en
Sentiment: positive
Positive: 0.99
Neutral: 0.01
Negative: 0.00

Review: The room was small and the air conditioning did not work properly.
Detected Language: English
Language Code: en
Sentiment: negative
Positive: 0.01
Neutral: 0.02
Negative: 0.97
```

## Adding Your Own Reviews

To analyze your own reviews:

1. Create text files in the `src/analyse-text/reviews/` directory
2. Add one review per line in each file
3. Run the script as shown above

## Dependencies

- **azure-ai-textanalytics** (>=5.4.0): Azure Cognitive Services Text Analytics client library
- **python-dotenv** (>=1.2.2): Load environment variables from .env file

## API Limits

The script processes reviews in batches of 10 to comply with Azure Text Analytics API limits. Adjust the batch size in the `analyze_reviews()` function if needed.

## Troubleshooting

### Authentication Error
- Verify your `AI_SERVICE_ENDPOINT` and `AI_SERVICE_KEY` are correct in the `.env` file
- Ensure your Azure AI Language service is active

### Module Not Found
- Make sure all dependencies are installed: `uv pip install -e .`
- Verify you're using Python 3.11 or higher

### No Reviews Found
- Check that review files exist in `src/analyse-text/reviews/`
- Ensure review files contain text (one review per line)

## License

This project is for educational purposes as part of Azure ML certification practical exercises.

## Contributing

Feel free to submit issues or pull requests to improve this project.
