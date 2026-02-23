import streamlit as st
st.markdown(
    """
<style>
.stApp{
background-image:url("cropped-NTG-Clarity-Logo-pk6lqv2fycz2q45ipyjvxu52cjouaxf1yuxe4lxjk2");
background-repeat:no-repeat;
background-attachment:fixed;
background-position:center;
background-size:300px;
opacity:0.1;
}
</style>
""",
    unsafe_allow_html=True
)
st.title("Candidate Evaluation System")
tech_score=st.number_input("Enter the candidate technical score:",min_value=0.0,max_value=100.0,value=50.0,step=0.5)
st.subheader(f"Score:{tech_score}%")
if tech_score==50:
    st.info("The candidateis in the average range")
elif tech_score>50:
    st.success("The candidate is above average")
else:
    st.warning("This candidate is below average")
