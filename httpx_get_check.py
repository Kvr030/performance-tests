import httpx
import time

create_user_payload = {
  "email": f"user.{time.time()}@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string",
  "phoneNumber": "string"
}

create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()


open_credit_card_account_payload = {
    "userId": create_user_response_data["user"]["id"] }

open_credit_card_account_response = httpx.post("http://localhost:8003/api/v1/accounts/open-credit-card-account",
                                               json=open_credit_card_account_payload)

open_credit_card_account_response_data = open_credit_card_account_response.json()

make_purchase_operation_payload = {
  "status": "IN_PROGRESS",
  "amount": 200,
  "cardId": open_credit_card_account_response_data["account"]["cards"][0]["id"],
  "accountId": open_credit_card_account_response_data["account"]["id"],
  "category": "taxi"
}
make_purchase_operation_response = httpx.post('http://localhost:8003/api/v1/operations/make-purchase-operation', json=make_purchase_operation_payload)
make_purchase_operation_response_data = make_purchase_operation_response.json()

take_check = httpx.get(f"http://localhost:8003/api/v1/operations/operation-receipt/{make_purchase_operation_response_data['operation']['id']}",)

take_check_data = take_check.json()
print(take_check_data)
print(take_check.status_code)