from typing import List, Dict

# Evaluation dataset containing realistic admission policy questions and their target source files
EVALUATION_SET: List[Dict[str, str]] = [
    {
        "question": "What is the minimum TOEFL score required for international graduate applicants?",
        "expected_document": "international_admission_policy.pdf"
    },
    {
        "question": "Are transfer credits accepted from non-accredited community colleges?",
        "expected_document": "transfer_credit_policy.pdf"
    },
    {
        "question": "What is the deadline to submit the FAFSA for priority financial aid consideration?",
        "expected_document": "financial_aid_policy.pdf"
    },
    {
        "question": "How long can an accepted student defer their enrollment?",
        "expected_document": "enrollment_deferral_policy.pdf"
    },
    {
        "question": "What GPA is required to maintain merit-based academic scholarships?",
        "expected_document": "scholarship_policy.pdf"
    },
    {
        "question": "Can waitlisted applicants submit additional recommendation letters to improve their chances?",
        "expected_document": "waitlist_policy.pdf"
    },
    {
        "question": "What is the refund schedule if a student withdraws from all classes in the first week?",
        "expected_document": "tuition_refund_policy.pdf"
    },
    {
        "question": "Are standardized test scores (SAT/ACT) required for home-schooled applicants?",
        "expected_document": "homeschool_admission_policy.pdf"
    },
    {
        "question": "Does the university offer application fee waivers for low-income domestic applicants?",
        "expected_document": "fee_waiver_policy.pdf"
    },
    {
        "question": "What is the maximum number of credits that can be transferred toward an undergraduate degree?",
        "expected_document": "transfer_credit_policy.pdf"
    }
]
