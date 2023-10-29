import boto3

class rds:
    def __init__(self):
        self.rds_client = boto3.client('rds')
        self.rds_db_subnet_group_name = 'your_db_subnet_group_name'  # RDS DB Subnet Group 이름 설정
        self.rds_db_instance_identifier = 'your_db_instance_identifier'  # RDS DB 인스턴스 식별자 설정

    # RDS 서브넷 가용 영역 관리 체크
    def check_rds_subnet_availability(self):
        response = self.rds_client.describe_db_subnet_groups(DBSubnetGroupName=self.rds_db_subnet_group_name)
        subnets = response['DBSubnetGroups'][0]['Subnets']
        availability_zones = set(subnet['AvailabilityZone'] for subnet in subnets)
        
        if len(availability_zones) == len(subnets):
            print("[PASS] RDS 서브넷 그룹 내 불필요한 가용 영역이 존재하지 않습니다.")
        else:
            print("[FAIL] RDS 서브넷 그룹 내 불필요한 가용 영역이 존재합니다.")

    # RDS 암호화 설정 체크
    def check_rds_encryption(self):
        response = self.rds_client.describe_db_instances(DBInstanceIdentifier=self.rds_db_instance_identifier)
        encryption_at_rest = response['DBInstances'][0]['StorageEncrypted']
        
        if encryption_at_rest:
            print("[PASS] RDS 데이터베이스 암호화가 활성화되어 있습니다.")
        else:
            print("[FAIL] RDS 데이터베이스 암호화가 비활성화되어 있습니다.")
    
    # RDS 로깅 설정 체크
    def check_rds_logging(self):
        response = self.rds_client.describe_db_log_files(DBInstanceIdentifier=self.rds_db_instance_identifier)
        log_files = response['DescribeDBLogFiles']
        
        if log_files:
            print("[PASS] CloudWatch 로그 스트림으로 보관하고 있습니다.")
        else:
            print("[FAIL] CloudWatch 로그 스트림으로 보관하고 있지 않습니다.")
    
    # RDS Public Access 설정 체크
    def check_rds_public_access(self):
        response = self.rds_client.describe_db_instances(DBInstanceIdentifier=self.rds_db_instance_identifier)
        db_instance = response['DBInstances'][0]
        publicly_accessible = db_instance['PubliclyAccessible']
        
        if publicly_accessible:
            print("[FAIL] RDS에 대해 Public Access가 허용되어 있습니다.")
        else:
            print("[PASS] RDS에 대해 Public Access가 허용되어 있지 않습니다.")
    
    # DB 생성 삭제 권한 설정 체크
    def check_db_creation_deletion_privileges(self):
        response = self.rds_client.describe_db_security_groups(DBInstanceIdentifier=self.rds_db_instance_identifier)
        db_security_groups = response['DBSecurityGroups']
        ec2_security_group_names = set()
        
        for db_security_group in db_security_groups:
            for ec2_security_group in db_security_group['EC2SecurityGroups']:
                ec2_security_group_names.add(ec2_security_group['EC2SecurityGroupName'])
        
        if 'your_db_creation_deletion_security_group' in ec2_security_group_names:
            print("[FAIL] DBE 이외의 사람이 데이터베이스 생성/삭제를 할 수 있도록 설정되어 있습니다.")
        else:
            print("[PASS] DBE만 데이터베이스 생성/삭제를 할 수 있도록 설정되어 있습니다.")

if __name__ == '__main__':
    rds_instance = rds()
    rds_instance.check_rds_subnet_availability()
    rds_instance.check_rds_encryption()
    rds_instance.check_rds_logging()
    rds_instance.check_rds_public_access()
    rds_instance.check_db_creation_deletion_privileges()
