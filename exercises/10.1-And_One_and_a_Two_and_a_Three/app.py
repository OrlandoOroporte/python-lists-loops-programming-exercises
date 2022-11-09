contact = {
    "fullname": "Jane Doe",
    "phone": "321-321-4321",
    "email": "test@test.com"
}
#Your code here:
def resp (obj):
    for i in obj:
        print(i + ' : ',obj[i])

print(resp(contact))

