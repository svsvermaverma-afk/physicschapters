import streamlit as st

# 1. पेज कॉन्फ़िगरेशन
st.set_page_config(
    page_title="UP Board Physics Portal", 
    page_icon="📚", 
    layout="wide"
)

# कस्टम स्टाइलिंग
st.markdown("""
    <style>
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📚 UP Board भौतिक विज्ञान (Class 11 & 12)</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">हिंदी माध्यम के विद्यार्थियों के लिए संपूर्ण यूनिट-वाइज वन-शॉट वीडियो लेक्चर्स</div>', unsafe_allow_html=True)

# 2. UP Board यूनिट्स एवं वेरीफाइड वीडियो डेटाबेस
PHYSICS_DATA = {
    "Class 11th": {
        "यूनिट 1: मात्रक तथा मापन (Units & Measurement)": {
            "विवरण": "मात्रक, विमीय सूत्र, विमाओं के अनुप्रयोग एवं सार्थक अंक का संपूर्ण अध्ययन।",
            "video_url": "https://www.youtube.com/watch?v=b2FE3KLJbxQ",
            "important_topics": ["विमीय समांगता का नियम", "त्रुटि विश्लेषण", "मूल एवं व्युत्पन्न मात्रक"]
        },
        "यूनिट 2: सदिश विश्लेषण एवं समतल में गति": {
            "विवरण": "सदिशों का योग, वियोजन, अदिश व सदिश गुणनफल एवं प्रक्षेप्य गति।",
            "video_url": "https://www.youtube.com/watch?v=09KFRCEQTsE",
            "important_topics": ["प्रक्षेप्य का पथ परवलयाकार सिद्ध करना", "सदिशों का डॉट एवं क्रॉस गुणनफल", "अधिकतम ऊँचाई व उड्डयन काल"]
        },
        "यूनिट 3: गति के नियम (Laws of Motion)": {
            "विवरण": "न्यूटन के गति नियम, संवेग संरक्षण का नियम एवं घर्षण बल।",
            "video_url": "https://www.youtube.com/watch?v=R52wYRfzAz4",
            "important_topics": ["संवेग संरक्षण का नियम", "घर्षण कोण एवं विराम कोण", "लिफ्ट में व्यक्ति का आभासी भार"]
        },
        "यूनिट 4: कार्य, ऊर्जा एवं शक्ति (Work, Energy & Power)": {
            "विवरण": "कार्य-ऊर्जा प्रमेय, स्थितिज ऊर्जा, संघट्ट (Collision) एवं शक्ति।",
            "video_url": "https://www.youtube.com/watch?v=utoATqRy7U8",
            "important_topics": ["कार्य-ऊर्जा प्रमेय का निगमन", "प्रत्यास्थ एवं अप्रत्यास्थ संघट्ट", "संरक्षी एवं असंरक्षी बल"]
        }
    },
    "Class 12th": {
        "यूनिट 1: विद्युत आवेश तथा क्षेत्र (Electric Charges & Fields)": {
            "विवरण": "कूलाम का नियम, विद्युत क्षेत्र की तीव्रता, विद्युत द्विध्रुव एवं गाउस की प्रमेय।",
            "video_url": "https://www.youtube.com/watch?v=jHaZ2ur_qpU",
            "important_topics": ["गाउस के नियम से तीव्रता निकालना", "विद्युत द्विध्रुव की अक्षीय व निरक्षीय स्थिति", "कूलाम के नियम का सदिश रूप"]
        },
        "यूनिट 2: स्थिर विद्युत विभव तथा धारिता": {
            "विवरण": "विद्युत विभव, समविभव पृष्ठ, समांतर पट्ट संधारित्र एवं ऊर्जा घनत्व।",
            "video_url": "https://www.youtube.com/watch?v=oiquJQOm6lM",
            "important_topics": ["समांतर पट्ट संधारित्र की धारिता", "परावैद्युत पदार्थ का प्रभाव", "विद्युत स्थितिज ऊर्जा"]
        },
        "यूनिट 3: चुंबक तथा द्रव्य (Magnetism & Matter)": {
            "विवरण": "चुंबकीय द्विध्रुव आघूर्ण, भू-चुंबकत्व के अवयव, प्रति/अनु/लौह-चुंबकीय पदार्थ।",
            "video_url": "https://www.youtube.com/watch?v=WRHQYcP5FQI",
            "important_topics": ["नति कोण एवं दिक्पात कोण", "चुंबकीय पदार्थों का वर्गीकरण", "बायो-सेवर्ट नियम के अनुप्रयोग"]
        },
        "यूनिट 4: वैद्युत आवेश एवं क्षेत्र (रिवीजन + PYQs)": {
            "विवरण": "बोर्ड परीक्षा के महत्वपूर्ण आंकिक प्रश्न (Numericals) और डेरीवेशन।",
            "video_url": "https://www.youtube.com/watch?v=zA4wi009miQ",
            "important_topics": ["गत वर्षों के बोर्ड प्रश्न (PYQ)", "5 अंक वाले महत्वपूर्ण डेरीवेशन", "आंकिक प्रश्नों का हल"]
        }
    }
}

# 3. साइडबार - नेविगेशन
with st.sidebar:
    st.header("🔍 विषय चयन")
    selected_class = st.radio("कक्षा चुनें:", ["Class 11th", "Class 12th"])
    
    units = list(PHYSICS_DATA[selected_class].keys())
    selected_unit = st.selectbox("यूनिट चुनें:", units)
    
    st.markdown("---")
    st.markdown("💡 **टिप:** यदि इंटरनेट धीमा हो तो वीडियो को सीधे YouTube पर भी देख सकते हैं।")

# 4. मुख्य डिस्प्ले एरिया
unit_data = PHYSICS_DATA[selected_class][selected_unit]

col_left, col_right = st.columns([2.8, 1.2])

with col_left:
    st.subheader(f"▶ {selected_unit}")
    
    # वीडियो प्लेयर
    st.video(unit_data["video_url"])
    
    # बैकअप लिंक बटन
    st.link_button("🔗 YouTube पर सीधे खोलें", unit_data["video_url"])

with col_right:
    st.markdown("### 📋 यूनिट सारांश")
    st.info(unit_data["विवरण"])
    
    st.markdown("### ⭐ मुख्य परीक्षा बिंदु")
    for topic in unit_data["important_topics"]:
        st.markdown(f"- {topic}")
        
    st.markdown("---")
    st.success("✅ **बोर्ड परीक्षा रणनीति:**\n- सभी फ़ॉर्मूलों की डायरी बनाएं\n- मात्रक एवं विमाएँ ज़रूर लिखें\n- डेरीवेशन का लिखकर अभ्यास करें")
