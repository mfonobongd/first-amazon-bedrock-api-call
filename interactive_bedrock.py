import boto3
from botocore.exceptions import ClientError


REGION = "us-east-1"
MODEL_ID = "amazon.nova-micro-v1:0"


client = boto3.client(
    "bedrock-runtime",
    region_name=REGION
)


def ask_bedrock(prompt):
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


    response = client.converse(
        modelId=MODEL_ID,
        messages=messages,
        inferenceConfig={
            "maxTokens": 300,
            "temperature": 0.3
        }
    )


    return response




def main():
    prompt = input("Ask Amazon Bedrock a question: ")


    if not prompt.strip():
        print("Please enter a question.")
        return


    try:
        response = ask_bedrock(prompt)


        text_blocks = [
            block["text"]
            for block in response["output"]["message"]["content"]
            if "text" in block
        ]


        print("\nModel response:\n")
        print("\n".join(text_blocks))


        usage = response["usage"]


        print("\nToken usage:")
        print(f"Input: {usage['inputTokens']}")
        print(f"Output: {usage['outputTokens']}")


    except ClientError as error:
        print("Request failed:")
        print(error.response["Error"]["Message"])




if __name__ == "__main__":
    main()
