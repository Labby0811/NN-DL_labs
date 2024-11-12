#formula using tuple
def conv_output_shape(nh, nw, kh, kw, ph, pw, sh, sw):
    output_height = (nh + 2 * ph - kh) // sh + 1
    output_width = (nw + 2 * pw - kw) // sw + 1 
    return output_height, output_width

#select the shape
print("Select the shape")
print("0. Squared")
print("1. Not Squared")
shape = int(input("Shape: "))

#if squared
#ask to insert the number
if shape == 0:
    n = int(input("n: "))
    k = int(input("k: "))
    p = int(input("p: "))
    s = int(input("s: "))
    print("Output shape: ", conv_output_shape(n, n, k, k, p, p, s, s))

#if not squared
#ask to insert the number
else:
    nh = int(input("nh: "))
    nw = int(input("nw: "))
    kh = int(input("kh: "))
    kw = int(input("kw: "))
    ph = int(input("ph: "))
    pw = int(input("pw: "))
    sh = int(input("sh: "))
    sw = int(input("sw: "))
    print("Output shape: ", conv_output_shape(nh, nw, kh, kw, ph, pw, sh, sw))

#hold the print
input("\nPress Enter to exit...")