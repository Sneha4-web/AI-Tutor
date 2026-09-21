import pandas as pd


def load_progress():
    """
    Load quiz progress from progress.csv.
    """

    try:
        data = pd.read_csv("data/progress.csv")
        return data

    except FileNotFoundError:
        return pd.DataFrame(
            columns=[
                "student_id",
                "subject",
                "topic",
                "quiz_score",
                "attempts",
                "date"
            ]
        )


def get_total_quizzes(progress):
    """
    Return the total number of quizzes taken.
    """

    return len(progress)


def get_average_score(progress):
    """
    Calculate the student's average quiz score.
    """

    if len(progress) == 0:
        return 0

    return progress["quiz_score"].mean()


def get_best_score(progress):
    """
    Return the student's highest quiz score.
    """

    if len(progress) == 0:
        return 0

    return progress["quiz_score"].max()


def get_subject_progress(progress):
    """
    Calculate average score for each subject.
    """

    if len(progress) == 0:
        return {}

    subject_scores = progress.groupby("subject")["quiz_score"].mean()

    return subject_scores.to_dict()


def get_weak_topics(progress):
    """
    Find topics where the student's average score is below 60%.
    """

    if len(progress) == 0:
        return []

    topic_scores = progress.groupby("topic")["quiz_score"].mean()

    weak_topics = topic_scores[topic_scores < 60]

    return weak_topics.to_dict()


def get_strong_topics(progress):
    """
    Find topics where the student's average score is 80% or higher.
    """

    if len(progress) == 0:
        return []

    topic_scores = progress.groupby("topic")["quiz_score"].mean()

    strong_topics = topic_scores[topic_scores >= 80]

    return strong_topics.to_dict()


def get_progress_summary(progress):
    """
    Return all important quiz statistics together.
    """

    return {
        "total_quizzes": get_total_quizzes(progress),
        "average_score": get_average_score(progress),
        "best_score": get_best_score(progress),
        "subject_progress": get_subject_progress(progress),
        "weak_topics": get_weak_topics(progress),
        "strong_topics": get_strong_topics(progress)
    }