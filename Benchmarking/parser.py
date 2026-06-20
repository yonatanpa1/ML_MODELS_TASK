from typing import NamedTuple


class WordPosition(NamedTuple):
    text: str
    tag: str
    start: int
    end: int


def sentences_from_text_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return connect_sentences(f.readlines())


def is_end_sentences(line, words) -> bool:
    return not line.strip() and words


def connect_sentences(lines) -> list[tuple[list[str], list[str]]]:
    sentences = []
    words, tags = [], []

    for line in lines:
        if is_end_sentences(line, words):
            sentences.append((words, tags))
            words, tags = [], []
            continue
        parts = line.split()
        if len(parts) >= 2:
            words.append(parts[0])
            tags.append(parts[-1])

    if words:
        sentences.append((words, tags))

    return sentences


def create_chunks(words: list[str], tags: list[str]) -> list[WordPosition]:
    chunks, position = [], 0
    for word, tag in zip(words, tags):
        start = position
        end = position + len(word)
        chunks.append(WordPosition(word, tag, start, end))
        position = end + 1
    return chunks


def should_close_entity(tag: str, current_label: str | None) -> bool:
    is_begin = tag.startswith("B-")
    is_inside = tag.startswith("I-") and current_label and tag[2:] == current_label
    return is_begin or not is_inside


def extract_entities(words: list[str], tags: list[str]) -> list[dict]:
    chunks = create_chunks(words, tags)
    entities, start_char, current_label, last_word_end = [], None, None, 0

    for chunk in chunks:
        if should_close_entity(chunk.tag, current_label) and start_char is not None:
            entities.append(
                {"start": start_char, "end": last_word_end, "label": current_label}
            )
            start_char, current_label = None, None
        if chunk.tag.startswith("B-"):
            start_char, current_label = chunk.start, chunk.tag[2:]
        elif not chunk.tag.startswith("I-"):
            start_char, current_label = None, None
        last_word_end = chunk.end

    if start_char is not None:
        entities.append(
            {"start": start_char, "end": last_word_end, "label": current_label}
        )

    return entities


def parse_dataset(path: str) -> list[dict]:
    return [
        {"text": " ".join(words), "entities": extract_entities(words, tags)}
        for words, tags in sentences_from_text_file(path)
    ]


if __name__ == "__main__":
    input_file = r"C:\ML_proj\DNRTI-A\DNRTI\train.txt"
    dataset = parse_dataset(input_file)
