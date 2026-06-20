def normalize(entities, mapping, key):
    normalized = []
    if mapping:
        for e in entities:
            map_label = mapping.get(e[key])
            if map_label:
                normalized.append(
                    {"start": e["start"], "end": e["end"], "entity_group": map_label}
                )

    return normalized
