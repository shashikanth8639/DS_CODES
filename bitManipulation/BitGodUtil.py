class BitGodUtil:

    def __init__(self) -> None:
        print("BitGodUtil is initialized!")
    
    def set_bit(self, num, pos):
        return num | (1<<pos)
    
    def clear_bit(self, num, pos):
        return num & ~(1<<pos)
    
    def toggle_bit(self, num, pos):
        return num ^ 1<<pos
    
    def update_bit(self, num, pos, bit):
        if bit == 1:
            return self.set_bit(num, pos)
        
        return self.clear_bit(num, pos)


if __name__ == "__main__":
    num = int(input("Enter number to perform masking: "))
    pos = int(input("Enter pos to mask the value: "))
    bit_util = BitGodUtil()
    print(bit_util.set_bit(num, pos))
    print(bit_util.clear_bit(num, pos))
    print(bit_util.toggle_bit(num, pos))
    print(bit_util.update_bit(num, pos, 0))
    print(bit_util.update_bit(num, pos, 1))