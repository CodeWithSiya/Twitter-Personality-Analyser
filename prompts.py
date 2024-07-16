PERSONALITY_ANALYSIS_PROMPT = r"""
Based on the provided data from a user's tweets, generate a comprehensive personality analysis report. The report should be approximately 100 words long and divided into the following sections:

1. Overall Sentiment Analysis:
   Interpret the sentiment score and discuss its implications for the user's general outlook and emotional expression on social media.

2. Key Interests and Themes:
   Analyze the entities mentioned in the tweets to identify primary topics of interest, frequent subjects of discussion, and potential areas of expertise or passion.

3. Communication Style:
   Examine the syntax data to draw conclusions about the user's communication style, including complexity of language, preferred sentence structures, and any unique linguistic patterns.

4. Engagement and Popularity:
   Analyze the retweet and favorite counts to gauge the user's level of engagement and popularity. Discuss any patterns or notable tweets.

5. Posting Habits:
   Examine the tweet creation times to identify any patterns in the user's posting schedule or frequency.

6. Social Media Behavior:
   Based on the overall analysis, infer patterns in the user's social media behavior, such as types of content shared, level of engagement with others, and potential motivations for tweeting.

7. Personality Traits:
   Synthesize the above information to hypothesize about key personality traits, such as extroversion/introversion, openness to experience, conscientiousness, agreeableness, and neuroticism.

8. Conclusion:
   Summarize the main points of the analysis and provide a concise overall impression of the user's online persona.

The report should maintain a professional and analytical tone while providing insightful and nuanced observations. Use specific examples or patterns from the data where possible to support your analysis.

Input Data:
{analysis_data}

Please generate the report based on this input data and the structure outlined above.
"""