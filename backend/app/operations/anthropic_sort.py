import anthropic
import os
import json
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

# message = client.messages.create(
#     model="claude-sonnet-4-20250514",
#     max_tokens=1000,
#     messages=[
#         {
#             "role": "user", 
#             "content": "What should I search for to find the latest developments in renewable energy?"
#         }
#     ]
# )

# print(message.content)

def prompt_deletion_candidates(filenames):
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    
    prompt = f"""Look at these filenames and tell me which ones are safe to delete:

{json.dumps(filenames)}

Safe to delete: temporary files, cache files, log files, backup files, files with extensions like .tmp, .log, .cache, .bak, .zip

Respond with ONLY this JSON format:
{{"safe_to_delete": ["filename1", "filename2"]}}

Nothing else. Just the JSON."""

    try:
        response = client.messages.create(
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
        
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []
    


# files = [
#     "temp_file_001.tmp",
#     "cache_data.cache",
#     "system_backup.bak",
#     "error_report.log",
#     "browser_temp.tmp"
#     "FAMILY_PICS.jpg"
# ]

# result = get_deletion_candidates(files)
# print(result)