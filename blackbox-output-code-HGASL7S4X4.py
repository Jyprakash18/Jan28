import razorpay

client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))
order = client.order.create({
    "amount": 50000,  # Amount in paisa (e.g., ₹500)
    "currency": "INR",
    "receipt": "order_rcptid_11"
})