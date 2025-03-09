from typing import Dict, Optional

OPENROUTER_API_BASE = "https://openrouter.ai/api/v1"
OPENROUTER_MODELS = {
    "claude-3-opus": {
        "name": "anthropic/claude-3-opus-20240229",
        "context_length": 200000,
    },
    "claude-3-sonnet": {
        "name": "anthropic/claude-3-sonnet-20240229",
        "context_length": 200000,
    },
    "mixtral": {
        "name": "mistralai/mixtral-8x7b-instruct",
        "context_length": 32000,
    },
    "mistral": {
        "name": "mistralai/mistral-7b-instruct",
        "context_length": 32000,
    }
}

def get_model_config(model_name: str) -> Optional[Dict]:
    return OPENROUTER_MODELS.get(model_name)