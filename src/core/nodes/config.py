from typing import Optional
from langchain_core.runnables import RunnableConfig
from src.core.state import SessionState
import time
async def hydrate_from_config(state: SessionState, config: Optional[RunnableConfig] = None) -> SessionState:
    cfg = (config or {}).get("configurable", {})

    # copy from config into state
    state.customer_id = cfg.get("customer_id") or state.customer_id
    state.opportunity_id = cfg.get("opportunity_id") or state.opportunity_id
    state.whisper_model_size = cfg.get("whisper_model_size", state.whisper_model_size)
    state.whisper_language = cfg.get("whisper_language", state.whisper_language)
    state.fail_fast = bool(cfg.get("fail_fast", state.fail_fast))

    state.last_updated_epoch = time.time()
    return state
