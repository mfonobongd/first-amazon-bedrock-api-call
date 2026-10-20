
import boto3
from botocore.exceptions import ClientError

# AWS configuration
REGION = "us-east-1"
MODEL_ID = "amazon.nova-micro-v1:0"

# Create Amazon Bedrock Runtime client
client = boto3.client(
    service_name="bedrock-runtime",
    region_name=REGION
)

# User prompt
prompt = input("Ask Amazon Bedrock a question: ").strip()


if not prompt:
    print("Please enter a question.")
    raise SystemExit(1)

# Structure the user message
messages = [
    {
        "role": "user",
        "content": [
            {
                "text": prompt
            }
        ]
    }
]

try:
    # Send request to Amazon Bedrock
    response = client.converse(
        modelId=MODEL_ID,

        # System prompt
        system=[
            {
                "text": (
                    "You are an experienced Developer Relations "
                    "professional and community strategist. "
                    "Provide practical, beginner-friendly advice "
                    "on building developer communities. "
                    "Use clear language, realistic examples, "
                    "and actionable recommendations. "
                    "Keep responses under 200 words."
                )
            }
        ],

        # User message
        messages=messages,

        # Inference configuration
        inferenceConfig={
            "maxTokens": 500,
            "temperature": 0.3
        }
    )

    # Extract generated text
    generated_text = (
        response["output"]["message"]["content"][0]["text"]
    )

    # Display model response
    print("\nModel response:\n")
    print(generated_text)

    # Extract request metrics
    usage = response["usage"]
    metrics = response["metrics"]

    print("\n--- Request Metrics ---")
    print(f"Input tokens: {usage['inputTokens']}")
    print(f"Output tokens: {usage['outputTokens']}")
    print(f"Total tokens: {usage['totalTokens']}")
    print(f"Latency: {metrics['latencyMs']} ms")
    print(f"Stop reason: {response['stopReason']}")

except ClientError as error:
    print("\nAmazon Bedrock returned an error:")
    print(error.response["Error"]["Message"])
