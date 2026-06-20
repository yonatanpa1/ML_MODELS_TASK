from Benchmarking.parser import parse_dataset
from Benchmarking.run_model import run_model
from Benchmarking.utils.Measurement import precision_recall, latency
from Benchmarking.utils.map_values import normalize
from consts import Models, MAP_DNRTI_TO_CYNER, MAP_SECUREBERT_TO_CYNER


def evaluate(path: str, model=Models.SECURE_BERT, mapping_type=MAP_SECUREBERT_TO_CYNER):
    sentences = parse_dataset(path)
    correct_set = set()
    predicted_set = set()
    final_time = 0.0

    for idx, s in enumerate(sentences):
        text, correct = s["text"], s["entities"]
        correct = normalize(correct, MAP_DNRTI_TO_CYNER, "label")
        predicted, running_time = run_model(model, text)
        final_time += running_time
        predicted = normalize(predicted, mapping_type, "entity_group")
        correct_set |= create_evaluate_format_set(idx, correct)
        predicted_set |= create_evaluate_format_set(idx, predicted)

    return precision_recall(correct_set, predicted_set), latency(
        final_time, len(sentences)
    )


def create_evaluate_format_set(idx, data):
    return {(idx, e["start"], e["end"], e["entity_group"]) for e in data}


if __name__ == "__main__":
    print(evaluate(r"C:\ML_proj\DNRTI-A\DNRTI\test.txt"))
