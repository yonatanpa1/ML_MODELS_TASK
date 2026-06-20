import time

from transformers import pipeline
from consts import Models

_PIPELINES = {}


def get_pipeline(model: str):
    if model not in _PIPELINES:
        _PIPELINES[model] = pipeline(
            "token-classification", model=model, aggregation_strategy="max", device=0
        )
    return _PIPELINES[model]


def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        return result, time.time() - start_time

    return wrapper


@execution_time
def run_model(model: str, text: str):
    return get_pipeline(model)(text)


if __name__ == "__main__":
    text1 = "The admin@338 has largely targeted organizations involved in financial , economic and trade policy , typically using publicly available RATs such as Poison Ivy , as well some non-public backdoors . The admin@338 started targeting Hong Kong media companies , probably in response to political and economic challenges in Hong Kong and China . Multiple China-based cyber threat groups have targeted international media organizations in the past . The admin@338 has targeted international media organizations in the past . "
    print(run_model(Models.CYNER, text1))
    # print(run_model(Models.SecureBERT,text1))
