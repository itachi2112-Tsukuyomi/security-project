\# AWS S3 Public Bucket Security Scanner



\## Overview

This project is a Python-based cloud security tool that detects publicly

accessible Amazon S3 buckets caused by insecure configurations such as

permissive bucket policies or ACLs.



The tool simulates real-world cloud security assessments performed by

SOC and Cloud Security teams to identify data exposure risks.



---



\## Why This Matters

Public S3 buckets are one of the most common causes of cloud data breaches.

Sensitive data such as backups, logs, credentials, or customer information

can be accessed by anyone on the internet if misconfigured.



This project demonstrates how such misconfigurations occur and how they

can be detected programmatically.



---



\## AWS Services Used

\- Amazon S3

\- AWS IAM

\- AWS CLI

\- AWS SDK for Python (boto3)



---



\## Security Checks Performed



\### 1. ACL-Based Public Access Detection

The tool checks S3 bucket Access Control Lists (ACLs) for grants provided

to the global `AllUsers` group.



Note: Modern AWS accounts often enforce Object Ownership, which disables

ACL-based public access.



\### 2. Bucket Policy-Based Public Access Detection

The tool analyzes bucket policies to detect permissive statements such as:

\- `Effect: Allow`

\- `Principal: "\*"`



This method detects modern, real-world public exposure scenarios and

prevents false negatives.



---



\## Test Scenario

\- Region: ap-south-1 (Mumbai)

\- A test bucket was intentionally misconfigured using a public bucket policy.

\- The file inside the bucket was accessible via Object URL without authentication.

\- The scanner successfully detected the exposure through policy analysis.



---



\## How to Run



\### Prerequisites

\- Python 3.x

\- AWS CLI configured with read-only S3 permissions

\- boto3 library installed



\### Steps

1\. Configure AWS credentials using `aws configure`

2\. Install dependencies:

&nbsp; -pip install boto3

3\. Run the scanner:

&nbsp; -python scanner.py



---



\## Sample Output



\[ALERT]\[POLICY] Public bucket detected: hitesh-public-test-bucket-123





---



\## Key Learnings

\- Public S3 access can exist even when ACLs are disabled.

\- Bucket policies are the primary source of public exposure in modern AWS.

\- Cloud security tools must check multiple access control layers.

\- False negatives can occur if only one control mechanism is analyzed.



---



\## Remediation Recommendations

\- Enable S3 Block Public Access at account and bucket level

\- Avoid using public bucket policies

\- Follow least privilege IAM principles

\- Regularly audit cloud configurations



---



\## Disclaimer

This project was created for educational and security research purposes

and was tested only on the author's own AWS resources.





