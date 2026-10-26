from pytest import raises
from block_44.score_counter import ScoreCounter

def test_score_counter():
    score = ScoreCounter(
        points=15
    )
    assert score.points == 15

def test_score_counter_negative():
    with raises(ValueError):
        score = ScoreCounter(
            points=-15
        )

def test_score_counter_zero():
    score = ScoreCounter(
        points=0
    )
    assert score.points == 0

def test_score_counter_sum():
    score_counter = ScoreCounter(
        points=52
    )
    score_counter.add_points(52)
    
    assert score_counter.points == 104

def test_score_counter_sum_negative():
    score_counter = ScoreCounter(
        points=52
    )
    with raises(ValueError):
        score_counter.add_points(-52)

def test_score_counter_sum_zero():
    score_counter = ScoreCounter(
        points=52
    )
    with raises(ValueError):
        score_counter.add_points(0)

def test_score_counter_extract():
    score_counter = ScoreCounter(
        points=15
    )
    score_counter.extract_points(15)
    assert score_counter.points == 0

def test_count_point(capsys):
    show_point = ScoreCounter(
        15
    )
    show_point.show_point(show_point.points)
    show_points = capsys.readouterr().out
    assert show_points.strip() == "your points are: 15"

def test_count_spent(capsys):
    show_point = ScoreCounter(
        1500
    )
    show_point.extract_points(450)

    show_point.show_points_spent(show_point)
    show_points = capsys.readouterr().out

    assert show_points.strip() == "your spent points are: 450"