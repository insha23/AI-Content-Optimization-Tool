import streamlit as st
import nltk
import textstat
import matplotlib.pyplot as plt
from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from wordcloud import WordCloud

# Download NLTK data
nltk.data.path.append("/home/appuser/nltk_data")


def simplify_text(text):
    replacements = {
        "optimization": "better",
        "optimize": "make better",
        "generative": "smart",
        "engine": "search",
        "content": "text",
        "structure": "format",
        "visibility": "reach",
        "information": "data",
        "improve": "make better",
        "improves": "makes better",
        "increase": "raise",
        "increases": "raises",
        "understand": "know",
        "understanding": "knowing",
        "benefits": "good points",
        "factors": "points",
        "important": "key",
        "readability": "easy reading",
        "keyword": "word",
        "keywords": "words",
    }

    simplified = text.lower()

    for word, simple in replacements.items():
        simplified = simplified.replace(word, simple)

    return simplified


st.title("AI Content Optimization Tool (GEO)")
st.write(
    "Analyze content for readability, keyword optimization, and structure "
    "to improve performance in AI-driven search engines (GEO)."
)

text = st.text_area("Enter your content here:")

if st.button("Convert to Easy Text"):
    if text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        easy_text = simplify_text(text)
        st.subheader("Simplified Text")
        st.text_area("Easy Version:", easy_text, height=150)

target_keyword = st.text_input(
    "Enter target keyword (for optimization analysis):",
    "optimization"
)

if st.button("Analyze Content"):

    if text.strip() == "":
        st.warning("Please enter some content to analyze.")
    else:
        # Text preprocessing
        sentences = sent_tokenize(text)
        words = word_tokenize(text.lower())

        stop_words = set(stopwords.words("english"))
        filtered_words = [
            word for word in words
            if word.isalnum() and word not in stop_words
        ]

        # Readability metrics
        readability_score = textstat.flesch_reading_ease(text)
        grade_level = textstat.flesch_kincaid_grade(text)

        # Keyword analysis
        keyword_count = sum(1 for word in words if word == target_keyword.lower())

        # Content metrics
        num_sentences = len(sentences)
        num_words = len(filtered_words)
        avg_sentence_length = num_words / num_sentences if num_sentences > 0 else 0

        # Heading detection
        lines = text.split("\n")
        possible_headings = [
            line.strip()
            for line in lines
            if len(line.split()) < 8 and line.strip().isupper()
        ]
        heading_count = len(possible_headings)

        # Lexical diversity
        unique_words = len(set(filtered_words))
        lexical_diversity = unique_words / num_words if num_words > 0 else 0

        # Top repeated words
        word_freq = Counter(filtered_words)
        top_words = word_freq.most_common(10)

        # Suggestions
        suggestions = []

        if readability_score < 60:
            suggestions.append("Improve readability by using shorter and simpler sentences.")
        if grade_level > 10:
            suggestions.append("Simplify vocabulary and sentence structure.")
        if keyword_count < 2:
            suggestions.append("Increase keyword usage naturally.")
        if keyword_count > 8:
            suggestions.append("Reduce keyword repetition.")
        if avg_sentence_length > 20:
            suggestions.append("Reduce sentence length.")
        if num_words < 150:
            suggestions.append("Content is too short.")
        if heading_count < 2:
            suggestions.append("Add more headings.")
        if lexical_diversity < 0.5:
            suggestions.append("Use more varied vocabulary.")

        # Readability score label
        score = round(readability_score, 2)
        if score < 0:
            display_score = f"{score} (Very Hard)"
        elif score < 50:
            display_score = f"{score} (Hard)"
        elif score < 70:
            display_score = f"{score} (Medium)"
        else:
            display_score = f"{score} (Easy)"

        st.markdown("---")
        st.subheader("📊 Results")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Readability Score", display_score)
            st.metric("Grade Level", round(grade_level, 2))

        with col2:
            st.metric("Keyword Count", keyword_count)
            st.metric("Total Words", num_words)
            st.metric("Headings Detected", heading_count)

        # Readability interpretation
        if readability_score < 0:
            st.info("Interpretation: Very difficult to read (academic level).")
        elif readability_score < 50:
            st.info("Interpretation: Difficult to read.")
        elif readability_score < 70:
            st.info("Interpretation: Standard readability.")
        else:
            st.info("Interpretation: Easy to read.")

        st.subheader("💡 Optimization Suggestions")
        for s in suggestions:
            st.markdown(f"- {s}")

        if possible_headings:
            st.subheader("Detected Headings")
            for h in possible_headings:
                st.write("•", h)

        st.subheader("Top Keywords")
        for word, count in top_words:
            st.write(f"{word} : {count}")

        st.markdown("---")
        st.subheader("Word Cloud")
        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color="white"
        ).generate(" ".join(filtered_words))

        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)

        report = f"""
Readability Score: {display_score}
Grade Level: {round(grade_level, 2)}
Keyword Count: {keyword_count}
Total Words: {num_words}
Headings Detected: {heading_count}
Lexical Diversity: {round(lexical_diversity, 2)}

Top Keywords:
""" + "\n".join(f"- {word}: {count}" for word, count in top_words) + """

Suggestions:
""" + "\n".join(f"- {s}" for s in suggestions)

        st.download_button(
            "Download Report",
            report,
            file_name="analysis_report.txt"
        )