import joblib

model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

ACADEMIC_KEYWORDS = [
    "project",
    "synopsis",
    "chapter",
    "abstract",
    "college",
    "university",
    "assignment",
    "training",
    "report",
    "student",
    "semester",
    "engineering",
    "technology",
    "computer science",
    "database",
    "implementation",
    "frontend",
    "backend",
    "research",
    "thesis",
    "internship",
    "lab",
    "experiment",
    "faculty",
    "curriculum",
    "lecture",
    "subject",
    "exam",
    "education",
    "spring boot",
    "mysql",
    "java",
    "python"
]


FINANCE_KEYWORDS = [
    "bank",
    "transaction",
    "account",
    "payment",
    "salary",
    "gst",
    "tax",
    "income",
    "statement",
    "credit",
    "debit",
    "investment",
    "insurance",
    "loan",
    "emi",
    "interest",
    "balance",
    "finance"
]


BILL_KEYWORDS = [
    "invoice",
    "bill",
    "electricity",
    "water bill",
    "wifi",
    "internet",
    "telephone",
    "recharge",
    "utility",
    "payment due",
    "receipt",
    "paid amount",
    "billing"
]


WORK_KEYWORDS = [
    "meeting",
    "client",
    "employee",
    "company",
    "office",
    "business",
    "manager",
    "team",
    "deadline",
    "startup",
    "proposal",
    "presentation",
    "work report",
    "professional",
    "organization",
    "job",
    "task"
]


PERSONAL_KEYWORDS = [
    "personal",
    "family",
    "diary",
    "holiday",
    "travel",
    "birthday",
    "friends",
    "memories",
    "vacation",
    "private",
    "photos",
    "trip",
    "self"
]


MEDICAL_KEYWORDS = [
    "hospital",
    "patient",
    "doctor",
    "prescription",
    "medical",
    "medicine",
    "blood test",
    "diagnosis",
    "treatment",
    "clinic",
    "health",
    "report",
    "xray",
    "scan"
]


LEGAL_KEYWORDS = [
    "agreement",
    "contract",
    "court",
    "legal",
    "affidavit",
    "license",
    
    "compliance",
    "policy",
    "terms",
    "condition",
    "case",
    "lawyer",
    "nda"
]


SHOPPING_KEYWORDS = [
    "amazon",
    "flipkart",
    "order",
    "delivery",
    "purchase",
    "shopping",
    "cart",
    "tracking",
    "product",
    "return",
    "refund",
    "invoice"
]


IDENTITY_KEYWORDS = [
    "aadhaar",
    "pan card",
    "passport",
    "driving license",
    "voter id",
    "identity",
    "government",
    "uidai",
    "citizen"
]


CERTIFICATE_KEYWORDS = [
    "certificate",
    "completion",
    "achievement",
    "participation",
    "award",
    "recognition",
    "credential"
]


RESUME_KEYWORDS = [
    "resume",
    "cv",
    "curriculum vitae",
    "skills",
    "experience",
    "linkedin",
    "career",
    "qualification"
]


PROJECT_KEYWORDS = [
    "source code",
    "github",
    "api",
    "software",
    "application",
    "development",
    "system design",
    "architecture",
    "module"
]


def keyword_classify(text):

    text = text.lower()

    academic_score = sum(
        keyword in text for keyword in ACADEMIC_KEYWORDS
    )

    finance_score = sum(
        keyword in text for keyword in FINANCE_KEYWORDS
    )

    medical_score = sum(
        keyword in text for keyword in MEDICAL_KEYWORDS
    )

    print("Academic Score:", academic_score)
    print("Finance Score:", finance_score)
    print("Medical Score:", medical_score)

    scores = {
    "Academics": sum(k in text for k in ACADEMIC_KEYWORDS),
    "Finance": sum(k in text for k in FINANCE_KEYWORDS),
    "Bills": sum(k in text for k in BILL_KEYWORDS),
    "Work": sum(k in text for k in WORK_KEYWORDS),
    "Personal": sum(k in text for k in PERSONAL_KEYWORDS),
    "Medical": sum(k in text for k in MEDICAL_KEYWORDS),
    "Legal": sum(k in text for k in LEGAL_KEYWORDS),
    "Shopping": sum(k in text for k in SHOPPING_KEYWORDS),
    "Identity": sum(k in text for k in IDENTITY_KEYWORDS),
    "Certificates": sum(k in text for k in CERTIFICATE_KEYWORDS),
    "Resume": sum(k in text for k in RESUME_KEYWORDS),
    "Projects": sum(k in text for k in PROJECT_KEYWORDS)
    }

    best_label = max(scores, key=scores.get)

    # IMPORTANT FIX
    if scores[best_label] >= 1:
        return best_label, 0.95

    return None, 0


def classify(text):

    # STEP 1 → KEYWORD RULES
    keyword_result, confidence = keyword_classify(text)

    if keyword_result is not None:

        print("Keyword Classification:", keyword_result)

        return keyword_result, confidence

    print("\n===================================")
    print("      AI CLASSIFICATION")
    print("===================================\n")

    # STEP 2 → ML MODEL
    vec = vectorizer.transform([text])

    prediction = model.predict(vec)[0]

    print("Predicted Category :", prediction[0])

    probabilities = model.predict_proba(vec)[0]

    confidence = max(probabilities)

    print("ML Prediction:", prediction)
    print("ML Confidence:", confidence)

    # STEP 3 → LOW CONFIDENCE
    if confidence < 0.50:
        return "Others", confidence

    return prediction, confidence
