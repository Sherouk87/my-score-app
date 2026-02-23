import streamlit as st
f"""
<style>.stApp{{background-image:url("https://www.google.com/search?sca_esv=0066cc4b3f6e172b&rlz=1C1YTUH_enEG1121EG1121&sxsrf=ANbL-n5f2qF4pIOwIhho4AjhHElGXaHYmw:1771871624903&udm=2&fbs=ADc_l-ZZQ33S6yhUgl80iFaiqdDgBxFVlXcWp4zX-xfHrNZs5oqQuodA0CZXKbLivSQ2QIsygz2X7VREjePlJqAWnuUzyDmzlwx8zhQAr5gxtOL2aCYCWEuDIKN2mhytgzArmFgHE30obT_mJNnrEiNxLBJ5VzSOXUk_qswlAUkX7ZzxffXYigMDLraK7Z4DRt9vgHlk2-fAt06k-e4Pj-bpZXCVPadpYds56uPtJkRdMVXgCYq050LX1lOaMHutMIl25CfxTEGxjPNbF2aFX64qj16uXRLLbw&q=ntg+clarity&sa=X&sqi=2&ved=2ahUKEwjOwqiWoPCSAxWaRUEAHf0zAVcQtKgLegQIGRAB&biw=1366&bih=641&dpr=1#sv=CAMSVhoyKhBlLTJaUWVfNWM1akx2ZDZNMg4yWlFlXzVjNWpMdmQ2TToOQjA3Vmx3bjV2VHhuSE0gBCocCgZtb3NhaWMSEGUtMlpRZV81YzVqTHZkNk0YADABGAcgleKkkgQwAkoIEAIYAiACKAI");background-repeat:no-repeat;background-attachment:fixed;background-position:center;background-size:300px;\*opacity:0.1;\*}}
<\style>""",unsafe_allow_html=True
st.title("Candidate Evaluation System")
tech_score=st.number_input("Enter the candidate technical score:",min_value=0.0,max_value=100.0,value=50.0,step=0.5)
st.subheader(f"Score:{tech_score}%")
if tech_score==50:
    st.info("The candidateis in the average range")
elif tech_score>50:
    st.success("The candidate is above average")
else:
    st.warning("This candidate is below average")
