import matplotlib.pyplot as plt


# Dashboard Color Palette
MATCHED_COLOR = "#10B981"   # Emerald Green
MISSING_COLOR = "#F43F5E"   # Rose Red
CENTER_TEXT_COLOR = "#1E293B"
TITLE_COLOR = "#0F172A"


def plot_skill_match(matched: int, missing: int):
    """
    Creates a professional doughnut chart showing
    matched vs missing skills.

    Parameters
    ----------
    matched : int
        Number of matched skills.

    missing : int
        Number of missing skills.

    Returns
    -------
    matplotlib.figure.Figure
        Doughnut chart figure.
    """

    total = matched + missing

    # Prevent division by zero
    if total == 0:
        matched = 1
        missing = 0
        total = 1

    match_percentage = round((matched / total) * 100)

    fig, ax = plt.subplots(
        figsize=(4.2, 4.2),
        dpi=150,
        facecolor="white"
    )

    ax.pie(
        [matched, missing],
        colors=[MATCHED_COLOR, MISSING_COLOR],
        startangle=90,
        counterclock=False,
        wedgeprops={
            "width": 0.34,
            "edgecolor": "white",
            "linewidth": 3,
        },
    )

    # Center Score
    ax.text(
        0,
        0.08,
        f"{match_percentage}%",
        ha="center",
        va="center",
        fontsize=24,
        fontweight="bold",
        color=CENTER_TEXT_COLOR,
    )

    ax.text(
        0,
        -0.18,
        "Skill Match",
        ha="center",
        va="center",
        fontsize=11,
        color="#64748B",
    )

    ax.set_title(
        "Skill Match Overview",
        fontsize=14,
        fontweight="bold",
        color=TITLE_COLOR,
        pad=18,
    )

    ax.legend(
        [
            f"Matched ({matched})",
            f"Missing ({missing})",
        ],
        loc="lower center",
        bbox_to_anchor=(0.5, -0.12),
        ncol=2,
        frameon=False,
        fontsize=10,
    )

    ax.set_aspect("equal")

    plt.tight_layout()

    return fig