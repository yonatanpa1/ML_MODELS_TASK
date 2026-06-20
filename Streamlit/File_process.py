from typing import List, Dict

import pandas as pd

from Model import ModelPipeline
from consts_streamlit import ModelsERT


class FileProcessor:
    def __init__(self, model_path: str = ModelsERT.SECURE_BERT):
        self.model_Path = model_path
        self.pipeline = ModelPipeline()

    def _split_to_sentences(self, text: str) -> List[str]:
        if not text:
            return []
        sentences = text.split(".")
        return [s.strip() for s in sentences if s.strip()]

    def process_text(self, text: str) -> pd.DataFrame:
        sentences = self._split_to_sentences(text)
        pip = self.pipeline.get_pipeline(self.model_Path)
        results = []
        for sentence in sentences:
            pip_result = pip(sentence)
            results.extend(pip_result)

        return self._format_to_table(results)

    def _format_to_table(self, results: List[Dict[str, str]]) -> pd.DataFrame:
        columns = ["word", "entity_group", "score", "start", "end"]
        if not results:
            return pd.DataFrame(columns)

        df = pd.DataFrame(results)
        df = df.drop_duplicates()
        return df.reindex(columns=columns)


if __name__ == "__main__":
    FileProcessor().process_text(
        "The admin@338 has largely targeted organizations involved in financial , economic and trade policy , typically using publicly available RATs such as Poison Ivy , as well some non-public backdoors . The admin@338 started targeting Hong Kong media companies , probably in response to political and economic challenges in Hong Kong and China . Multiple China-based cyber threat groups have targeted international media organizations in the past . The admin@338 has targeted international media organizations in the past . "
    )
