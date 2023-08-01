# app.py
from flask import Flask, render_template, request
from stories import Story

app = Flask(__name__)
story_instance = Story([], "")  # Initialize a default Story instance

def generate_completed_story(story_template, user_answers):
    completed_story = story_template

    for prompt, answer in user_answers.items():
        completed_story = completed_story.replace("{" + prompt + "}", answer)

    return completed_story

@app.route("/", methods=["GET", "POST"])
def home():
    global story_instance  # setting up a global instance to keep track

    if request.method == "POST":
        # Get user-submitted words from the form
        adjective_1 = request.form["adjective_1"]
        noun_1 = request.form["noun_1"]
        verb_1 = request.form["verb_1"]
        adjective_2 = request.form["adjective_2"]
        noun_2 = request.form["noun_2"]
        adverb_1 = request.form["adverb_1"]
        verb_2 = request.form["verb_2"]
        adverb_2 = request.form["adverb_2"]

        # Construct the user answers dictionary
        user_answers = {
            "noun": noun_1,
            "verb": verb_1,
            "adjective": adjective_2,
            "plural_noun": noun_2,
        }

        # Generating the story
        completed_story = generate_completed_story(story_instance.template, user_answers)

        print("Completed Story:", completed_story)  # printing

        return render_template("result.html", completed_story=completed_story)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
