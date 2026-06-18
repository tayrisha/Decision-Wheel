"""Pure scoring logic — no FastAPI imports."""


def score(
    options: list[str],
    factors: list[str],
    weights: list[int],
    scores: list[list[int]],
) -> dict:
    """
    Compute normalized weighted scores per option.

    Implemented in the next stage.
    """
    raise NotImplementedError("Scoring logic not implemented yet")
