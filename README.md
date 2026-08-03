## ReadME File -> Final Project 

The original project is the Music Recommender Simulation from Module 3. The original goal of this project was to finetune recommendations using AI and recommend the user of this system songs based on their emotions, preferred genre, and general mood. 

## Title & Summary 
The title of this system is a Music Recommender Reliability Studio. This project builds a recommending system that uses a workflow to rank songs based on user preferences, such as mood, genre, emotions, or energy. Recommendation systems need to be undersatanble and cater to the user's current moods to give proper recommendations. for this project, I added a reliability  system to test how well the AI powered recommendation system preforms.  

## Architecture Overview 
The system starts with a user profile input which would be normalized and check the values. The profile will move into the planning phase where the system decides how to apply genre, mood and energy matching. After that, the recommender system will score the song catalog and shows the top-ranked songs based on the preference. The AI reliability system would evaluate the recommendations for confidence and case issues to mantain that the results are sensible and consistent 

## Setup Instructions 
1. Open in terminal in the project folder 
2. Install the requirements.txt 
3. for the streamlit: PYTHONPATH=. streamlit run src/streamlit_app.py in terminal 


## Sample Interactions 
a sample interaction would be: 
Round 1: 
Input: I put my favorite genre is pop and my favorite mood is happy
My target energy is 0.8. I choose not to add acoustic tracks 
Output: After running the workflow -> 
Plan
{
"genre_strategy":"exact-match-first"
"mood_strategy":"mood-match-second"
"energy_strategy":"gaussian-target-proximity"
}
Reliability summary: 
Confidence: 0.2140
Guardrails:
1. Genre and mood are categorical guardrails; numerical features are similarity-based.
2. Unrecognized genres fall back to the generic distant style and receive no genre bonus.
3. Low-confidence recommendation: the top result is too close to the runner-up.

Recommended songs
Mad Love — Mabel
Score: 7.3739

Reasons:

Genre exact match: +1 pts
Mood match: +1 pts
Energy similarity (0.79 vs 0.75): +1.93 pts
Tempo similarity (120 vs 120 BPM): +1.00 pts
Valence similarity (0.76 vs 0.75): +1.00 pts
Danceability similarity (0.74 vs 0.70): +0.95 pts
Preference for produced music: +0.5 pts
Starboy — The Weeknd
Score: 6.9459

Reasons:

Genre exact match: +1 pts
Mood match: +1 pts
Energy similarity (0.83 vs 0.75): +1.73 pts
Tempo similarity (124 vs 120 BPM): +0.97 pts
Valence similarity (0.73 vs 0.75): +0.99 pts
Danceability similarity (0.79 vs 0.70): +0.75 pts
Preference for produced music: +0.5 pts
Timber — Kesha
Score: 6.8749

Reasons:

Genre exact match: +1 pts
Mood match: +1 pts
Energy similarity (0.82 vs 0.75): +1.79 pts
Tempo similarity (118 vs 120 BPM): +0.99 pts
Valence similarity (0.84 vs 0.75): +0.84 pts
Danceability similarity (0.79 vs 0.70): +0.75 pts
Preference for produced music: +0.5 pts
Give Me Everything — Pitbull
Score: 6.1174

Reasons:

Genre exact match: +1 pts
Mood match: +1 pts
Energy similarity (0.88 vs 0.75): +1.37 pts
Tempo similarity (128 vs 120 BPM): +0.87 pts
Valence similarity (0.79 vs 0.75): +0.97 pts
Danceability similarity (0.86 vs 0.70): +0.41 pts
Preference for produced music: +0.5 pts
Middle of the Night — Elley Duhe
Score: 5.8759

Reasons:

Genre exact match: +1 pts
Energy similarity (0.81 vs 0.75): +1.85 pts
Tempo similarity (126 vs 120 BPM): +0.92 pts
Valence similarity (0.75 vs 0.75): +1.00 pts
Danceability similarity (0.82 vs 0.70): +0.61 pts
Preference for produced music: +0.5 pts

Round 2: 
Input: Genre -> Rock 
Mood: Sad
Target Energy: 0.65 
Prefers Acoustic Tracks 
Output: 
Plan
{
"genre_strategy":"exact-match-first"
"mood_strategy":"mood-match-second"
"energy_strategy":"gaussian-target-proximity"
}
Reliability summary
Confidence: 0.0262
Guardrails:
Genre and mood are categorical guardrails; numerical features are similarity-based.
Unrecognized genres fall back to the generic distant style and receive no genre bonus.
Low-confidence recommendation: the top result is too close to the runner-up.

Recommended songs
Hey Soul Sister — Train
Score: 5.3302
Reasons:
Genre similar: +0.5 pts
Energy similarity (0.72 vs 0.75): +1.96 pts
Tempo similarity (102 vs 120 BPM): +0.49 pts
Valence similarity (0.82 vs 0.75): +0.90 pts
Danceability similarity (0.68 vs 0.70): +0.99 pts
Preference for acoustic music: +0.5 pts

Warriors — Imagine Dragons
Score: 5.2778
Reasons:
Genre exact match: +1 pts
Energy similarity (0.89 vs 0.75): +1.29 pts
Tempo similarity (120 vs 120 BPM): +1.00 pts
Valence similarity (0.76 vs 0.75): +1.00 pts
Danceability similarity (0.72 vs 0.70): +0.99 pts

Live Like Legends — Ruelle
Score: 5.2777
Reasons:
Genre similar: +0.5 pts
Energy similarity (0.81 vs 0.75): +1.85 pts
Tempo similarity (116 vs 120 BPM): +0.97 pts
Valence similarity (0.72 vs 0.75): +0.98 pts
Danceability similarity (0.68 vs 0.70): +0.99 pts

From the Islands — Frozy
Score: 5.2730
Reasons:
Energy similarity (0.76 vs 0.75): +2.00 pts
Tempo similarity (110 vs 120 BPM): +0.80 pts
Valence similarity (0.78 vs 0.75): +0.98 pts
Danceability similarity (0.71 vs 0.70): +1.00 pts
Preference for acoustic music: +0.5 pts

Legends Never Die — Against the Current
Score: 5.2688
Reasons:
Genre similar: +0.5 pts
Energy similarity (0.82 vs 0.75): +1.79 pts
Tempo similarity (118 vs 120 BPM): +0.99 pts
Valence similarity (0.74 vs 0.75): +1.00 pts
Danceability similarity (0.72 vs 0.70): +0.99 pts


## Design Decisions 
I kept the scoring model simple so the recommendations are easy to explain and used a point-based scoring system so it would be easier to find recommendations to tailor to the user preferences. The mood is lightweight and simple in its design. The user just adds its genre, mood, and energy levels and it will output the plan, edge cases, guardrails, and the songs 
## Testing Summary 
The core test was done after the import issue was fixed and the command-line reliability demo successfuly ran. It shows the guardrails for uncertain or edge cases. I learned that the reliability features from AI are valuable because they check and show that despite the certainity of the AI in its recommendations, this is why it chose its answer. 
## Reflection
During this project, I used AI to clean up and annotate my code as well as suggest ways in which I am able to make the app into a proper system. I also experienced limitations such as dataset size constraints and similarity biases to underrepresenting certain genres and songs.
