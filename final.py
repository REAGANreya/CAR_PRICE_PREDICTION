# IMPORT LIBRARIES
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import time
# PAGE CONFIGURATION
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background-color: #f5f7fa;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

h1 {
    color: #0b3d91;
    font-size: 42px;
    font-weight: 800;
    text-align: center;
    margin-bottom: 5px;
}

h2 {
    color: #0b3d91;
    font-weight: 700;
}

h3 {
    color: #1565c0;
    font-weight: 700;
}

.stApp p {
    font-size: 16px;
    color: #263238;
}


/* Expanders */

div[data-testid="stExpander"] {
    background-color: #ffffff;
    border: 1px solid #d6dee8;
    border-radius: 12px;
    margin-bottom: 12px;
    box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.05);
    overflow: hidden;
}

div[data-testid="stExpander"] summary {
    padding: 16px 18px;
    font-size: 17px;
    font-weight: 700;
    color: #0b3d91;
}

div[data-testid="stExpander"] summary:hover {
    background-color: #eef4fb;
}


/* Tabs */

.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background-color: #ffffff;
    padding: 8px;
    border-radius: 12px;
    border: 1px solid #dce3ec;
    box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.05);
    margin-top: 15px;
    margin-bottom: 25px;
}

.stTabs [data-baseweb="tab"] {
    height: 50px;
    padding: 0px 20px;
    font-size: 16px;
    font-weight: 600;
    border-radius: 8px;
    color: #263238;
}

.stTabs [aria-selected="true"] {
    background-color: #0b3d91;
    color: white;
}


/* Input boxes */

.stSelectbox > div > div,
.stNumberInput > div > div > input {
    border-radius: 8px;
    border: 1px solid #b8c7d9;
    background-color: white;
}


/* Input labels */

.stSelectbox label,
.stNumberInput label {
    font-weight: 600;
    color: #263238;
}


/* Buttons */

.stButton > button {
    width: 100%;
    background-color: #0b3d91;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px 20px;
    font-size: 18px;
    font-weight: 700;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    background-color: #1565c0;
    color: white;
    transform: translateY(-2px);
    box-shadow: 0px 4px 10px rgba(11, 61, 145, 0.25);
}


/* Alerts */

.stAlert {
    border-radius: 10px;
    font-size: 16px;
}


/* Sidebar */

section[data-testid="stSidebar"] {
    background-color: #f1f4f8;
    border-right: 1px solid #d6dee8;
}

section[data-testid="stSidebar"] p {
    color: #263238;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #0b3d91;
    font-weight: 700;
}


/* Sidebar Dev Info expander */

section[data-testid="stSidebar"] div[data-testid="stExpander"] {
    background-color: #ffffff;
    border: 1px solid #d6dee8;
    border-radius: 12px;
    box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.06);
}

section[data-testid="stSidebar"] div[data-testid="stExpander"] summary {
    color: #0b3d91;
    font-weight: 700;
}

section[data-testid="stSidebar"] div[data-testid="stExpander"] summary:hover {
    background-color: #eaf2fb;
}


/* Developer table */

.developer-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 12px;
    background-color: white;
    color: #222222;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.08);
}

.developer-table th {
    background-color: #0b3d91;
    color: white;
    padding: 9px 7px;
    border: 1px solid #d9e0e8;
    text-align: left;
    font-weight: 700;
}

.developer-table td {
    padding: 8px 7px;
    border: 1px solid #d9e0e8;
    color: #263238;
    background-color: white;
}

.developer-table tr:nth-child(even) td {
    background-color: #f7f9fc;
}

.developer-table tr:hover td {
    background-color: #eaf2fb;
}


/* Dataframes */

[data-testid="stDataFrame"] {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid #d6dee8;
}


/* File uploader */

[data-testid="stFileUploader"] {
    background-color: white;
    border: 2px dashed #0b3d91;
    border-radius: 12px;
    padding: 15px;
}


/* Dividers */

hr {
    border: none;
    border-top: 1px solid #d5dce5;
    margin: 25px 0;
}


/* Download button */

[data-testid="stDownloadButton"] button {
    width: 100%;
    background-color: #2e7d32;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px;
    font-size: 16px;
    font-weight: 700;
    transition: 0.3s;
}

[data-testid="stDownloadButton"] button:hover {
    background-color: #388e3c;
    color: white;
    transform: translateY(-2px);
}


/* Mobile */

@media (max-width: 768px) {

    h1 {
        font-size: 30px;
    }

    h2 {
        font-size: 24px;
    }

    h3 {
        font-size: 20px;
    }

    .stTabs [data-baseweb="tab"] {
        padding: 0px 8px;
        font-size: 13px;
    }

    .developer-table {
        font-size: 10px;
    }

    .developer-table th,
    .developer-table td {
        padding: 6px 4px;
    }

}

</style>
""", unsafe_allow_html=True)


# LOAD MODEL, PREPROCESSOR AND DATASET
model = joblib.load("model.joblib")
preprocessor = joblib.load("preprocessor.joblib")
df = pd.read_csv("clean_car_data.csv")
# MAIN TITLE
st.title("🚗 CAR PRICE PREDICTION")
st.write(
    "A machine learning system for predicting car prices "
    "using important vehicle features."
)
col3, col4 = st.columns([1,1])
with col3:
    with st.expander("🚗 About Model"):
        st.write(
        "This system uses machine learning to predict the price "
        "of a car based on important vehicle characteristics.")
        st.write(
            "The model was trained using selected categorical and "
            "numerical features including brand, fuel type, car body, "
            "drive wheel, cylinder number, engine size, horsepower "
            "and symboling.")
        st.write(
            "The trained Random Forest model is used to generate "
            "individual and batch car price predictions.")


    with st.expander("📞 Contacts"):
        st.write("For more information about this project, contact the development team.")
        st.write("📧 Email: carpriceprediction@example.com")
        st.write("📱 Phone: +256 XXX XXX XXX")

with col4:
    st.image('UICT.jpg', caption='@uict', width=140)

# CREATE THREE TABS
prediction_tab, visualization_tab, company_tab = st.tabs(
    [
        "🚗 Price Prediction",
        "📊 Visualizations",
        "🏢 Company Predictions"
    ]
)
# TAB 1 — INDIVIDUAL CAR PRICE PREDICTION
with prediction_tab:

    st.header("🚗 Predict the Price of a Car")

    st.write(
        "Enter the details of the car below and click "
        "**Predict Price**."
    )

    # CAR INFORMATION
    st.subheader("Car Information")

    col1, col2 = st.columns(2)

    # BRAND
    with col1:

        Brand = st.selectbox(
            "Brand",
            sorted(df["Brand"].dropna().unique()),
            help=(
                "The manufacturer or brand of the car. "
                "For example, Toyota, BMW, Honda or Audi."
            )
        )

    # FUEL TYPE
    with col2:

        fueltype = st.selectbox(
            "Fuel Type",
            sorted(df["fueltype"].dropna().unique()),
            help=(
                "The type of fuel used by the car, "
                "such as gas or diesel."
            )
        )

    # CAR BODY
    with col1:

        carbody = st.selectbox(
            "Car Body",
            sorted(df["carbody"].dropna().unique()),
            help=(
                "The body style of the vehicle, "
                "such as sedan, hatchback, wagon or convertible."
            )
        )

    # NUMBER OF DOORS
    with col2:

        doornumber = st.selectbox(
            "Number of Doors",
            sorted(df["doornumber"].dropna().unique()),
            help=(
                "The number of doors on the vehicle."
            )
        )

    # DRIVE WHEEL
    with col1:

        drivewheel = st.selectbox(
            "Drive Wheel",
            sorted(df["drivewheel"].dropna().unique()),
            help=(
                "Shows which wheels receive power from "
                "the engine, such as front-wheel drive, "
                "rear-wheel drive or four-wheel drive."
            )
        )

    # ENGINE INFORMATION
    st.subheader("⚙️ Engine Information")

    col1, col2 = st.columns(2)

    # CYLINDER NUMBER
    with col1:

        cylindernumber = st.selectbox(
            "Cylinder Number",
            sorted(df["cylindernumber"].dropna().unique()),
            help=(
                "The number of cylinders in the vehicle's engine. "
                "More cylinders can generally provide greater "
                "engine power."
            )
        )

    # ENGINE SIZE
    with col2:

        enginesize = st.number_input(
            "Engine Size",
            min_value=float(df["enginesize"].min()),
            max_value=float(df["enginesize"].max()),
            value=float(df["enginesize"].median()),
            help=(
                "The size of the engine measured in cubic centimetres (cc). "
                "Larger engines generally have greater capacity."
            )
        )

    # HORSEPOWER
    with col1:

        horsepower = st.number_input(
            "Horsepower",
            min_value=float(df["horsepower"].min()),
            max_value=float(df["horsepower"].max()),
            value=float(df["horsepower"].median()),
            help=(
                "The power produced by the engine. "
                "Higher horsepower generally indicates a more powerful car."
            )
        )

    # SYMBOLING
    st.subheader("⭐ Vehicle Rating")

    symboling = st.number_input(
        "Symboling",
        min_value=float(df["symboling"].min()),
        max_value=float(df["symboling"].max()),
        value=float(df["symboling"].median()),
        help=(
            "A risk or insurance-related rating assigned to the vehicle. "
            "It is one of the characteristics used by the model "
            "to predict price."
        )
    )
    # PREDICTION BUTTON
    st.divider()

    if st.button(
        "🔮 Predict Price",
        use_container_width=True
    ):
        # CREATE INPUT DATAFRAME
        input_data = pd.DataFrame({
            "Brand": [Brand],
            "fueltype": [fueltype],
            "symboling": [symboling],
            "doornumber": [doornumber],
            "carbody": [carbody],
            "drivewheel": [drivewheel],
            "cylindernumber": [cylindernumber],
            "enginesize": [enginesize],
            "horsepower": [horsepower]
        })
        with st.spinner('Predicting Price...'):
            time.sleep(1.5)
            input_transformed = preprocessor.transform(input_data)
            prediction = model.predict(input_transformed)

        # Display prediction
            time.sleep(1.5)
            st.success(
            f"💰 Predicted Car Price: {prediction[0]:,.2f}")



# TAB 2 — VISUALIZATIONS
with visualization_tab:

    st.header("📊 Car Price Visualizations")

    st.write(
        "Explore the relationships and distributions "
        "of important variables in the dataset."
    )

    # NUMERICAL VARIABLES
    st.subheader("Numerical Variables")
    
    # ENGINE SIZE VS PRICE
    st.write("### Engine Size vs Price")

    fig, ax = plt.subplots()

    ax.scatter(
        df["enginesize"],
        df["price"]
    )

    ax.set_xlabel("Engine Size")
    ax.set_ylabel("Price")
    ax.set_title("Engine Size vs Price")

    st.pyplot(fig)

    st.divider()
    
    # HORSEPOWER VS PRICE
    st.write("### Horsepower vs Price")

    fig, ax = plt.subplots()

    ax.scatter(
        df["horsepower"],
        df["price"], color='red'
    )

    ax.set_xlabel("Horsepower")
    ax.set_ylabel("Price")
    ax.set_title("Horsepower vs Price")

    st.pyplot(fig)

    st.divider()
    
    # SYMBOLING VS PRICE
    st.write("### Symboling vs Price")

    fig, ax = plt.subplots()

    ax.scatter(
        df["symboling"],
        df["price"], color='darkgreen'
    )

    ax.set_xlabel("Symboling")
    ax.set_ylabel("Price")
    ax.set_title("Symboling vs Price")

    st.pyplot(fig)

    st.divider()

    st.subheader("Cylinder Number vs Price")

    fig4, ax4 = plt.subplots()

    ax4.scatter(
        df["cylindernumber"],
        df["price"], color='navy'
    )

    ax4.set_xlabel("Cylinder Number")
    ax4.set_ylabel("Price")
    ax4.set_title("Cylinder Number vs Price")

    st.pyplot(fig4)

    # CATEGORICAL VARIABLES
    st.subheader("Categorical Variables")

    # CAR BODY — PIE CHART
    st.write("### Car Body Style Distribution")

    body_counts = df["carbody"].value_counts()

    fig, ax = plt.subplots()

    ax.pie(
        body_counts,
        labels=body_counts.index,
        autopct="%1.1f%%",
        startangle=50
    )

    ax.set_title("Distribution of Car Body Styles")

    st.pyplot(fig)

    st.divider()

    # BRAND — BAR CHART
    st.write("### Car Brand Distribution")

    brand_counts = df["Brand"].value_counts()

    fig, ax = plt.subplots()

    brand_counts.plot(
        kind="bar",color='navy',
        ax=ax
    )

    ax.set_xlabel("Brand")
    ax.set_ylabel("Number of Cars")
    ax.set_title("Distribution of Car Brands")

    plt.xticks(rotation=90)

    st.pyplot(fig)

    st.divider()

    # FUEL TYPE — BAR CHART
    st.write("### Fuel Type Distribution")

    fuel_counts = df["fueltype"].value_counts()

    fig, ax = plt.subplots()

    fuel_counts.plot(
        kind="bar", color='gold',
        ax=ax
    )

    ax.set_xlabel("Fuel Type")
    ax.set_ylabel("Number of Cars")
    ax.set_title("Distribution of Fuel Types")

    st.pyplot(fig)

    st.divider()

    # NUMBER OF DOORS — BAR CHART
    st.write("### Number of Doors Distribution")

    door_counts = df["doornumber"].value_counts()

    fig, ax = plt.subplots()

    door_counts.plot(
        kind="bar", color='red',
        ax=ax
    )

    ax.set_xlabel("Number of Doors")
    ax.set_ylabel("Number of Cars")
    ax.set_title("Distribution of Number of Doors")

    st.pyplot(fig)

    st.divider()

    # DRIVE WHEELS — BAR CHART
    st.write("### Drive Wheel Distribution")

    drive_counts = df["drivewheel"].value_counts()

    fig, ax = plt.subplots()

    drive_counts.plot(
        kind="bar",color='purple',
        ax=ax
    )

    ax.set_xlabel("Drive Wheel")
    ax.set_ylabel("Number of Cars")
    ax.set_title("Distribution of Drive Wheels")

    st.pyplot(fig)
    
# TAB 3 — COMPANY BATCH PREDICTIONS
with company_tab:

    st.header("🏢 Company Car Price Predictions")

    st.write(
        "Companies can upload a CSV containing information "
        "about multiple cars and receive price predictions "
        "for all vehicles at once."
    )

    # REQUIRED COLUMNS
    required_columns = [
        "Brand",
        "fueltype",
        "symboling",
        "doornumber",
        "carbody",
        "drivewheel",
        "cylindernumber",
        "enginesize",
        "horsepower"
    ]


    st.info(
        "Your CSV file must contain the following columns:"
    )

    st.code(
        ", ".join(required_columns)
    )

    # UPLOAD CSV
    uploaded_file = st.file_uploader(
        "📂 Upload Company CSV File",
        type=["csv"]
    )


    if uploaded_file is not None:
        
        # READ CSV
        company_data = pd.read_csv(
            uploaded_file
        )

        # DISPLAY UPLOADED DATA
        st.subheader("Uploaded Dataset")

        st.dataframe(
            company_data,
            use_container_width=True
        )

        # CHECK REQUIRED COLUMNS
        missing_columns = [
            column
            for column in required_columns
            if column not in company_data.columns
        ]


        if missing_columns:

            st.error(
                "❌ Some required columns are missing."
            )

            st.write("Missing columns:")

            st.write(
                missing_columns
            )


        else:

            st.success(
                "✅ All required columns are available."
            )

            # SELECT MODEL FEATURES
            company_features = company_data[
                required_columns
            ]

            # GENERATE PREDICTIONS
            if st.button(
                "🔮 Generate Company Predictions",
                use_container_width=True
            ):

                # TRANSFORM DATA
                company_transformed = preprocessor.transform(
                    company_features
                )

                # PREDICT PRICES
                predictions = model.predict(
                    company_transformed
                )

                # ADD PREDICTIONS TO DATASET
                company_data["predicted_price"] = predictions

                # DISPLAY RESULTS
                st.subheader(
                    "📋 Prediction Results"
                )

                st.dataframe(
                    company_data,
                    use_container_width=True
                )

                # DOWNLOAD CSV
                csv = company_data.to_csv(
                    index=False
                ).encode("utf-8")


                st.download_button(
                    label="⬇️ Download Predictions CSV",
                    data=csv,
                    file_name="car_price_predictions.csv",
                    mime="text/csv",
                    use_container_width=True
                )

                st.success(
                    "✅ Predictions generated successfully. "
                    "You can now download the results."
                )

# SIDEBAR — DEVELOPERS
with st.sidebar:

    st.header("👨‍💻 Developers")

    st.write("Project Development Team")

    st.markdown(
        """
        <style>
        .developer-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 13px;
        }

        .developer-table th,
        .developer-table td {
            border: 1px solid #888;
            padding: 6px;
            text-align: left;
        }

        .developer-table th {
            font-weight: bold;
        }
        </style>

        <table class="developer-table">
            <tr>
                <th>Name</th>
                <th>Registration Number</th>
            </tr>
            <tr>
                <td>YABIRAKU REAGAN</td>
                <td>2025/DSMA/DAY/1562/G</td>
            </tr>
            <tr>
                <td>NAKATE JANE</td>
                <td>2025/DSMA/DAY/1564/G</td>
            </tr>
            <tr>
                <td>KATENDE DOUGLAS</td>
                <td>2025/DSMA/DAY/1560/G</td>
            </tr>
            <tr>
                <td>AKULLU GLADYS</td>
                <td>2025/DSMA/DAY/2503/G</td>
            </tr>
            <tr>
                <td>SSEMBOWA DOMINIC VICENT</td>
                <td>2025/DSMA/DAY/1487/G</td>
            </tr>
        </table>
        """,
        unsafe_allow_html=True
    )

    st.divider()
    with st.expander('👨‍💻Dev Info'):
        st.write('This prediction model was developed by the above students wwho are currently persuing a Diploma in Data Science Management and Analytics at Uganda Institute of Information and Communication Technology(UICT).')
        st.write('The above students created a group called GROUP C that enabled them to work together and come up with such an amazing project')

    st.caption(
        "Car Price Prediction System"
    )
