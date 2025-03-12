def ones_complement_sum(a, b, bit_size=16):
   #print("Perform one's complement addition of two numbers.")
    print(a,b)
    result = a + b
    if result >= (1 << bit_size): # If there's an overflow
        result = (result + 1) & ((1 << bit_size) - 1) # Wrap around carry
    return result

def calculate_checksum(data, bit_size=16):
    #print("Compute one's complement checksum for a list of integers.")
    print(data)
    checksum = 0
    for word in data:
        checksum = ones_complement_sum(checksum, word, bit_size)
    return ~checksum & ((1 << bit_size) - 1) # One's complement

def verify_checksum(data, received_checksum, bit_size=16):
    """Verify the checksum by adding it to the computed sum."""
    total = 0
    for word in data:
      total = ones_complement_sum(total, word, bit_size)
    total = ones_complement_sum(total, received_checksum, bit_size)
    return total == (1 << bit_size) - 1 # Valid if all bits are 1
# Example Usage
data = [0b1010101010101010, 0b1100110011001100, 0b1111000011110000] # Example
#16-bit words
checksum = calculate_checksum(data)
print(f"Calculated Checksum: {bin(checksum)}")
# Verification
is_valid = verify_checksum(data, checksum)
print("Checksum is valid" if is_valid else "Checksum is invalid")

#addition example manually
#0b1010101010101010,
#0b1100110011001100,


#0b0111011101110111
#0b1111000011110000

#0b0110100001101000
#0b0001011110010111
#0b1111111111111111