def precision_recall(correct, model_prediction):
    model_prediction = set(model_prediction)
    correct = set(correct)
    tp = len(correct & model_prediction)
    fp = len(model_prediction - correct)
    fn = len(correct - model_prediction)
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0

    print("TP:" + str(tp))
    print("FP:" + str(fp))
    print("FN:" + str(fn))
    print("Precision:" + str(precision))
    print("Recall:" + str(recall))
    return precision, recall


def latency(time, length):
    return time / length if length >= 0 else 0
