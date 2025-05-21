import hashlib
import time
import base64

print("|-----------------|")
print("|Welcome TO PyHASH|")
print("|-----------------|")

print("What are you doing today?")
option1 = "1:Encode to sha256"
option2 = "2:Encode to md5"
option3 = "3:Encode to base64"
print(option1)
print(option2)
print(option3)
select = int(input("Select and option number: "))

if select == 1:
    message = input("Put your message you wnat to encode in sha256: ")
    byting_input = message.encode('utf-8')
    hash_object = hashlib.sha256(byting_input)
    hex_digest = hash_object.hexdigest()
    print("Encoding....")
    time.sleep(1)
    print("Complete")
    print(f"\n{hex_digest}")

if select == 2:
    message2 = input("Put your message you wnat to encode in md5: ")
    byting_input2 = message2.encode('utf-8')
    hash_object2 = hashlib.md5(byting_input2)
    hex_digest2 = hash_object2.hexdigest()
    print("Encoding....")
    time.sleep(1)
    print("Complete")
    print(f"\n{hex_digest2}")

if select == 3:
    message3 = input("Put your message you wnat to encode in base64: ")
    byting_input3 = message3.encode('utf-8')
    encoded_base64 = base64.b64encode(byting_input3)
    encoded_base64_str = encoded_base64.decode('utf-8')
    print("Encoding....")
    time.sleep(1)
    print("Complete")
    print(f"\n{encoded_base64_str}")

