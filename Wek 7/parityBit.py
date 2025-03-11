def even_bit_parity(data):
    return sum(data) % 2


data = [0,1,0,1,1,0,1,0]
parity_bit = even_bit_parity(data)
print("Original Data: ", data)
print("Computed Parity Bit (Even):", parity_bit)

transmitted_data = data + [parity_bit]
#print("\nTransmitted Data (Data + Parity):", transmitted_data)

error_index = 5
data_with_error = transmitted_data.copy()
data_with_error[error_index] = 1 - data_with_error[error_index]
print("\nData with an Error Introduced at index", error_index, ":",data_with_error)
# At the receiver, perform the parity check.
# For even parity, the sum of all bits should be even.
if sum(data_with_error) % 2 == 0:
    print("\nNo error detected (Parity Check Passed)")
else:
    print("\nError detected (Parity Check Failed)")