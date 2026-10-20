# My First Amazon Bedrock API Call with Python

A beginner-friendly Python project demonstrating how to invoke Amazon Nova Micro through Amazon Bedrock using Boto3 and the Converse API.

# Read the full Article here

- [How to Make Your First Amazon Bedrock API Call with Python](https://docs.aws.amazon.com)

## What This Project Does

- Sends prompts to Amazon Bedrock
- Uses system prompts to guide model responses
- Generates responses using Amazon Nova Micro
- Displays token usage and inference latency
- Handles common AWS API errors

## Technologies Used

- Python 3
- Amazon Bedrock
- Amazon Nova Micro
- Boto3
- Amazon Bedrock Converse API

## Getting Started

### Prerequisites

- Python 3.10 or later
- An AWS account with access to Amazon Bedrock
- A valid Amazon Bedrock API key

### Installation

Clone or download this repository, open the project directory in Terminal, and create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Configure your Bedrock API key:

```bash
IFS= read -r -s "AWS_BEARER_TOKEN_BEDROCK?Paste your Bedrock API key: "
export AWS_BEARER_TOKEN_BEDROCK
```

Run the application:

```bash
python3 first_bedrock_call.py
```

## AWS Configuration

- **Region:** `us-east-1`
- **Model:** `amazon.nova-micro-v1:0`
- **API:** Amazon Bedrock Converse API

## Security

Never commit AWS API keys or other credentials to this repository. For production applications, use appropriate IAM roles or temporary credentials.

## Documentation

- [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
- [Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference.html)
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
