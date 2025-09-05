

class Endpoints:
    @staticmethod
    def get_company_list() -> str:
        return "/public/company"

    @staticmethod
    def make_policy_calc(company_id: str) -> str:
        return f"/public/policy/calc/{company_id}"