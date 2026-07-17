# DecodeLabs Industrial Training: Project 2

## 💰 Dynamic Expense Tracker Engine
A real-time numeric data accumulator built to demonstrate state-preserving loops, numeric transformation validation, and boundary error handling.

---

## 🏗️ Technical Core Topics Addressed
*   **State Ledger Management:** Variables are declared globally outside the runtime environment to guarantee memory protection across iterations.
*   **Data Aggregation Pipeline:** Implements the classic computational accumulator pattern via float-point arithmetic assignments.
*   **Boundary Type Safety:** Intercepts invalid alphanumeric strings using structured try/except blocks to enforce clean data inputs.
*   **Sentinel Termination:** Employs a specific command-driven kill switch to ensure graceful script shutdowns without application crashes.

---

## ⚙️ Requirements Met
*   **State:** Successfully maintains dynamic records over multiple continuous runs.
*   **Defense:** Robust handling of type errors (ValueError anomalies).
*   **Standard:** Structured inside a clean `main()` execution gatekeeper wrapper.
