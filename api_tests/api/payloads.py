

class Payloads:
    @staticmethod
    def policy_calc(product: str) -> dict:
        return {
                "civilMin": "20000000",
                "householdMin": "20000000",
                "interiorMin": "20000000",
                "additionalItems": [],
                "calcSource": "direct",
                "form": {},
                "product": product,
                "paymentType": "annual" # из за этого параметра Post запрос может упасть,
                                        # так как не все продукты поддерживают этот тип оплаты

        }