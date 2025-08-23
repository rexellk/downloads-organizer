"""Anthropic API integration for file deletion recommendations."""
import json
import os
from typing import List

import anthropic
from dotenv import load_dotenv

load_dotenv()

anthropic_client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)


def prompt_deletion_candidates(filenames: List[str]) -> List[str]:
    """
    Use Anthropic API to suggest which files are safe to delete.
    
    Args:
        filenames: List of filenames to analyze
        
    Returns:
        List of filenames that are safe to delete
    """
    local_client = anthropic.Anthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY")
    )

    prompt = f"""Look at these filenames and tell me which ones are safe to delete:

{json.dumps(filenames)}

Safe to delete: temporary files, cache files, log files, backup files, files with extensions like .tmp, .log, .cache, .bak, .zip

Respond with ONLY this JSON format:
{{"safe_to_delete": ["filename1", "filename2"]}}

Nothing else. Just the JSON."""

    try:
        response = local_client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}]
        )

        # Extract text from the first text block in content
        text_content = None
        for block in response.content:
            if block.type == "text":
                text_content = block.text
                break

        if not text_content:
            print("Error: No text content found in response")
            return []

        result = json.loads(text_content.strip())
        return result["safe_to_delete"]

    except json.JSONDecodeError as json_error:
        print(f"Error parsing JSON: {json_error}")
        return []
    except anthropic.APIError as api_error:
        print(f"Anthropic API error: {api_error}")
        return []
    except Exception as general_error:
        print(f"Error: {general_error}")
        return []