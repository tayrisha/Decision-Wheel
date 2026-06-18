import pytest
from app.core.scoring import score


def test_score_raises_not_implemented() -> None:
    with pytest.raises(NotImplementedError, match="not implemented yet"):
        score(
            options=["Apply now", "Wait"],
            factors=["Salary"],
            weights=[1],
            scores=[[5], [3]],
        )
