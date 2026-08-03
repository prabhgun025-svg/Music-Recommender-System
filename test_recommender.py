from src.recommender import Song, UserProfile, Recommender

def make_small_recommender() -> Recommender:
    songs = [
        Song(
            id=1,
            title="Test Pop Track",
            artist="Test Artist",
            genre="pop",
            mood="happy",
            energy=0.8,
            tempo_bpm=120,
            valence=0.9,
            danceability=0.8,
            acousticness=0.2,
        ),
        Song(
            id=2,
            title="Chill Lofi Loop",
            artist="Test Artist",
            genre="lofi",
            mood="chill",
            energy=0.4,
            tempo_bpm=80,
            valence=0.6,
            danceability=0.5,
            acousticness=0.9,
        ),
    ]
    return Recommender(songs)


def test_recommend_returns_songs_sorted_by_score():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    results = rec.recommend(user, k=2)

    assert len(results) == 2
    # Starter expectation: the pop, happy, high energy song should score higher
    assert results[0].genre == "pop"
    assert results[0].mood == "happy"


def test_explain_recommendation_returns_non_empty_string():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    song = rec.songs[0]

    explanation = rec.explain_recommendation(user, song)
    assert isinstance(explanation, str)
    assert explanation.strip() != ""


def test_energy_weight_is_doubled_in_scoring():
    user = UserProfile(
        favorite_genre="jazz",
        favorite_mood="sad",
        target_energy=0.75,
        likes_acoustic=False,
    )
    song = Song(
        id=3,
        title="Target Energy",
        artist="Test Artist",
        genre="electronic",
        mood="neutral",
        energy=0.75,
        tempo_bpm=100,
        valence=0.5,
        danceability=0.5,
        acousticness=0.1,
    )
    rec = Recommender([song])
    score, reasons = rec._score_song(user, song)

    assert any("Energy similarity" in reason for reason in reasons)
    assert score >= 2.0
    assert any("+2.00" in reason for reason in reasons)


def test_genre_weight_is_halved_in_scoring():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="sad",
        target_energy=0.0,
        likes_acoustic=False,
    )
    song = Song(
        id=4,
        title="Pop Match",
        artist="Test Artist",
        genre="pop",
        mood="neutral",
        energy=0.0,
        tempo_bpm=50,
        valence=0.0,
        danceability=0.0,
        acousticness=0.9,
    )
    rec = Recommender([song])
    score, reasons = rec._score_song(user, song)

    assert any("Genre exact match" in reason for reason in reasons)
    assert abs(score - 1.0) < 1e-3
