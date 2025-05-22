def classify(features: list[float]) -> str:
    # Dummy rule-based model
    if sum(features) > 10:
        return "class A"
    else:
        return "class B"
