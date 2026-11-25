# Mission 5 — Numbers and data

## 2. Task / objective
Convert values between bases, verify conversions with Python, build a converter and explain text encoding.

## 3. Work completed
### Manual conversions
| Question | Working and answer |
|---|---|
| Decimal 13 to binary | 13 = 8 + 4 + 1 = `1101₂` |
| Decimal 25 to binary | 25 = 16 + 8 + 1 = `11001₂` |
| Binary 1010 to decimal | 1×8 + 0×4 + 1×2 + 0×1 = `10₁₀` |
| Binary 1101 to decimal | 1×8 + 1×4 + 0×2 + 1×1 = `13₁₀` |
| Hexadecimal A to decimal | A represents ten = `10₁₀` |
| Hexadecimal 1F to decimal | 1×16 + 15 = `31₁₀` |
| Binary 1111 to hexadecimal | 1111₂ = 15₁₀ = `F₁₆` |

### Python verification
Use `bin(13)`, `int('1010', 2)`, `hex(31)`, and `int('1F', 16)`. These return Python representations (for example, `0b1101` and `0x1f`); the prefixes indicate the base. Observed results: `bin(13)` → `0b1101`; `int('1010', 2)` → `10`; `hex(31)` → `0x1f`; `int('1F', 16)` → `31`.

### Converter checks
| Test number | Binary | Hexadecimal |
|---:|---:|---:|
| 13 | 1101 | d |
| 25 | 11001 | 19 |
| 255 | 11111111 | ff |

`bin()` returns a binary string with a `0b` prefix and `hex()` returns hexadecimal with a `0x` prefix. The program strips those prefixes for a cleaner display.

### Text encoding
ASCII decimal codes: uppercase `A` = 65; lowercase `a` = 97. An encoding standard maps characters to numbers so computers can store, transmit and interpret text consistently. A character outside basic ASCII is `€` (Euro sign); UTF-8 can encode it.

## 4. Commands / tools used
Python 3 built-ins `bin`, `int`, `hex`; run `python3 number_converter.py`. Tested the converter with 13, 25 and 255; outputs matched the table below.

## 5. My understanding
Binary is base 2, decimal is base 10 and hexadecimal is base 16. Place values depend on the base. Character encoding defines a shared mapping from text characters to bytes; UTF-8 supports a much wider range than basic ASCII.

## 6. Difficulties faced
No major difficulties. I checked each result against the place-value calculations above.

## 7. How I resolved them
Used the built-in conversion functions and compared outputs with the manual sums and place values.

## 8. Evidence / files
`number_converter.py` (included alongside this README).

## 9. Commit details
Suggested message: `Build number converter and practise data representation`. Commit hash: https://github.com/oppachan-art/digital-detective-8090 (see Git history).
