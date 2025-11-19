from fastapi import UploadFile
import aiohttp
import re
import json

async def describe_image(file_data: bytes, file: UploadFile):
    url = "https://facee.ru/api/public/describe-image"
    
    headers = {
        "accept": "*/*",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1pc3Rlci52b2tlcjYzQGdtYWlsLmNvbSIsImlhdCI6MTc2MzQ3NDk4N30.Rg4q637BZcMM2N_449fmJXNUwapFjDOiuw8J5TtTbt0",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin"
    }
    
    data = aiohttp.FormData()
    data.add_field('file', file_data, filename=file.filename, content_type=file.content_type)
    data.add_field('filename', file.filename)
    data.add_field('describeType', 'calories-by-photo')
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=data) as response:
            result = await response.text()
            print(f"Status Code: {response.status}")
            print(f"Response: {result}")

            try:
                checkError = json.loads(result)
                if 'message' in checkError:
                    return checkError['message']
            except:
                print(result)

            return parse_text(result)
        
def parse_text(text: str):
    """Расширенная версия с дополнительными паттернами"""
    patterns = [
        # Паттерн 1: **250** или **250-350** с БЖУ
        r'\*\*(\d+)(?:-(\d+))?\*\*.*?БЖУ:\s*(\d+)\s*белков\s*/\s*(\d+)\s*жиров\s*/\s*(\d+)\s*углеводов',
        # Паттерн 2: Без звездочек, но с тем же форматом
        r'калорий.*?порции:\s*(\d+)(?:-(\d+))?;.*?БЖУ:\s*(\d+)\s*белков\s*/\s*(\d+)\s*жиров\s*/\s*(\d+)\s*углеводов',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            calories_min = int(match.group(1))
            calories_max = int(match.group(2)) if match.group(2) else calories_min
            
            return {
                'calories_min': calories_min,
                'calories_max': calories_max,
                'proteins': int(match.group(3)),
                'fats': int(match.group(4)),
                'carbs': int(match.group(5)),
                'origin_text': text
            }
    
    return None