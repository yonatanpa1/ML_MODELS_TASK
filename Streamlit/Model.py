from transformers import pipeline


class ModelPipeline:
    def __init__(self):
        self._model = {}

    def get_pipeline(self, path: str):
        if path not in self._model:
            self._model[path] = pipeline(
                "token-classification", model=path, aggregation_strategy="max", device=0
            )
        return self._model[path]
