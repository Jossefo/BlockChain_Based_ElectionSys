import streamlit as st
import vote_chain
import app

st.set_page_config(
    page_title="BlockChain based voting System",
    page_icon="🗳️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# chain = vote_chain.BlockChain()
# israel_election = chain
#replaced 2 line above to the next lone (for not losing data)
israel_election = app.israel_election

st.title("BlockChain based - Voting System:")

# Add a candidates
new_candidate = st.text_input("New Candidate Name:")

if st.button("Add Candidate"):
    vote_chain.candidates.append(new_candidate)
    st.success(f"Added candidate -> {new_candidate} successfully.")

# Display the current candidates
st.write("Current candidates:")
st.write(f"{vote_chain.candidates}")

# voter data logic
voter_name = st.text_input("Voter Name") #get the voter name
voter_code = vote_chain.voter_code #generate a code for the voter
vote_chain.voter_code += 1 #increse the code count
option_list = [_ for _ in vote_chain.candidates]
voter_choose = st.selectbox("Choose your candidate to vote for", option_list)
new_voter = vote_chain.Voter(voter_name, voter_code)

if st.button("Vote"):
    new_vote = vote_chain.Vote(new_voter.key, voter_choose)
    israel_election.create_block(new_vote)
    st.success(f"Voted to -> {voter_choose}")

st.title("Current Score for Elections:")
st.write(f"{israel_election.get_votes()}")