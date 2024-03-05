from dao.PolicyDAO import PolicyDAO
from exception.PolicyNotFoundException import PolicyNotFoundException

class InsuranceServiceImpl(PolicyDAO):
    def __init__(self):
        super().__init__()

    #To get policy details of a particular policy
    def getPolicy(self,policyId):
        try:
            self.open()
            self.stmt.execute(f'''SELECT COUNT(*) FROM Policy WHERE policyId = {policyId}''')
            count = self.stmt.fetchone()[0]
            if count == 0:
                return PolicyNotFoundException(policyId)
            else:
                self.stmt.execute(f'''SELECT * FROM Policy WHERE policyId = {policyId}''')
                records = self.stmt.fetchall()
                self.close()
                return records
        except PolicyNotFoundException as e:
            return e
        except Exception as e:
            return e

    #To get all Policies

    def getAllPolicies(self):
        try:
            self.open()
            self.stmt.execute(f'''SELECT * FROM Policy''')
            records = self.stmt.fetchall()
            self.close()
            return records
        except Exception as e:
            return e

    def update_policy(self):
        p = PolicyDAO()
        p.update_policy()
        pass

    def delete_policy(self):
        p = PolicyDAO()
        p.delete_policy()
        pass