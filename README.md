# Email Classification for Support Team

This project is designed to classify customer support emails into predefined categories while masking any personally identifiable information (PII) prior to classification. The system also supports restoring the original content and is deployed via a FastAPI endpoint.

## Features
- PII masking using Regex
- Email classification using Multinomial Naive Bayes
- Deployed API with FastAPI
- JSON output with masked entity info and category

## Usage
- POST request to `/classify` with `{ "email": "<your_email_body>" }`
- Receives structured JSON with masked email, entity list, and classification category



