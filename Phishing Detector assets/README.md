# 🛡️ Phishing Website Detector

Random Forest phishing classifier (100 trees, 16 features). The whole model is embedded in
`phishing_detector.html` and runs in the browser, so no Python ML libraries are needed to deploy.

## Files
| File | Purpose |
|---|---|
| `phishing_detector.html` | The full app (UI + model). Open it directly. |
| `app.py` | Streamlit wrapper that displays the HTML. |
| `requirements.txt` | Only `streamlit`. |

## Run in VS Code (HTML only)
1. Install the **Live Server** extension.
2. Right-click `phishing_detector.html` → **Open with Live Server** (or just double-click the file).

## Run Streamlit locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud
1. Push these files to a GitHub repo (root of the repo).
2. Go to https://share.streamlit.io → **New app** → pick the repo, branch `main`, main file `app.py`.

## Model performance tab
The **Model performance** tab shows metrics, a confusion matrix, an ROC curve and feature importance
(feature importance is read from your trained model; the other three come from `const PERF` in the HTML).

The file ships with **sample values copied from a screenshot** (benign/attack, AUC 0.857, hand-traced ROC) and shows a
warning until you replace them:

1. In Colab, run `export_performance.py` (needs `X_test`, `y_test`, `model`). It prints one JSON line.
2. Either paste that JSON into the app (**Load your own results**), or replace the `const PERF = {...};` line near the
   top of the `<script>` in `phishing_detector.html` with `const PERF = <your JSON>;` and commit.
