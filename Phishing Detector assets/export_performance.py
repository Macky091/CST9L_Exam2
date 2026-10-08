# Run this in your Colab notebook, AFTER you have X_test / y_test and the loaded model.
# It prints one JSON line to paste into the app's "Load your own results" box,
# or to replace `const PERF = {...}` in phishing_detector.html (set "source":"real").
import json
import numpy as np
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score

# model = joblib.load("phishing_random_forest_model.skl")["model"]
FEATURES = list(model.feature_names_in_)           # same column order used in training
Xt = X_test[FEATURES]

phish_col = list(model.classes_).index(-1)         # class -1 = phishing
score = model.predict_proba(Xt)[:, phish_col]      # P(phishing)
y_pos = (np.asarray(y_test) == -1).astype(int)     # 1 = phishing (positive class)
y_hat = (model.predict(Xt) == -1).astype(int)

fpr, tpr, _ = roc_curve(y_pos, score)
keep = np.unique(np.linspace(0, len(fpr) - 1, min(250, len(fpr))).astype(int))

perf = {
    "source": "real",
    "labels": ["Legitimate", "Phishing"],           # last label = positive class
    "cm": confusion_matrix(y_pos, y_hat, labels=[0, 1]).tolist(),   # [[TN, FP], [FN, TP]]
    "auc": round(float(roc_auc_score(y_pos, score)), 4),
    "fpr": [round(float(v), 4) for v in fpr[keep]],
    "tpr": [round(float(v), 4) for v in tpr[keep]],
}
print(json.dumps(perf, separators=(",", ":")))
