import mercadopago
import json

class GatewayMercadoPago:

    sdk = mercadopago.SDK("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

    #retorna status da transação
    #approved
    def WebHook (id):
        payment_response = GatewayMercadoPago.sdk.payment().get(id)
        return payment_response["response"].get("status")

    #retora qr code em base64
    def Pix (product_data, user_data):
        payment_data = {
        "transaction_amount": product_data["value"],
        "description": product_data["description"],
        "payment_method_id": "pix",
        "payer":
        {
            "email": user_data["e-mail"],
            "first_name": user_data["first_name"],
            "last_name": user_data["last_name"],
            "identification": {
                                "type": "CPF",
                                "number": user_data["cpf"]},
            "address": {
                        "zip_code": user_data["cep"],
                        "street_name": user_data["street"],
                        "street_number": user_data["street_number"],
                        "neighborhood": user_data["neighborhood"],
                        "city": user_data["city"],
                        "federal_unit": user_data["state"]}
        }
        }
        payment_response = GatewayMercadoPago.sdk.payment().create(payment_data)
        payment = payment_response["response"]
        print(payment)
        #return [payment["point_of_interaction"].get("transaction_data")["qr_code_base64"], payment["id"]]

product_data = {"value" : 0.1, "description" : "gold_coins", }
user_data = {"e-mail" : "a email", "first_name" : "Joao", "last_name" : "De Lucas", "cpf" : "854681149-09", "cep" : "80420-010", "street" : "Avenida Vicente Machado", "street_number" : "400", "neighborhood" : "Centro", "city" : "Curitiba", "state" : "PR"}
GatewayMercadoPago.Pix(product_data, user_data)
#print(GatewayMercadoPago.WebHook(the_id_you_receive))