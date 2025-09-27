import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# === Load model ===
model = joblib.load("delivery_time_model_linear_regression.pkl")

# === Sidebar menu ===
st.sidebar.title("📌 Menu")
menu = st.sidebar.radio("Pilih Halaman:", ["🏠 Home", "📊 EDA", "🤖 Prediksi", "📈 Evaluasi Model"])

# ================= HOME =================
if menu == "🏠 Home":
    st.title("🚚 Food Delivery Time Prediction")
    st.markdown("""
    ## Business Understanding
    Dalam industri *food delivery*, kecepatan pengantaran adalah kunci kepuasan pelanggan.  
    Tujuan utama project ini:
    1. Memprediksi waktu pengantaran makanan.
    2. Mengidentifikasi faktor yang paling memengaruhi waktu pengantaran.
    3. Memberikan rekomendasi untuk meningkatkan efisiensi operasional.

    **Model terbaik:** `Linear Regression` dengan akurasi (R²) ≈ **0.77**.
    """)

# ================= EDA =================
elif menu == "📊 EDA":
    st.title("📊 Exploratory Data Analysis (EDA)")

    uploaded_file = st.file_uploader("Upload dataset CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file).dropna().drop_duplicates()
        st.subheader("Data Sample")
        st.write(df.head())

        chart_type = st.selectbox("Pilih visualisasi:", [
            "Distribusi Waktu Pengantaran",
            "Jarak vs Waktu",
            "Cuaca vs Waktu",
            "Traffic vs Waktu"
        ])

        if chart_type == "Distribusi Waktu Pengantaran":
            fig, ax = plt.subplots()
            sns.histplot(df["Delivery_Time_min"], bins=30, kde=True, ax=ax)
            plt.axvline(df['Delivery_Time_min'].mean(), color='r', linestyle='--', label='Mean')
            ax.legend()
            st.pyplot(fig)

        elif chart_type == "Jarak vs Waktu":
            fig, ax = plt.subplots()
            sns.scatterplot(x="Distance_km", y="Delivery_Time_min", data=df, alpha=0.6, ax=ax)
            st.pyplot(fig)

        elif chart_type == "Cuaca vs Waktu":
            fig, ax = plt.subplots()
            sns.boxplot(x="Weather", y="Delivery_Time_min", data=df, ax=ax)
            st.pyplot(fig)

        elif chart_type == "Traffic vs Waktu":
            fig, ax = plt.subplots()
            sns.boxplot(x="Traffic_Level", y="Delivery_Time_min", data=df, ax=ax)
            st.pyplot(fig)
    else:
        st.info("Silakan upload dataset untuk EDA.")

# ================= PREDIKSI =================
elif menu == "🤖 Prediksi":
    st.title("🤖 Prediksi Waktu Pengantaran")

    distance = st.number_input("Jarak (km)", min_value=0.0, step=0.1)
    prep_time = st.number_input("Preparation Time (menit)", min_value=1, step=1)
    weather = st.selectbox("Cuaca", ["Clear", "Rainy", "Foggy", "Storm"])
    traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High"])
    vehicle = st.selectbox("Jenis Kendaraan", ["Scooter", "Bike", "Car"])
    experience = st.slider("Pengalaman Kurir (tahun)", 0, 10, 1)
    time_of_day = st.selectbox("Waktu Pengantaran", ["Morning", "Afternoon", "Evening", "Night"])

    # Mapping categorical
    weather_map = {"Clear":0, "Rainy":1, "Foggy":2, "Storm":3}
    traffic_map = {"Low":0, "Medium":1, "High":2}
    vehicle_map = {"Scooter":0, "Bike":1, "Car":2}
    time_map = {"Morning":0, "Afternoon":1, "Evening":2, "Night":3}

    input_data = pd.DataFrame([{
        "Distance_km": distance,
        "Preparation_Time_min": prep_time,
        "Weather": weather_map[weather],
        "Traffic_Level": traffic_map[traffic],
        "Vehicle_Type": vehicle_map[vehicle],
        "Courier_Experience_yrs": experience,
        "Time_of_Day": time_map[time_of_day]
    }])

    if st.button("Prediksi"):
        prediction = model.predict(input_data)[0]
        st.success(f"⏱️ Estimasi waktu pengantaran: **{prediction:.2f} menit**")

# ================= EVALUASI MODEL =================
elif menu == "📈 Evaluasi Model":
    st.title("📈 Evaluasi Model")

    results = {
        "Linear Regression": {"MAE": 6.957, "RMSE": 9.598, "R2": 0.775},
        "Decision Tree": {"MAE": 10.305, "RMSE": 15.214, "R2": 0.434},
        "Random Forest": {"MAE": 7.060, "RMSE": 9.965, "R2": 0.757},
        "XGBoost": {"MAE": 7.690, "RMSE": 10.985, "R2": 0.705},
    }

    df_eval = pd.DataFrame(results).T
    st.dataframe(df_eval)
