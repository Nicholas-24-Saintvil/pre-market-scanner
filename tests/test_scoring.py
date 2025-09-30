from src.news import score_headline

def test_scoring_detects_keywords():
    title = "Company soars after beats expectations and raises guidance"
    assert score_headline(title) >= 10
