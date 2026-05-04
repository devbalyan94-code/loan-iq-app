import streamlit as st

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="LoanIQ", layout="wide")

# ---------------- TITLE ----------------
st.title("🏦 LoanIQ")
st.write("AI-based Loan Approval & Risk Analysis System")
st.markdown("### Enter Applicant Details (Only whole numbers allowed)")

# ---------------- INPUT SECTION ----------------
col1, col2 = st.columns(2)

with col1:
    total_loans = st.number_input(
        "Total Loans Taken",
        min_value=-100,
        max_value=1000,
        step=1,
        value=0,
        format="%d"
    )

    active_loans = st.number_input(
        "Active Loans",
        min_value=-100,
        max_value=1000,
        step=1,
        value=0,
        format="%d"
    )

    closed_loans = st.number_input(
        "Closed Loans",
        min_value=-100,
        max_value=1000,
        step=1,
        value=0,
        format="%d"
    )

    missed_payments = st.number_input(
        "Missed EMIs",
        min_value=-100,
        max_value=1000,
        step=1,
        value=0,
        format="%d"
    )

with col2:
    loans_6m = st.number_input(
        "Loans in Last 6 Months",
        min_value=-100,
        max_value=1000,
        step=1,
        value=0,
        format="%d"
    )

    closed_6m = st.number_input(
        "Closed Loans (Last 6 Months)",
        min_value=-100,
        max_value=1000,
        step=1,
        value=0,
        format="%d"
    )

    credit_score = st.number_input(
        "Credit Score",
        min_value=300,
        max_value=900,
        step=1,
        value=650,
        format="%d"
    )

    loan_activity = st.number_input(
        "Loan Activity (%)",
        min_value=-100,
        max_value=100,
        step=1,
        value=0,
        format="%d"
    )

# ---------------- PREDICTION ----------------
st.markdown("---")

if st.button("🔍 Predict Loan Decision"):

    risk = 0

    # -------- RULE-BASED LOGIC --------

    # Missed payments (strong factor)
    if missed_payments >= 3:
        risk += 40
    elif missed_payments > 0:
        risk += 20

    # Active loans risk
    if active_loans > total_loans:
        risk += 30

    if active_loans >= 5:
        risk += 20

    # No repayment history
    if closed_loans == 0:
        risk += 20

    # Credit score impact
    if credit_score < 600:
        risk += 30
    elif credit_score < 700:
        risk += 15

    # Too many recent loans
    if loans_6m >= 5:
        risk += 15

    # High activity %
    if loan_activity >= 70:
        risk += 10

    # Normalize risk
    risk = max(0, min(100, risk))

    # ---------------- RESULT ----------------
    st.subheader("Result")

    if risk > 70:
        st.error(f"🔴 High Risk ({risk}%) → Reject Loan")
    elif risk > 40:
        st.warning(f"🟡 Medium Risk ({risk}%) → Manual Review Required")
    else:
        st.success(f"🟢 Low Risk ({risk}%) → Loan Approved")

    st.progress(risk)

    # ---------------- INSIGHTS ----------------
    st.subheader("Insights")

    if credit_score < 600:
        st.write("• Low credit score detected")

    if missed_payments > 0:
        st.write("• Customer has missed EMI payments")

    if active_loans >= 5:
        st.write("• Too many active loans")

    if closed_loans == 0:
        st.write("• No past loan closure history")

    if loans_6m >= 5:
        st.write("• Too many recent loans taken")