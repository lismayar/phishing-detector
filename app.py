
import streamlit as st
import re
import urllib.parse
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# نموذج تدريبي بسيط (للتجربة فقط)
def extract_features(url):
    parsed_url = urllib.parse.urlparse(url)
    length = len(url)
    https = 1 if parsed_url.scheme == "https" else 0
    subdomains = len(parsed_url.netloc.split("."))
    special_chars = len(re.findall(r'[\-\_]', url))
    return [length, https, subdomains, special_chars]

# بيانات تدريب وهمية
X_train = [
    [20, 1, 2, 0],   # آمن
    [30, 0, 3, 2],   # احتيالي
    [18, 1, 2, 0],   # آمن
    [35, 0, 4, 3]    # احتيالي
]
y_train = [0, 1, 0, 1]

# تدريب النموذج
model = RandomForestClassifier()
model.fit(X_train, y_train)

# واجهة Streamlit
st.title("أداة كشف المواقع الاحتيالية")
st.write("تحقق مما إذا كان الرابط آمنًا أو لا")

user_url = st.text_input("أدخل الرابط:")

if st.button("تحقق"):
    if user_url:
        features = extract_features(user_url)
        prediction = model.predict([features])[0]
        if prediction == 1:
            st.error("⚠️ الموقع احتيالي")
        else:
            st.success("✅ الموقع آمن")
    else:
        st.warning("الرجاء إدخال رابط أولًا.")
