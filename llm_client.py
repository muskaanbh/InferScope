import httpx

# accepts a prompt and llm server's address
async def generate_text(prompt, base_url):

    async with httpx.AsyncClient() as client:
        response = await client.post(f"{base_url}/v1/completions", json={"prompt": prompt, "model": "Qwen/Qwen2.5-3B-Instruct", "max_tokens": 100})
        response.raise_for_status()
        # preventing our application from treating that failed response as a successful result
        return response.json()

