import streamlit as st
import pandas as pd
import random

# Set the title of the app
st.title("Pretend Prodigy")
st.markdown(
    """
    *Welcome to Pretend Prodigy, a ChatGPT powered "board game" where your goal is to 
    fool everyone else into believing your made up answers to impossible questions.*

    *Well it's not yet powered by ChatGPT but instead uses a mix of AI-generated and 
    self-made prompts.*
    """
)

# Add a description of the app
with st.expander("Expand to See Game Rules"):
    st.markdown("""
        ### Game Rules

        **Setup**: Every player needs a pen and a piece of paper. 

        In each round...

        1. **Read the Prompt**  
        One of you assumes the role as moderator. The moderator's job is to read out the my prompt to the group. For example, say the prompt is an obscure word that all of you probably have never heard before, like "Enantiodromia."

        2. **Come up with Fake Answers**  
        Every player except the moderator then have to come up with their fake but believable-sounding responses to the prompt, which they secretly write down on a piece of paper. The moderator writes down the true response, which will be provided alongside the prompt.

        3. **Read out Answers**  
        The moderator then collects all responses, shuffles them, and reads them out loud, starting with answer A, then B, then C, and so on. Tip for the moderator: make sure you can read all answers before starting to read them out loud.

        4. **Voting**  
        Each player then votes for which of the answers they think is the correct one. You can do this simply by having everyone write down the letter and have them reveal it to the group at the same time.

        5. **Distribute Points**  
        Finally, the moderator reveals which answer was written by which player and at the same time counts the votes. Every vote that a fake answer receives is a point for the player who wrote it. In addition, every player who voted for the correct answer receives a point too.

        By the way, the true definition of "_Enantiodromia_" is: the tendency for things to change into their opposites.

        You can pass around the role of moderator or stick to one player, whatever you prefer. 

        There are different kinds of prompts, with "Obscure Words" being only one of them. The prompt can come from different categories such as History, Movie Plots, Famous People, or Weird Professions. And may require you to change the style of your response accordingly to fit the prompt.

        The moderator can either pick a category or let the AI decide randomly.
        """
    )

# Load the CSV file containing the prompts
df = pd.read_csv("./data/prompts.csv", dtype='string')

# Define the categories
categories = ['Words', 'History', 'Culture & Traditions',
              'Famous People', 'Surprise Me']

# Create a horizontal radio button group to select the category
st.write("")
category = st.radio("Select a Category", categories, horizontal=True)
st.write("")

tab1, tab2, tab3 = st.tabs(["Moderator View", "Prompt Only View", "Under the Hood"])

def get_random_prompt(category):
    if category == "Surprise Me":
        return df.sample(1)
    else:
        subset = df[df.category==category]
        return subset.sample(1)

prompt = get_random_prompt(category)

with tab1:
    # Filter the dataframe to only show prompts from the selected category
    st.markdown(f"""
        #### Category: {category}
        **Prompt**: *{prompt.iloc[0].prompt}*  
        **Answer**: *{prompt.iloc[0].answer}*
    """)

with tab2:
    st.markdown(f"""
        #### Prompt: *{prompt.iloc[0].prompt}*  
        **Category**: {category}
    """)

with tab3:
    st.markdown(f"""
        #### The Role of ChatGPT

        Interested in knowing how we can make an AI come up with new prompts and answers for the game?

        We use so-called *in-context learning* to help the AI understand what kind of response we 
        would like to receive. In other words, by providing not only the task but also some 
        samples of ideal responses (ie sample questions and answers), we can get better results.

        For example here is the full ChatGPT prompt that generated the current prompt that you're
        playing with. Check back here whenever you want to see how a prompt was generated.

        >*Hi ChatGT, let's play a game.  
        >tbd*
    """)

st.write("")
if st.button('New Prompt'):
    st.experimental_rerun()
