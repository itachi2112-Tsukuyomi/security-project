import boto3
import json

s3 = boto3.client("s3")

print("\n[+] Starting S3 Public Bucket Scan...\n")

response = s3.list_buckets()

for bucket in response.get("Buckets", []):
    bucket_name = bucket.get("Name")
    is_public = False

    # ---- Check ACLs (old method) ----
    try:
        acl = s3.get_bucket_acl(Bucket=bucket_name)
        for grant in acl.get("Grants", []):
            grantee = grant.get("Grantee", {})
            uri = grantee.get("URI", "")
            if uri == "http://acs.amazonaws.com/groups/global/AllUsers":
                is_public = True
                print(f"[ALERT][ACL] Public bucket detected: {bucket_name}")
    except Exception:
        pass

    # ---- Check Bucket Policy (modern method) ----
    try:
        policy_response = s3.get_bucket_policy(Bucket=bucket_name)
        policy = json.loads(policy_response["Policy"])

        for statement in policy.get("Statement", []):
            principal = statement.get("Principal")
            effect = statement.get("Effect")

            if effect == "Allow" and principal == "*":
                is_public = True
                print(f"[ALERT][POLICY] Public bucket detected: {bucket_name}")
    except s3.exceptions.NoSuchBucketPolicy:
        pass
    except Exception as e:
        print(f"[ERROR] Policy check failed for {bucket_name}: {e}")

    if not is_public:
        print(f"[OK] {bucket_name} is not public")

print("\n[+] Scan completed.")
