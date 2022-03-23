# All About Python Formats

num = 1.234
print(f'{num:.3g}') # 1.23
num = 1.239
print(f'{num:.3g}') # 1.24
print(f'''{num:.1f} and {num:.2f} and {num}''')

txt = "We have {:<8} bananas - Left Align"
print(txt.format(49)) # Left align
txt = "We have {:>5} cars - Right Align"
print(txt.format(50)) # Right align
txt = "Texas capital is {:^20} - Center Align"
print(txt.format("Austin")) # Center align
txt = "The temp is {:=8} - plus/minus at the left most position"
print(txt.format(-10)) # Minus/Plus align

txt = "The temperature is"
