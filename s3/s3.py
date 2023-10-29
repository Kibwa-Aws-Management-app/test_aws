import boto3

class s3:
    def __init__(self):
        self.s3_client = boto3.client('s3')
        self.s3_buckets = self.s3_client.list_buckets()['Buckets']

    # S3 버킷의 객체 잠금 상태를 확인합니다.
    def check_s3_bucket_object_lock(self):
        for bucket in self.s3_buckets:
            bucket_name = bucket['Name']
            bucket_versioning = self.s3_client.get_bucket_versioning(Bucket=bucket_name)

            if 'Status' in bucket_versioning and bucket_versioning['Status'] == 'Enabled':
                print(f"[PASS] S3 Bucket {bucket_name}: 객체 잠금이 활성화되어 있습니다.")
            else:
                print(f"[FAIL] S3 Bucket {bucket_name}: 객체 잠금이 활성화되어 있지 않습니다.")

    # S3 버킷의 정책 존재 여부를 확인합니다.
    def check_s3_bucket_policy(self):
        for bucket in self.s3_buckets:
            bucket_name = bucket['Name']
            bucket_policy = self.s3_client.get_bucket_policy(Bucket=bucket_name)

            if not bucket_policy:
                print(f"[PASS] S3 Bucket {bucket_name}: 버킷 정책이 없습니다.")
            else:
                print(f"[FAIL] S3 Bucket {bucket_name}: 버킷 정책이 있습니다.")

    # S3 버킷의 안전한 전송 정책 존재 여부를 확인합니다.
    def check_s3_bucket_secure_transport_policy(self):
        for bucket in self.s3_buckets:
            bucket_name = bucket['Name']
            bucket_policy = self.s3_client.get_bucket_policy(Bucket=bucket_name)

            if not bucket_policy:
                print(f"[FAIL] S3 Bucket {bucket_name}: 안전하지 않은 전송에 대해 요청 거부하는 정책이 없습니다.")
            else:
                print(f"[PASS] S3 Bucket {bucket_name}: 안전하지 않은 전송에 대해 요청 거부하는 정책이 있습니다.")

    # S3 버킷의 SSL 엔드포인트 사용 여부를 확인합니다.
    def check_s3_ssl_endpoint(self):
        for bucket in self.s3_buckets:
            bucket_name = bucket['Name']
            bucket_policy = self.s3_client.get_bucket_policy(Bucket=bucket_name)
            
            if not bucket_policy:
                print(f"[FAIL] S3 Bucket {bucket_name}: S3 SSL 엔드포인트를 사용하지 않습니다.")
            else:
                print(f"[PASS] S3 Bucket {bucket_name}: S3 SSL 엔드포인트를 사용하여 HTTPS를 통해 데이터를 전송할 수 있습니다.")

    # S3 버킷의 서버 측 암호화 상태를 확인합니다.
    def check_s3_server_side_encryption(self):
        for bucket in self.s3_buckets:
            bucket_name = bucket['Name']
            bucket_policy = self.s3_client.get_bucket_policy(Bucket=bucket_name)

            if not bucket_policy:
                print(f"[FAIL] S3 Bucket {bucket_name}: x-amz-server-side-encryption(서버 측 암호화) 헤더가 포함되지 않는 경우, 객체 업로드 (S3:PutObject) 권한을 거부하고 있지 않습니다.")
            else:
                print(f"[PASS] S3 Bucket {bucket_name}: x-amz-server-side-encryption(서버 측 암호화) 헤더가 포함되지 않는 경우, 객체 업로드 (S3:PutObject) 권한을 거부하고 있습니다.")

    # S3 버킷의 버전 관리 상태를 확인합니다.
    def check_s3_bucket_versioning(self):
        for bucket in self.s3_buckets:
            bucket_name = bucket['Name']
            bucket_versioning = self.s3_client.get_bucket_versioning(Bucket=bucket_name)

            if 'Status' in bucket_versioning and bucket_versioning['Status'] == 'Enabled':
                print(f"[PASS] S3 Bucket {bucket_name}: 버킷에 저장된 모든 객체 보존 및 복원이 (자동화) 되어 있습니다.")
            else:
                print(f"[FAIL] S3 Bucket {bucket_name}: 버킷에 저장된 모든 객체 보존 및 복원이 (자동화) 되어 있지 않습니다.")

    # S3 버킷의 ACL(Access Control List)을 확인합니다.
    def check_s3_bucket_acl(self):
        for bucket in self.s3_buckets:
            bucket_name = bucket['Name']
            bucket_acl = self.s3_client.get_bucket_acl(Bucket=bucket_name)

            all_accounts = ['http://acs.amazonaws.com/groups/global/AllUsers', 'http://acs.amazonaws.com/groups/global/AuthenticatedUsers']
            
            for grant in bucket_acl.get('Grants', []):
                grantee = grant.get('Grantee', {}).get('URI', '')

                if grantee in all_accounts:
                    print(f"[FAIL] S3 Bucket {bucket_name}: 모든 S3 계정 수준에서 접근이 허용되고 있습니다.")
                    return
            
            print(f"[PASS] S3 Bucket {bucket_name}: 모든 S3 계정 수준에서 접근이 금지되어 있습니다.")

if __name__ == '__main__':
    s3_instance = s3()
    s3_instance.check_s3_bucket_object_lock()
    s3_instance.check_s3_bucket_policy()
    s3_instance.check_s3_bucket_secure_transport_policy()
    s3_instance.check_s3_ssl_endpoint()
    s3_instance.check_s3_server_side_encryption()
    s3_instance.check_s3_bucket_versioning()
    s3_instance.check_s3_bucket_acl()