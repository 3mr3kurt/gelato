from barcode import Code128
from barcode.writer import ImageWriter

vanilla = "vanilla"
chocolate = 'chocolate'
vanilla_code = Code128(vanilla, writer=ImageWriter())
chocolate_code = Code128(chocolate, writer=ImageWriter())
vanilla_code.save("vanilla")
chocolate_code.save("chocolate")

