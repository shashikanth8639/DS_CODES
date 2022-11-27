# Bit Manipulation (between two operands)

  - **AND Operation**: Returns 1 if both operands are 1 [1&1 --> 1] else 0
    - performing AND with 0 on the respective bit 0 will set it to 0 [masking]

  - **OR  Operation**: Returns 0 if both operands are 0 [0|0 --> 0] else 1
    - performing OR  with 1 on the respective bit 0 will set it to 0

  - **XOR Operation**: Returns 1 if both operands are different else 0 [0^1 --> 1]
    - performing XOR with 1 on the respective bit will toggle nth bit

  - **Left Shift**: Will multiply the operand by 2 [4<<1 --> 8]

  - **Right Shift**: Will divide the operand by 2  and value will be floored  [4>>1 --> 2]


## Representing Negative Numbers:

    Typically a negative integer is stored in two's compilment form [inverse plus 1]. The very first bit is used to represent sign. 
    [+ve -> 0 & -ve -> 1]

    Adding the positive and negative of same number will return zero. It is repsented in a way that the adding this value to the postive of number will         return the 2^8 value [for an 8-bit number].


### Logical Shift vs Arithmetic Shift:

    Arithmetic right shift will preserves the arithmetic relationship between the otiginal number and the new one. 
    Right shift will pick up the ceil value for negaative numbers

### Satements | Facts

  - doing AND with 1 will return whether number is odd or even

  - **OR opertion will always be >= AND, XOR**
  
  - All these operators are both commutative and associative
    - a|b|c --> b|a|c
  
  - a|a -> a, a|0 -> a, a&a -> a, a&0 -> 0, a^a -> 0, a^0 -> a
