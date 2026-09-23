import streamlit as st

# पेज कॉन्फ़िगरेशन
st.set_page_config(page_title="UP Board Physics Portal", layout="wide")

st.title("📚 UP Board भौतिक विज्ञान (Class 11 & 12)")
st.caption("हिंदी माध्यम के विद्यार्थियों के लिए संपूर्ण यूनिट-वाइज वीडियो लेक्चर्स")

# UP Board यूनिट्स और वीडियो का डेटाबेस (YouTube Embed Links)
PHYSICS_DATA = {
    "Class 11th": {
        "यूनिट 1: भौतिक जगत एवं मापन (Physical World & Measurement)": {
            "विवरण": "मात्रक, विमाएं एवं त्रुटि विश्लेषण का संपूर्ण रिवीजन",
            "video_url": "https://www.youtube.com/watch?v=kGgZ4A8YV94"
        },
        "यूनिट 2: शुद्ध गतिकी (Kinematics)": {
            "विवरण": "सरल रेखा में गति एवं समतल में गति (प्रक्षेप्य गति)",
            "video_url": "https://www.youtube.com/watch?v=3lhn3yEflQc"
        },
        "यूनिट 3: गति के नियम (Laws of Motion)": {
            "विवरण": "न्यूटन के गति नियम, संवेग संरक्षण एवं घर्षण",
            "video_url": "https://www.youtube.com/watch?v=2nF8m_v7_n4"
        },
        "यूनिट 4: कार्य, ऊर्जा एवं शक्ति (Work, Energy & Power)": {
            "विवरण": "कार्य-ऊर्जा प्रमेय, संघट्ट एवं स्थितिज ऊर्जा",
            "video_url": "https://www.youtube.com/watch?v=1FhF0i6rYQo"
        }
    },
    "Class 12th": {
        "यूनिट 1: स्थिर वैद्युतिकी (Electrostatics)": {
            "विवरण": "कूलाम का नियम, विद्युत क्षेत्र, गाउस की प्रमेय एवं संधारित्र",
            "video_url": "https://www.youtube.com/watch?v=8V7I0m_z4mE"
        },
        "यूनिट 2: धारा विद्युत (Current Electricity)": {
            "विवरण": "ओम का नियम, किरचॉफ के नियम एवं व्हीटस्टोन सेतु",
            "video_url": "https://www.youtube.com/watch?v=5tI1h9q7E5I"
        },
        "यूनिट 3: धारा का चुंबकीय प्रभाव एवं चुंबकत्व (Magnetic Effects of Current)": {
            "विवरण": "बायो-सेवर्ट नियम, ऐम्पीयर का नियम एवं चुंबकीय द्विध्रुव",
            "video_url": "https://www.youtube.com/watch?v=9gH2J8k1_7Q"
        },
        "यूनिट 4: प्रकाशिकी (Optics - किरण एवं तरंग प्रकाशिकी)": {
            "विवरण": "लेंस मेकर सूत्र, सूक्ष्मदर्शी, हाइगेंस सिद्धांत एवं व्यतिकरण",
            "video_url": "https://www.youtube.com/watch?v=4fW9t6j8P_Y"
        }
    }
}

# साइडबार - कक्षा और यूनिट चयन
with st.sidebar:
    st.header("🔍 विषय चयन")
    selected_class = st.radio("कक्षा चुनें:", ["Class 11th", "Class 12th"])

    units = list(PHYSICS_DATA[selected_class].keys())
    selected_unit = st.selectbox("यूनिट चुनें:", units)

# मुख्य स्क्रीन पर वीडियो और विवरण दिखाना
current_unit_data = PHYSICS_DATA[selected_class][selected_unit]

col1, col2 = st.columns([3, 1])

with col1:
    st.subheader(f"▶ {selected_unit}")
    st.video(current_unit_data["video_url"])

with col2:
    st.markdown("### 📝 यूनिट सारांश")
    st.info(current_unit_data["विवरण"])
    st.markdown("---")
    st.write("**UP Board विशेष निर्देश:**")
    st.markdown(
        "- सभी महत्वपूर्ण डेरिवेशन नोट करें\n- पिछले 5 वर्षों के बोर्ड प्रश्न हल करें\n- आंकिक प्रश्नों का अभ्यास करें")