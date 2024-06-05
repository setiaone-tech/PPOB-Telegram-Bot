import midtransclient

def BAYAR(order_id, harga, uname):
    snap = midtransclient.Snap(
        is_production=False,
        server_key='' #Server Key Midtrans,
        client_key='' #Client Key Midtrans
    )

    # prepare SNAP API parameter ( refer to: https://snap-docs.midtrans.com ) minimum parameter example
    param = {
        "transaction_details": {
            "order_id": order_id,
            "gross_amount": harga
        }, "customer_details": {
        "first_name": uname
        }, "credit_card":{
            "secure" : True
        }
    }

    # create transaction
    transaction = snap.create_transaction(param)
    
    return transaction
