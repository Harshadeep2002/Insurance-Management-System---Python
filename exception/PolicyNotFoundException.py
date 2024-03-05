class PolicyNotFoundException(Exception):
    def __init__(self,policyId):
        super().__init__(f"Policy ID : {policyId} not found in the system..")