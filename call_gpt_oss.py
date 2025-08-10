"""Simple example script to query a local GPT-OSS 20B model.

The script assumes an OpenAI-compatible API exposed at ``http://localhost:8000``.
Update ``base_url`` and ``api_key`` as needed for your environment.
"""

from openai import OpenAI


def main() -> None:
    """Send a test prompt to the local model and print the reply."""
    client = OpenAI(
        base_url="http://localhost:8000/v1",
        api_key="not-needed",  # Replace if your server requires authentication
    )

    response = client.chat.completions.create(
        model="gpt-oss:20B",
        messages=[{"role": "user", "content": "Hello from Python!"}],
    )

    # ``message`` returned as a dictionary to maintain compatibility with
    # older versions of the OpenAI client library.
    print(response.choices[0].message["content"])


if __name__ == "__main__":
    main()
